---

**Learning outcomes**

- *Understand the action of SELECT and PREPARE oracles.*

---

Let's think a bit more about the twice-nested circuit from the last
node:

<img src="pics/lcu-nest2.svg" width="550px">

where

$$
V_\kappa =
\frac{1}{\sqrt{\kappa+1}}\begin{bmatrix}
\sqrt{\kappa} & -1 \\
1 & \sqrt{\kappa}
\end{bmatrix}.
$$

Recall that this circuit non-deterministically realizes the linear combination

$$
\tilde{U} = I + tU + \frac{1}{2}t^2U^2
$$

First of all, note that we can move the gates $V_{t/2}, V^\dagger_{t/2}$ outside the controlled subcircuit, since they will simply cancel if the subcircuit is not triggered:

<img src="pics/subroutines.svg" width="650px">

This leads to a generalized PREPARE subroutine, which we've coloured red, and a generalized SELECT subroutine which we've coloured blue. By just piping through the inputs, we can see that SELECT subroutine acts as follows:

$$
\begin{align*}
\text{SELECT}\vert 00\rangle \vert \psi\rangle & = \vert 00\rangle U^2 \vert \psi\rangle \\
\text{SELECT}\vert 01\rangle \vert \psi\rangle & = \vert 01\rangle U^1 \vert \psi\rangle \\
\text{SELECT}\vert 10\rangle \vert \psi\rangle & = \vert 10\rangle U^0 \vert \psi\rangle \\
\text{SELECT}\vert 11\rangle \vert \psi\rangle & = \vert 11\rangle U^0 \vert \psi\rangle.
\end{align*}
$$

The repetition of $U^0$ is annoying. Suppose that, as part of the
PREPARE routine, and after we apply the gates $V_t, V_{t/2}$), we can
apply a measurement which checks if we are in the state $\vert
10\rangle$ or not in this state. With some probabability, we are *not*
in this state. In this case, PREPARE acts on the auxiliary register as follows:

$$
\begin{align*}
\text{PREPARE}\vert 00\rangle & = V_t \vert 0\rangle \otimes V_{t/2} \vert 0\rangle \\
& = \frac{1}{\sqrt{(t+1)(t/2 +1)}}\left(\sqrt{t}\vert 0\rangle + \vert 1\rangle\right)\otimes\left(\sqrt{t/2}\vert 0\rangle + \vert 1\rangle\right) \\
& \propto \frac{t}{\sqrt{2}}\vert 00\rangle + \sqrt{t}\vert 01\rangle + \sqrt{\frac{t}{2}}\vert 10\rangle + \vert 11\rangle \\
& \to \frac{t}{\sqrt{2}}\vert 00\rangle + \sqrt{t}\vert 01\rangle + \vert 11\rangle,
\end{align*}
$$

where on the last line we got rid of the $\vert 10\rangle$ state,
since we were lucky enough to not measure it.
Up to a normalization, the coefficients of the terms on this last line
are the *square roots* of the coefficients in the linear combination!
To summarize, we can view

$$
\begin{align*}
\text{SELECT}\vert \mathbf{x}\rangle \vert \psi\rangle & = \vert \mathbf{x}\rangle U_\mathbf{x} \vert \psi\rangle \\
\text{PREPARE}\vert 00\rangle & \propto \sum_{\mathbf{x}} \sqrt{\alpha_{\mathbf{x}}} \vert \mathbf{x}\rangle,
\end{align*}
$$

for $\mathbf{x}\in\{00, 01, 11\}$ and $U_{00} = U^2,$ $U_{01} = U^1$, $U_{11} = U^0$. This suggests the following general definitions of SELECT and PREPARE. For an LCU

$$
\tilde{U} = \sum_j \alpha_j U_j,
$$

with positive coefficients $\alpha_j \geq 0$, we define

$$
\begin{align*}
\text{SELECT}\vert j\rangle \vert \psi\rangle & = \vert j\rangle U_j \vert \psi\rangle \\
\text{PREPARE}\vert 0\rangle & = \vert\alpha\rangle \propto \sum_{j} \sqrt{\alpha_{j}} \vert j\rangle \\
\end{align*}
$$

