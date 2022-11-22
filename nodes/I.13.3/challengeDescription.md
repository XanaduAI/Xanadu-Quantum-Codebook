It takes three $CNOT$s to implement a $SWAP$:

<img src="pics/swap-cnots.svg" width=300>

Note that since $SWAP$ is symmetric, we can just as well turn this circuit
"upside down" and change the direction of all the $CNOT$s.

---

The next gates we'll explore have more than 2 qubits. The **Toffoli** is an
extremely important gate in both quantum computing, and the realm of *classical
reversible computing*, for which it is a *universal* gate. A computation is
reversible if it is possible to run it both forwards and backwards (note that
quantum computing is inherently reversible; the operations are unitary, and can
be implemented backwards by taking the inverse, which is the adjoint of each
operation). For example, a normal AND gate acting on two bits $a$ and $b$ is
*not* reversible:


<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> $ab$ </th>
  <th> $AND(ab)$ </th>
 </tr>
 <tr>
  <td style="text-align:center">  00 </td>
  <td style="text-align:center">  0 </td>
 </tr>
 <tr>
  <td style="text-align:center">  01 </td>
  <td style="text-align:center">  0 </td>
 </tr>
 <tr>
  <td style="text-align:center">  10 </td>
  <td style="text-align:center">  0 </td>
 </tr>
 <tr>
  <td style="text-align:center">  11 </td>
  <td style="text-align:center">  1 </td>
 </tr>
</table>

We cannot determine, from the result of AND$(ab)$, what $a$ and $b$ were (unless
the result is 1). But by adding another bit to store the result, we can make a
reversible AND: the Toffoli.

\begin{equation}
TOF (abc) =  ab (c \oplus (a \cdot b)). \tag{1}
\end{equation}

The operation keeps the two bits we are taking the AND of intact, and adds the
results modulo 2 to a third bit, $c$. The quantum equivalent of Toffoli acts on
the computational basis states in the same way:

\begin{equation}
TOF|abc\rangle = |ab(c\oplus {a \cdot b))\rangle. \tag{2}
\end{equation}

Now, the AND operation only products a non-zero result when the first two bits
are 1; when this is true, it adds 1 to the bit $c$, which is equivalent to
performing a NOT gate (flipping the bit). For this reason, the Toffoli is also
known as a controlled-controlled-NOT. Instead of controlling on the state of
just one qubit, we control on the state of two. That means that the NOT, or $X$,
is applied only if *both* qubits are in the state $\vert 1\rangle$. In a
circuit, the Toffoli gate looks like this:

<img src="pics/toffoli.svg" width="100px">

In PennyLane, [`qml.Toffoli`](https://docs.pennylane.ai/en/stable/code/api/pennylane.Toffoli.html)
is called using the following syntax:

```python
def circuit():
    qml.Toffoli(wires=[control1, control2, target])
```

Notice that this is similar to the 2-qubit controlled gates we've seen, but that
we must specify all three qubits in the list in the correct order.

***Codercise I.13.3.*** Now that you've learned about the Toffoli gate, can you
   use it to construct a **controlled SWAP** operation?

*Tip.* The controlled-$SWAP$ gate is sometimes known as the **Fredkin gate**.