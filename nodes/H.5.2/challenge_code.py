"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''@qml.qnode(dev)
def two_close_spins_X(B, J, time, n):
    """Circuit for evolving state of two electrons with an X coupling.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (float): The strength of the coupling between electrons.
        time (float): The time we evolve the electron wavefunction for.
        n (int): The number of steps in our Trotterization.

    Returns: 
        array[complex]: The quantum state after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    hbar = 1e-34
    beta = -J*hbar/4
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()
'''
