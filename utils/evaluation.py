import json
import re
from pathlib import Path

def load_evaluation_dataset():
    """Load the evaluation dataset"""
    dataset_path = Path(__file__).parent.parent / 'data' / 'evaluation_dataset.json'
    with open(dataset_path, 'r') as f:
        return json.load(f)

def evaluate_response(response, expected_keywords):
    """Evaluate if response contains expected keywords"""
    response_lower = response.lower()
    matches = []
    
    for keyword in expected_keywords:
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        if re.search(pattern, response_lower):
            matches.append(keyword)
    
    score = len(matches) / len(expected_keywords)
    return score, matches

def run_evaluation(model, prompt_func, dataset=None):
    """Run evaluation on the model"""
    if dataset is None:
        dataset = load_evaluation_dataset()
    
    results = []
    total_score = 0
    
    for i, test_case in enumerate(dataset):
        prompt = prompt_func(test_case['input'])
        response = model.generate_content(prompt)
        
        score, matches = evaluate_response(response.text, test_case['expected_keywords'])
        total_score += score
        
        results.append({
            'input': test_case['input'],
            'response': response.text,
            'expected_keywords': test_case['expected_keywords'],
            'matched_keywords': matches,
            'score': score
        })
        
        print(f"Test {i+1}: Score = {score:.2f}")
        print(f"Input: {test_case['input']}")
        print(f"Response: {response.text[:100]}...")
        print(f"Matched: {matches}")
        print("-" * 50)
    
    average_score = total_score / len(dataset)
    print(f"Average Score: {average_score:.2f}")
    
    return results, average_score