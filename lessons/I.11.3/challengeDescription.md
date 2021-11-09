---

***Codercise I.11.3.*** Write a PennyLane circuit that creates the state
   $|1-\rangle = |1\rangle \otimes |-\rangle$. Then, measure the expectation
   value of the *two-qubit observable* $Z \otimes X$. In PennyLane, you can
   combine observables using the `@` symbol to represent the tensor product,
   e.g., `qml.PauliZ(0) @ qml.PauliZ(1)`.