---

**Learning outcomes**
 
 - *Define and apply a set of common multi-qubit operations: the controlled-$Z$, Toffoli, and SWAP gates.*
 - *Express common 3-qubit operations in terms of 1- and 2-qubit operations.*

---

## Controlled-$Z$

The **controlled-$Z$** gate is similar in spirit to the controlled-NOT gate.
The difference is that rather than applying an $X$ controlled on a qubits state,
we apply a $Z$. Its matrix representation is

$$
    CZ = \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & -1
    \end{pmatrix}.
$$

It also has two different representations in circuit diagrams; the first is more
common, however they are used quite interchangeably, unlike the $CNOT$ where
there is a more well-defined preference.

<img src="pics/cz.svg" width="200px">

The controlled-$Z$ gate is also known as the $CZ$ gate, or the **controlled
phase** gate.

---

***Exercise I.13.1.*** As we did for the $CNOT$, compute the action of
   controlled-$Z$ on the computational basis states. Do this for two cases:
   for the first qubit as control and the second qubit as target, and for the second qubit as control and first
   qubit as target. What do you notice about these two cases?


<details>
  <summary><i>Solution.</i></summary>

It doesn't matter in which the direction the control goes; you'll
 always get the same output! The controlled-$Z$ gate is *symmetric*.

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $\vert ab\rangle$ </th>
  <th> $CZ\vert ab\rangle$ </th>
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
  <td style="text-align:center">  $\vert 10\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 11\rangle$ </td>
  <td style="text-align:center">  $-\vert 11 \rangle$ </td>
 </tr>
</table>

<div align="right"> ▢ </div>

</details>

---

***Exercise I.13.2.*** Earlier, we worked out that $Z = HXH$. Using this knowledge,
can you express $CZ$ in terms of $H$ and $CNOT$?

<details>
  <summary><i>Solution.</i></summary>

At first, you might write down the circuit

<img src="pics/cz_cnot_controlled_h.svg" width="300px">

This is correct, however the controls on the $H$ aren't actually necessary.

<img src="pics/cz_cnot.svg" width="300px">

You can understand why by considering the case where the first qubit is in state
$\vert 0 \rangle$. The $CNOT$ will not be applied; since $H$ is its own inverse,
the two $H$ simply cancel out!  If instead the first qubit is in state $\vert 1
\rangle$, then $HXH = Z$ is applied to the second qubit. ▢

</details>


---

## The SWAP gate

The **SWAP gate** is exactly what it sounds like: it exchanges the state of two
qubits:

$$
SWAP( \vert \psi\rangle \otimes \vert \varphi\rangle ) = \vert \varphi\rangle \otimes \vert \psi\rangle.
$$

It is denoted by the following circuit element:

<img src="pics/swap.svg" width="100px">

---

***Exercise I.13.3.*** Deduce the matrix form of the $SWAP$ gate by considering
   how it acts on the computational basis states.


<details>
  <summary><i>Solution.</i></summary>

You'll find that $|00\rangle$ and $|11\rangle$ are unchanged, but
 $|01\rangle$ and $|10\rangle$ are exchanged. Therefore, the matrix
 representation is

$$
\begin{equation}
    SWAP = \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 1
    \end{pmatrix}.
\end{equation}
$$

<div align="right"> ▢ </div>

</details>

---


## The Toffoli gate

Earlier we mentioned that we could make controlled operations with any number of
qubits. By far the most common such gate is the **Toffoli gate**. The Toffoli
has two control qubits, and behaves effectively like a controlled-$CNOT$, or
controlled-controlled-NOT. Its matrix representation is below:

$$
    \hbox{TOF} = \begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0\\
    \end{pmatrix}.
$$

Its circuit element is 

<img src="pics/toffoli.svg" width="100px">

which looks precisely like a controlled-$CNOT$.

---

