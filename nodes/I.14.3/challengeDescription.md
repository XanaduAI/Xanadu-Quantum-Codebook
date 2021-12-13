*Solution*. All of these operations can be expressed as controlled operations,
 but controlled on different states. Since each operation will "trigger" only on
 a specific input state, we can apply them one after another in a circuit:

<img src="pics/challenge-exercise.svg" width="300px">

We now need to re-express, or *compile* these gates in terms of the Toffoli
available in PennyLane.

For the first gate, a controlled-controlled-$X$ is simply a Toffoli. Since one of the
controls is controlling on 0, we must apply an $X$ both before and after the
controls.

For the second gate, recall that $Z = HXH$, and that a controlled $Z$ consisted
of $H$, CNOT, and $H$. Thus, a Toffoli has a similar identity, and a
controlled-controlled-$Z$ ($CCZ$) can be implemented using a Toffoli and
application of $H$ on both sides of the target qubit. Again, since one of the
controls is $0$, we have to apply $X$ before and after.

For the final gate, we need the identity $Y = S X S^\dagger$, meaning we can
implement a controlled-controlled-$Y$ by applying $S^\dagger$ and $S$ before and
after a Toffoli respectively. Our final circuit is thus

<img src="pics/challenge-exercise-unrolled.svg" width="650px">
