To implement Grover search, we need to give circuit-friendly constructions of the oracle and diffusion operators; arbitrary matrices are hard to build! To help us, we introduce an extra qubit called the **auxiliary qubit**. The original $n$ qubits are called the **query register**:

<img src="pics/grover-iter-1.svg" width="400px">

Here, $\hat{U}$ and $\hat{D}$ refer to operators which act not only on the query register but also the auxiliary qubit. We've also omitted the $f$ subscript to simplify our notation a little.
To implement the behaviour of an oracle, the $n$ query qubits can be used to trigger a phase flip on the auxiliary qubit when they are in the solution state. More concretely, we can do this using a multi-controlled $X$ gate with control string $\mathbf{s}$, and the auxiliary register in the $\vert -\rangle$ state:

$$
\hat{U}(\vert \mathbf{x} \rangle\otimes \vert -\rangle) =
\begin{cases}
\vert \mathbf{x}\rangle \otimes X\vert -\rangle = -\vert \mathbf{x}\rangle \otimes \vert -\rangle & \text{ if } \mathbf{x} = \mathbf{s} \\
\vert \mathbf{x}\rangle \otimes \vert -\rangle & \text{otherwise.}
\end{cases}
$$

This method is called the **phase kickback trick**, since the phase is "kicked back" to the query register. Here is a picture of the implementation of $\hat{U}$:

<img src="pics/oracle-circuit.svg">

(Recall that white dots indicate the control bit is "0" and black dots "1". The combination here is simply meant to illustrate an arbitrary control string.)

---

***Codercise G.3.1.*** Define the oracle operator $\hat{U}$ using the [``MultiControlledX``](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.MultiControlledX.html) gate from PennyLane.

*Tip.* ``MultiControlledX(control_wires, wires, control_values)`` has a specified set of ``control_wires``, a single target wire given by ``wires``, and a string of control values, e.g., ``control_values = "1011"`` rather than a list of bits  ``[1,0,1,1]``.
