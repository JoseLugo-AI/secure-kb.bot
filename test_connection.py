import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# 1. Load the .env file from the current directory
load_dotenv()

# 2. Get the settings from the .env file
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

# 3. Simple Check: Print if the key was found (but don't show the whole key!)
if not api_key:
    print("❌ ERROR: .env file not found or AZURE_OPENAI_API_KEY is missing.")
else:
    print(f"✅ Credentials loaded. Connecting to: {endpoint}")

    # 4. Try a real connection
    try:
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version
        )

        response = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": "Respond with 'Success!'"}]
        )
        print(f"🚀 {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")