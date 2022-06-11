"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''n_bits = 4

def diffusion_matrix():
    """Return the diffusion matrix.

    Returns: 
        array[float]: The matrix representation of the diffusion operator.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    pass # FORM A DIFFERENCE OF MATRICES

@qml.qnode(dev)
def difforacle_amp(combo):
    """Prepare the uniform superposition and apply the oracle and diffusion matrix.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The quantum state (amplitudes) after applying the oracle
        and diffusion.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()
'''
