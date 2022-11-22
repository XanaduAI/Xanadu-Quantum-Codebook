---

## Uniform superposition

You might have noticed that we've been using this operation a lot:

$$
    U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1& -1   \end{pmatrix}. \tag{2}
$$

This is one of the most famous operations in all of quantum computing. It is
called the **Hadamard gate**, and is typically denoted by *H*. In PennyLane, it
is implemented as <a
href="https://docs.pennylane.ai/en/stable/code/api/pennylane.Hadamard.html"
target="_blank"><tt>qml.Hadamard</tt></a> In a circuit diagram, it is
represented as:

<img src="pics/h.svg" alt="" width="150px">

The Hadamard is special because it can create a *uniform superposition* of the
two states $|0\rangle$ and $|1\rangle$.

---

***Codercise I.4.2.*** What do you think is meant by *uniform superposition*?
   Let's explore this using PennyLane. Complete the quantum function below such
   that it:

 - applies a Hadamard gate to the qubit, 
 - returns the *state* of the qubit with `qml.state`.