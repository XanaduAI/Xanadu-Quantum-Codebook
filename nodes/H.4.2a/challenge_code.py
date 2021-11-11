"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''n_bits = 5
dev = qml.device("default.qubit", wires=n_bits)
    
##################
# YOUR CODE HERE #
##################
coeffs = [1] # MODIFY THIS
obs = [qml.PauliZ(0)] # MODIFY THIS
H = qml.Hamiltonian(coeffs, obs)

@qml.qnode(dev)
def energy(init):
    """Circuit for measuring expectation value of Hamiltonian in a given state.
    
    Args:
        init (list[int]): An initial computational basis state, specified by five bits.

    Returns: 
        float: Expectation value of the Hamiltonian H.
    """
    qml.BasisState(init, wires=range(n_bits))
    return qml.expval(H)'''
