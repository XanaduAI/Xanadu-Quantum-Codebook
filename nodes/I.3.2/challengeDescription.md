---

Since unitary matrices have such special properties, you might be wondering if
there is a more prescribed way to construct them. It is hard to write down a
unitary matrix arbitrarily at random, element by element. Fortunately,
unitary matrices can be **parametrized**. A single-qubit unitary operation
can be expressed in terms of just three real numbers:

$$
U(\phi, \theta, \omega) = \begin{pmatrix} e^{-i(\phi + \omega)/2} \cos(\theta/2) & -e^{i(\phi - \omega)/2} \sin(\theta/2) \\ e^{-i(\phi - \omega)/2} \sin(\theta/2) & e^{i(\phi + \omega)/2} \cos(\theta/2)  \end{pmatrix}. \tag{2}
$$

In PennyLane, this parametrized operation is implemented as a gate called
<a href="https://docs.pennylane.ai/en/stable/code/api/pennylane.Rot.html" target="_blank"><tt>Rot</tt></a>. `Rot` takes three parameters, which are precisely the angles in the formula above:

<code>

    qml.Rot(phi, theta, omega, wires=wire)

</code>

---

***Codercise I.3.2.*** Apply the `Rot` operation to a qubit using the input
   parameters. Then, complete the QNode to return the quantum state vector,
   using `qml.state()`.
