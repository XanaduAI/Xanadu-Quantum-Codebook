---

**Learning outcomes**

- *Implement a linear combination of unitaries.*

---

Previously, we saw how to approximate $e^{A+B}$ by breaking it into steps of the form $e^{A/n}e^{B/n}$. This strategy was helpful if $A$ and $B$ were easily exponentiated, but didn't commute. Another, more direct strategy is to look at the definition of the exponential itself:

$$
\begin{align*}
U(t) & = e^{-it\hat{H}/\hbar} \\
& = I + \left( \frac{-i\hat{H}}{\hbar}\right) + \frac{1}{2!}\left(\frac{-i\hat{H}}{\hbar}\right)^2 + \cdots
\end{align*}
$$

Instead of focusing on subterms of $\hat{H}$ and the approximations that come from trying to commute these subterms, let us instead truncate the power series after some finite number of terms:

$$
\begin{align*}
\tilde{U} & = I + \left( \frac{-i\hat{H}}{\hbar}\right) + \frac{1}{2!}\left(\frac{-i\hat{H}}{\hbar}\right)^2 + \cdots + \frac{1}{K!}\left(\frac{-i\hat{H}}{\hbar}\right)^K.
\end{align*}
$$

For large $K$, this should give a reasonable approximation to the time evolution of the system. But is there any sensible way to implement this on a quantum computer? The truncation $\tilde{U}$ need not be unitary, nor any of the individual terms, so none of them exist individually as a gate in a quantum circuit. And even if they were unitary, how could we implement their *sum*? The whole business seems hopeless.

There is a powerful method called **linear combination of unitaries (LCU)** which circumnavigates all these difficulties. To start with, let's assume we are trying to create a gate which acts as a sum of unitaries:

$$
\tilde{U} = U_0 + U_1 + \cdots + U_{K-1}.
$$

We'll focus on the most convenient situation where $K = 2^k$ is a binary power, and label the unitaries $U_{\mathbf{x}}$ for a binary string $\mathbf{x} \in \{0, 1\}^k$. If each unitary $U_{\mathbf{x}}$ can be implemented in a controlled way, it's surprisingly easy to create a circuit which *probabilistically* performs the sum. We set up $k$ auxiliary wires corresponding to the bits in $\mathbf{x}$, in addition to the main register on which the unitaries act. The auxiliary register starts in state $\vert \mathbf{0}\rangle$ and is Hadamard transformed, while the main register starts in some arbitrary state $\vert\psi\rangle$ we want to apply the sum of unitaries to:

<img src="pics/su-circuit.svg" width="650px">

For each $U_{\mathbf{x}}$, we attach $k$ control bits, with control string $\mathbf{x}$. This part of the circuit is sometimes called a *quantum multiplexer*, but we will refer to it as the **SELECT subroutine**. For a product state of the form $\vert \mathbf{x}\rangle \otimes \vert \psi\rangle$, it has the effect

$$
\text{SELECT}\vert \mathbf{x}\rangle \otimes \vert \psi\rangle = \vert
\mathbf{x}\rangle \otimes U_\mathbf{x}\vert \psi\rangle.
$$

Finally, we apply another Hadamard transform to the auxiliary register and measure. If we get lucky and observe the right thing, we will have applied the sum of unitaries! The Hadamard transform on the auxiliary register is called the **PREPARE subroutine**.

---

***Exercise H.6.1.*** Follow the circuit and show that if the outcome of measuring the auxiliary register is $\mathbf{0}$, then the state on main register is $\tilde{U}\vert\psi\rangle$ up to normalization.

<details>
<summary><i>Hint.</i></summary>
To see the outcome state when $\mathbf{0}$ is observed,
apply the bra $\langle\mathbf{0}\vert$ on the auxiliary register.
Also, the Hadamard transform of $\vert
\mathbf{x}\rangle$ is

