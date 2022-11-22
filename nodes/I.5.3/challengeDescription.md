---

$Z$ is not the only such rotation that has a special name. In the previous
exercise, you found that $Z = RZ(\pi)$. This is also sometimes called a "half
turn around Z", since it is half of a full rotation of angle $2\pi$. The quarter
turn and eighth turn also have their own names: the **phase gate**, $S$, and the
**$T$ gate**:

<img src="pics/st.svg" alt="" width="150px">

In PennyLane, they are implemented directly as the non-parametrized operations
<a href="https://docs.pennylane.ai/en/stable/code/api/pennylane.S.html"
target="_blank"><tt>qml.S</tt></a> and <a
href="https://docs.pennylane.ai/en/stable/code/api/pennylane.T.html"
target="_blank"><tt>qml.T</tt></a>.

Now, if we can rotate forwards, we can also rotate backwards by negating the
angle. These rotations are unitary operations, meaning that $U^{-1} =
U^{\dagger}$. The conjugate transpose of $U$, $U^\dagger$, is also called the
**adjoint** of $U$. We can compute and apply adjoints with PennyLane, rather
than simply perform rotations with negative values, as taking the adjoint is
much more general.

---

***Codercise I.5.3.*** Adjoints in PennyLane can be computed by applying the <a
   href="https://docs.pennylane.ai/en/stable/code/api/pennylane.adjoint.html"
   target="_blank"><tt>qml.adjoint</tt></a> transform to an operation before
   specifying its parameters and wires. For example,

<code>

    qml.adjoint(qml.RZ)(phi, wires=0)

</code>

performs the same computation as `qml.RZ(-phi, wires=0)`. Implement the circuit
below, using adjoints when necessary, and return the quantum state.

<img src="pics/circuit_153.svg" alt="" width="400px">