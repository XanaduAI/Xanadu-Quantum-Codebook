---

**Learning outcomes**

- *Explain how the phase kickback trick works and why it is useful for Grover search.*
- *Implement diffusion and oracle operators using multi-controlled $X$ gates.*

---

Although we have a mathematical description of the oracle and
diffusion operators, we don't really have any idea how to implement
them in terms of standard gates inside our quantum computers. In this
section we'll discuss how to do so, starting with the oracle and using
the same approach for the diffusion operator.

The oracle adds a phase of $-1$ when it acts on $\vert\mathbf{s}\rangle$ and does nothing otherwise. This looks a lot like a controlled operation with a control string $\mathbf{s}$. The only problem is that if our $n$ qubits are triggering the controlled operation, then the controlled gate must be acting on something else! How can we bring the phase back?

The solution is simple: introduce an extra qubit, called the
**auxiliary qubit**, to store the phase! We call the original $n$
qubits the **query register**, since that's the place the solution to
our query is stored. (In general, there can be more than one auxiliary
qubit, in which case we call it the **auxiliary register.**) This strategy of shifting a phase from the auxiliary qubit to the query register is called the **phase kickback trick**, since the phase is "kicked back". We will see precisely how it works in a moment.

Let $\hat{U}$ and $\hat{D}$ refer to operators which act not only on the query register but on the auxiliary qubit, dropping the $f$ subscript to declutter our notation:

<img src="pics/grover-iter-1.svg" width="400px">

To start with, let's define our new oracle gate $\hat{U}$. It will act in an entirely classical way on bit strings, defined by

$$
\hat{U} \vert \mathbf{x}, y\rangle = \vert \mathbf{x}, y \oplus f(\mathbf{x})\rangle.
$$

Here, $\oplus$ just means addition modulo $2$, so $1 \oplus 1 = 0$. In the next exercise, you'll use this to implement the phase oracle.


---

***Exercise G.2.1.*** Show that $\hat{U} (\vert \mathbf{x}\rangle \otimes \vert -\rangle) = (-1)^{f(\mathbf{x})}\vert \mathbf{x}\rangle \otimes \vert -\rangle$.

<details>
<summary><i>Solution.</i></summary>

First, let's apply $\hat{U}$:

$$
\begin{align*}
\hat{U} (\vert \mathbf{x}\rangle \otimes \vert-\rangle) & = \frac{\hat{U}\vert \mathbf{x}0\rangle - \hat{U}\vert \mathbf{x}1\rangle}{\sqrt{2}} \\ & = \frac{\vert \mathbf{x}, 0 \oplus f(\mathbf{x})\rangle - \vert \mathbf{x}, 1\oplus f(\mathbf{x})\rangle}{\sqrt{2}}.
\end{align*}
$$

If $f(\mathbf{x}) = 0$, then $y \oplus f(\mathbf{x}) = y$, and the state is left alone. However, if $f(\mathbf{x}) = 1$, then $1$ and $0$ swap roles. This has the effect of multiplying the state by an overall phase $(-1)$! Thus, we multiply the state by $(-1)^{f(\mathbf{x})}$, so this has the same effect as applying the oracle $U$ (which does not involve the auxiliary qubit) to the query register. ▢

</details>

---

We haven't yet explained how to implement $\hat{U}$ at the circuit
level. We'll illustrate by considering a simple (and therefore bad!)
secret combination for our lock: $\mathbf{s} = \mathbf{1}$, where
every element is $1$. In this case, we only want to flip the phase of
$\vert \mathbf{x}\rangle$ if every bit has value $1$. This can be
achieved very simply using a multi-controlled $X$ gate. This is like
the usual CNOT gate, except with multiple control qubits. In the
simplest case, it acts on classical basis states (for the combined
system of query register and an auxiliary qubit) as follows:

$$
\text{C}^{(n)}\text{NOT}\vert \mathbf{x}, y\rangle =
\begin{cases}
\vert \mathbf{x}\rangle \otimes X\vert y\rangle & \text{ if } \mathbf{x} = \mathbf{1} \\
\vert \mathbf{x}, y\rangle & \text{otherwise.}
\end{cases}
$$

Here is a picture of the circuit:

<img src="pics/cnnot.svg" width="200px">

The top group of $n$ qubits are the control bits, and the qubit at the bottom is the target. Now, remember that $\vert -\rangle$ is an eigenstate of the Pauli $X$ gate:

$$
X \vert -\rangle = \frac{X\vert 0\rangle - X\vert 1\rangle}{\sqrt{2}} = \frac{\vert 1\rangle - \vert 0\rangle}{\sqrt{2}} = -\vert -\rangle.
$$

It follows that, for this choice of secret combination,

