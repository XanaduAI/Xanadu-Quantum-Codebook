---

**Learning outcomes**:
 
 - *Explain why we can understand how an operation works by applying it to the basis states.*
 - *Describe the action of the X gate, its matrix representation, and eigenvalues.*
 - *Describe the action of the Hadamard gate, its matrix representation, and eigenvalues.*
 
---

## Describing quantum operations

Expressing unitary operations in their parametrized form, or even matrix form in
general, is quite cumbersome. Before we see some actual gates, it is useful to
learn some shorthand for describing how operations work.

Suppose we have an operation $U$. As long as we know how $U$ acts on the two
computational basis states, we can use that as a shortcut to evaluate its action
on any other state. Let's assume that $U$ does the following to the
computational basis states:

$$
\begin{align*}
 U \vert 0\rangle &= \alpha \vert 0\rangle + \beta \vert 1\rangle, \\
 U \vert 1\rangle &= \gamma \vert 0\rangle + \delta \vert 1\rangle. \\
\end{align*} \tag{1}
$$

To evaluate the action of $U$ on an arbitrary state, $\vert \psi\rangle = p\vert
0\rangle + q\vert 1\rangle$, we take advantage of the fact that matrix-vector
multiplication is **linear**:

$$
\begin{equation}
 U \vert \psi \rangle = U (p\vert 0\rangle + q \vert 1\rangle) = U(p \vert 0\rangle) + U(q\vert 1\rangle) = p\cdot U\vert 0\rangle + q \cdot U\vert 1\rangle.
\end{equation} \tag{2}
$$

---

***Exercise I.4.1***. Finish evaluating the above expression to express $U\vert
   \psi\rangle$ as a linear combination of the two basis states.

<details>
  <summary><i>Solution.</i></summary>
  
$$
\begin{align*}
U \vert \psi \rangle &= p\cdot U\vert 0\rangle + q \cdot U\vert 1\rangle \\
& = p (\alpha \vert 0\rangle + \beta \vert 1\rangle) + q (\gamma \vert 0 \rangle + \delta \vert 1 \rangle)\\
& = (p\alpha + q \gamma) \vert 0 \rangle + (p\beta + q\delta) \vert 1 \rangle.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

---

While avoiding matrix multiplication doesn't save us much time in this small
case, as you start to work with multiple qubits, you'll learn very quickly that
the matrices will get in the way! In what follows, we will primarily work with
ket notation.

In addition to the action of a gate on the computational basis states, there are
a few other properties of gates that are handy to have. Their matrix
representations are still valuable, even if we don't want to perform any
explicit computations with it. Instead, we use them to obtain their eigenvalues
and eigenvectors. Furthermore, we would like to know how to graphically
represent them in a quantum circuit. In a later node, we will provide a
convenient reference table with all this information.

## Pauli X

The first gate we will explore is the Pauli $X$ gate. This operation is
represented by the following unitary matrix $X$:

$$
\begin{align*}
X\vert 0\rangle &= \vert 1\rangle, \\
X\vert 1\rangle &= \vert 0\rangle. 
\end{align*} \tag{3}
$$

This is also known as the **bit flip** operation, or **NOT gate**, due to its
similarity to the Boolean NOT operation. From its action on the basis states,
it is straightforward to deduce that $X$ should have the following form (you can
check this by hand, too):

$$
\begin{equation}
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
\end{equation}. \tag{4}
$$

There are two representations of $X$ used in quantum circuits:

<img src="pics/x.svg" alt="" width="150px">

The first, an $X$ in a box, is far more common. The second, a circle with a
vertical line, in some special cases where $X$ is involved in a 2-qubit
operation (you might remember these from the graphics in I.2). While this
notation can be still be used for the single-qubit gate, it is rarely
encountered in the wild.

---

