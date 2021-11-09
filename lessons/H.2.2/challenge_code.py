"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''n_bits = 1
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def unitary_circuit(operator):
    """
    Applies a matrix to the state if is unitary and correctly sized.
    
    Args:
        operator (array[complex]): A square complex-valued array.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    return qml.state()
'''
