"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''dev = qml.device("default.qubit", wires=1)

input = 0 # MODIFY EXAMPLE
reps = 1
print("The probability distribution after applying the secret box to ", input)
print("a total of ", reps, "time(s) is ")
# We will secretly apply the function and return the result!

@qml.qnode(dev)
def quantum_box(bit, reps):
    """Implements the secret quantum rule on a single (qu)bit.
    
    Args:
        bit (int): A bit representing an initial condition.
        reps (int): Number of times gate is repeated.

    Returns:
        list[float]: The output probability distribution.
    """
    if bit == 1:
        qml.PauliX(wires=0)
    for _ in range(reps):
        ##################
        # YOUR CODE HERE #
        ##################
        pass
    return qml.probs(wires=0)
'''
