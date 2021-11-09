"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''@qml.qnode(dev)
def X_plus_Z():
    """Apply X + Z to |0> and return the state."""
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

print("The amplitudes on the main register are proportional to", X_plus_Z()[:2], ".")
'''
