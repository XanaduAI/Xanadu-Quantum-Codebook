In a combination lock, a combination is either right (the lock opens) or wrong (it doesn't). We can describe this using a function $f: \{0, 1\}^n \to \{0, 1\}$ which says "right" or "wrong" in binary, for a secret combination $\mathbf{s}$:

$$
f(\mathbf{x}) =
  \begin{cases}
    1 & \mathbf{x} = \mathbf{s} \\
    0 & \text{otherwise}.
  \end{cases}
$$

We can also represent these answers as a (unitary) matrix, since this
tells us explicitly how it acts on states by matrix multiplication.
$U_f$ acting on computational basis states as follows:

$$
\begin{align*}
  U_f\vert \mathbf{x}\rangle & = (-1)^{f(\mathbf{x})}\vert
  \mathbf{x}\rangle \\
  & =
    \begin{cases}
    -\vert \mathbf{x}\rangle & \mathbf{x} = \mathbf{s} \\
    \vert \mathbf{x}\rangle & \text{otherwise}.
  \end{cases}
\end{align*}
$$

Equivalently, we can write the matrix $U_f$ in terms of bras and kets:

$$
U_f = I - 2 \vert \mathbf{s}\rangle\langle \mathbf{s}\vert.
$$

This is called an **oracle**, and applying it is called a **query**. It tells us when the combination is
correct by flipping the sign, so we can try to incorporate it into our
lock-breaking circuit. Let's start by creating the oracle operation as
a matrix.
The simplest way to do this is to create the $2^n \times 2^n$ *identity matrix*

$$
I =
\begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
&& \ddots & \\
 0& \cdots &  & 1
\end{bmatrix},
$$

and then simply change the entry corresponding to the solution from
$+1$ to $-1$.

---

***Codercise A.2.1.*** Write a function which returns the oracle in matrix form for a given secret combination.