***Exercise I.4.2.*** Compute the eigenvalues and normalized eigenvectors of the
   $X$ operation (you'll want to keep these in mind for the future!). Express
   the eigenvectors in ket notation as linear combinations of the basis kets.

<details>
  <summary><i>Solution.</i></summary>

The eigenvectors of $X$ are $ \begin{pmatrix} 1 \\ 1  \end{pmatrix}$ and $ \begin{pmatrix} 1 \\ -1  \end{pmatrix}$. As a normalized linear combination of basis kets, the eigenvectors can be represented in the following way:

$$
\begin{align*}
 \vert v_1 \rangle = \frac{1}{\sqrt{2}} \left( \vert 0 \rangle + \vert 1 \rangle \right), \\
 \vert v_2 \rangle = \frac{1}{\sqrt{2}} \left( \vert 0 \rangle - \vert 1 \rangle \right). \\
\end{align*}
$$

Their associated eigenvalues are $\lambda_1 = 1$ and $\lambda_2 = -1$ respectively. ▢

</details>

---

## Hadamard

The next operation we will meet is one of the most famous in quantum computing:
the **Hadamard gate**. It is typically denoted by $H$, and represented as such
in a circuit diagram:

$$
    H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1& -1   \end{pmatrix} \tag{5}
$$

<img src="pics/h.svg" alt="" width="100px">

The Hadamard is special because it can create a *uniform superposition* of the
two states $\vert 0\rangle$ and $\vert 1\rangle$:

$$
\begin{align*}
 H\vert 0\rangle &= \frac{1}{\sqrt{2}} (\vert 0\rangle + \vert 1\rangle), \\
 H\vert 1\rangle &= \frac{1}{\sqrt{2}} (\vert 0\rangle - \vert 1\rangle).
\end{align*} \tag{6}
$$

These two states occur so often that they have special labels based on the sign
of the amplitudes:
    
$$
\begin{align*}
 \vert +\rangle &= \frac{1}{\sqrt{2}} (\vert 0\rangle + \vert 1\rangle), \\
 \vert -\rangle &= \frac{1}{\sqrt{2}} (\vert 0\rangle - \vert 1\rangle).
\end{align*} \tag{7}
$$ 

---

***Exercise I.4.3.*** What happens when we apply a Hadamard gate twice to an
   input state, e.g., $HH\vert 0\rangle$ or $HH\vert 1\rangle$? Work out the
   result using bra-ket notation.

<details>
  <summary><i>Solution.</i></summary>

Using bra-ket notation, and taking advantage of the linearity of matrix-vector
multiplication,

$$
\begin{align*}
HH \vert 0 \rangle
&= H \left( \frac{1}{\sqrt{2}} \left( \vert 0 \rangle + \vert 1 \rangle \right) \right) \\
&= \frac{1}{\sqrt{2}} \left( H \vert 0 \rangle + H \vert 1 \rangle \right) \\
&= \frac{1}{\sqrt{2}} \left( \frac{1}{\sqrt{2}} \left(\vert 0 \rangle + \vert 1 \rangle \right) + \frac{1}{\sqrt{2}} \left( \vert 0 \rangle - \vert 1 \rangle \right) \right) \\
&= \frac{1}{2} \left( \vert 0 \rangle + \vert 1 \rangle + \vert 0 \rangle - \vert 1 \rangle \right) \\
&= \vert 0 \rangle.
\end{align*}
$$

Thus, $HH\vert 0\rangle = \vert 0\rangle$ and similarly, you can work out that 
$HH\vert 1\rangle = \vert 1\rangle$. The Hadamard is its own inverse, and it can
both create and destroy uniform superpositions! The behaviour will be extremely
useful later when we start exploring its use in quantum algorithms.  ▢

</details>

---

***Exercise I.4.4.*** Show that together, $\vert + \rangle$ and $\vert - \rangle$
constitute an *orthonormal basis* for single-qubit states, i.e., they are normalized,
and orthogonal. (This basis is called the Hadamard basis.)

<details>
  <summary><i>Solution.</i></summary>

First, let's show that the two are normalized. If a state is normalized, taking the
inner product with itself should give us precisely 1:

$$
\begin{align*}
 \langle + \vert + \rangle &= \frac{1}{2} \left( \langle 0 \vert + \langle 1 \vert\right)\left(\vert 0 \rangle + \vert 1 \rangle \right) \\
 &=  \frac{1}{2} \left(  \langle 0 \vert 0 \rangle + \langle 0 \vert 1 \rangle + \langle 1 \vert 0 \rangle + \langle 1 \vert 1 \rangle \right) \\
 &= \frac{1}{2}( 1 + 0 + 0 + 1) \\
 &= 1, \\
 \langle - \vert - \rangle &= \frac{1}{2} \left(\langle 0 \vert - \langle 1 \vert\right)\left(\vert 0 \rangle - \vert 1 \rangle \right) \\
 &= \frac{1}{2} \left(  \langle 0 \vert 0 \rangle - \langle 0 \vert 1 \rangle - \langle 1 \vert 0 \rangle + \langle 1 \vert 1 \rangle \right) \\
 &= \frac{1}{2}( 1 - 0 - 0 + 1) \\
 &= 1.
\end{align*}
$$

Now let's check that the two are orthogonal. We can take their inner product in any order and will obtain the same result:

$$
\begin{align*}
 \langle - \vert + \rangle
 &= \frac{1}{2} \left( \langle 0 \vert - \langle 1 \vert \right)\left(\vert 0 \rangle + \vert 1 \rangle \right) \\
 &= \frac{1}{2} \left( \langle 0 \vert 0 \rangle + \langle 0 \vert 1 \rangle - \langle 1 \vert 0 \rangle - \langle 1 \vert 1 \rangle \right) \\
 &= \frac{1}{2}(1 + 0 - 0 - 1) \\
 &= 0.
\end{align*}
$$

Thus, $\vert + \rangle$ and $\vert - \rangle$ do indeed form an orthonormal basis. ▢


</details>
