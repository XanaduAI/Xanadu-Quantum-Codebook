---

**Learning outcomes**

- *Describe the geometry of Grover search for multiple solutions.*
- *Compute the scaling of Grover search for multiple solutions.*

---

So far, we have focused on the case of searching for a single solution
in a list of $N = 2^n$ possibilities. But Grover search generalizes,
almost without modification, to $M$ solutions! Rather than generate
*all* solutions, our goal will be to observe *any* solution $\mathbf{s}
\in S$ with high probability, where $S$ is the set of $M$
solutions. We can then consider a two-dimensional subspace spanned by the uniform
superposition of solution states (which corresponds to a uniform
probability of observing a solution), and the uniform superposition
over all states. This directly generalizes our strategy for Grover search
with a single solution.

Let $T = \{0,1\}^n\backslash S$ be our set of non-solutions as before, and $N = 2^n$. It turns out that our two-dimensional geometric picture works almost exactly the same way if, instead of the unique solution $\vert \mathbf{s}\rangle$ from earlier, we consider the uniform superposition of solution states,

$$
\vert S\rangle = \frac{1}{\sqrt{M}}\sum_{\mathbf{s}\in S}\vert \mathbf{s}\rangle.
$$

We can also define the uniform superposition of non-solution states, which is orthogonal to $\vert S\rangle$:

$$
\vert T\rangle = \frac{1}{\sqrt{N-M}}\sum_{\mathbf{t}\in T}\vert \mathbf{t}\rangle.
$$

As before, we start with the uniform superposition $\vert\psi\rangle$ over *all* states, and a Grover step consists of an oracle followed by the diffusion operator. While the diffusion operator is the same, the oracle is now the multi-solution oracle:

$$
U_f = I - \sum_{\mathbf{s}\in S} 2\vert \mathbf{s}\rangle \langle \mathbf{s}\vert .
$$

This is easily constructed using multi-controlled $X$ gates,  as in the single-solution case. We just apply a gate for each solution!

---

***Exercise G.5.1.*** For solutions $\mathbf{s}_1, \mathbf{s}_2,
   \ldots, \mathbf{s}_M$, show that the following circuit implements
   the multi-solution oracle $\hat{U}$ (where the hat reminds us that
   it acts on the auxiliary qubit as well):

<img src="pics/multi-oracle-circuit.svg">

where $C^{(\mathbf{s_{i}})}X$ represents a multi-controlled $X$ gate with control string $\mathbf{s_{i}}$ for $i \in \{1,...,M\}$.

<details>
<summary><i>Solution.</i></summary>

We can visualize the effects of this circuit by considering what
happens when an arbitrary computational basis state $\vert
\mathbf{x}\rangle$ is fed in as input. We need our multi-solution
oracle $\hat{U}$ to flip the phase of a basis state $\vert
\mathbf{x}\rangle$ just in case $\mathbf{x} \in S = \{\mathbf{s}_1,
\mathbf{s}_2, \ldots, \mathbf{s}_M\}$. When we hit the first gate
(assuming the auxiliary is in state $\vert -\rangle$), there is a
phase flip only if $\mathbf{x} = \mathbf{s}_1$; otherwise nothing
happens. After, at the second gate, the phase is flipped if
$\mathbf{x} = \mathbf{s}_2$; otherwise nothing happens. And so on for
each solution! The end result is that $\vert \mathbf{x}\rangle$ will
get its phase flipped if $\mathbf{x} = \mathbf{s}$ for some solution
$\mathbf{s} \in S$. Since these solutions are distinct, it can get its
phase flipped at most once. ▢

</details>

---

So, each oracle step will now consist of $M$ multi-controlled $X$ gates, one for each solution. Diffusion is the same, and our Grover step (on query and auxiliary systems) is $G = \hat{D}\hat{U}$. We can then repeat the arguments from the last section more or less word for word! The initial probability to observe a solution is $p = \vert \langle S\vert \psi\rangle\vert ^{2} = M/N$, and hence the amplitude is

