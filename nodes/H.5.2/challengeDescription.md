---

Another way to express this circuit is in matrix form, $U(t) = e^{i\alpha t Z_1}e^{i\alpha tZ_2}$. Schrödinger's equation tells us, on the other hand, that $U(t) = e^{-t \hat{H}/\hbar} = e^{i\alpha t (Z_1 + Z_2)}$. These two expressions appear to be equal by virtue of the rule $e^{x + y} = e^x e^y$. But not so fast! We are dealing with *matrices* rather than numbers, and this makes a huge change.

It turns out that, for matrices $A$ and $B$, $e^{A + B} = e^A e^B$ is only true when $A$ and $B$ can be freely reordered, or $AB = BA$. We say such matrices **commute**. When terms do not commute, exponentiating their sum is hard. As a concrete example, consider two nearby electrons, who can feel each other's magnetic field. The Hamiltonian will now include an interaction term since the spins of these electrons would like to anti-align:

<img src="pics/dimagnets.svg" width="400px">

For simplicity, we'll make this interaction term proportional to $X_1 X_2$:

$$
\hat{H} = -\frac{\hbar Be}{2 m_e}(Z_1 + Z_2) + \frac{J\hbar^2}{4}X_1X_2, \tag{1} \label{non-comm}
$$

where $J$ depends on how close they are. (The factor of $(\hbar/2)^2$ comes from converting spins into Pauli operators.) To time evolve this system we need to exponentiate these non-commuting terms, which is hard. Thankfully, there is a beautiful approximation called the **Trotter-Suzuki decomposition**:

$$
e^{A+B} = \lim_{n\to\infty} (e^{A/n}e^{B/n})^n.
$$

This leads to a simple algorithm called **Trotterization** for simulating a quantum system. Suppose we have a Hamiltonian $\hat{H} = \hat{H}_1 + \hat{H}_2$ where $\hat{H}_1$ and $\hat{H}_2$ can be easily exponentiated in our computer, but don't commute. Then Trotter-Suzuki tells us that, for some large number of steps $n$,

$$
U(t) = e^{-it\hat{H}/\hbar} = e^{(-it\hat{H}_1/\hbar) + (-it\hat{H}_2/\hbar)} \approx \left[e^{-i(t/n)\hat{H}_1/\hbar}e^{-i(t/n)\hat{H}_2/\hbar}\right]^n = \left[U_1(t/n)U_2(t/n)\right]^n,
$$

where $U_1(t)$ and $U_2(t)$ are the unitaries associated with exponentiating the terms $\hat{H}_1$ and $\hat{H}_2$. Thus, we can approximate $U(t)$ with the circuit

<img src="pics/trotter-circ.svg" width="450px">

for some large $n$. Let's see how this works for (\ref{non-comm}).

---

***Codercise H.5.2.*** Write a circuit to Trotterize the evolution of two electrons with Hamiltonian (\ref{non-comm}).

*Tip.* For exponentiating $X_1X_2$, you will find <a href="https://pennylane.readthedocs.io/en/stable/code/api/pennylane.PauliRot.html" target=_"blank"><tt>qml.PauliRot</tt></a> helpful.
