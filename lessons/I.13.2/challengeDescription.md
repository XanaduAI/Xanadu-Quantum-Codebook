---

***Codercise I.13.2.*** The **SWAP** operation ([`qml.SWAP`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.SWAP.html)) exchanges the states of two qubits. 

<img src="pics/swap.svg" width="100px">

The $SWAP$ can be implemented using only $CNOT$s. In the code below, try to find the
sequence of $CNOT$s to match the output state to that produced by a $SWAP$.


<details>
  <summary><i>Hint.</i></summary>

 Consider what happens when you apply a $CNOT$ twice; from there, deduce
 how sequences of them must combine in order to have the desired effect.

</details>