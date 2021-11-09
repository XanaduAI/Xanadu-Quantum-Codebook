"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''def ham_close_spins(B, J):
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    hbar = 1e-34
    ##################
    # YOUR CODE HERE #
    ##################
    coeffs = [] # MODIFY THIS
    obs = [] # MODIFY THIS
    return qml.Hamiltonian(coeffs, obs)
'''
