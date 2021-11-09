After measuring $0$ on the auxiliary qubit, the main register is in a state proportional to $H\vert 0\rangle = \vert +\rangle$. This is what we expect, since $X + Z \propto H$.

---

It turns out that this circuit generalizes to a sum of unitaries

$$
\tilde{U} = U_0 + U_1 + \cdots + U_{K-1},
$$

provided the number of unitaries happens to be a binary power, $K = 2^k$. In that case, we can associate a binary control string to each component unitary $U_j$, which is just the expansion of $j$ in binary. Here is the circuit:

<img src="pics/su-circuit.svg" width="650px">

The section in the middle is called the *multiplexer* or **SELECT
subroutine**. The Hadamards acting on the auxiliary register are
called the **PREPARE subroutine**.

---

***Codercise H.6.2.*** (a) Finish the code below to implement the
   SELECT subcircuit.

*Hint.* Use [``qml.ControlledQubitUnitary``](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.ControlledQubitUnitary.html).
