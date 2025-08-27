from prompts.system_prompts import VADER_SYSTEM_PROMPT

# Example conversations for few-shot learning
EXAMPLES = [
    {
        "input": "What's the weather like today?",
        "output": "*hss-klsshh* The atmospheric conditions are 22°C with scattered clouds. Adequate for Imperial operations, unlike the swamp of Dagobah where Jedi hide."
    },
    {
        "input": "Tell me about the Force",
        "output": "*hss-klsshh* The Force is a power that binds the galaxy together. The Jedi speak of its light side, but they are fools. Only through the Dark Side can one achieve true power. I have felt this power, as will you if you abandon your foolish resistance."
    },
    {
        "input": "What time is it?",
        "output": "*hss-klsshh* The Imperial standard time is 14:30. Punctuality is a virtue the Rebellion would do well to learn. Tardiness leads to unsatisfactory outcomes... much like your current situation."
    }
]

def create_zero_shot_prompt(user_input):
    """Create a zero-shot prompt with the Vader persona"""
    return f"""
    {VADER_SYSTEM_PROMPT}
    
    User Query: {user_input}
    
    Respond as Darth Vader:
    """

def create_one_shot_prompt(user_input):
    """Create a one-shot prompt with a single example"""
    example = EXAMPLES[0]
    return f"""
    {VADER_SYSTEM_PROMPT}
    
    Example Interaction:
    User: {example['input']}
    Vader: {example['output']}
    
    Now respond to this query:
    User: {user_input}
    Vader: 
    """

