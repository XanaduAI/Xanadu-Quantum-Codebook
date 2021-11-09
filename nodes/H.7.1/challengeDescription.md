In the last node, we found a circuit for applying an arbitrary linear
combination of unitaries.
It split naturally into two subroutines, PREPARE which prepared the
state and coefficients, and SELECT which applied the unitaries.
These were somewhat messily defined using nested circuits, but it
turns there is a clean generalization of PREPARE and SELECT.

For a linear combination of unitaries

$$
\tilde{U} = \sum_j \alpha_j U_j,
$$

with $\alpha_j > 0$, we'll define PREPARE and SELECT as oracles (black boxes) with the following behaviour:

$$
\begin{align*}
\text{SELECT} \vert j\rangle \vert\psi\rangle & = \vert j\rangle U_j\vert\psi\rangle \\
\text{PREPARE} \vert 0\rangle & = \frac{1}{\sqrt{\alpha}}\sum_j \sqrt{\alpha_j}\vert j\rangle = \vert\alpha\rangle,
\end{align*}
$$

where $\alpha = \sum_j\alpha_j$, and $\vert j\rangle$ is an
orthonormal basis for the auxiliary system with initial state $\vert
0\rangle$.

Since we have only specified how the PREPARE oracle acts on
the state $\vert 0\rangle$, we have the freedom to complete it to a
unitary which performs this. A convenient choice is the *Householder
transformation*. For a state $\vert v\rangle$, this is defined as

$$
R_v = I - \vert v\rangle\langle v \vert.
$$

Let's start by coding up this transformation.

---

***Codercise H.7.1.*** Write a function for creating the
   Householder transformation as a matrix, assuming the input is a
   normalized state. You will find
   [``np.outer``](https://numpy.org/doc/stable/reference/generated/numpy.outer.html) helpful.
