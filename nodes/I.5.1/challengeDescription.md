In the previous exercise, you found that applying the sequence of operations
`[Hadamard, PauliX, Hadamard]` to the computational basis states had the
following effect:

$$
\begin{align*}
\vert 0\rangle &\rightarrow \vert 0\rangle, \\
\vert 1\rangle &\rightarrow -\vert 1\rangle.
\end{align*} \tag{1}
$$

The sign of the state changed, but the measurement outcome probabilities didn't!
This factor of $-1$ that affects the whole ket is called a **global phase**.

This sequence of operations corresponds to another well known gate, known as the
**Pauli $Z$** gate (denoted $Z$), or the **phase flip** gate.  Applying $Z$
"flips the phase" (i.e., multiplies the phase by $-1$) of the $\vert 1\rangle$
state, while leaving the $\vert 0\rangle$ state intact. In PennyLane, you can
implement it by calling <a
href="https://docs.pennylane.ai/en/stable/code/api/pennylane.PauliZ.html"
target="_blank"><tt>qml.PauliZ</tt></a>. It has the following circuit element:

<img src="pics/z.svg" alt="" width="100px">


---

***Codercise I.5.1.*** Write a QNode that applies `qml.PauliZ` to the $\vert
   +\rangle$ state and returns the state. What state is this? How do the
   measurement probabilities differ from those of $\vert +\rangle$?