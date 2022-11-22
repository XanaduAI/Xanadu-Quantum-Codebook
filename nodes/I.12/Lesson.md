---

**Learning outcomes**
 
 - *Define and apply entangling operations to multi-qubit systems.*
 - *Define the controlled-NOT (CNOT) gate, and write its matrix representation.*
 - *Define and apply general controlled operations.*
 
---

## Mathematics of entangled states

We now come to a very important property of quantum systems:
**entanglement**. Along with superposition, entanglement is one of the two
hallmark features of quantum computing that underscore its
advantage. Entanglement is used as a *resource* in many quantum algorithms,
including quantum teleportation, which you will explore later in this
module. The following two-part exercise will show you what it means for a
multi-qubit state to be entangled.

---

***Exercise I.12.1.*** *(a)*

Suppose we have two single-qubit states

$$
\vert \psi_1\rangle = \alpha \vert 0\rangle + \beta \vert 1 \rangle, \quad \vert \psi_2\rangle = \gamma \vert 0\rangle + \delta \vert 1\rangle.
$$

Take the tensor product of these two states to express $\vert \psi_1\rangle
\otimes \vert \psi_2\rangle$ as a linear combination of two-qubit computational
basis states. Use the distributive property of the tensor product rather than
working with explicit vectors.


<details>
  <summary><i>Solution.</i></summary>


The tensor product of these two states can be computed as follows:

$$
\begin{align*}
\vert \psi_1\rangle \otimes \vert \psi_2\rangle 
&= (\alpha \vert 0\rangle + \beta \vert 1 \rangle) \otimes (\gamma \vert 0\rangle + \delta \vert 1\rangle) \\
&= \alpha \vert 0\rangle \otimes  (\gamma \vert 0\rangle + \delta \vert 1\rangle) + \beta \vert 1 \rangle \otimes \left(\gamma \vert 0\rangle + \delta \vert 1\rangle \right) \\
&= \alpha \gamma \vert 00\rangle + \alpha\delta \vert 01\rangle + \beta\gamma\vert 10\rangle + \beta\delta\vert 11\rangle.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

*(b)* Consider the state

$$
\vert \psi\rangle = \frac{1}{\sqrt{2}} \left( \vert 00\rangle + \vert 11\rangle \right).
$$

Using the results of the previous exercise, show that you cannot find two single-qubit states
that tensor together to create this state.

<details>
  <summary><i>Solution.</i></summary>

We can see this as follows. Given the previous exercise, we need to find
$\alpha, \beta, \gamma, \delta$ that satisfy the following set of equations:

$$
\begin{align*}
 \alpha \gamma &= 1, \\
 \alpha \delta &= 0, \\
 \beta \gamma &= 0, \\
 \beta \delta &= 1.
\end{align*}
$$

Each variable appears in two equations, one of which is equal to 1, and the
other 0. But for any of the 0 ones to be true, we'd need at least one variable
to be 0, and that would immediately contradict the other equation it is
part of where the solution is 1. Therefore, there is no solution, and we can't
describe this state as two separate qubits, so they are entangled! ▢

</details>

---

By definition, a state is **entangled** if it cannot be described as a tensor
product of individual qubit states (if it can, it is **separable**). An entangled state
can only be described by specifying the full state. Entanglement generalizes to
larger systems as well. For example, a famous 3-qubit entangled state is the
Greenberg-Horne-Zeilinger, or GHZ state:

$$
\vert \hbox{GHZ}\rangle = \frac{1}{\sqrt{2}} (\vert 000\rangle + \vert 111\rangle).\tag{1}
$$

Quantum states with more than two qubits may also have varying degrees of
entanglement. The GHZ state above is **fully entangled**, as none of the qubits
can be written independently of the others. However, one can create states
such as


