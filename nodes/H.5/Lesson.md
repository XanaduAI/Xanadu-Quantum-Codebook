---

**Learning outcomes**

- *Derive the Trotter-Suzuki decomposition.*
- *Use Trotterization to simulate a simple physical system.*

---

Now we know how to simulate a single electron in a magnetic field. What about two electrons? If they are far away, they don't know about each other and won't interact at all! They only care about the big magnetic field:

<img src="pics/twomagnets.svg" width="420px">

As a result, the measured energy of the system will just be the sum of the energy for the first electron and the second electron separately. If the magnetic field points in the $z$-direction (once again, just for simplicity) then the resulting Hamiltonian is

$$
\hat{H} = \hat{H}_1 + \hat{H}_2 = -\frac{e\hbar B}{2 m_e}(Z_1 + Z_2),
$$

where $Z_1 = Z \otimes I$ is the Pauli $Z$ operator on the first electron and $Z_2= I \otimes Z$ the Pauli $Z$ on the second. If we wanted to measure the energy in a circuit, we could just take two measurements in the computational basis, and convert them to energies as below:

<img src="pics/twospin.svg" width="520px">

Because these electrons are independent, evolving the system in time should consist of evolving the first and second states independently. We also know what those independent parts look like, since in the last node we learned how to time-evolve an individual electron. So, with $\alpha = eB/2m_e$ as before, we're naturally led to guess that the combined unitary is just a product of unitaries on each electron:

$$
U = U_1 U_2 = e^{i\alpha t Z_1}e^{i\alpha t Z_2}.
$$

In circuit form:

<img src="pics/prod-circ.svg" width="400px">

Is this neat formula true? Schrödinger's equation tells us that

$$
U = e^{-i t\hat{H}/\hbar} = e^{i\alpha t(Z_1 + Z_2)}.
$$

So our neat formula will be true as long as

$$
e^{i\alpha t(Z_1 + Z_2)} = e^{i\alpha tZ_1}e^{i\alpha tZ_2}. \tag{1} \label{prod}
$$

This should seem familiar: it's the usual index law for exponentials, $e^{x+y} = e^xe^y$, but now with matrices $Z_1$ and $Z_2$ instead of numbers $x$ and $y$. And in fact, the proof works the same way! There are lots of ways of defining the exponential, but here is a useful one:

$$
e^x = \lim_{n \to \infty}\left(1 + \frac{x}{n}\right)^n.
$$

Even more precisely, we can state that

$$
e^x = \left(1 + \frac{x}{n}\right)^n + O\left(\frac{1}{n^2}\right).
$$

The notation $O(1/n^2)$ indicates a term which, for
large $n$, is bounded above by a multiple of $1/n^2$, i.e.,

$$
O\left(\frac{1}{n^2}\right) \leq \frac{C}{n^2}
$$

as $n \to \infty$. Let's draw a little cartoon to help us:

<img src="pics/exp(x).svg" width="420px">

Let's see why the index law $e^{x+y} = e^x e^y$ is true from this definition. First of all, we can write

$$
e^{x + y} = \lim_{n \to \infty}\left(1 + \frac{x + y}{n}\right)^n. \tag{2} \label{exp-lhs}
$$

That's easy enough! The product, on the other hand, is

$$
e^{x}e^y = \lim_{n \to \infty}\left(1 + \frac{x}{n}\right)^n \cdot \lim_{m \to \infty}\left(1 + \frac{y}{m}\right)^m = \lim_{n, m \to \infty}\left(1 + \frac{x}{n}\right)^n \left(1 + \frac{y}{m}\right)^m.
$$

We can do a trick now, and let $n = m$. This doesn't affect the value of the limit, as long as both are defined. So we have

$$
e^{x}e^y = \lim_{n \to \infty}\left(1 + \frac{x}{n}\right)^n\left(1 + \frac{y}{n}\right)^n= \lim_{n \to \infty}\left[\left(1 + \frac{x}{n}\right)\left(1 + \frac{y}{n}\right)\right]^n = \lim_{n \to \infty}\left[1 + \frac{x + y}{n} + \frac{xy}{n^2}\right]^n. \tag{3} \label{exp-rhs}
$$

