---

**Learning outcomes**

- *Describe how unitarity arises from preservation of marginal probabilities.*

---

Evidently, the black boxes in quantum mechanics do something over and above the black boxes in a random classical system. But it can't be *too* different, since we still have observation probabilities $p(\mathbf{y}\vert \mathbf{x})$ which add up to $1$ when we fix $\mathbf{x}$ and sum over $\mathbf{y}$. Recall the theory of projective measurements, which tells us that if the state of the system is $\vert \psi\rangle$, the probability of observing the basis state $\mathbf{y}$ is

$$
p(\mathbf{y}\vert \mathbf{x}) = \vert \langle \mathbf{y}\vert  \psi\rangle\vert ^2 = (\langle \mathbf{y}\vert  \psi\rangle)^\dagger\langle \mathbf{y}\vert  \psi\rangle.
$$

Suppose that our black box acts as a linear operator $U$, taking an initial state $\vert \mathbf{x}\rangle$ to the state $U\vert \mathbf{x}\rangle = \vert \psi\rangle$.

<img src="pics/unitary.svg" width="450px">

Then the requirement that the conditional probabilities $p(\mathbf{y}\vert \mathbf{x})$ add to $1$ becomes

$$
\sum_{\mathbf{y}} (\langle \mathbf{y}\vert  \psi\rangle)^\dagger\langle \mathbf{y}\vert  \psi\rangle = \sum_{\mathbf{y}} \langle \mathbf{x}\vert  U^\dagger\vert \mathbf{y}\rangle\langle \mathbf{y}\vert  U\vert \mathbf{x}\rangle = 1.
$$

Since $\mathbf{y}$ labels a complete basis, the sum over $\mathbf{y}$ is just matrix multiplication, and we can rewrite this condition as

$$
\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}\rangle = 1. \tag{1}\label{diag}
$$

---

***Exercise H.2.1.*** Show that (\ref{diag}) follows from the
condition

$$
\sum_{\mathbf{y}} \langle \mathbf{x}\vert  U^\dagger\vert
\mathbf{y}\rangle\langle \mathbf{y}\vert  U\vert \mathbf{x}\rangle = 1.
$$

<details>
<summary><i>Hint.</i></summary>
First show that

$$
\sum_{\mathbf{y}} \vert \mathbf{y}\rangle \langle \mathbf{y}\vert = I.
$$
</details>

<details>
<summary><i>Solution.</i></summary>
Let us prove the equation in the hint first.
To check that

$$
\sum_{\mathbf{y}} \vert \mathbf{y}\rangle \langle \mathbf{y}\vert = I,
$$

it suffices to show that both act on computational basis elements in
the same way.
By definition of the identity, $I\vert\mathbf{x}\rangle =
\vert\mathbf{x}\rangle$.
Since $\mathbf{y}$ ranges over computational basis elements, and
$\langle \mathbf{y}\vert \mathbf{x}\rangle = 0$ unless $\mathbf{y} =
\mathbf{x}$,

$$
\begin{align*}
\sum_{\mathbf{y}} \vert \mathbf{y}\rangle \langle \mathbf{y}\vert
\mathbf{x}\rangle & = \vert \mathbf{x}\rangle \langle \mathbf{x}\vert
\mathbf{x}\rangle \\
&= \vert\mathbf{x}\rangle
\end{align*}
$$

since $\langle \mathbf{x}\vert \mathbf{x}\rangle =1$, i.e., states are
normalized.
Thus, the hint is proved. We can now use this as follows:

$$
\begin{align*}
\sum_{\mathbf{y}} \langle \mathbf{x}\vert  U^\dagger\vert
\mathbf{y}\rangle\langle \mathbf{y}\vert  U\vert \mathbf{x}\rangle & =
\langle \mathbf{x}\vert  U^\dagger \left[\sum_{\mathbf{y}}\vert
\mathbf{y}\rangle\langle \mathbf{y}\vert \right]  U\vert
\mathbf{x}\rangle \\
& =
\langle \mathbf{x}\vert  U^\dagger I U\vert
\mathbf{x}\rangle \\
& =
\langle \mathbf{x}\vert  U^\dagger U\vert
\mathbf{x}\rangle.
\end{align*}
$$

Thus,

$$
\sum_{\mathbf{y}} \langle \mathbf{x}\vert  U^\dagger\vert
\mathbf{y}\rangle\langle \mathbf{y}\vert  U\vert \mathbf{x}\rangle = 1
$$

is equivalent to (\ref{diag}). ▢
</details>

---

In fact, you can repeat this argument with an arbitrary initial state $\vert \psi_0\rangle$. The conditional probabilities $p(\mathbf{y}\vert \psi_0) = \vert \langle\mathbf{y}\vert \psi_0\rangle\vert ^2$ must add up to $1$, and hence

$$
\langle \psi_0\vert U^\dagger U\vert \psi_0\rangle = 1.
$$

As you can check below, this implies that