$$
\hat{U}\vert \mathbf{x}, y\rangle = \text{C}^{(n)}\text{NOT}\vert \mathbf{x}, y\rangle.
$$

Since these operators agree on basis states, they agree on all states,
so the oracle is just the C${}^{(n)}$NOT gate! In the next couple of
exercises, you can see how to extend this to other solutions.
We can extend this iterated CNOT gate to be controlled on an arbitrary bit
string $\mathbf{s}$.
Let's call this gate $C^{(\mathbf{s})}X$, so its action is

$$
C^{(\mathbf{s})}X\vert \mathbf{x}, y\rangle =
\begin{cases}
\vert \mathbf{x}\rangle \otimes X\vert y\rangle & \text{ if } \mathbf{x} = \mathbf{s} \\
\vert \mathbf{x}, y\rangle & \text{otherwise.}
\end{cases}
$$

---

***Exercise G.2.2.*** Show how to implement an oracle for an arbitrary solution $\mathbf{s}$ using a multi-controlled $X$ gate, and draw the circuit diagram (schematically).

<details>
<summary><i>Solution.</i></summary>

To obtain the oracle associated with a solution $\mathbf{s}$, we
simply use $C^{(\mathbf{s})}X$ instead of $C^{(n)}X$.
Let's check first that this acts correctly on the solution state:

$$
\begin{align*}
C^{(\mathbf{s})}X(\vert \mathbf{s}\rangle \otimes \vert -\rangle) & = \vert \mathbf{s}\rangle \otimes X\vert -\rangle \\ & = -\vert \mathbf{s}\rangle \otimes \vert -\rangle.
\end{align*}
$$

On the other hand, if $\mathbf{x}\neq\mathbf{s}$, it does nothing. So
in general,

$$
C^{(\mathbf{s})}X(\vert \mathbf{x}\rangle \otimes \vert -\rangle) = (U \vert \mathbf{x}\rangle) \otimes \vert -\rangle.
$$

The circuit diagram is then

<img src="pics/oracle-circuit.svg">

Recall that white nodes mean the control bit is ``0`` rather than ``1``. Here, we have used white and black nodes to indicate an arbitrary control string. ▢

</details>

---

Now you know how to implement an oracle on a quantum computer! The other component of the Grover iteration is diffusion, $D = 2\vert \psi\rangle\langle \psi\vert  - I$. This looks slightly different from the oracle, since we have the uniform superposition $\vert\psi\rangle$ appearing in the definition, rather than a computational basis state $\vert\mathbf{s}\rangle$. But with a simple trick—using a Hadamard transform on either side—we can apply exactly the same technique we used for the oracle.

---

***Exercise G.2.3.*** Show that the following circuit implements $-\hat{D}$.

<img src="pics/diffusion.svg">

<details>
<summary><i>Solution.</i></summary>

The effect of $-D = I - 2\vert \psi\rangle\langle \psi\vert$ is to flip $\vert \psi\rangle$ and leave any orthogonal states alone. Remember that $\vert \psi\rangle = H^{\otimes n}\vert \mathbf{0}\rangle$ and $H^{\otimes n} \cdot H^{\otimes n} = I$, so if $\vert \psi\rangle$ comes along in the query register then

$$
\vert \psi\rangle \overset{H^{\otimes n}}{\to} H^{\otimes n} \cdot H^{\otimes n} \vert \mathbf{0}\rangle = \vert \mathbf{0}\rangle.
$$

This will trigger the controlled $X$ gate! Assuming the auxiliary qubit is in the $\vert -\rangle$ state as pictured, this produces the required sign flip. The second layer returns the state to $\vert \psi\rangle$. A state $\vert\psi_\perp\rangle$ orthogonal to $\vert \psi\rangle$ will remain orthogonal after $H^{\otimes n}$, since

$$
\langle \psi\vert H^{\otimes n} \cdot H^{\otimes n} \vert \psi_\perp\rangle = \langle \psi\vert \psi_\perp\rangle = 0.
$$

Thus, any such $\vert\psi_\perp\rangle$ will not trigger the multi-controlled $X$ gate. So the circuit implements $-\hat{D}$. ▢

</details>

---

Now we have all the components for the circuit implementation of the Grover operator! The only thing we have to do is initialize the query and auxiliary systems to the uniform superposition and $\vert - \rangle$ respectively. Assuming everything starts in the $\vert 0\rangle$ state, we apply an $X$ to get $\vert 1\rangle$, and a Hadamard to get $\vert -\rangle$ on the auxiliary qubit. We Hadamard transform the query register as usual. We then simply copy and paste the oracle and diffusion operators from above:

<img src="pics/grover-iter-2.svg">

To perform the full algorithm for Grover search, we will repeat the green and purple subcircuits some number of times, then measure!