This is almost the same as (\ref{exp-lhs}), except for that pesky term $xy/n^2$. But for *fixed* $x$ and $y$, as $n$ gets large this is much smaller than $(x + y)/n$, so

$$
1 + \frac{x + y}{n} + \frac{xy}{n^2} \approx 1 + \frac{x + y}{n}.
$$

We recover (\ref{exp-lhs}) after all, and conclude that $e^{x+y} = e^x e^y$. In terms of our cartoon, this really boils down to equating the following boxes:

<img src="pics/exp(x)exp(y).svg" width="800px">

If you want a little more rigor, you can fill in an important mathematical detail in the next exercise.

---

***Exercise H.5.1.*** *Bonus.* Argue that, as $n$ gets large,

$$
\left(1 + \frac{x + y}{n} + \frac{xy}{n^2}\right)^n = \left(1 + \frac{x + y}{n}\right)^n + O\left(\frac{1}{n}\right),
$$

so the correction is suppressed as $n$ gets large. *Hint*. Use the binomial expansion.

<details>
<summary><i>Solution.</i></summary>

The binomial expansion gives

$$
\begin{align*}
\left[\left(1 + \frac{x + y}{n}\right) + \frac{xy}{n^2}\right]^n & = \sum_{k=0}^n \binom{n}{k}\left(\frac{xy}{n^2}\right)^k\left(1 + \frac{x + y}{n}\right)^{n-k}.
\end{align*}
$$

Each term for $k \geq 1$ will have a coefficient

$$
\binom{n}{k}\left(\frac{xy}{n^2}\right)^k = \frac{n(n-1)\cdots (n-k+1)}{k!} \cdot \frac{(xy)^k}{n^{2k}} \leq \frac{(xy)^k}{n^k} = O\left(\frac{1}{n}\right).
$$

This leaves 

$$
\begin{align*}
\left[\left(1 + \frac{x + y}{n}\right) + \frac{xy}{n^2}\right]^n & =\left(1 + \frac{x + y}{n}\right)^n + \sum_{k=1}^n \binom{n}{k}\left(\frac{xy}{n^2}\right)^k\left(1 + \frac{x + y}{n}\right)^{n-k} \\ & = \left(1 + \frac{x + y}{n}\right)^n + O\left(\frac{1}{n}\right),
\end{align*}
$$

as required. ▢

</details>

---

The point of going through this in detail is to understand what happens when we replace $x$ and $y$ with matrices. The definition of the exponential is the same,

$$
e^A = \lim_{n\to \infty} \left(I + \frac{A}{n}\right)^n,
$$

where $I$ is the identity matrix. (This is equivalent to the Taylor series definition,

$$
e^A = \sum_{k=0}^\infty \frac{A^k}{k!},
$$

but the limit will be more useful here.) Our argument almost goes through as before, except for one important subtlety. Above, we made the innocuous-seeming jump

$$
\left(1 + \frac{x}{n}\right)^n \left(1 + \frac{y}{n}\right)^n = \left[\left(1 + \frac{x}{n}\right)\left(1 + \frac{y}{n}\right)\right]^n.
$$

But this isn't always true if we replace $x$ and $y$ with matrices $A$ and $B$:

$$
\left(I + \frac{A}{n}\right)^n \left(I + \frac{B}{n}\right)^n \overset{?}{=} \left[\left(I + \frac{A}{n}\right)\left(I + \frac{B}{n}\right)\right]^n. \tag{4} \label{jump}
$$

On the LHS, all the $x$ terms are to the left of the $y$ terms. On the RHS, the $x$ and $y$ terms get interwoven. Thus, this identity makes tacit use of the fact that numbers $x$ and $y$ **commute**, i.e., they can be freely reordered. In pictures:

<img src="pics/reorder.svg" width="800px">

If $A$ and $B$ happen to commute, then we can do the reordering and conclude that

$$
e^A e^B = e^{A + B}.
$$

An example is (\ref{prod}), since the Paulis $Z_1$ and $Z_2$ acting on separate electrons can be reordered:

