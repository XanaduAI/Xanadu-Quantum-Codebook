*Solution*. The four circuits are

<img src="pics/bell-circuits.svg" width="600px">

There may be some variation as well; for example, to create
$\frac{1}{\sqrt{2}}(\vert 00\rangle - \vert 11\rangle)$, the $Z$ gate can be applied
to either qubit to obtain the same result.

---

***Codercise I.14.2.***
Implement a 3-qubit circuit in PennyLane that can perform the following:
 
 - If the first two qubits are both $\vert 0\rangle$, do nothing
 - If the first qubit is $\vert 0\rangle$ and the second is $\vert 1\rangle$, apply `PauliX` to the third qubit
 - If the first qubit is $\vert 1\rangle$ and the second is $\vert 0\rangle$, apply `PauliZ` to the third qubit
 - If the first two qubits are both $\vert 1\rangle$, apply a `PauliY` operation the third qubit

The circuit must produce the exact state that would be obtained by applying
these operations, i.e., not just up to a global phase.

There is no need to use any `if` statements in your part of the quantum
function; it can all be implemented using quantum operations alone!

*Tip*. This type of operation is called a **quantum multiplexer**. When all
 $2^n$ possible cases of $n$ control qubits are implemented, and the target
 operation is a single-qubit rotation, it is called a **uniformly controlled
 rotation**.

<details>
  <summary><i>Hint.</i></summary>

If you're not sure how to start, consider the following small circuit.

<img src="pics/multiplexer_hint.svg" width="300px">

If the state of the first qubit is $\vert 0 \rangle$, is the $RZ$
applied to the second qubit? Similarly, if the state of the first qubit is $\vert 1 \rangle$,
is the $RY$ applied?

</details>

<details>
  <summary><i>Hint.</i></summary>

The only doubly-controlled operations implemented in PennyLane are the Toffoli
and the controlled-$SWAP$. To implement the controlled-controlled-$Y$ and $Z$,
you'll have to use some circuit identities to relate these back to the Toffoli,
(which is a controlled-controlled-$X$). What gate can we use to turn an $X$ into
a $Z$? Or an $X$ into a $Y$?

</details>