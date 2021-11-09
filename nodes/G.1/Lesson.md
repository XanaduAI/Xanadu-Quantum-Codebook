---

**Learning outcomes**

- *Describe the strategy of amplitude amplification.*
- *Define the diffusion operator and visualize its effect on the uniform superposition.*

---

When trying to break a combination lock, the best quantum algorithm we came up with in part **A** was to test candidate solutions in pairs, and use our oracle to tell when the solution was present. Interesting, but not particularly impressive! In this section, we'll present a much more powerful algorithm which lets us search through lock combinations more efficiently than any classical algorithm.

<img src="pics/grover-lock.svg">

To start us off, recall that the test-in-pairs algorithm told us when a solution was present, but not which member of the pair it was. It would be much more convenient if we could run our algorithm, take a measurement, and observe the solution with high probability! With this goal in mind, let's change our approach and try to *shift amplitude* into the solution state using our oracle and possibly other operators. This is called **amplitude amplification**. Rather than work with pairs (where we can't do better than we've already done), we are going to consider $N$ orthogonal states all together. As usual, we'll start in the uniform superposition of these $N$ states:

<img src="pics/new-amp-1.svg" width="500px">

The second state is the solution. We want to somehow increase its
amplitude so we're more likely to observe it when we take a
measurement. Our first step, as usual, is to apply the oracle, which flips the sign of the amplitude for $\vert \mathbf{s}\rangle$:

<img src="pics/new-amp-2.svg" width="500px">

Applying the oracle again will only undo the phase flip, so we need to introduce a new element here. The key insight is that, although the amplitude of $\vert \mathbf{s}\rangle$ is equal in size to the other states, it has a *different* phase. We can write this as a difference from the uniform superposition. In fact, it will turn out the technically correct thing to do is split the state into a part proportional to the uniform superposition $\vert \psi\rangle$ (top), and a part orthogonal to $\vert \psi\rangle$ (bottom):

<img src="pics/new-amp-3.svg" width="500px">

What can we do with this? Well, suppose we have operator $D$ which
flips the part which is orthogonal to the uniform state. Since the
orhogonal part has a small negative overlap with all other states, the effect is
to steal a little of the amplitude from all the other states and pump it into the solution state:

<img src="pics/new-amp-4.svg" width="500px">

This is exactly what we want! $D$ actually stands for the **diffusion operator** rather than "difference", since it helps spread or diffuse the amplitude around. We should make a guess about how $D$ looks. Remember that the oracle associated with a solution $\mathbf{s}$ could be written

$$
U_f = I - 2 \vert \mathbf{s}\rangle\langle \mathbf{s}\vert .
$$

This flips the sign of $\vert \mathbf{s}\rangle$ and nothing else. As
an example, if $\mathbf{s} = \mathbf{0}$, then

$$
U_f \vert\mathbf{0}\rangle = \vert\mathbf{0}\rangle - 2 \vert
\mathbf{0}\rangle\langle \mathbf{0}\vert \mathbf{0}\rangle = -\vert\mathbf{0}\rangle,
$$

since $\langle \mathbf{0}\vert \mathbf{0}\rangle = 1$, and

$$
U_f \vert\mathbf{x}\rangle = \vert\mathbf{x}\rangle - 2 \vert
\mathbf{0}\rangle\langle \mathbf{0}\vert \mathbf{x}\rangle = \vert\mathbf{x}\rangle
$$

for $\mathbf{x}\neq\mathbf{0}$ since $\langle \mathbf{0}\vert \mathbf{x}\rangle=0$.
Now we want something which leaves the uniform superposition $\vert \psi\rangle$ alone, but flips the sign of "everything else", i.e., the states orthogonal to $\vert \psi\rangle$. So a good guess is

$$
D = 2\vert \psi\rangle\langle \psi\vert  - I,
$$

with a factor of $2$ to make sure we don't get *zero* when applied to $\vert \psi\rangle$. You can check in the exercise below that this works! It's clear that repeating these two steps will pump more amplitude into the solution, which we can demonstrate visually:

<img src="pics/ampamp.gif" width="500px">

The combination $G = DU_f$ is called the **Grover operator**, and the
algorithm consisting of repeatedly applying the operator, until the amplitude of $\vert
\mathbf{s}\rangle$ is maximized, is called **Grover search**. In the
second exercise below, you can see a very heuristic argument that the
number of such repetitions scales as $\sqrt{N}$, which represents a
quadratic speedup on the best classical algorithm! In the rest of this
module, we will dive into the details and see how Grover search
works.

---

***Exercise G.1.1.*** Verify that $D\vert \psi\rangle = \vert \psi\rangle$ and $D\vert \phi\rangle = -\vert \phi\rangle$ for any state orthogonal to $\vert \psi\rangle$.

<details>
<summary><i>Solution.</i></summary>

