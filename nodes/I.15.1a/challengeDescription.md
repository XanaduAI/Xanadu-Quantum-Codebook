One of the most famous (and most media-hyped) algorithms in quantum computing is
**teleportation**.

<img src="pics/teleportation-annotated.svg" width="500px">

In this node, we're going to implement the teleportation algorithm from end to
end. Teleportation is a protocol that transfers the state of a qubit held by one
party to that of a qubit held by a second party; the key ingredient is that the
parties share a pair of entangled qubits.

---

***Codercise I.15.1.*** (a) Prepare your favourite single-qubit quantum state on
   the first qubit in the `state_preparation` function below. It can be
   anything, as long as it's a single qubit state (you can even leave the function
   as-is, or make it parametrized!).

   Note that this quantum function will be used as a subroutine; therefore you do
   not need to return a measurement or create a QNode.