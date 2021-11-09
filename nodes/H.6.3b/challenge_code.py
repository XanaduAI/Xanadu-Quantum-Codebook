"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''def exp_U_second(U, t):
    """
    Implement the second-order approximation of exp(tU).
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        t (float): A time to evolve by.
    """
    qml.QubitUnitary(V(t), wires=aux[0])    
    def subcircuit():
        ##################
        # YOUR CODE HERE #
        ##################
        pass
    qml.PauliX(wires=aux[0])
    # ADD CONTROLLED OPERATION HERE
    qml.PauliX(wires=aux[0])
    qml.QubitUnitary(np.transpose(V(t)), wires=aux[0])
'''