$$
Z_1 Z_2 = (Z \otimes I)(I \otimes Z) = Z \otimes Z = (I \otimes Z)(Z \otimes I) = Z_2 Z_1.
$$

It's easy to see this in terms of the circuit. Since the $Z$ gates act on separate wires, we can freely drag them past each other:

<img src="pics/reorder-z.svg" width="600px">

So our guess (\ref{prod}) for the evolution of two distant electrons
is correct. But matrices do not always commute! A simple example is
Pauli matrices, e.g., $XY = Z$ while $YX = -Z$. Physically, we will
have problems when our electrons get too close and feel each other's magnetic field. They will interact, and in the simplest case, want to *anti-align*, just like iron filings arranging themselves along field lines:

<img src="pics/dimagnets.svg" width="400px">

This introduces an energy cost for spins aligning, measured
classically by a term $J \mathbf{S}_1\cdot \mathbf{S}_2$, where $J$
captures the strength of the interaction. Quantum-mechanically, this leads to a Hamiltonian

$$
\hat{H} = \hat{H}_1 + \hat{H}_2 + \hat{H}_{12} = -\frac{\hbar Be}{2 m_e}(Z_1 + Z_2) + \frac{J\hbar^2}{4}(X_1X_2 + Y_1Y_2 + Z_1Z_2), \tag{5} \label{Jcouple}
$$

since $\mathbf{S} \mapsto {\hbar/2}(X, Y, Z)$. Each of the terms in the Hamiltonian is *individually* easy to exponentiate, as you can check in the next exercise. The problem is that they don't commute!

---

***Exercise H.5.2.*** (a) Verify that

$$
e^{i\beta t X_1X_2} = \cos(\beta t) \cdot I + i \sin(\beta t) \cdot X_1X_2.
$$

Explain why the result is true if we replace $X_1X_2$ by $Y_1Y_2$ or $Z_1Z_2$.

(b) Show that the terms in (\ref{Jcouple}) do not commute.

<details>
<summary><i>Solution.</i></summary>

(a) Since $X_1$ and $X_2$ commute (they act on different electrons), $(X_1X_2)^k = X_1^k X_2^k$. Hence,

$$
e^{i\beta t X_1X_2} = \sum_{k= 0}^\infty \frac{(i\alpha t)^k}{k!} (X_1X_2)^k = \sum_{k= 0}^\infty \frac{(i\alpha t)^k}{k!} X_1^kX_2^k.
$$

The even terms are trivial, $X_1^{2k}X_2^{2k} = I$, and hence the odd terms give $X_1^{2k+1}X_2^{2k+1} = X_1X_2$. This is the same as the single Pauli case, so the same formula drops out. In fact, it's clear that if we replace $X_1X_2$ with any matrix $G$ satisfying $G^2 = I$ (such as $G = Y_1Y_2$ or $G = Z_1Z_2$), the same result will hold.

(b) We can look at the terms proportional to, say, $Z_1$ and $X_1X_2$. Since $X_1$ and $Z_1$ *anticommute*, while $Z_1$ and $X_2$ commute, we will have

$$
Z_1 X_1 X_2 = - X_1 Z_1 X_2 = - X_1 X_2 Z_1.
$$

So we won't be able to write the exponential of (\ref{Jcouple}) as a
product of exponentials of its terms. ▢

</details>

---

Most of the Hamiltonians Nature gives us do not split into commuting terms, even if (as often happens) the component terms are themselves simple and easy to exponentiate. It seems as if each time we want to run a simulation, we need to solve some horrible matrix exponential that cannot be decomposed into simpler parts. But it turns out we can simply reinterpret (\ref{jump}) in an extremely useful way. The Taylor expansion of the exponential $e^x \approx 1 + x$, for small $x$, has the analogue

$$
e^{A/n} = I + \frac{A}{n} + O\left(\frac{1}{n^2}\right)
$$

for matrices $A$.
So we can understand the RHS of (\ref{jump}), in the limit of large $n$, as

