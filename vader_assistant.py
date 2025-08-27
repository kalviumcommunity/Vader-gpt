import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def initialize_model():
    """Initialize the Gemini model"""
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    return model

def main():
    model = initialize_model()
    print("Vader-GPT Initialized. I am altering the deal. Pray I don't alter it any further.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit', 'goodbye']:
            print("Vader: I find your lack of faith disturbing. Until we meet again.")
            break
        
        # Process input
        response = model.generate_content(user_input)
        print(f"Vader: {response.text}")

if __name__ == "__main__":
    main()