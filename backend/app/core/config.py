from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DATABASE_URL = os.getenv("DATABASE_URL")

SUPABASE_URL = os.getenv("SUPABASE_URL")

SUPABASE_KEY = os.getenv("SUPABASE_KEY")

SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")