"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''aux = 0
main = 1
n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

def add_two_unitaries(U, V):
    """A circuit to apply the sum of two unitaries non-deterministically.
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        V (array): A unitary matrix, stored as a complex array.
    """
    qml.Hadamard(wires=aux)
    ##################
    # YOUR CODE HERE #
    ##################
    qml.Hadamard(wires=aux)
'''
