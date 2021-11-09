---

The idea of a controlled-controlled-NOT generalizes to
   an arbitrary number of controls. Furthermore, there are many applications in
   quantum computing where the "polarities" of the control gates are mixed,
   i.e., on some qubits you may want to control on a qubit being in the state
   $\vert 0\rangle$, rather than $\vert 1\rangle$. This is generally accomplished
   by first applying a Pauli $X$ to the control qubit to switch its state to $\vert 1 \rangle$,
   applying the gate controlled on $\vert 1 \rangle$ as per usual, and then applying
   another Pauli $X$ to return the control qubit back to normal.

---

***Codercise I.13.4.*** In PennyLane, mixed-polarity multi-controlled Toffoli
gates can be easily implemented using the
[`MultiControlledX`](https://pennylane.readthedocs.io/en/latest/code/api/pennylane.MultiControlledX.html)
operation. With this gate, a string of control bits, `control_values`, can be
specified as an input argument. Write a 4-qubit PennyLane circuit that applies a
Hadamard to the control qubits, then applies a `MultiControlledX` on the fourth
qubit, controlled on the first 3 qubits being in the state $\vert
001\rangle$. This is depicted in the circuit below: "control on 0" is denoted by
an open circle on the control qubits, rather than a filled circle. What do you
expect will happen to the target qubit?

<img src="pics/mcx.svg" width="100px">