We start with $\vert \psi\rangle$ itself. Since $\vert \psi\rangle$ is normalized, with $\langle \psi\vert \psi\rangle =1$, we have

$$
D\vert \psi\rangle = 2\vert \psi\rangle\langle \psi\vert \psi\rangle - \vert \psi\rangle = 2\vert \psi\rangle -\vert \psi\rangle = \vert \psi\rangle.
$$

Now, if $\vert \phi\rangle$ is orthogonal to the uniform superposition, $\langle\psi\vert \phi\rangle = 0$. Then

$$
D\vert \phi\rangle = 2\vert \psi\rangle\langle \psi\vert \phi\rangle - \vert \phi\rangle = 2\cdot 0 -\vert \phi\rangle = -\vert \phi\rangle.
$$

So $D$ has the desired properties. ▢

</details>

---

***Exercise G.1.2.*** Consider large $N$ and a state $\vert v\rangle$
   whose overlap with the uniform state $\langle\psi\vert v\rangle
   \approx 1$ and whose overlap with the solution state
   $\langle\mathbf{s}\vert v\rangle = c/\sqrt{N}$. Note that, since we
   are working in the limit $N \to \infty$, this means
   $\vert\mathbf{s}\rangle$ and $\vert v\rangle$ are almost orthogonal!

(a) Prove using the definition of oracle that

$$
U_f\vert v\rangle = \vert v\rangle - \frac{2c}{\sqrt{N}}\vert \mathbf{s}\rangle.
$$

(b) Next apply the diffusion operator $D$, and explain why the Grover step $G$ transfers a chunk of amplitude proportional to $1/\sqrt{N}$ to the solution state $\vert \mathbf{s}\rangle$. 

(c) Conclude (sloppily!) that the optimal number of steps should scale
as $\sqrt{N}$. There is a short appendix below on Big O notation,
which is a helpful way to talk about scaling.

<details>
<summary><i>Solution. (a)</i></summary>

This is immediate from the definition of the oracle:

$$
\begin{align*}
U_f \vert v\rangle & = (I - 2\vert \mathbf{s}\rangle\langle \mathbf{s}|)\vert v\rangle \\
& = \vert v\rangle - 2\vert \mathbf{s}\rangle\langle \mathbf{s}\vert v\rangle \\
& = \vert v\rangle - \frac{2c}{\sqrt{N}}\vert \mathbf{s}\rangle.
\end{align*}
$$

</details>

<details>
<summary><i>(b)</i></summary>

To apply $D$, we need to split $U_f\vert v\rangle$ into a part proportional to $\vert\psi\rangle$ and a part orthogonal to it. Since $\langle\psi\vert v\rangle \approx 1,$ we will treat $\vert v\rangle$ itself as proportional to $\vert \psi\rangle$, and the solution state as orthogonal, since it has overlap $1/\sqrt{N}$ and $N$ is large. Thus,

$$
\begin{align*}
DU_f \vert v\rangle & = D\left(\vert v\rangle - \frac{2c}{\sqrt{N}}\vert \mathbf{s}\rangle\right)\\
& = \vert v\rangle + \frac{2c}{\sqrt{N}}\vert \mathbf{s}\rangle.
\end{align*}
$$

Thus, we have transferred a chunk of amplitude of size $2c/\sqrt{N}$ into the solution state.

</details>

<details>
<summary><i>(c)</i></summary>

Assuming that the transferred chunks remain proportional to $O(1/\sqrt{N})$, to get an amplitude $O(1)$, we require $S$ steps where

$$
S \cdot O\left(\frac{1}{\sqrt{N}}\right) = O(1) \quad \Longrightarrow \quad S = O(\sqrt{N}).
$$

This is correct, and we will show it by more rigorous means soon! ▢

</details>

---

<details>
<summary><i>Appendix on Big O notation.</i></summary>
In order to count the number of steps involved in an algorithm, there is a useful
piece of mathematical terminology called <b>Big O notation</b>.
If $N = 2^n$ refers to the total number of bit strings, and hence the
number of basis states in our problem, we can ask roughly how many
steps a protocol will take in terms of $N$.
As an example, recall the Deutsch-Jozsa algorithm
for telling whether a function $f$ is constant or balanced (given the
promise that it is one or the other).
It needed $2n = 2 \log_2 N$ gates and a single oracle call. We ignore
the factor of $2$ out the front, and say that it runs in

$$
O(\log_2 N)
$$

steps (which here are gates). Technically, this means that for large $N$, the number of steps
$S$ satisfies

$$
S \leq C \log_2 N
$$

for some fixed constant $C$. Similarly, the best deterministic classical algorithm
for solving this problem takes $O(N)$ steps, and the best random
classical algorithm takes $O(1)$ steps (if we only worry about the
dependence on $N$ and not on the error $\epsilon$). In general, we
write $h(x) = O(g(x))$ to mean that for large $x$,

$$
|h(x)| \leq C g(x)
$$

for some constant $C$.
</details>
