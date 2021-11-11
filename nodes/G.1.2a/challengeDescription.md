---

Clearly the oracle flips the sign of the amplitude of the solution. But just flipping the sign is not useful by itself, since the *probability* (amplitude squared) of observing it when we measure does not change. We need a new ingredient! Note that the oracle

$$
U_f = I - 2\vert \mathbf{s}\rangle\langle \mathbf{s}\vert
$$

has the effect of flipping the sign of a special state, namely the
solution $\vert \mathbf{s}\rangle$. The only other state that has
appeared and seems to play an interesting role is the uniform superposition $\vert \psi\rangle$, so a simple guess for another operator to play with is

$$
D = 2\vert \psi\rangle\langle\psi\vert  - I.
$$

The choice of sign will become clear in subsequent challenges. $D$ is
called the **diffusion operator**. If we split the state into a part
proportional to $\vert \psi\rangle$ and a part orthogonal to it, it
flips the sign of the orthogonal part. We will apply the diffusion
operator after applying the oracle, in a combined operator $G = DU_f$
called the **Grover operator**.

---

***Codercise G.1.2.*** (a) Define the diffusion operator as a matrix,
   and visualize its effect on the amplitudes in the post-oracle
   state. We'll plot the amplitudes for
   ``combo=[0, 0, 0, 0]``. Note that ``oracle_matrix(combo)`` remains available.

<details>
<summary><i>Hint.</i></summary>
The diffusion matrix can be written as

$$
D = \frac{1}{2^{n-1}}\mathbf{1} - I,
$$

where $\mathbf{1}$ is the $2^n\times 2^n$ matrix with $1$ in each entry. You will therefore find [``np.ones()``](https://numpy.org/doc/stable/reference/generated/numpy.ones.html) useful in addition to [``np.eye()``](https://numpy.org/devdocs/reference/generated/numpy.eye.html).
</details>
