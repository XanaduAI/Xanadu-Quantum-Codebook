---

**Learning outcomes**

 - *Construct the state of a multi-qubit system using the tensor product.*
 - *Define and apply separable operations to multiple qubits.*
 
---

## The tensor product

Recall that single-qubit states live in a Hilbert space, which is a
2-dimensional vector space spanned by basis vectors $\vert 0\rangle$ and $\vert
1\rangle$. In order to work with multiple qubits, we must learn how these vector
spaces compose. Hilbert spaces are combined using an operation called the
**tensor product**. This operation is best understood through example. Suppose
we have a pair of two-dimensional vectors (e.g., two single-qubit states). The
tensor product can be computed like so:

$$
\begin{equation}
\begin{pmatrix} a \\ b \end{pmatrix} \otimes \begin{pmatrix} c \\ d \end{pmatrix} = \begin{pmatrix} a \begin{pmatrix} c \\ d \end{pmatrix} \\ b \begin{pmatrix} c \\ d \end{pmatrix} \end{pmatrix} = \begin{pmatrix} ac \\ ad \\ bc \\ bd \end{pmatrix}.
\end{equation}\tag{1}
$$

The tensor product also applies to the unitary operations that act on
qubits. For example,

$$
\begin{equation}
\begin{pmatrix} a & b \\ c & d \end{pmatrix} \otimes \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}
= \begin{pmatrix} a  \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} & b  \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}\\ c  \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} & d  \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} \end{pmatrix} = \begin{pmatrix}
 a\alpha & a\beta & b\alpha & b\beta \\
 a\gamma & a\delta & b\gamma & b\delta \\
 c\alpha & c\beta & d\alpha & d\beta \\
 c\gamma & c\delta & d\gamma & d\delta
 \end{pmatrix}.
\end{equation}\tag{2}
$$

## Multi-qubit bases

***Exercise I.11.1.*** The two-qubit computational basis consists of 4 vectors:
   $\vert 0\rangle \otimes \vert 0\rangle$, $\vert 0\rangle \otimes \vert
   1\rangle$, $\vert 1 \rangle \otimes \vert 0\rangle$, and $\vert 1\rangle
   \otimes \vert 1\rangle$. These vectors constitute every possible pairing of
   two qubits in the two possible single-qubit basis states. Apply the tensor
   product to evaluate the 4-dimensional basis vectors. What do you notice about
   these vectors?
 
<details>
  <summary><i>Solution.</i></summary>

Let's work these out using the tensor product formula above:

$$
\begin{align*}
\vert 0\rangle \otimes \vert 0\rangle &= \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes  \begin{pmatrix} 1 \\ 0 \end{pmatrix} =  \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \\
\vert 0\rangle \otimes \vert 1\rangle &= \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes  \begin{pmatrix} 0 \\ 1 \end{pmatrix} =  \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \\
\vert 1\rangle \otimes \vert 0\rangle &= \begin{pmatrix} 0 \\ 1 \end{pmatrix} \otimes  \begin{pmatrix} 1 \\ 0 \end{pmatrix} =  \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \\
\vert 1\rangle \otimes \vert 1\rangle &= \begin{pmatrix} 0 \\ 1 \end{pmatrix} \otimes  \begin{pmatrix} 0 \\ 1 \end{pmatrix} =  \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}. 
\end{align*}
$$

There are two things to note here: the first is that each vector contains only a
single 1! This makes it clear that we have a basis, because we can create any $4
\times 1$ complex-valued vector by taking a linear combination of these basis
states. The second point relates to where exactly the 1 sits in the vector. This
is related to the binary expression of the product of basis states. For example,
$\vert 0\rangle \otimes \vert 0\rangle$ has a 1 in the zero'th entry, which
corresponds to `00` in binary. The vector $\vert 1\rangle \otimes \vert
0\rangle$ has a 1 in the second entry (indexing from 0) - `10` is 2 in
binary. Thus, to construct an arbitrary basis vector, instead of taking a tensor
product, you can just create a vector with a 1 at the element that corresponds
to that basis state's binary representation! ▢

</details>

---

*Tip*. To avoid writing so many $\otimes$ symbols, multi-qubit states are often
 abbreviated by concatenating the bits and stuffing them inside a single
 ket. For example, the 4-qubit state $\vert 0\rangle \otimes \vert 1\rangle
 \otimes \vert 1\rangle \otimes \vert 0\rangle$ becomes $\vert 0110\rangle$,
 which takes much less effort to write!

---

***Exercise I.11.2.*** Consider the number and size of the vectors in the
   2-qubit computational basis; how many vectors do you expect to have in the
   3-qubit computational basis, and what size will they be? Generalize this
   result to an $n$-qubit system (this should be a clear indication of why we
   need to actually *build* quantum computers, rather than just simulating
   them!).

