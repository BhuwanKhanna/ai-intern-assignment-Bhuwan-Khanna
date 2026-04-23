import os
import sys
import warnings

# Suppress warnings before importing the library
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment.")
        print("Please create a .env file and add your GEMINI_API_KEY.")
        sys.exit(1)

    # Configure the Gemini API
    genai.configure(api_key=api_key)
    
    # Initialize an available model
    model = genai.GenerativeModel('gemini-flash-latest')

    print("\n--- Gemini LLM Query Script ---")
    question = input("Enter your question: ")

    if not question.strip():
        print("Empty question. Exiting.")
        return

    print("\nThinking...")
    
    try:
        # Generate response
        response = model.generate_content(question)
        
        # Print the response
        print("\n--- Model Response ---")
        print(response.text)
        print("-" * 23)
        
    except Exception as e:
        if "429" in str(e):
            print("\nError: Quota exceeded. Please wait a few minutes and try again.")
        elif "API_KEY_INVALID" in str(e):
            print("\nError: Your API key is invalid. Please check your .env file.")
        else:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