where $\vert 0\rangle$ is the initial state of the auxiliary register
and the $\vert j\rangle$ form an orthonormal basis for the auxiliary
system. These two routines are often viewed as *oracles*, i.e., black
boxes with specified behavior.

---

***Exercise H.7.1.*** (a) Show that the circuit consisting of PREPARE, SELECT and PREPARE${^\dagger}$ oracles:

<img src="pics/ps-oracles.svg" width="450px">

applies $\tilde{U}$ to $\vert \psi\rangle$, provided $\vert 0\rangle$ is measured on the auxiliary register.

(b) We have only specified how PREPARE acts on the state $\vert 0 \rangle$, namely $\text{PREPARE}\vert 0\rangle = \vert\alpha\rangle$. Verify that it can take the form

$$
\text{PREPARE} = I - \frac{(\vert 0\rangle - \vert \alpha\rangle)(\langle 0\vert - \langle \alpha \vert)}{1 - \langle 0\vert\alpha\rangle}.
$$

<details>
<summary><i>Solution.</i> (a)</summary>

Let's start by applying PREPARE and SELECT:

$$
\begin{align*}
\text{SELECT} \cdot \text{PREPARE} \vert 0\rangle \vert \psi\rangle & \propto \text{SELECT} \sum_j \sqrt{\alpha_j}\vert j\rangle \vert\psi\rangle\\
& = \sum_j \sqrt{\alpha_j}\vert j\rangle U_j\vert\psi\rangle.
\end{align*}
$$

We then apply PREPARE${}^\dagger$. If we observe $\vert 0\rangle$ on the auxiliary register, the corresponding output state is obtained (up to normalization) by taking the overlap with $\vert 0\rangle$:

$$
\begin{align*}
\langle 0\vert \text{PREPARE}^\dagger \sum_j \sqrt{\alpha_j}\vert j\rangle U_j\vert\psi\rangle &
\propto \sum_{j,k} \sqrt{\alpha_j\alpha_k}\langle k\vert j\rangle U_j\vert\psi\rangle \\
& = \sum_{j} \alpha_j U_j\vert\psi\rangle \\
& = \tilde{U}\vert \psi\rangle,
\end{align*}
$$

as required. ▢

</details>

<details>
<summary>(b)</summary>

First, let's check this acts in the correct way on $\vert 0\rangle$:

$$
\begin{align*}
\text{PREPARE}\vert 0\rangle & = \vert 0\rangle - \frac{(\vert 0\rangle - \vert \alpha\rangle)(\langle 0\vert 0\rangle - \langle \alpha \vert 0\rangle)}{1 - \langle 0\vert\alpha\rangle} \\
& = \vert 0\rangle - (\vert 0\rangle - \vert \alpha\rangle) \\
& = \vert \alpha\rangle,
\end{align*}
$$

since $\langle 0\vert 0\rangle = 1$. To show it is unitary, we note that, since $\vert \alpha\rangle$ has real coefficients,

$$
\begin{align*}
|\langle 0\vert \alpha \rangle|^2 & = (\langle 0\vert - \langle \alpha \vert)(\vert 0\rangle - \vert \alpha\rangle) \\
& = \langle 0\vert 0\rangle + \langle \alpha\vert\alpha \rangle - 2\langle 0\vert \alpha\rangle \\
& = 2(1 - \langle 0\vert \alpha\rangle).
\end{align*}
$$

Hence, we can write

$$
\begin{align*}
\text{PREPARE} & = I - \frac{2(\vert 0\rangle - \vert \alpha\rangle)(\langle 0\vert - \langle \alpha \vert)}{\vert \vert 0\rangle - \vert \alpha\rangle \vert^2} \\
& = I - 2 \vert 0 - \alpha\rangle \langle 0 - \alpha \vert,
\end{align*}
$$

where $\vert 0 - \alpha\rangle$ is the normalized difference of states. This is a reflection (in fact, it has the fancy name of *Householder transformation*), and hence unitary by the same logic as, e.g., the oracle $U = I - 2\vert \mathbf{s}\rangle\langle \mathbf{s}\vert$. ▢

</details>

---

So, let's briefly recap how we ended up here.
We wanted to simulate Hamiltonian evolution by truncating the Taylor
series at some finite number of terms,

