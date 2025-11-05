from dotenv import load_dotenv
import os

print("Loading .env file...")
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

key = os.getenv("GROQ_API_KEY")
if key:
    print("✅ GROQ_API_KEY loaded successfully!")
    print("Key starts with:", key[:8] + "...")
else:
    print("❌ Failed to load GROQ_API_KEY. Check .env file location and format.")
