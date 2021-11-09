Suppose we want to break a lock, described by $n$ bits, with a quantum
computer. Naively, it looks as if we could create a uniform
superposition over all $n$-bit strings and immediately determine the
correct combination. To create a uniform superposition, recall that we can apply the Hadamard gate:

$$
H\vert 0\rangle = \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle).
$$

Correspondingly, to create a uniform superposition over all possible $n$-qubit basis states, we can do

$$
(H \otimes H \otimes \cdots \otimes H)\vert 0 \cdots 0\rangle = \frac{1}{\sqrt{2^n}}\sum_{\mathbf{x}\in\{0,1\}^n} \vert \mathbf{x}\rangle.
$$

We can write this a little more compactly. We will use bold letters
for strings of $n$ bits, $\mathbf{x} \in \{0, 1\}^n$, and in
particular, the string of $n$ zeroes will be denoted by $\mathbf{0}$.
We'll also denote the string of bits which opens the lock by
$\mathbf{s}$, for "solution".
Thus, we can write the uniform superposition $\vert \psi\rangle = H^{\otimes n}\vert \mathbf{0}\rangle = \vert \psi\rangle$, where $H^{\otimes n}$ is the $n$-fold tensor product of Hadamard gates. As a circuit:

![](pics/uniform.svg)

This will prepare a state which includes $\vert \mathbf{s}\rangle$, so
if we measure, we should find it.

---

***Codercise A.1.1.*** Fill in the following code to create the
   uniform superposition over $n$ qubits. It will plot the probability
   of observing different outcomes. Does putting the circuit in a
   uniform superposition help us break the lock?

*Note.* The ``pass`` is a placeholder you will replace with your code.
