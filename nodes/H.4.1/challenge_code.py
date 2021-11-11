"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def zz_circuit(alpha, time, init):
    """Circuit for evolving two electrons with a ZZ interaction.
    
    Args:
        alpha (float): The strength of the interaction.
        time (float): The time we evolve the electron wavefunction for.
        init (array[int]): An initial state specified by two bits [x, y]. Prepare the
            system in this state prior to applying the time evolution circuit.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """
    hbar = 1e-34
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.probs(wires=range(n_bits))
'''
