Now that you've learned about $Z$ rotations, you might be wondering a few
things. First, we know how to change the phase of the amplitudes, but how
do we change their magnitudes?  Furthermore, two of our friends,
$H$ and $X$, don't fit this picture; are they maybe different kinds of
rotations?

The answer to this is of course yes. In addition to $RZ$, we also have $RX$
and $RY$. These are available in PennyLane as
[`qml.RX`](https://docs.pennylane.ai/en/stable/code/api/pennylane.RX.html) and
[`qml.RY`](https://docs.pennylane.ai/en/stable/code/api/pennylane.RY.html).


***Codercise I.6.1.*** Write a QNode that applies `qml.RX` with an angle of $\pi$ to
   one of the computational basis states. What operation is this?