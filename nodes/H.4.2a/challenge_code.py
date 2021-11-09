"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''n_bits = 5
dev = qml.device("default.qubit", wires=n_bits, shots=None)


##################
# YOUR CODE HERE #
##################
    
coeffs = [1] # MODIFY THIS
obs = [qml.PauliZ(0)] # MODIFY THIS
H = qml.Hamiltonian(coeffs, obs)

# Specify circuit
def circuit(init, **kwargs):
    """Circuit for initializing state.
    
    Args:
        init (list): An initial computational basis state, specified by five bits.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    pass

# Invoke ExpvalCost
cost_fn = qml.ExpvalCost(circuit, H, dev)
'''
