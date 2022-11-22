*Solution*. After running this on both $\vert 0\rangle$ and $\vert 1\rangle$,
you'll notice that the outcome probabilities are equal (0.5) for both states! If
ever you were in a situation where you needed to figure out which of the two
states you had, you'd be out of luck, as they are *indistinguishable*.

---

The outcome of the previous exercise may seem dire. There are situations where
measuring in the computational basis makes it impossible to distinguish between
two states! However, we can work towards a solution to this problem by measuring
in different bases. Rather than asking for the outcome probabilities of $\vert
0\rangle$ and $\vert 1\rangle$, we can compute the outcome probabilities of two
states in a different basis. In an earlier node, we learned that $\vert
+\rangle$ and $\vert -\rangle$ themselves form a basis, the **Hadamard
basis**. Thus, if we apply $H$ and measure with respect to the Hadamard basis
instead of the computational one, we will be able to determine with certainty
which state we have, because we are already asking about things with respect to
$\vert +\rangle$ and $\vert -\rangle$.

However, a common limitation of quantum computing hardware (and, to some extent,
software) is that measurements in other bases are non-trivial or unavailable in
practice, while it is straightforward to perform measurements in the
computational basis. Given this, how can we access a different basis when we can
only measure in the computational one?

The secret is to perform a **basis rotation** prior to measurement. If we want
to measure in the Hadamard basis, we can "trick" the quantum computer by simply
rotating the states before performing the measurement; we must apply an
operation that maps between the two bases. Namely, it should map $\vert
+\rangle$ back to $\vert 0\rangle$, and $\vert -\rangle$ back to $\vert
1\rangle$. Then, if we measure and observe $\vert 0\rangle$, we'll know that what
we *really* had was $\vert +\rangle$, and similarly for $\vert 1\rangle$ and
$\vert -\rangle$. In this case, the Hadamard is its own inverse; but in general,
you have to apply the adjoint of the operation whose basis you want to measure
in.

---

***Codercise I.9.2.*** *(a)* Suppose we have prepared the state

$$
\vert \psi\rangle = \frac{1}{2} \vert 0\rangle + i \frac{\sqrt{3}}{2} \vert 1\rangle,
$$

and want to make a measurement in the basis 

$$
\begin{align*}
 \vert y_+\rangle &= \frac{1}{\sqrt{2}} \left(\vert 0\rangle + i\vert 1\rangle \right), \\
 \vert y_-\rangle &= \frac{1}{\sqrt{2}} \left(\vert 0\rangle - i\vert 1\rangle \right).
\end{align*}
$$

First, implement a quantum function `prepare_psi` that prepares the state $\vert
\psi \rangle$.  Then, determine how to prepare the two basis states $\vert y_+
\rangle$ and $\vert y_-\rangle$ from $\vert 0\rangle$ and $\vert
1\rangle$ respectively. Implement this as a second quantum function, `y_basis_rotation`.
**Note that the two functions should not return any values**; we will use them as
subroutines in a QNode in the next exercise.

*Tip*. The states $\vert y_+\rangle$ and $\vert y_-\rangle$ are given these labels
because they are the eigenvectors of the Pauli $Y$ operation.