$$
\begin{align*}
\langle\mathbf{s}\vert \psi\rangle & =\sqrt{\frac{M}{N}}.
\end{align*}
$$

Pictorially, we have

<img src="pics/multi.svg">

The angle $\alpha$ between $\vert \psi\rangle$ and $\vert S\rangle$ then obeys

$$
\begin{align*}
\cos\alpha & = \sqrt{\frac{M}{N}} \\
& = \sin\theta,
\end{align*}
$$

where $\theta = \tfrac{\pi}{2}-\alpha$ is the complementary angle. If $M \ll N$, the small angle approximation formula tells us that

$$
\theta \approx \sqrt{\frac{M}{N}},
$$

and hence after a Grover rotation, we perform a counter-clockwise rotation by
$2\theta \approx 2\sqrt{M/N}$ in the two-dimensional subspace spanned
by $\vert S\rangle$ and $\vert \psi\rangle$, or equivalently, $\vert
S\rangle$ and $\vert T\rangle$, since this is just a different basis
for the same space. Let's draw this:

<img src="pics/multi-grover.svg">

Thus, the optimal number of steps is approximately

$$
\begin{align*}
S & \approx \frac{\tfrac{\pi}{2} - \sqrt{M/N}}{2\sqrt{M/N}} \\ & \approx \frac{\pi}{4}\sqrt{\frac{N}{M}}.
\end{align*}
$$

If we measure, we won't observe $\vert S\rangle$ itself, but rather, select a solution uniformly at random. In the following exercises, you can do the math to understand how things work *without* approximating.

---

***Exercise G.5.2.*** Show that we can write the uniform superposition over all states as

$$
\vert \psi\rangle = \sqrt{\frac{N-M}{N}}\vert T\rangle + \sqrt{\frac{M}{N}}\vert S\rangle.
$$

<details>
<summary><i>Solution.</i></summary>

This is easily verified:

$$
\begin{align*}
\sqrt{\frac{N-M}{N}}\vert T\rangle + \sqrt{\frac{M}{N}}\vert S\rangle & = \frac{1}{\sqrt{N}} \sum_{\mathbf{t}} \vert \mathbf{t}\rangle+ \frac{1}{\sqrt{N}} \sum_{\mathbf{s}}\vert \mathbf{s}\rangle \\ & = \frac{1}{\sqrt{N}}\sum_{\mathbf{x}}\vert \mathbf{x}\rangle & \\ & = \vert \psi\rangle.
\end{align*}
$$

<div align="right">▢</div>

</details>

---

***Exercise G.5.3.*** Determine the effect of the oracle and diffusion operators on $\vert S\rangle$ and $\vert T\rangle$.

<details>
<summary><i>Solution.</i></summary>

We'll start with the oracle:

$$
\begin{align*}
U_f \vert S\rangle & = (I - 2\vert S\rangle\langle S\vert ) \vert S\rangle = -\vert S\rangle \\ U_f \vert T\rangle & = (I - 2\vert S\rangle\langle S\vert ) \vert T\rangle = \vert T\rangle,
\end{align*}
$$

using $\langle S\vert T\rangle = 0$. Easy!

Using ***Exercise G.5.2***, we have

$$
\begin{align*}
\langle\psi\vert S\rangle & = \sqrt{\frac{M}{N}} \\ \langle\psi\vert T\rangle & = \sqrt{\frac{N-M}{N}}.
\end{align*}
$$

Hence, the effect of the diffusion operator is

$$
\begin{align*}
D \vert S\rangle & = (2\vert \psi\rangle\langle\psi\vert  - I)\vert S\rangle \\ & = 2\sqrt{\frac{M}{N}} \vert \psi\rangle - \vert S\rangle \\ & = \frac{2\sqrt{M(N-M)}}{N}\vert T\rangle - \frac{(N - 2M)}{N}\vert S\rangle \\
D \vert T\rangle & = (2\vert \psi\rangle\langle\psi\vert  - I)\vert T\rangle \\ & = 2\sqrt{\frac{N-M}{N}} \vert \psi\rangle - \vert T\rangle \\ & = \frac{(N-2M)}{N}\vert T\rangle + 2\frac{\sqrt{M(N-M)}}{N}\vert S\rangle.
\end{align*}
$$

