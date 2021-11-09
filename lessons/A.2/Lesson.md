---

**Learning outcomes**
- *Explain the role of oracles in quantum algorithms.*
- *Express the action of an oracle as a unitary matrix applied to computational basis states.*

---

Let's think a bit more about how this lock breaking actually works. Call the correct combination for an $n$-bit lock $\mathbf{s} \in \{0, 1\}^n$. We can model the lock as a function $f$ from $n$-bit strings $\mathbf{x} \in \{0, 1\}^n$ to a bit $y \in \{0, 1\}$, with $f(\mathbf{x}) = 0$ meaning "the combination doesn't work" and $f(\mathbf{x}) = 1$ meaning "the combination works". More concisely,

$$
  f(\mathbf{x}) =
  \begin{cases}
    1 & \mathbf{x} = \mathbf{s} \\
    0 & \text{otherwise}.
  \end{cases}
$$

We'll assume that the function $f$ is a black box that the computer
(quantum or classical) cannot look inside. However, the computer can
*ask* the if a combination is correct, and get a "yes" or "no" answer
immediately. In computer science, such a black box is called an
**oracle**, since its inner workings appear mysterious. You can think
of it as a magic 8-ball. You shake it and an answer emerges from the
shadowy depths. The act of shaking it and letting the answer emerge is
called a **query**.

![](pics/oracle-lock.svg)

The classical brute-force algorithm for breaking a lock is simple. We
simply comb through the $\mathbf{x}\in\{0, 1\}^n$ in whatever order we
like, asking the oracle to compute $f(\mathbf{x})$ until we arrive at
$f(\mathbf{x}) = 1$. We then declare $\mathbf{x} = \mathbf{s}$ as the
solution. What about the quantum case?
Here, we need to be careful about what the oracle is doing, since only
*unitary* operations are allowed.
A clever choice is to put the oracle's answer into a *phase*:

$$
  \vert \mathbf{x}\rangle \mapsto (-1)^{f(\mathbf{x})} \vert \mathbf{x}\rangle.
$$

We encode this as a unitary operator, $U_f$, which acts on basis states as

$$
\begin{align*}
  U_f\vert \mathbf{x}\rangle & = (-1)^{f(\mathbf{x})}\vert
  \mathbf{x}\rangle \\
  & =
    \begin{cases}
    -\vert \mathbf{x}\rangle & \mathbf{x} = \mathbf{s} \\
    \vert \mathbf{x}\rangle & \text{otherwise}.
  \end{cases}
\end{align*}
$$

Since this acts on a given basis state, and does not change the size
of the amplitude, it is immediate that the oracle is unitary. Fixing
the size of amplitudes giveth a unitary operator, but it also taketh
away; by itself, we cannot use the oracle to increase the probability
of measuring the secret combination of our lock! The probability is
the amplitude squared, and adding a phase can't change that. Put
differently, a change in global phase is unobservable. But there are
other clever things we can do with the oracle, as we'll soon see.

*Tip*. We could imagine instead recording the magic 8-ball's "yes" or "no" into a new qubit, initialized to state $|0\rangle$:

$$
\begin{align*}
\vert \mathbf{s}\rangle \vert 0\rangle &\to \vert \mathbf{s}\rangle \vert 1\rangle \\
\vert \mathbf{x}\rangle \vert 0\rangle &\to \vert \mathbf{x}\rangle \vert 0\rangle,
\end{align*}
$$

where $\mathbf{x} \neq \mathbf{s}$. This can in fact be implemented as a multi-controlled $X$ gate, but we'll stick to the simpler phase oracle in this section.

---

***Exercise A.2.1.*** (a) Show that we can also write the oracle in
   terms of the identity matrix $I$ and projector $\vert
   \mathbf{s}\rangle\langle\mathbf{s}\vert$ as follows:

$$
       U_f = I - 2\vert \mathbf{s}\rangle\langle\mathbf{s}\vert. \tag{1} \label{u_f}
$$

<details>
<summary><i>Hint.</i></summary>
Two operators are equal if they have the same action on basis states.
</details>

<details>
<summary><i>Solution.</i></summary>

(a) Let's apply the right-hand side of Eq. (\ref{u_f}) to the solution state to begin with:

$$
\begin{align*}
(I - 2\vert \mathbf{s}\rangle\langle\mathbf{s}\vert ) \vert \mathbf{s}\rangle & = \vert \mathbf{s}\rangle - 2\vert \mathbf{s}\rangle\langle\mathbf{s}\vert \mathbf{s}\rangle \\
& = -\vert \mathbf{s}\rangle,
\end{align*}
$$

since $\langle\mathbf{s}|\mathbf{s}\rangle = 1$. This is what we expect $U_f$ to do! If we consider a non-solution $\vert \mathbf{x}\rangle$, with $\langle \mathbf{s}\vert \mathbf{x}\rangle = 0$, we find

$$
\begin{align*}
(I - 2\vert \mathbf{s}\rangle\langle\mathbf{s}\vert ) \vert \mathbf{x}\rangle & = \vert \mathbf{x}\rangle - 2\vert \mathbf{s}\rangle\langle \mathbf{s}\vert \mathbf{x}\rangle \\
& = \vert \mathbf{x}\rangle - 2 \cdot 0 \\ & = \vert \mathbf{x}\rangle.
\end{align*}
$$
	
So the phase is unchanged. It follows that the right-hand side of
Eq. (\ref{u_f}) acts on basis states precisely as $U_f$, and hence
must be equal. ▢

</details>

(b) Verify that $U_f$ is unitary directly from this equation.

<details>
<summary><i>Hint.</i></summary>
Note that $(\vert \mathbf{s}\rangle \langle \mathbf{s}\vert )^2 =
\vert \mathbf{s}\rangle \langle \mathbf{s}\vert $.
</details>

<details>
<summary><i>Solution.</i></summary>
(b) First, we note that $U_f^\dagger = U_f$, since $I^\dagger = I$ and $(\vert \mathbf{s}\rangle\langle\mathbf{s}\vert )^\dagger = \vert \mathbf{s}\rangle\langle\mathbf{s}\vert $. Then

$$
\begin{align*}
U_f U_f^\dagger = U_f^2 & = (I - 2\vert \mathbf{s}\rangle\langle\mathbf{s}\vert )^2 \\
& = I\cdot I - 4\vert \mathbf{s}\rangle\langle\mathbf{s}\vert  + 4 (\vert \mathbf{s}\rangle\langle\mathbf{s}\vert )^2 \\ & = I,
\end{align*}
$$

using $(\vert \mathbf{s}\rangle \langle \mathbf{s}\vert )^2 = \vert
\mathbf{s}\rangle \langle \mathbf{s}\vert $. So $U_f$, defined as in
Eq. (\ref{u_f}), is unitary. ▢

</details>

---
