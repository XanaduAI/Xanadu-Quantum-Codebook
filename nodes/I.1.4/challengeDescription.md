---

We now know how to perform the beginning and end of a quantum algorithm. We can
write down the state of a qubit (in other words, "prepare the state"), and using
the amplitudes we can simulate the outcomes of measuring it. All we're missing
is the step in between: manipulating the qubit in an interesting way!

Qubit states are vectors; to manipulate the vector we need something that we can
apply to it that will produce another vector. Furthermore, the new vector
must also be a valid, normalized quantum state. What object can we use to
achieve this?

Here we turn to linear algebra; quantum operations are represented as
matrices. In fact, they are a special type of matrix called a **unitary**
matrix. For some $2 \times 2$ complex-valued unitary matrix $U$, the state of
the qubit after an operation is

$$
\begin{equation}
\vert \psi^\prime \rangle = U \vert \psi \rangle.
\end{equation}
$$

You'll learn all about the properties of unitary matrices and some commonly used
ones in the upcoming nodes. For now, let's simulate the process.

---

***Codercise I.1.4.*** Complete the function below to apply the provided quantum
   operation ``U`` to an input state.

<details>
  <summary><i>Example.</i></summary>

  Consider the following unitary matrix and qubit state vector:

  <pre>
  U = np.array([[0, 1], [1, 0]])
  state = np.array([0.8, 0.6])</pre>

  If we apply ``U`` to ``state``, we will receive the vector 

  <pre>
  np.array([0.6, 0.8])</pre>

  You can see that the output is still a valid normalized quantum state.
</details>

