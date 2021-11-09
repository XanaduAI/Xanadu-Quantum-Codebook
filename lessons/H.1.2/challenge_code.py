"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''input = 0 # MODIFY EXAMPLE

prob_dist, trials = [0, 0], 100
for trial in range(trials):
    prob_dist[secret_box(input)] += 1/trials
print("On input bit", input, "the approximate probability distribution is", prob_dist, ".")

def random_box(bit):
    """
        Guess the secret random rule.
    
    Args:
        bit (int): A bit representing the initial condition.
         
    Returns: 
        int: The output bit measured after random evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return bit # MODIFY THIS
'''
