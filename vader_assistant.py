import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts.user_prompts import create_zero_shot_prompt, create_one_shot_prompt, create_few_shot_prompt

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
    
    # Prompting technique selection
    techniques = {
        '1': ('Zero-Shot', create_zero_shot_prompt),
        '2': ('One-Shot', create_one_shot_prompt),
        '3': ('Few-Shot', create_few_shot_prompt)
    }
    
    print("\nSelect prompting technique:")
    for key, (name, _) in techniques.items():
        print(f"{key}: {name}")
    
    technique_choice = input("Enter choice (1-3): ") or '1'
    technique_name, prompt_func = techniques.get(technique_choice, techniques['1'])
    
    print(f"\nUsing {technique_name} prompting. Your insolence will be remembered.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit', 'goodbye']:
            print("Vader: I find your lack of faith disturbing. Until we meet again.")
            break
        
        # Create prompt based on selected technique
        prompt = prompt_func(user_input)
        
        # Process input
        response = model.generate_content(prompt)
        print(f"Vader: {response.text}")

if __name__ == "__main__":
    main()