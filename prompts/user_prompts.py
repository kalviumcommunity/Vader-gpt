from prompts.system_prompts import VADER_SYSTEM_PROMPT


def create_zero_shot_prompt(user_input):
    """Create a zero-shot prompt with the Vader persona"""
    return f"""
    {VADER_SYSTEM_PROMPT}
    
    User Query: {user_input}
    
    Respond as Darth Vader:
    """