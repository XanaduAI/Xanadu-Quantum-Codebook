Trotterization approximates time evolution by reexpressing the full
Taylor series as a product of simpler Taylor series.
Another way to approximate this evolution is to truncate the Taylor series at some term $K$:

$$
e^{-it\hat{H}/\hbar} \approx 1 + \left(\frac{it\hat{H}}{\hbar}\right) + \cdots + \frac{1}{k!}\left(\frac{it\hat{H}}{\hbar}\right)^K.
$$

If $K$ is large, this should be a good approximation. If $\hat{H}$ is
a weighted sum of unitary operators (as in the case of spins, where
terms are built of out Pauli operators, e.g., $\alpha Z \otimes Z$),
then each term in the sum will be proportional to a unitary, since a product of unitary matrices is unitary. So the problem reduces to implementing a **linear combination of unitaries (LCU)**.

As a warm-up, let's consider the problem of adding two unitaries, $U$ and $V$, and applying them to an arbitrary state:

$$
\vert \psi\rangle \to (U + V) \vert \psi\rangle.
$$

The sum $U+V$ won't be unitary in general, so there is no gate which
applies it with certainty. However, we can *non-deterministically*
apply it, in the sense that we can write down a circuit which applies
it with some probability less than one.
Here is the circuit:

<img src="pics/h-circuit.svg" width="400px">

The top wire is an auxiliary qubit we measure as part of our circuit,
while the bottom wire is the main register carrying the state we want
to apply the combined operation to. If the outcome is $0$, then the
outcome (up to normalization) is

$$
(U + V)\vert \psi\rangle.
$$

Let's code this up and check it works for a concrete example.

---

***Codercise H.6.1.*** (a) Write a circuit for applying a sum of
   unitaries non-deterministically. Don't worry about initialization
   of the state just yet.

*Tip.* Use
 [``qml.ControlledQubitUnitary``](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.ControlledQubitUnitary.html)
 to apply these unitaries with control bits.