***Exercise I.13.4.*** Determine the action of the Toffoli gate on the 3-qubit
   computational basis states. Look closely at the structure of the qubit
   states; can you find a mathematical relationship between the first two
   control bits and the target bit after the operation?


<details>
  <summary><i>Hint.</i></summary>

 We are working with bits, and so are dealing with a Boolean
 function. Consider which states actually get affected by the Toffoli — what
 Boolean operation produces a non-zero result only for those states when fed the
 two control bits? What other Boolean operation can be applied to use that
 result to modify the target bit?
</details>


<details>
  <summary><i>Solution.</i></summary>

The action of the Toffoli is


<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $\vert abc\rangle$ </th>
  <th> $TOF \vert abc\rangle$ </th>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 000\rangle$ </td>
  <td style="text-align:center">  $\vert 000\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 001\rangle$ </td>
  <td style="text-align:center">  $\vert 001\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 010\rangle$ </td>
  <td style="text-align:center">  $\vert 010\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 011\rangle$ </td>
  <td style="text-align:center">  $\vert 011\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 100\rangle$ </td>
  <td style="text-align:center">  $\vert 100\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 101\rangle$ </td>
  <td style="text-align:center">  $\vert 101\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 110\rangle$ </td>
  <td style="text-align:center">  $\vert 111\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 111\rangle$ </td>
  <td style="text-align:center">  $\vert 110\rangle$ </td>
 </tr> 
</table>


If you look closely at the bits, you'll find that $TOF|abc\rangle = |ab(c\oplus
(a\cdot b))\rangle$. The value of the AND of bits $a$ and $b$ gets added to the third
bit modulo 2. ▢

</details>

---

As a final point, in a previous section, we discussed quantum circuit synthesis.
We now know that $\{CNOT, H, T\}$ is a universal gate set for multi-qubit
gates. That means we should be able to decompose gates like the Toffoli gate
down into 1- and 2-qubit gates. Often, this can be done in multiple different ways. For
example, the following two circuits below both implement the Toffoli gate:

<img src="pics/toffoli-decomp.svg" width="400px">

<img src="pics/toffoli-decomp_2.svg" width="450px">

You can see that each of them require the same number of $T$ gates, however the
$T$ depth is different, as is the number of $CNOT$s. The one you would choose if
you were implementing a circuit in practice depends on a number of factors, such
as how easy it is to perform two-qubit operations in your physical system (if
it's hard, better to choose the second implementation since it uses fewer
$CNOT$s), or the maximum depth you can implement, if your system is noisy and the
qubits have a low *coherence time* (the first circuit has lower depth, so would
be better in such a situation).

---

***Exercise I.13.5.*** Another common 3-qubit operation is the
   controlled-controlled-$Z$ ($CCZ$).

<img src="pics/ccz.svg" width="200px">

Using what you know about controlled operations, $Z$, and the Toffoli gate,
express the $CCZ$ as a sequence of 1- and 2-qubit operations.


<details>
  <summary><i>Solution.</i></summary>

We know a decomposition for the Toffoli gate, so if we can re-express $CCZ$ in
terms of the Toffoli, then we can recover the decomposition quite easily. Recall that
we can express a $CZ$ in terms of $H$ and $CNOT$; we can extrapolate to the $CCZ$ case:

<img src="pics/ccz_toffoli.svg" width="300px">

Thus, we need only take our Toffoli decomposition, and apply a Hadamard on each
side. In fact, if you look at both decompositions above, there is already a
Hadamard on the third qubit at the start and end of the circuit! These will
cancel out, leaving us with the following circuit for $CCZ$:

<img src="pics/ccz_decomp.svg" width="400px">

When working with large quantum circuits, it is often possible to perform small
**circuit optimizations** like this, such as cancelling adjacent inverse gates,
merging two adjacent rotation gates of the same type, etc. Generally, we would
like automated tools to do this for us, though, as the task becomes cumbersome
very quickly. ▢

</details>