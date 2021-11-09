---

***Codercise I.15.3.*** Implement a quantum function, `rotate_and_controls`, that
performs both a change of basis, and the controlled gates at the end circuit.

<img src="pics/teleportation-4part.svg" width="500px">

Note that the `rotate_and_controls` function does not a return a measurement
here; this is because when we put all the subroutines together in the full
teleportation protocol, we will need *that* quantum function to return a
measurement in order to be bound into a QNode.