$$
\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle = \delta_{\mathbf{x}\mathbf{x}'} \quad \text{or equivalently} \quad U^\dagger U = I.
$$

In other words, the adjoint of $U$ is its inverse, $U^\dagger = U^{-1}$.

<img src="pics/twonitary.svg" width="550px">

This is the defining property of a **unitary** matrix. By thinking about probability and black boxes, we have rediscovered that the black boxes of quantum mechanics are unitary operators!

---

***Exercise H.2.2.***  For a system of $n$ qubits, how many real,
   independent parameters are required to specify the unitary matrix
   $U$? Compare to the number of parameters in a classical random
   system, $2^{2n} - 2^n$.

More parameters means more types of behaviour are possible, and in
theory, more powerful computers!

<details>
<summary><i>Solution.</i></summary>

For $n$ qubits, the state vector $\vert \psi\rangle$ has $2^n$ components. Thus, $U$ is a $2^n \times 2^n$ matrix of complex entries, each of which is specified by two real numbers. This gives a total of $2 \cdot 2^n \cdot 2^n = 2 \cdot 2^{2n}$ parameters. The equation $U^\dagger U = I$ gives us a whole $2^n \times 2^n$ grid of real conditions to satisfy, so the total number of independent real parameters is

$$
2 \cdot 2^{2n} - 2^{2n} = 2^{2n}.
$$

This is a factor of $2^n$ more than the number of parameters in a classical random matrix. Much more is possible in the quantum realm! ▢

</details>

---

***Exercise H.2.3.***  Let $\mathbf{x}\neq\mathbf{x}'$ be distinct computational basis states, and define

$$
\vert \psi_0\rangle = \alpha\vert \mathbf{x}\rangle+\beta\vert \mathbf{x}'\rangle, \quad \vert \alpha\vert ^2 + \vert \beta\vert ^2 = 1.
$$

Assuming the condition $\langle \psi_0\vert U^\dagger U\vert \psi_0\rangle = 1$, this sequence of exercises will guide you to the conclusion that $U^\dagger U = I$.

(a) Show that $\langle \psi_0\vert U^\dagger U\vert \psi_0\rangle = 1$ implies

$$
\Re[\alpha^*\beta \langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x'}\rangle] = 0,
$$

where $\Re$ denotes the real component of a complex number.

(b) By choosing $\alpha$ and $\beta$ judiciously, argue that $\langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle = 0$.

(c) Conclude that $\langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle = \delta_{\mathbf{x}\mathbf{x}'}$,
and thus $U^\dagger U = I$. Here, $\delta_{\mathbf{x}\mathbf{x}'}$ is
the *Kronecker delta*, defined by

$$
\delta_{\mathbf{x}\mathbf{x}'} =
\begin{cases}
1 & \mathbf{x} = \mathbf{x}' \\
0 & \text{otherwise.}
\end{cases}
$$

<details>
<summary><i>Solution.</i></summary>
(a) A little algebra shows that

$$
\langle \psi_0\vert U^\dagger U\vert \psi_0\rangle = \vert \alpha\vert ^2\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}\rangle + \vert \beta\vert ^2\langle \mathbf{x}'\vert U^\dagger U\vert \mathbf{x}'\rangle + \alpha^*\beta\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle + (\alpha^*\beta\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle)^\dagger.
$$

From (\ref{diag}), the first term in brackets gives $\vert \alpha\vert ^2$ and the second $\vert \beta\vert ^2$, which sum to $1$ since $\vert \psi_0\rangle$ is normalized. Hence

$$
\langle \psi_0\vert U^\dagger U\vert \psi_0\rangle = 1 + \alpha^*\beta\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle + (\alpha^*\beta\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle)^\dagger = 1 + 2\Re [\alpha^*\beta\langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle],
$$

since the sum of a complex number and its conjugate is twice the real part. Assuming $\langle \psi_0\vert U^\dagger U\vert \psi_0\rangle = 1$ then implies that the real part of $\alpha^*\beta \langle \mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle$ must vanish.

(b) We can now simply choose $\alpha$ and $\beta$ to ensure that the expression is real! Take for instance $\vert \alpha\vert  = \vert \beta\vert  = 1/\sqrt{2}$, and choose the phases so that $\alpha^*\beta = e^{-i\theta}/2$ cancels the phase $e^{i\theta}$ of $\langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle$. Then

$$
\Re [\alpha^*\beta\langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle] = \frac{1}{2}e^{-i\theta}\langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle = 0 \quad \Longrightarrow \quad \langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle = 0.
$$

(c) We know from (\ref{diag}) that $\langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}\rangle = 1$ for all $\mathbf{x}$, and hence $\langle\mathbf{x}\vert U^\dagger U\vert \mathbf{x}'\rangle = \delta_{\mathbf{x}\mathbf{x}'}$. This is just the component form of the statement $U^\dagger U = I$, so $U$ is unitary as claimed! ▢

</details>

---
