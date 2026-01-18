import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_core.prompts import ChatPromptTemplate

try:
    from langchain_classic.chains import create_retrieval_chain
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
except ImportError:
    st.error("Missing package! Please run: pip install langchain-classic")
    st.stop()

load_dotenv()

# --- 1. Setup Connections ---
embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

vector_store = AzureSearch(
    azure_search_endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    azure_search_key=os.getenv("AZURE_SEARCH_ADMIN_KEY"),
    index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
    embedding_function=embeddings.embed_query,
)

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    temperature=0
)

# --- 2. Streamlit UI ---
st.set_page_config(page_title="Secure KB Assistant", page_icon="🛡️")
st.title("🛡️ Secure KB Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about security docs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        system_prompt = (
            "You are a helpful security assistant. Use the following context to answer. "
            "If the answer isn't in the context, say you don't know. "
            "\n\nContext: {context}"
        )
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])
        
        # Build the Chain
        question_answer_chain = create_stuff_documents_chain(llm, prompt_template)
        rag_chain = create_retrieval_chain(vector_store.as_retriever(), question_answer_chain)
        
        with st.spinner("Searching documents..."):
            # Get the full response which includes the 'context' documents
            response = rag_chain.invoke({"input": prompt})
            answer = response["answer"]
            
            # --- EXTRACT SOURCES ---
            # We get the unique filenames from the metadata of the retrieved chunks
            sources = set()
            for doc in response.get("context", []):
                # 'source' is the metadata field where the PDF loader stores the filename
                filename = os.path.basename(doc.metadata.get("source", "Unknown"))
                sources.add(filename)
            
            # Add sources to the answer if they exist
            if sources:
                source_list = "\n\n**Sources:**\n* " + "\n* ".join(sources)
                full_response = f"{answer}{source_list}"
            else:
                full_response = answer

        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})