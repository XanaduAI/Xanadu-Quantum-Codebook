"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''@qml.qnode(dev)
def mag_z_0_v2(B, time):
    """
    Simulates an electron (initial state |0>) in a magnetic field, using a Z rotation.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

B, t = 0.1, 0.6
if np.allclose(mag_z_0_v1(B, t), mag_z_0_v2(B, t)):
    print("The two circuits give the same answer!")
'''
