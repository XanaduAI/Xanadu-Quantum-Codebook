The result of applying the Hadamard-oracle-Hadamard circuit for a
single solution is a probability distribution peaked at $\mathbf{0}$,
whatever the secret combination.
Although we can't use it to break the lock, perhaps we can determine
some property of the solution set when there is more than one, just
like the pair-testing circuit.

To see whether this is possible, let's implement the same
Hadamard-oracle-Hadamard circuit, but now for multiple solutions:

![](pics/hadamard.svg)

Since $\mathbf{0}$ seemed to be the interesting state, we can plot how
the probability of observing $\mathbf{0}$ changes with the number of solutions.

---

***Codercise A.6.1.*** Implement the circuit above for a set of
   solutions ``combos``, and return probabilities. As before,
   you are given ``multisol_oracle_matrix(combos)``, which returns the
   associated oracle in matrix form.

Hitting submit will plot the probability of observing $\mathbf{0}$ as a function
   of the size of the solution set; as for a single solution, this
   does not depend on the secret combinations themselves. What pattern
   do you observe?
