---

Any closed quantum system evolves by a unitary, but we are going be most interested in doing stuff with $n$ qubits. Since the vector space of states of $n$ qubits is $2^n$-dimensional, a unitary is just some $2^n \times 2^n$ matrix with the property that $U^\dagger U = I$. We can throw any such $U$ into a circuit!

<img src="pics/Ugate.svg" width="350px">

---

***Codercise H.2.2.*** Create a circuit which applies a matrix if it is correctly sized and unitary using ``unitary_check(operator)``, and otherwise does nothing. You will need the [``qml.QubitUnitary``](https://docs.pennylane.ai/en/stable/code/api/pennylane.QubitUnitary.html) gate from PennyLane.
