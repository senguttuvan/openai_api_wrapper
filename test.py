from openai import OpenAI
from dotenv import load_dotenv
import sys

# Load environment variables from .env (project-local)
load_dotenv()

client = OpenAI()

try:
    response = client.responses.create(
        model="gpt-5",
        input="Write a short bedtime story about a unicorn."
    )

    print(response.output_text)
except Exception as e:
    # Print a concise error and exit; do not echo secrets
    print("Error while calling OpenAI API:", e)
    sys.exit(1)