$$
\frac{1}{2} \left(\vert 000\rangle + \vert 100\rangle + \vert 011\rangle + \vert 111\rangle \right) =
\frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle ) \otimes \frac{1}{\sqrt{2}} (\vert 00\rangle + \vert 11\rangle),\tag{2} 
$$

where some qubits (the second and third) are entangled with each other,
but others (the first one) are not. Such a state is called **bipartite** because
it can be split into two subsystems.

## The CNOT gate

You might be wondering how it is possible to make such a state, since
thus far we've only encountered multi-qubit operations that consist of tensor
products of single-qubit operations. What we need are *entangling gates*:
operations that involve interactions between qubits. An **entangling gate** is
an operation that transforms *some* separable state into an entangled state. It
doesn't have to be every state. In fact for many of the examples you'll see,
they may only be entangling for qubits already in superpositions, and not for
the individual computational basis states. Like entangled states, entangling
gates *cannot* be rewritten as a tensor product of individual single-qubit
gates.

The most important entangling gate is the **controlled-NOT**, or **CNOT**
gate. This is a two-qubit gate that performs an operation (specifically, a Pauli
$X$ or "NOT" gate) on one qubit depending on the state of another.


<img src="pics/cnot.svg" width="200px">

Its matrix representation is 

$$
    CNOT = \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 1 & 0
    \end{pmatrix}. \tag{3}
$$

The first qubit, denoted with the solid dot, is the **control qubit**. The state
of this qubit does not change, but its state is the one that determines whether
the operation is performed. The second qubit is the **target qubit**.


---

***Exercise I.12.2.*** Evaluate the action of $CNOT$ on the computational basis
   states $\vert ab\rangle$, where the first qubit is the control, and second
   qubit is the target. How do they change? Can you express how the second bit
   transforms based on the first using a Boolean function of $a$ and $b$?



<details>
  <summary><i>Solution.</i></summary>

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $\vert ab\rangle$ </th>
  <th> $CNOT_{ab}\vert ab\rangle$ </th>
 </tr>
 <tr>
  <td style="text-align:center"> $\vert 00\rangle$ </td>
  <td style="text-align:center"> $\vert 00\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $\vert 01\rangle$ </td>
  <td style="text-align:center">$\vert 01\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $\vert 10\rangle$ </td>
  <td style="text-align:center"> $\vert 11\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $\vert 11\rangle$ </td>
  <td style="text-align:center"> $\vert 10\rangle$ </td>
 </tr>
</table>

The $CNOT$ performs an effective XOR operation by adding the first bit to the
second bit modulo 2: $CNOT\vert ab\rangle = \vert a(b\oplus a)\rangle$. ▢

</details>

---

***Exercise I.12.3.*** Suppose that instead of the first qubit being the control
   and the second the target (which we denote as $CNOT_{ab}$), we exchange their
   roles. Given a state $\vert ab\rangle$, the state $\vert b\rangle$ determines
   whether an $X$ is applied to the state $\vert a \rangle$. Determine the action of this
   operation on the computational basis states; use this to recover the matrix
   representation of the $CNOT$ gate $CNOT_{ba}$, acting on the qubits "backwards".


<details>
  <summary><i>Solution.</i></summary>

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $\vert ab\rangle$ </th>
  <th> $CNOT_{ba}\vert ab\rangle$ </th>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 00\rangle$ </td>
  <td style="text-align:center">  $\vert 00\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 01\rangle$ </td>
  <td style="text-align:center">  $\vert 11\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 10\rangle$ </td>
  <td style="text-align:center">  $\vert 10\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 11\rangle$ </td>
  <td style="text-align:center">  $\vert 01\rangle$ </td>
 </tr>
</table>

Note that $CNOT$ simply permutes the basis states. We can write this in matrix
form as

$$
    \hbox{CNOT} = \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0
    \end{pmatrix}.
$$

<div align="right"> ▢ </div>

</details>

---

## Universal gate sets

