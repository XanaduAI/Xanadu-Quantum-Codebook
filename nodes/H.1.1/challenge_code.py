"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''input = [1, 1, 0] # MODIFY EXAMPLE
print("The result of applying the secret box to ", input, "is ")
# We will secretly apply the function and return the result!

def deterministic_box(bits):
    """Guess the secret deterministic rule.
    
    Args:
        bits (list[int]): A list of bits representing an initial condition.
         
    Returns: 
        list[int]: The output bits measured after deterministic evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return bits # MODIFY THIS
'''
