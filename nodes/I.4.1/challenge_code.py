"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''dev = qml.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qml.qnode(dev)
def varied_initial_state(state):
    """Complete the function such that we can apply the operation U to
    either |0> or |1> depending on the input argument flag.
    
    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.
  
    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    # KEEP THE QUBIT IN |0> OR CHANGE IT TO |1> DEPENDING ON THE state PARAMETER

    # APPLY U TO THE STATE


    return qml.state()
'''
