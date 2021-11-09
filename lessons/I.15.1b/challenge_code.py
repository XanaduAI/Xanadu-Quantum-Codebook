"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''dev = qml.device("default.qubit", wires=1)

##################
# YOUR CODE HERE #
##################

# OPTIONALLY REPLACE THIS STATE PREPARATION ROUTINE WITH
# THE ONE FROM THE PREVIOUS EXERCISE

def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def state_prep_only():
    state_preparation()
    return qml.state()

print(state_prep_only())
'''
