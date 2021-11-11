"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''@qml.qnode(dev)
def XH_plus_HZ():
    """Apply XH + HZ to |01> and return the state."""
    U_list = [np.kron(qml.PauliX.matrix, qml.PauliX.matrix),
              np.kron(qml.PauliZ.matrix, qml.PauliZ.matrix),
              np.kron(qml.PauliX.matrix, qml.PauliZ.matrix),
              np.kron(qml.PauliZ.matrix, qml.PauliX.matrix)]
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

print("The amplitudes on the main register are proportional to", XH_plus_HZ()[:4], ".")
'''