$$
  H^{\otimes k} \vert \mathbf{x}\rangle = \vert \hspace{-1pt}\pm^{x_1}\rangle
  \vert \hspace{-1pt}\pm^{x_2}\rangle \cdots \vert \hspace{-1pt}\pm^{x_k}\rangle.
$$
</details>

<details>
<summary><i>Solution.</i></summary>

Let's follow the circuit. It starts in state $\vert \mathbf{0}\rangle \otimes \vert \psi\rangle$, and after the Hadamard transform on the auxiliary register, becomes

$$
\frac{1}{\sqrt{K}}\sum_{\mathbf{x}\in\{0,1\}^k}\vert \mathbf{x}\rangle \otimes \vert \psi\rangle.
$$

The SELECT subroutine turns this into

$$
\frac{1}{\sqrt{K}}\sum_{\mathbf{x}\in\{0,1\}^k}\vert \mathbf{x}\rangle \otimes U_\mathbf{x}\vert \psi\rangle.
$$

Applying the Hadamard transform to the auxiliary register again and
using the hint, we find 

$$
\frac{1}{\sqrt{K}}\sum_{\mathbf{x}\in\{0,1\}^k} \vert \hspace{-1pt}\pm^{x_1}\rangle
  \vert \hspace{-1pt}\pm^{x_2}\rangle \cdots \vert \hspace{-1pt}\pm^{x_k}\rangle \otimes U_\mathbf{x}\vert \psi\rangle.
$$

Finally, if we measure $\mathbf{0}$ on the auxiliary, the post-observation state (ignoring normalization) is

$$
\begin{align*}
\frac{1}{\sqrt{2^k}}\sum_{\mathbf{x}\in\{0,1\}^k} \langle 0 \vert \hspace{-1pt}\pm^{x_1}\rangle
  \langle 0 \vert \hspace{-1pt}\pm^{x_2}\rangle \cdots \langle 0 \vert \hspace{-1pt}\pm^{x_k}\rangle \otimes U_\mathbf{x}\vert \psi\rangle & = \frac{1}{2^k}\sum_{\mathbf{x}\in\{0,1\}^k} U_\mathbf{x}\vert \psi\rangle \\
  & = \frac{1}{2^k}\tilde{U}\vert \psi\rangle,
  \end{align*}
$$

since $\langle 0 \vert \hspace{-1pt}\pm^x\rangle = 1/\sqrt{2}$ for either value of $x$. Up to the normalization, we have applied the sum of unitaries! ▢

</details>

---

