"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''def mag_z_unitary(B, time):
    """Creates unitary operator to evolve state of electron in magnetic field.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time (t) we evolve the electron state for.
        
    Returns:
        array[float]: The unitary matrix implementing time evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    ##################
    # YOUR CODE HERE #
    ##################
    matrix = np.array([[0, 0], [0, 0]]) # CHANGE THIS
    return matrix

B, t = 0.1, 0.6
if unitary_check(mag_z_unitary(B, t)):
    print("The output is unitary for B =", B, "and t =", t, ".")
'''