Earlier, we learned about universal gate sets for single-qubit operations. What
about for multi-qubit operations? It turns out that we just need one more gate:
the $CNOT$. The sets $\{CNOT, H, T\}$, $\{CNOT, RY, RZ\}$ are both universal gate
sets for multi-qubit computation. Isn't that amazing?

While we could do everything with just the $CNOT$ gate, it is just one of many possible
controlled operations. Any operation, on any number of qubits, can be
implemented as a controlled operation, controlled on the state of one or more
other qubits. For example, an arbitrary controlled unitary on two qubits is
expressed like so:


<img src="pics/cu.svg" width="100px">

The matrix representation of a 2-qubit controlled operation has a block
structure

$$
    CU = \begin{pmatrix}
    I_2 & 0 \\
    0 & U \\
    \end{pmatrix},\tag{4}
$$

where $I_2$ is the $2\times 2$ identity matrix, and the $0$ are $2\times 2$ zero
matrices.

---

***Exercise I.12.4.*** Determine the action of a controlled-Hadamard gate on the
   two-qubit computational basis. You can write out the matrix, but try also to
   work it out using only bra-ket notation and your knowledge of how the Hadamard
   affects the single-qubit computational basis states.


<details>
  <summary><i>Solution.</i></summary>

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $\vert ab\rangle$ </th>
  <th> $CH\vert ab\rangle$ </th>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 00\rangle$ </td>
  <td style="text-align:center">  $\vert 00\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 01\rangle$ </td>
  <td style="text-align:center">  $\vert 01\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 10\rangle$ </td>
  <td style="text-align:center">  $\frac{1}{\sqrt{2}}(\vert 10\rangle + \vert 11\rangle)$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 11\rangle$ </td>
  <td style="text-align:center">  $\frac{1}{\sqrt{2}}(\vert 10\rangle - \vert 11\rangle)$ </td>
 </tr>
</table>

<div align="right"> ▢ </div>

</details>

---

*Pro tip*. When applying a controlled-$U$ to two adjacent qubits, creating the
 matrix representation is straightforward: we simply insert the $4\times 4$
 matrix in place of two $2 \times 2$ matrices. Suppose we have a 4-qubit system,
 and we apply a Hadamard to the first and last qubit, and a controlled-$U$ from
 the second qubit to the third. The matrix representation would be

$$
 H \otimes CU \otimes H,\tag{5}
$$

which would produce a $16\times 16$ matrix. 

Now suppose we want to apply the controlled-$U$ from qubit 1 to 3. How can we
take the tensor product of something like this? We can't just put in the
matrix because there's a qubit in the middle! The trick lies in noting the block
structure of the matrix, and re-writing it like so, for a system of two qubits:

$$
\begin{pmatrix}
 1 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 \\
 0 & 0 & U_{11} & U_{12} \\
 0 & 0 & U_{21} & U_{22} \\
\end{pmatrix} = 
\vert 0\rangle \langle 0\vert  \otimes I + \vert 1\rangle \langle 1 \vert  \otimes U.\tag{6}
$$

We can interpret this as projections. When the first qubit is in state $\vert
0\rangle$, the first term will trigger and an $I$ will be applied to the second
qubit. But if the first qubit is $\vert 1\rangle$, the other term triggers and
$U$ is applied to the second qubit.

Now that we have a sum of tensor products, we can apply them to the relevant
parts of the system, and linearity allows us to add them together. Let's return
to the 4-qubit example and suppose we apply Hadamards to qubits 2 and 4, and a
controlled-$U$ between qubits 1 and 3. The matrix representation is found by
expanding:

$$
\vert 0\rangle \langle 0\vert  \otimes H \otimes I \otimes H + \vert 1\rangle \langle 1\vert  \otimes H \otimes U \otimes H.\tag{7}
$$

This trick works for any controlled operation on any pair of qubits, including
in "reverse" order — simply exchange the order of the terms in the sum of tensor
products.