---

Indeed, the state you obtained by running this circuit,

$$
\begin{equation}
\frac{1}{\sqrt{2}} \left( \vert 00 \rangle + \vert 11 \rangle \right)
\end{equation}\tag{2}
$$
is a very famous entangled state called a **Bell state**. Try as you might, you
will not be able to separate this state into a tensor product of two
single-qubit states. The $CNOT$, then, is an entangling gate.

Entanglement is a hallmark of quantum computing and part of what allows us to
do interesting things. Therefore, it is sensible that the $CNOT$, or another
entangling gate, is part of a **universal gate set** for multi-qubit
computation.  The $CNOT$, together with any universal gate set for single-qubit
computation (such as $H$ and $T$, or $RY$ and $RZ$), forms a universal gate
set. The fact that you can perform *any* quantum computation, on any number of qubits,
with just 3 gates is really quite amazing!

While in principle the $CNOT$ is the only two-qubit gate you need, it is often
convenient to express algorithms using more general **controlled
operations**.

<img src="pics/cu.svg" width="100px">

PennyLane contains a number of common controlled operations, for
example,
[`qml.CRX`](https://docs.pennylane.ai/en/stable/code/api/pennylane.CRX.html),
[`qml.CRY`](https://docs.pennylane.ai/en/stable/code/api/pennylane.CRY.html)
and
[`qml.CRZ`](https://docs.pennylane.ai/en/stable/code/api/pennylane.CRz.html). These
implement the appropriate rotation depending on the state of the control
qubit. For example,

$$
\begin{align*}
CRX(\theta) \vert 00\rangle &= \vert 00\rangle, \\
CRX(\theta) \vert 10\rangle &= \vert 0\rangle \otimes \left(\cos(\theta/2) \vert 0\rangle -i \sin(\theta/2)\vert 1\rangle \right).
\end{align*}\tag{3}
$$

We can apply such operations in PennyLane as we did for `RX`, `RY`, and `RZ` by
passing a parameter. We must also specify the wires they act on just like `CNOT`.

```python
def circuit(theta):
    qml.CRX(theta, wires=[control, target])
```

---

***Codercise I.12.3.*** Write a circuit in PennyLane that implements the
   following sequence of operations. Return the measurement outcome
   probabilities.

<img src="pics/circuit_i-12-3.svg" width="400px">