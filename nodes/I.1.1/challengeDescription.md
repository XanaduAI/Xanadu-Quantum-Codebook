All modern classical computation is done using binary digits, or bits. Instead
of regular bits, which take one of two values (0 or 1), quantum computing uses
**qubits**. Qubits are physical systems that,
just like bits, can exist in a "0" state and a "1" state. For now, you can think
of these two states like the two sides of a coin, "heads" or "tails".

Mathematically, the state of a qubit is written as a complex-valued vector with
two elements. These vectors, or "state vectors", are denoted by the symbol
$\vert \cdot \rangle$, which is called a **ket** (this is known as **Dirac
notation**). The qubit's "0" and "1" states are expressed as follows:

$$
\begin{equation}
\vert 0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \vert 1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \tag{1}
\end{equation}
$$

The element sitting within the $\vert \cdot \rangle$ is the label for that
state. These two vectors might look familiar; they look just like the two
basis vectors you would use for drawing vectors on a 2-dimensional plane. In
fact, these two states form a **basis** for single-qubit states called
the **computational basis**. 

As a consequence of this mathematical description, unlike a bit, a qubit is not
limited to being in one of these two states. Qubits can exist in what's known as a
**superposition** of states. A superposition is a linear combination of two
basis vectors.  Mathematically,

$$
\vert \psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \tag{2}
$$

where $\alpha$ and $\beta$ are **complex** numbers. These $\alpha$ and $\beta$
are called **amplitudes**, and for a state to be valid they must be chosen carefully
to satisfy the following criteria:

$$
\begin{equation}
\vert \alpha\vert ^2 + \vert \beta\vert ^2 = \alpha \alpha^* + \beta \beta^* = 1, \tag{3}
\end{equation}
$$

where the * indicates the complex conjugate. When $\alpha$ and $\beta$ satisfy
this property, a quantum state is called **normalized**. When a qubit is in a
superposition, it is not in both $\vert 0 \rangle$ and $\vert 1 \rangle$
"simultaneously", but is rather in some intermediate combination of the two. If
you consider again the analogy of a coin, if $\vert 0 \rangle$ and $\vert 1
\rangle$ are "heads" and "tails", a superposition would be like a coin spinning
on its edge.

---

***Codercise I.1.1.*** Suppose we are given an unnormalized quantum state

$$
\vert \psi \rangle = \alpha \vert 0 \rangle + \beta \vert 1 \rangle, \quad |\alpha|^2 + |\beta|^2 \neq 1.
$$

We can turn this into an equivalent, valid quantum state by *normalizing* it. Write a
function that, given $\alpha$ and $\beta$, normalizes this state to

$$
\vert \psi^\prime \rangle = \alpha^\prime  \vert 0 \rangle + \beta^\prime \vert 1 \rangle, \quad |\alpha^\prime|^2 + |\beta^\prime|^2 = 1.
$$

<details>
  <summary><i>Example.</i></summary>

  Suppose we are given the inputs

  <pre>
  alpha = 2.0 + 1.0j
  beta = -0.3 + 0.4j </pre>

  Your function should return the vector

  <pre>
  np.array([ 0.87287156+0.43643578j, -0.13093073+0.17457431j]) </pre>

  which represents the qubit state

  $$
  \begin{equation}
      \vert \psi \rangle =  (0.87287156+0.43643578i) \vert 0 \rangle + (-0.13093073+0.17457431i) \vert 1 \rangle.
  \end{equation}
  $$

</details>

<details>
  <summary><i>Hint.</i></summary>

What we must do here is essentially *rescale* the coefficients of the state
vector such that it has unit length. Consider how you would do so for a
real-valued vector; then determine how to manipulate the amplitudes in the
complex case.

</details>

