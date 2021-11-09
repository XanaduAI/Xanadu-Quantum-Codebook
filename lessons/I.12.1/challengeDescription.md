The most straightforward type of multi-qubit operation is **separable**. This is
what you were doing in the previous node: every qubit gets acted on
by single-qubit gates, and there are no interactions between them. However,
multi-qubit states can be **entangled**. There are some two-qubit states
$|\Psi\rangle$ such that it simply is not possible to write

$$
\begin{equation}
\vert \Psi \rangle = \vert \psi \rangle \otimes \vert \varphi\rangle,
\end{equation}\tag{1}
$$

where $\vert \psi\rangle, \vert \varphi\rangle$ are single-qubit states.

Regular states can be turned into entangled states using **entangling
operations**. Operations are considered entangling if there is at least one
separable, tensor-product state of qubits that it transforms into an entangled
state.

The prime example of such an operation is the controlled-NOT, or **CNOT** gate
(also sometimes written as "CX"). This gate applies a Pauli $X$ gate to a **target
qubit** only if a **control qubit** is in state $|1\rangle$. You'll recognize
its circuit diagram element from earlier nodes:

<img src="pics/cnot.svg" width="200px">

(The first depiction is far more common; the control qubit is the one with the
small solid dot, and the target qubit is the one being acted on by the $X$
operation.)

In PennyLane, CNOTs can be applied using [`qml.CNOT`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.CNOT.html)
and the following syntax:

```python
def circuit():
    qml.CNOT(wires=[control, target])
```

where `control` and `target` are the wire labels (e.g., `qml.CNOT(wires=[0, 1])`).

---

***Codercise I.12.1.*** Write a circuit that implements a $CNOT$ gate between two
   qubits. Test it out on all four computational basis states. What are the
   resulting states? Express your answer in a dictionary that takes the form
   of a *truth table*, i.e., a table that details a set of output bits given the
   set of input bits:

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $\vert ab\rangle$ </th>
  <th> $CNOT \vert ab\rangle$ </th>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 00\rangle$ </td>
  <td style="text-align:center">  $\vert ??\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 01\rangle$ </td>
  <td style="text-align:center">  $\vert ??\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 10\rangle$ </td>
  <td style="text-align:center">  $\vert ??\rangle$ </td>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 11\rangle$ </td>
  <td style="text-align:center">  $\vert ??\rangle$ </td>
 </tr>
</table>

As an explicit example, the truth table of $X$ is 

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $\vert b\rangle$ </th>
  <th> $X\vert b\rangle$ </th>
 </tr>
 <tr>
  <td style="text-align:center">  $\vert 0\rangle$ </td>
  <td style="text-align:center">  $\vert 1\rangle$ </td>
 <tr>
  <td style="text-align:center">  $\vert 1\rangle$ </td>
  <td style="text-align:center">  $\vert 0\rangle$ </td>
 </tr>
</table>