One issue with this construction is that we are not guaranteed to
observe $\mathbf{0}$. The whole circuit only gives us some probability
of applying the sum, so it is *non-deterministic*, i.e., only works
with some probability. But it turns out
that, if $\tilde{U}$ is approximately unitary, we can boost the
chances of applying the sum using **amplitude amplification**
(see
[Childs and Wiebe (2012)](https://arxiv.org/abs/1202.5822) and
[Berry et al. (2014)](https://arxiv.org/pdf/1412.4687v1.pdf) for
details).

But there is a more glaring problem: the terms in our truncated Taylor
series are not unitary, even when the Hamiltonian $\hat{H}$ is!
Instead, it is a sum of unitaries with coefficients, aka a linear
combination of unitaries.
This is where the name comes from!
Thus, we need to generalize our circuit from sums to linear combinations.
In fact, this will also work for time evolution with Hamiltonians of
the form

$$
\hat{H} = \sum_j \alpha_j U_j,
$$

where each $U_j$ is unitary. When we write the Taylor series and
truncate it, each power of $\hat{H}$ will get expanded into products
of unitaries (which are unitary) with coefficients!

To warm us up, let's start with a linear combination of two unitaries:

$$
\tilde{U} = \kappa U + V.
$$

Since we have two unitaries, we use a single auxiliary qubit, but
instead of applying the Hadamard gate, we need to do something a bit
more imaginative! It turns out that the gate

$$
V_\kappa =
\frac{1}{\sqrt{\kappa+1}}\begin{bmatrix}
\sqrt{\kappa} & -1 \\
1 & \sqrt{\kappa}
\end{bmatrix}
$$

does what we need.
We set up the circuit in the same way as before, but with $V_k$ (and its adjoint) replacing $H$:

<img src="pics/vk-circuit.svg" width="400px">

You can check that this gives the right answers!

---

***Exercise H.6.2.*** Show that if we measure $0$ on the auxiliary wire, the state on the main register is $(\kappa U + V)\vert \psi\rangle$ up to normalization.

<details>
<summary><i>Solution.</i></summary>

We start in state $\vert 0\rangle \otimes\vert \psi\rangle$, and applying $V_\kappa$ gives

$$
\frac{1}{\sqrt{\kappa + 1}} (\sqrt{\kappa}\vert 0 \rangle + \vert 1\rangle)\otimes \vert \psi\rangle.
$$

Passing through SELECT yields

$$
\frac{1}{\sqrt{\kappa + 1}} (\sqrt{\kappa}\vert 0 \rangle \otimes U\vert \psi\rangle + \vert 1\rangle \otimes V\vert \psi\rangle).
$$

Finally, applying $V_\kappa^\dagger$ (and doing a little algebra) produces a state

$$
\frac{1}{\kappa + 1} \vert 0\rangle \otimes \left(\kappa U + V\right) \vert\psi\rangle + \frac{\sqrt{\kappa}}{\kappa + 1} \vert 1\rangle \otimes \left(V - U\right)\vert \psi\rangle.
$$

If we measure $0$ on the auxiliary, we therefore obtain $\left(\kappa
U + V\right) \vert\psi\rangle$ on the main register, up to
normalization. ▢

</details>

---

It turns out that knowing how to linearly combine two unitaries is
sufficient for combining any number of unitaries! Rather than describe
how to do this in full generality, we'll illustrate it for a useful case. Suppose we want to simulate the evolution

$$
e^{tU} = I + tU + \frac{1}{2}t^2 U^2 + \cdots
$$

for some unitary $U$. Let's consider the first-order approximation,

$$
I+ tU = U^0 + tU^1.
$$

The reason for including powers will become clear in a moment. This combination is non-deterministically implemented by the circuit:

<img src="pics/lcu-nest1.svg" width="400px">

The second-order approximation is

$$
I + tU + \frac{1}{2}t^2U^2 = I + t\left(U^1 + \frac{t}{2}U^2\right).
$$

This replaces $U^1$ in the diagram above with a new linear combination of two unitaries, $U^1 + (t/2)U^2$. The corresponding circuit has a *controlled subcircuit*:

<img src="pics/lcu-nest2.svg" width="550px">

We can continue on in this way as long as we like!

---

***Exercise H.6.3.*** Show that to go to the next order in approximating $e^{tU}$, we replace

$$
U^j \mapsto U^j + \frac{t}{j+1} U^{j+1}.
$$

We can then replace $U^j$ with the (non-deterministic) circuit which
implements this sum!

<details>
<summary><i>Solution.</i></summary>

This is simply a check of the power series. If we have the first $j + 1$ terms of $e^{tU}$,

$$
I + tU^1 + \cdots + \frac{1}{j!}t^{K}U^j,
$$

then the next term is obtained by making the suggested replacement:

$$
\begin{align*}
I + tU^1 + \cdots + \frac{1}{j!}t^{j}U^j & \to I + tU^1 + \cdots + \frac{1}{j!}t^{j}\left(U^j + \frac{t}{j+1} U^{j+1}\right)\\
& = I + tU^1 + \cdots + \frac{1}{j!}t^{j}U^j + \frac{1}{(j+1)!}t^{j+1} U^{j+1}.
\end{align*}
$$

We can use similar methods to implement an arbitrary LCU! ▢

</details>

---
