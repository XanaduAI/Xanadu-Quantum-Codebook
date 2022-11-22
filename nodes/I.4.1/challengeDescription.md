## Flipping bits

The simplest quantum operation has the following effect:

$$
\begin{align*}
U|0\rangle &= |1\rangle, \\
U|1\rangle &= |0\rangle.
\end{align*} \tag{1}
$$

This is called a **bit flip**, or NOT operation. It is also known as the **Pauli
X**, or $X$ gate, and can be found in PennyLane as <a
href="https://docs.pennylane.ai/en/stable/code/api/pennylane.PauliX.html"
target="_blank"><tt>qml.PauliX</tt></a>. There are two ways to write it in a
quantum circuit:

<img src="pics/x.svg" alt="" width="150px">

When applying a single-qubit $X$ operation, we will use the first notation, an
$X$ in a box.

---

***Codercise I.4.1.*** A common use of the $X$ gate is in initializing the state
   of a qubit at the beginning of an algorithm. Quite often, we would like our
   qubits to start in state $\vert 0 \rangle$ (which is the default in
   PennyLane), however there are many cases where we instead would like to start
   from $|1\rangle$. Complete the function below by using `qml.PauliX` to
   initialize the qubit's state to $\vert 0 \rangle$ or $\vert 1 \rangle$ based
   on an input flag. Then, use `qml.QubitUnitary` to apply the provided `U`.

<details>
  <summary><i>Hint.</i></summary>

The `PauliX` operation is a non-parametrized gate, meaning to call it in PennyLane,
all we need to do is specify the wires:

<pre>
qml.PauliX(wires=wire)</pre>

</details>