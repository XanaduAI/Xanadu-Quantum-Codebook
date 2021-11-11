"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''dev = qml.device("default.qubit", wires=1)

def evolve_plus_state(B, time):
    """Simulates an electron (initial state |+>) in a magnetic field.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################

@qml.qnode(dev)
def mag_z_plus_X(B, time):
    """Simulates an electron (initial state |+>) in a magnetic field and returns <X>.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        float: Expectation value for the Pauli X operator.
    """
    evolve_plus_state(B, time)
    return qml.expval(qml.PauliX(0))

@qml.qnode(dev)
def mag_z_plus_Y(B, time):
    """Simulates an electron (initial state |+>) in a magnetic field and returns <Y>.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        float: Expectation value for the Pauli X operator.
    """
    evolve_plus_state(B, time)
    return qml.expval(qml.PauliY(0))

##################
# HIT SUBMIT FOR #
# PLOTTING MAGIC #
##################
'''
