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
def mag_z_0_v1(B, time):
    """
    Simulates an electron (initial state |0>) in a magnetic field, using a unitary matrix.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()
'''
