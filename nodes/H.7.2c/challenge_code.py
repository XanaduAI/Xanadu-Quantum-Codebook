"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''U_list = [np.kron(qml.PauliX.matrix, qml.PauliX.matrix),
          np.kron(qml.PauliZ.matrix, qml.PauliZ.matrix),
          np.kron(qml.PauliX.matrix, qml.PauliZ.matrix),
          np.kron(qml.PauliZ.matrix, qml.PauliX.matrix)]
alpha_list = [1, 0.5, 0.5, 1]

@qml.qnode(dev)
def my_circuit():
    """Apply H(X + Z/2) to the state |11> using LCU."""
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

print("The amplitudes on the main register are proportional to", my_circuit()[:4], ".")
'''
