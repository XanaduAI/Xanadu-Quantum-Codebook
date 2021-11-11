---

We know that PREPARE and SELECT are useful for Hamiltonian
simulation. But it turns out that we can also use them to implement
memory on a quantum computer!
We imagine that the auxiliary states $\vert j\rangle_A$ are memory
addresses and the main register stores data $\vert D_j\rangle_D$,
prepared from some initial state $\vert 0\rangle_D$ by acting with a unitary, $\vert
D_j\rangle_D = U_j \vert 0\rangle_D$
(we've added subscripst for clarity.)
The quantum computer may wish not only to retrieve individual states
from their addresses, but to create an arbitrary superposition of data
states.
In order to remember which data belongs where, we assume they remain
correlated with their addresses, so the task of our is to take
the initial state $\vert 0\rangle_A \vert 0\rangle_D$ to a state of the form

$$
\vert\beta\rangle = \sum_j \beta_j \vert j\rangle_A \vert D_j\rangle_D.
$$

For $\beta_j \geq 0$, this can be created using the PREPARE and SELECT
oracles associated with the LCU $\tilde{U} = \sum_j \beta_j^2
U_j$. Specifically,

$$
\vert\beta\rangle = \text{SELECT} \cdot \text{PREPARE} \vert 0\rangle_A \vert 0\rangle_D.
$$

It's possible to modify this to allow for *arbitrary* superpositions,
but in the last codercise, you can implement the simpler case of positive coefficients.

---

***Codercise H.7.3.*** Use the PREPARE and SELECT procedures you
   defined above to generate superpositions of two-qubit
   computational basis states,

$$
\vert\beta\rangle = \beta_{00}\vert 00\rangle + \beta_{01}\vert
01\rangle+\beta_{10}\vert 10\rangle + \beta_{11}\vert 11\rangle.
$$

Is this correctly producing the maximally entangled state, $(\vert
00\rangle + \vert 11\rangle)/\sqrt{2}$?
