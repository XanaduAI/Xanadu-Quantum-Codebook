"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''@qml.qnode(dev)
def quantum_memory(beta_list):
    """
    Produce a data state with positive coefficients beta_list.

    Args:
        beta_list (list[float]): The amplitudes for our superposition.

    Returns: 
        list[float]: The state on both address and data registers.
    """
    U_list = [np.identity(2), np.identity(2), 
              np.identity(2), np.identity(2)] # MODIFY THIS
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

beta_list = [1, 0, 0, 1]
normalized_coefficients = [quantum_memory(beta_list)[i].item() for i in range(0, 20, 5)]
print("The amplitudes on the main register are proportional to", normalized_coefficients, ".")
'''