<details>
  <summary><i>Solution.</i></summary>

 The 3-qubit computational basis will consist of 8 vectors of length
 8. Every time another qubit is added, we multiply by 2, so an $n$-qubit system
 has $2^n$ basis vectors with $2^n$ elements. Consider that this also means
 that, to operate on such basis vectors, we'll need unitary matrices of size
 $2^n \times 2^n$. This exponential dependence means that simulating quantum
 computers will become computationally intractable very quickly. ▢

</details>

---

***Exercise I.11.3.*** Use the tensor product to compute the state vector of a
   two-qubit system where the first qubit is in state $\vert +\rangle$, and the
   second is in state $\vert 1\rangle$. Express that state as a linear
   combination of the two-qubit computational basis vectors, and verify that
   this state is still normalized.

*Tip*. There are two approaches to working this problem. One is to express the
 states as two vectors and take the tensor product. The other is to work at the
 level of computational basis states, and leverage the fact that the tensor
 product is *distributive*, i.e. $(\vert a\rangle + \vert b\rangle)\otimes \vert
 c\rangle = \vert a\rangle \otimes \vert c\rangle + \vert b\rangle \otimes \vert
 c\rangle$ (and similarly for matrices).

<details>
  <summary><i>Solution.</i></summary>

 We would like to compute $\vert +\rangle \otimes \vert 1\rangle$,
 where we recall that

$$
\vert +\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \vert 1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.
$$

Using the first method, we can compute

$$
\vert +\rangle \otimes \vert 1\rangle =  \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} \otimes \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ 1 \\ 0 \\ 1 \end{pmatrix}.
$$


By inspecting the basis vectors above, we find that $\vert +\rangle \otimes
\vert 1\rangle = \frac{1}{\sqrt{2}} \left( \vert 01\rangle + \vert 11\rangle
\right)$. The modulus square of all the vector entries sums to 1, and so our
state is still normalized.

For the second method, we can use the distributive property of the tensor
product and obtain the linear combination directly:

$$
\vert +\rangle \otimes \vert 1\rangle =  \frac{1}{\sqrt{2}} (\vert 0\rangle + \vert 1\rangle) \otimes \vert 1\rangle = \frac{1}{\sqrt{2}} (\vert 01\rangle + \vert 11\rangle).
$$

We can obtain the state vector by rewriting the computational basis states in
their vector form to obtain the same results as above. This method is much more
compact, but does take some time to get used to. ▢

</details>

---

## Separable operations

Operations on multiple qubits can take one of two forms. The first type looks
essentially like performing single-qubit operations on individual qubits, but in
a multi-qubit system, multiple single-qubit operations can be applied in
parallel.  We'll call these *separable* operations, because they can be
expressed simply as tensor products of individual qubit operations. For example,

<img src="pics/t-optimization-after.svg" alt="" width="400px">

You can imagine each "layer" of this circuit as a single multi-qubit
operation. For example, the first step in the circuit is to apply a Hadamard to
each qubit. This corresponds to applying $H \otimes H \otimes H$. The second
layer applies $S \otimes T \otimes T^\dagger$, and so on. While circuits are
read from left to right, the matrices are applied to the states from right
to left, i.e., the result of applying the first two layers of gates to an
input state $\vert \psi \rangle$ would be
$(S \otimes T \otimes T^\dagger)(H \otimes H \otimes H)\vert \psi \rangle$.

---

***Exercise I.11.4.*** Suppose we have two tensor product operations, $A \otimes
   B$, and $C \otimes D$. A cool fact is that if we multiply these two together,
   the multiplication works on each side of the tensor product independently,
   i.e., $(A \otimes B) \cdot (C \otimes D) = (AC) \otimes (BD)$. If you like,
   you can take a crack at proving this mathematically. However, there is a more
   intuitive way of understanding this: using a circuit diagram and your
   knowledge of how single- and two-qubit operations work, reason why this
   identity must hold.

<details>
  <summary><i>Hint.</i></summary>
Start by drawing the quantum circuit that applies $A \otimes B$ followed by $C \otimes D$,
then look at the operations acting on the individual qubits.
</details>

<details>
  <summary><i>Solution.</i></summary>

 Let's start by drawing what this would look like as a quantum
 circuit:

<img src="pics/tensor_product_identity_1.svg" alt="" width="250px">

We can think of it as $(A \otimes B) \cdot (C \otimes D)$ like so:

<img src="pics/tensor_product_identity_2.svg" alt="" width="250px">

However, since these are separable operations, the qubits are acted on
independently of each other, so we could just as well conceptually group the
operations together like so:

<img src="pics/tensor_product_identity_3.svg" alt="" width="250px">

Each qubit has two unitary operations acting on it; applying $C$ then $A$ to the
first qubit is equivalent to applying the combined operation $AC$, and similarly
for the second qubit. Thus, we can rewrite this circuit as

<img src="pics/tensor_product_identity_4.svg" alt="" width="200px">

which we can now see to be the tensor product $AC \otimes BD$. ▢

</details>