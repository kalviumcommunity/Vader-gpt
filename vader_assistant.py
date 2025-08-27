import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts.user_prompts import (
    create_zero_shot_prompt, create_one_shot_prompt, 
    create_few_shot_prompt, create_dynamic_prompt,
    create_chain_of_thought_prompt
)
from utils.evaluation import run_evaluation

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def initialize_model(generation_config=None):
    """Initialize the Gemini model with optional generation config"""
    if generation_config is None:
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40,
            "max_output_tokens": 1024,
        }
    
    model = genai.GenerativeModel(
        'gemini-2.5-flash-lite',
        generation_config=generation_config
    )
    return model

def main():
    # Configure generation parameters
    temperature = float(input("Enter temperature (0.0-1.0, default 0.7): ") or 0.7)
    top_p = float(input("Enter top-p (0.0-1.0, default 0.9): ") or 0.9)
    top_k = int(input("Enter top-k (1-100, default 40): ") or 40)
    
    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": 1024,
    }
    
    model = initialize_model(generation_config)
    print("Vader-GPT Initialized. I am altering the deal. Pray I don't alter it any further.")
    
    # Check if user wants to run evaluation
    if input("Run evaluation? (y/N): ").lower() == 'y':
        techniques = {
            '1': ('Zero-Shot', create_zero_shot_prompt),
            '2': ('One-Shot', create_one_shot_prompt),
            '3': ('Few-Shot', create_few_shot_prompt),
            '4': ('Chain-of-Thought', create_chain_of_thought_prompt)
        }
        
        print("\nSelect prompting technique for evaluation:")
        for key, (name, _) in techniques.items():
            print(f"{key}: {name}")
        
        technique_choice = input("Enter choice (1-4): ") or '1'
        technique_name, prompt_func = techniques.get(technique_choice, techniques['1'])
        
        print(f"\nEvaluating {technique_name} prompting...")
        results, avg_score = run_evaluation(model, prompt_func)
        
        print(f"\nEvaluation complete. Average score: {avg_score:.2f}")
        return
    
    # Normal conversation mode
    techniques = {
        '1': ('Zero-Shot', create_zero_shot_prompt),
        '2': ('One-Shot', create_one_shot_prompt),
        '3': ('Few-Shot', create_few_shot_prompt),
        '4': ('Dynamic', lambda input: create_dynamic_prompt(input, conversation_history)),
        '5': ('Chain-of-Thought', create_chain_of_thought_prompt)
    }
    
    print("\nSelect prompting technique:")
    for key, (name, _) in techniques.items():
        print(f"{key}: {name}")
    
    technique_choice = input("Enter choice (1-5): ") or '1'
    technique_name, prompt_func = techniques.get(technique_choice, techniques['1'])
    
    print(f"\nUsing {technique_name} prompting. Your insolence will be remembered.")
    
    conversation_history = []
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit', 'goodbye']:
            print("Vader: I find your lack of faith disturbing. Until we meet again.")
            break
        
        # Create prompt based on selected technique
        prompt = prompt_func(user_input)
        
        # Process input
        response = model.generate_content(prompt)
        vader_response = response.text
        
        # Store conversation history for dynamic prompting
        conversation_history.append({
            'user': user_input,
            'vader': vader_response
        })
        
        print(f"Vader: {vader_response}")

if __name__ == "__main__":
    main()