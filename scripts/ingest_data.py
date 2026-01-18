import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores.azuresearch import AzureSearch

load_dotenv()

# 1. Setup Embeddings (The "Translator" that turns text into numbers)
embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# 2. Setup Azure AI Search connection
vector_store = AzureSearch(
    azure_search_endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    azure_search_key=os.getenv("AZURE_SEARCH_ADMIN_KEY"),
    index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
    embedding_function=embeddings.embed_query,
)

def run_ingestion():
    data_folder = "./data"
    print(f"Checking for PDFs in {data_folder}...")
    
    for filename in os.listdir(data_folder):
        if filename.endswith(".pdf"):
            print(f"--- Processing {filename} ---")
            
            # Load PDF
            loader = PyPDFLoader(os.path.join(data_folder, filename))
            documents = loader.load()
            
            # Split into chunks (AI works better with small pieces)
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            docs = text_splitter.split_documents(documents)
            
            # Upload to Azure AI Search
            print(f"Uploading {len(docs)} chunks to Azure Search...")
            vector_store.add_documents(documents=docs)
            print(f"✅ Finished uploading {filename}")

if __name__ == "__main__":
    run_ingestion()