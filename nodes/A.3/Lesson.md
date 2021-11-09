---

**Learning outcomes**
- *Describe how the oracle can be applied to a pair of candidate
  solutions to determine if the secret combination is present.*
- *Determine the average number of queries required to find a
  solution when testing in pairs.*

---

Applying the oracle by itself is not enough to improve our lock
picker. The problem is that we introduce a phase change which is
unobservable without further processing. In order to make some
progress, we must *combine* states to induce a *relative* change of phase which is detectable. To illustrate, let's take a superposition of two states $\vert \mathbf{x}\rangle$ and $\vert \mathbf{y}\rangle,$ and apply the oracle:

$$
\begin{align*}
  \vert \psi_{\mathbf{x}\mathbf{y}}\rangle & = \frac{1}{\sqrt{2}}(\vert \mathbf{x}\rangle +
  \vert \mathbf{y}\rangle) \\ & \mapsto \frac{1}{\sqrt{2}}\left((-1)^{f(\mathbf{x})}|\mathbf{x}\rangle +
  (-1)^{f(\mathbf{y})}\vert \mathbf{y}\rangle\right).
\end{align*}
$$

Instead of working in the space spanned by $\vert \mathbf{x}\rangle, \vert
\mathbf{y}\rangle$, we could measure in the (orthonormal) basis $\tfrac{1}{\sqrt{2}}(\vert
\mathbf{x}\rangle + \vert \mathbf{y}\rangle), \tfrac{1}{\sqrt{2}}(\vert
\mathbf{x}\rangle - \vert \mathbf{y}\rangle)$. If we
measure and observe the second state, we know one of the states had
its phase flipped, so the correct combination is either $\mathbf{x}$ or $\mathbf{y}$. But if we get $+$, then no phase got flipped and neither $\mathbf{x}$ nor $\mathbf{y}$ is the right combination. We give an illustration below, where $\mathbf{t}_1, \ldots, \mathbf{t}_7$ stand for non-solutions, and $\mathbf{s}$ is the secret combination:

![](pics/pairs.svg)

This leads to a rudimentary algorithm: test solutions in pairs. This is almost the brute force algorithm, except that instead of searching through $2^n$ combinations, we search through $2^{n-1}$ pairs, so we improve by a constant factor. Once we have identified the correct pair, we can just test both classically. This last step doesn't scale with $n$, so we have a very modest quantum speedup!

In principle, we could divide the full set of strings $\{0, 1\}^n$
into pairs any way we please. A particularly simple scheme is to split
each $n$-bit string $\mathbf{x}\in \{0,1\}^n$ into its first $n - 1$ bits and its last bit, e.g.,

$$
00101010 \mapsto (0010101, 0).
$$

Since there are two possible values for the last bit, $0$ and $1,$ we
can label pairs by the first $n -1$ bits. For instance, the $7$-bit
string $0010101$ labels the two $8$-bit strings,

$$
00101010 \mapsto 0010101\mathbf{0}, \quad 0010101\mathbf{1}.
$$

We'll label basis states on $n-1$ qubits using the string
$\tilde{\mathbf{x}}$, i.e., $\vert \tilde{\mathbf{x}}\rangle$.

---

***Exercise A.3.1.*** Let $\tilde{\mathbf{x}} \in \{0,1\}^{n-1}$ range over the $n-1$-bit strings we will use to label pairs. Argue that, for this scheme, the linear combination we want to apply the oracle to is

$$
\begin{align*}
      \vert \psi_{\tilde{\mathbf{x}}}\rangle & = \vert \tilde{\mathbf{x}}\rangle
      \otimes \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) \\
      & = \vert \tilde{\mathbf{x}}\rangle
      \otimes \vert +\rangle.
\end{align*}
$$

<details>
<summary class><i>Solution.</i></summary>

For an arbitrary pair $\mathbf{x}, \mathbf{y}$, we want to apply the oracle to