$$
e^{-it \hat{H}/\hbar} \approx I + \left( \frac{-i\hat{H}}{\hbar}\right) + \frac{1}{2!}\left(\frac{-i\hat{H}}{\hbar}\right)^2 + \cdots + \frac{1}{K!}\left(\frac{-i\hat{H}}{\hbar}\right)^K.
$$

This could be associated with a number of tiny interacting magnets or
the Hamiltonian for solving a graph problem.
To actually implement this on a quantum computer, we built a
non-deterministic circuit for applying linear combinations of unitaries.
We singled out two subroutines, PREPARE and SELECT, and streamlined
them to present them in the form given here.

This was not just an exercise in abstraction!
The PREPARE and SELECT oracles turn out to be useful for a broader
range of tasks than performing a linear combination of unitaries.
In the next node, we will see how they can used for yet another method
of Hamiltonian simulation.
But we'll end this node on a somewhat different note, and apply them
to quantum memory!

Suppose we have a number of memory cells in our quantum computer, indexed by
$j$.
We would like to retrieve data from them and even place it in superpositions.
One approach is to create (1) an **address register** for storing the index $j$, with a
corresponding orthonormal set of states $\vert j\rangle_A$, and (2) a **data register**
for storing (quantum or classical) data in the form of states $\vert D_j\rangle_D$.
We also assume these data states are prepared from the initial state
$\vert 0\rangle_D$ of the data register via a unitary $U_j$, $\vert
D_j\rangle_D = U_j\vert 0\rangle_D$.
In the course of running its algorithms, a quantum computer may wish
to generate a *superposition* of these data states, tagged with their
addresses, starting from an initial state:

$$
\vert 0\rangle_A \vert 0\rangle_D \to  \sum_j \beta_j \vert
j\rangle_A \vert D_j\rangle_D.
$$

We can perform the retrieval and superposition using
one application of the PREPARE and SELECT oracles associated with the
LCU

$$
\tilde{U} = \sum_j \beta_j^2 U_j.
$$

You can check this below.
The moral is that PREPARE and SELECT are not only relevant to Hamiltonian
simulation, but quantum architecture design!

---

***Exercise H.7.2.*** Since PREPARE and SELECT involve a *positive*
linear combination, it seems our data superpositions will be
restricted to positive coefficients.
To address this (pun intended), we just need to add another gate.
Suppose we would like to prepare a quantum data
   state with complex coefficients,

$$
\vert \phi\rangle = \sum_j \phi_i \vert j\rangle_A \vert D_j\rangle_D,
$$

where $\phi_j = \vert \phi_j\vert e^{i\theta_j}$ and $\vert D_j\rangle_D
= U_j\vert 0\rangle_D$. Define a unitary gate
$\Theta$ acting on the address register as $\Theta \vert j\rangle_A =
e^{i\theta_j} \vert j\rangle_A.$
Show that we can prepare this state by applying $\Theta$ after
$\text{SELECT}\cdot \text{PREPARE}$, for the oracles associated with
the LCU

$$
\tilde{U} = \sum_j \vert\phi_j\vert^2 U_j.
$$

<details>
<summary><i>Solution.</i></summary>

From ***Exercise H.7.1.***, we know that

$$
\begin{align*}
\text{SELECT} \cdot \text{PREPARE} \vert 0\rangle_A \vert 0\rangle_D &
\propto \sum_j \sqrt{\vert\phi_j\vert^2}\vert j\rangle_A
U_j\vert 0\rangle_D\\
& \sum_j \vert\phi_j\vert \, \vert j\rangle_A \vert D_j\rangle_D.
\end{align*}
$$

Applying $\Theta$ gives

$$
\begin{align*}
\Theta\sum_j \vert\phi_j\vert \, \vert j\rangle_A \vert D_j\rangle_D &
=\sum_j \vert\phi_j\vert \Theta\vert j\rangle_A \vert D_j\rangle_D\\
& =\sum_j \vert\phi_j\vert e^{i\theta_j}\vert j\rangle_A \vert
D_j\rangle_D\\
& =\sum_j \phi_j \vert j\rangle_A \vert D_j\rangle_D \\ & = \vert \phi\rangle,
\end{align*}
$$

as required. ▢

</details>

---
