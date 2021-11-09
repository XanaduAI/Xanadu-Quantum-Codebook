"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''def V(t):
    """Matrix for the PREPARE subroutine."""
    return np.array([[np.sqrt(t)/np.sqrt(t+1), -1/np.sqrt(t+1)],
                    [1/np.sqrt(t+1), np.sqrt(t)/np.sqrt(t+1)]])

def exp_U_first(U, t):
    """
    Implement the first two terms in the Taylor series for exp(tU).
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        t (float): A time to evolve by.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    pass
'''
