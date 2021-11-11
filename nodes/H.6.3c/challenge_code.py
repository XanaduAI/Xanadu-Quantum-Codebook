"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''aux = [0, 1]
main = 2
all_bits = range(3)
dev = qml.device("default.qubit", wires=all_bits)

# Part (i)

@qml.qnode(dev)
def first_approx(t):
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

# Part (ii)

@qml.qnode(dev)
def second_approx(t):
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

# Part (iii)

@qml.qnode(dev)
def full_series(t):
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

##################
# HIT SUBMIT FOR #
# PLOTTING MAGIC #
##################
'''