<div align="right">▢</div>

</details>

---

***Exercise G.5.4.*** (a) Demonstrate that

$$
\sin (2\theta) = \frac{2\sqrt{M(N - M)}}{N}, \quad \cos (2\theta) = \frac{N-2M}{N},
$$

and conclude that after $k$ Grover iterations, the state of the system is

$$
G^k\vert \psi\rangle = \cos\left[(2k+1)\theta\right] \vert T\rangle + \sin\left[(2k+1)\theta\right] \vert S\rangle,
$$

where $\theta$ is the complement of the angle between $\vert S\rangle$
and $\vert \psi\rangle$, or equivalently, the angle between $\vert
T\rangle$ and $\vert\psi\rangle$.

(b) From part (a), argue that for $N \gg M$, the optimal number of Grover
steps is

$$
S \approx \frac{\pi}{4}\sqrt{\frac{N}{M}},
$$

as claimed above.

<details>
<summary><i>Hint.</i></summary>
Write the effect of $G = DU_f$ as a $2\times 2$ matrix on the space
spanned by $\vert S\rangle$ and $\vert T\rangle$.
</details>

<details>
<summary><i>Solution.</i> (a)</summary>

First, note from the geometry of our diagram that

$$
\begin{align*}
\sin\theta & = \langle\psi\vert S\rangle \\ & = \sqrt{\frac{M}{N}} \\
\cos\theta & = \langle\psi\vert T\rangle \\ & = \sqrt{\frac{N-M}{N}}.
\end{align*}
$$

Hence,

$$
\begin{align*}
\sin(2\theta) & = 2\sin\theta\cos\theta \\ & = \frac{2\sqrt{M(N-M)}}{N} \\
\cos(2\theta) & = 1 - 2\sin^2\theta \\ & = \frac{N - 2M}{N}.
\end{align*}
$$

From ***Exercise G.5.3***, it follows that $G = DU_f$ acts on the space spanned by $\vert T\rangle, \vert S\rangle$ as

$$
\begin{bmatrix}
\cos(2\theta) & -\sin(2\theta) \\
\sin(2\theta) & \cos(2\theta)
\end{bmatrix}.
$$

This is just a rotation matrix in our two-dimensional space! So it follows immediately that

$$
G^k\vert \psi\rangle = \cos\left[(2k+1)\theta\right] \vert T\rangle + \sin\left[(2k+1)\theta\right] \vert S\rangle.
$$

Done. ▢

</details>

<details>
<summary>(b)</summary>

The amplitude for observing any solution in the superposition $\vert
S\rangle$ is

$$
\langle S \vert G^k\vert \psi\rangle = \sin[(2k+1)\theta].
$$

As in the previous node, this is first maximized for

$$
(2k + 1)\theta \approx \frac{\pi}{2}.
$$

For $N \gg M$,

$$
\begin{align*}
\sin(2\theta) & = \frac{2\sqrt{M(N-M)}}{N} \\
& \approx \frac{2\sqrt{MN}}{N} \\
& = 2\sqrt{\frac{M}{N}} \\ & \ll 1.
\end{align*}
$$

Since $\sin(2\theta) \ll 1$, the small-angle approximation gives
$\sin(2\theta)\approx 2\theta$. Hence, the amplitude for observing a
solution is maximized when

$$
(2k + 1)\theta \approx 2k\sqrt{\frac{M}{N}} \approx \frac{\pi}{2},
$$

and hence

$$
S \approx \frac{\pi}{4}\sqrt{\frac{N}{M}}
$$

as required. ▢
</details>

---