$$
\vert \psi_{\mathbf{x}\mathbf{y}}\rangle = \frac{1}{\sqrt{2}}(\vert \mathbf{x}\rangle +
  \vert \mathbf{y}\rangle).
$$
  
When $\mathbf{x}=\tilde{\mathbf{x}}0$ and $\mathbf{y}=\tilde{\mathbf{x}}1$, this becomes

$$
\begin{align*}
\vert \psi_{\tilde{\mathbf{x}}}\rangle & = \frac{1}{\sqrt{2}}(\vert \tilde{\mathbf{x}}0\rangle + \vert \tilde{\mathbf{x}}1\rangle) \\
& = \vert \tilde{\mathbf{x}}\rangle \otimes \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) \\ & = \vert \tilde{\mathbf{x}}\rangle \otimes \vert +\rangle.
\end{align*}
$$

<div align="right">▢</div>

</details>

---

Given this method for splitting all the strings into pairs based on the first $(n-1)$ bits, labelled by $\tilde{\mathbf{x}}$, we can provide a fairly concrete scheme for finding the secret combination to our lock. Let $H_n$ refer to the Hadamard acting on the last qubit. Since $H\vert 0\rangle = \vert +\rangle$, if the $n$th qubit is in state $|0\rangle$, acting with $H_n$ gives us $\vert +\rangle$ on that qubit, and hence $\vert \psi_{\tilde{\mathbf{x}}}\rangle = H_n\vert \tilde{\mathbf{x}}0\rangle$. Applying the oracle yields

$$
\begin{align*}
U_f\vert \psi_{\tilde{\mathbf{x}}}\rangle & = \vert \tilde{\mathbf{x}}\rangle \otimes \frac{1}{\sqrt{2}}\left((-1)^{f(\tilde{\mathbf{x}}0)}\vert 0\rangle +
(-1)^{f(\tilde{\mathbf{x}}1)}\vert 1\rangle\right) \\ & =
\begin{cases}
\pm\vert \tilde{\mathbf{x}}\rangle \otimes \vert -\rangle & \text{solution present} \\
\vert \tilde{\mathbf{x}}\rangle \otimes \vert +\rangle & \text{otherwise.}
\end{cases}
\end{align*}
$$

If we apply $H_n$ once more, we convert the $\vert +\rangle$ state to $\vert 0\rangle$, and the $\vert -\rangle$ state to $\vert 1\rangle$:

$$
\begin{align*}
      \vert \varphi\rangle & = H_n U_f \vert \psi_{\tilde{\mathbf{x}}}\rangle \\
      & = 
      \begin{cases}
\pm \vert \tilde{\mathbf{x}}1\rangle & \text{solution present} \\
\pm \vert \tilde{\mathbf{x}}0\rangle & \text{otherwise.}
\end{cases}
\end{align*}
$$

So we can simply measure the last qubit and see what we get! In case you find the math a bit dry, here is a circuit diagram to indicate what is actually going on:

![](pics/flowchart.svg)

Although we can speed up our lock-breaking by testing in pairs, we
will still need to test many pairs before finding the solution! The next exercise tells us how many pairs we will need to test on average.

---

***Exercise A.3.2.*** When searching for an $n$-bit solution, how many
   queries are required on average when we test in pairs?

<details>
<summary class><i>Hint.</i></summary>
Suppose that each position in the list is equally likely, and compute
the expected position.
</details>

<details>
<summary class><i>Solution.</i></summary>
Let $L = 2^{n-1}$, the number of pairs. If the position $\ell$ of the combination is random and uniform in the list, the average position is

$$
\begin{align*}
\sum_{\ell=1}^L \frac{\ell}{L} & = \frac{1}{L}(1 + 2 + \cdots + L) \\
& = \frac{1}{2L} L(L + 1) \\ & = \frac{1}{2}(L+1).
\end{align*}
$$

Thus, the average number of pairs we will need to test is $(L+1)/2 = (2^{n-1}+1)/2$. ▢

</details>

---
