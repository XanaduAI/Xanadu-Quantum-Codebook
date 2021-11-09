"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

challenge_code = '''dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.
    
    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE BASIS STATE
    
    return qml.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")
'''
