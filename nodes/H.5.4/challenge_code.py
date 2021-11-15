"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''@qml.qnode(dev)
def two_close_spins(B, J, time, n):
    """Circuit for evolving the state of two nearby electrons with an arbitrary coupling.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (array[float]): The coupling strengths J = [J_X, J_Y, J_Z] between electrons.
        time (float): The time we evolve the electron wavefunction for.
        n (int): The number of steps in our Trotterization.

    Returns: 
        array[complex]: The quantum state after evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()
'''