$$
\begin{align*}
\left(e^{A/n}e^{B/n}\right)^n & =
\left[\left(I + \frac{A}{n} + O\left(\frac{1}{n^2}\right)\right) \left(I + \frac{B}{n} + O\left(\frac{1}{n^2}\right)\right)\right]^n
\\
& =\left[\left(I + \frac{A}{n}\right) \left(I + \frac{B}{n}\right) + O\left(\frac{1}{n^2}\right)\right]^n
\\
& = \left[\left(I + \frac{A}{n}\right) \left(I + \frac{B}{n}\right)\right]^n+
n \cdot O\left(\frac{1}{n^2}\right)\\
&
=\left[\left(I + \frac{A}{n}\right) \left(I + \frac{B}{n}\right)\right]^n+
O\left(\frac{1}{n}\right),
\end{align*}
$$

where we've used the binomial expansion on the third line. But the LHS is what we get from $e^{A+B}$, and discarding the term $AB/n^2$ which introduces an error $O(1/n),$ as per **Exercise H.5.1**. In cartoons, both expressions have the "interleaved" form:

<img src="pics/ntimes.svg" width="400px">

Since the difference shrinks as $1/n$, we arrive at the famous **Trotter-Suzuki decomposition**:

$$
e^{A + B} = \left(e^{A/n}e^{B/n}\right)^n + O\left(\frac{1}{n}\right). \tag{6} \label{trotter}
$$

This leads to the elegant limit

$$
e^{A + B} = \lim_{n\to\infty}\left(e^{A/n}e^{B/n}\right)^n.
$$

The formula (\ref{trotter}) gives us a general method for simulating quantum systems called **Trotterization**. Suppose our Hamiltonian is a sum of terms

$$
\hat{H} = \hat{H}_1 + \hat{H}_2,
$$

and each unitary $e^{-i t\hat{H}_1/\hbar} = U_1(t)$, $e^{-i t\hat{H}_2/\hbar} = U_2(t)$, is easily simulated. Even if $\hat{H}_1$ and $\hat{H}_2$ don't commute, we can split time evolution $U(t)$ by $t$ into $n$ steps and interleave, with an error of order $1/n$:

$$
U(t) = e^{-i t\hat{H}/\hbar} = e^{-i t(\hat{H}_1 + \hat{H}_2)/\hbar} = \left[U_1(t/n) U_2(t/n)\right]^n + O\left(\frac{1}{n}\right).
$$

Thus, we can replace $U(t)$ with the circuit

<img src="pics/trotter-circ.svg" width="450px">

Let's see a concrete example of how this works for (\ref{Jcouple}), or rather, a slightly simplified version which only keeps the $X_1X_2$ term in the interaction.

---

***Exercise H.5.3.***  Consider a Hamiltonian

$$
\hat{H} = -\frac{\hbar Be}{2 m_e}(Z_1 + Z_2) + \frac{J\hbar^2}{4}X_1X_2.
$$

Let $U(t)$ by the unitary evolving this system by time $t$. Using (\ref{trotter}), split this evolution into $n$ time steps and write the corresponding unitary $U$.

<details>
<summary><i>Solution.</i></summary>

Let $\alpha = Be/2m_e$ and $\beta = -J\hbar/4$. Then

$$
U = e^{-it\hat{H}/\hbar} = e^{i\alpha t(Z_1 + Z_2) + i\beta t X_1X_2}.
$$

Invoking (\ref{trotter}) and interleaving $n$ steps gives

$$
U(t) = \left[e^{i\alpha t (Z_1 + Z_2)/n}e^{-i\beta tX_1X_2/n}\right]^n + O\left(\frac{1}{n}\right) = \left[e^{i\alpha t Z_1/n}e^{i\alpha t Z_2/n}e^{i\beta tX_1X_2/n}\right]^n + O\left(\frac{1}{n}\right),
$$

since $e^{i\alpha t (Z_1 + Z_2)/n} = e^{i\alpha t Z_1/n}e^{i\alpha t Z_2/n}$. We can then evaluate each term individually. We know from the previous node that

$$
e^{i\alpha tZ/n} = \cos\left(\frac{\alpha t}{n}\right) \cdot I + i \sin \left(\frac{\alpha t}{n}\right) \cdot Z,
$$

and from the previous exercise

$$
e^{i\beta t X_1X_2/n} = \cos\left(\frac{\beta t}{n}\right) \cdot I + i \sin \left(\frac{\beta t}{n}\right) \cdot X_1X_2.
$$

Thus, we obtain a Trotterized time evolution

$$
U(t) \approx \left[\left(\cos\left(\frac{\alpha t}{n}\right) \cdot I + i \sin \left(\frac{\alpha t}{n}\right) \cdot Z_1\right)\left(\cos\left(\frac{\alpha t}{n}\right) \cdot I + i \sin \left(\frac{\alpha t}{n}\right) \cdot Z_2\right)\left(\cos\left(\frac{\beta t}{n}\right) \cdot I + i \sin \left(\frac{\beta t}{n}\right) \cdot X_1X_2\right)\right]^n,
$$

with each piece easily simulable on a quantum computer. ▢

</details>

---

We can generalize (\ref{trotter}) to a Hamiltonian built from $L$ simple pieces,

$$
\hat{H} = \hat{H}_1 + \hat{H}_2 + \cdots + \hat{H}_L.
$$

In this case, (\ref{trotter}) becomes

$$
U(t) = e^{-it\hat{H}/\hbar} = \left[U_1(t/n)U_2(t/n)\cdots U_L(t/n)\right]^n + O\left(\frac{1}{n}\right), \tag{7} \label{trotterL}
$$

where $U_k(t) = e^{-it\hat{H}_k/\hbar}$. In circuit form, we can replace $U(t)$ with

<img src="pics/trotterL.svg" width="500px">

This lets us extend the results of ***Exercise H.5.3*** to more complicated Hamiltonians like (\ref{Jcouple}), which have more than two individually simple but non-commuting terms. So, we're beginning to get a good handle on how to simulate the black boxes of nature!

---

***Exercise H.5.4.*** *Bonus.* Derive (\ref{trotterL}) by generalizing the derivation of (\ref{trotter}).

<details>
<summary><i>Solution.</i></summary>

The basic idea is straightforward. Let's simplify the constants and consider $e^{A_1 + A_2 + \cdots + A_L}$ for possibly non-commuting matrices $A_1, A_2, \ldots, A_L$. From the limit definition we've been using,

$$
e^{A_1 + A_2 + \cdots + A_L} = \lim_{n\to\infty} \left(I + \frac{A_1 + A_2 + \cdots + A_L}{n}\right)^n.
$$

Using $e^{A_k/n} \approx I + A_k/n + O(1/n^2)$, we also have

$$
\begin{align*}
e^{A_1/n}e^{A_2/n}\cdots e^{A_L/n} & = \left(I + \frac{A_1}{n}\right)\left(I + \frac{A_2}{n}\right)\cdots \left(I + \frac{A_L}{n}\right) + O\left(\frac{1}{n^2}\right) \\
& = I + \frac{A_1 + A_2 + \cdots + A_L}{n} + O\left(\frac{1}{n^2}\right).
\end{align*}
$$

Thus, 

$$
\begin{align*}
\left(e^{A_1/n}e^{A_2/n}\cdots e^{A_L/n}\right)^n & = \left(I + \frac{A_1 + A_2 + \cdots + A_L}{n} + O\left(\frac{1}{n^2}\right)\right)^n \\
& = \left(I + \frac{A_1 + A_2 + \cdots + A_L}{n}\right)^n + O\left(\frac{1}{n}\right),
\end{align*}
$$

where the change from $O(1/n^2)$ to $O(1/n)$, as we shift the term outside the brackets, comes from the binomial expansion. Combining with the limit definition (which has a smaller error $O(1/n^2)$, which we can ignore), we obtain

$$
e^{A_1 + A_2 + \cdots + A_L} = \left(e^{A_1/n}e^{A_2/n}\cdots e^{A_L/n}\right)^n + O\left(\frac{1}{n}\right),
$$

which leads immediately to (\ref{trotterL}). ▢

</details>

---
