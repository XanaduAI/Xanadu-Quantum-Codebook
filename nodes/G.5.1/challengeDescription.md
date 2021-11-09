So far, we've focused on searching for a single solution or marked item. For $M$ solutions (or marked items), Grover search works almost exactly the same way. For a solution set $S$, our goal will be to maximize the amplitude of

$$
\vert S\rangle = \frac{1}{\sqrt{M}}\sum_{\mathbf{s}\in S}\vert \mathbf{s}\rangle,
$$

so we observe a solution with high probability. Note that we're assuming it doesn't matter which one we observe, as long as we find one with high probability! Let's introduce an auxiliary register, and apply some optimal number of Grover steps, consisting of an oracle followed by the diffusion operator. The diffusion operator is the same as before, but the oracle will need to be modified since there are now multiple solutions. But the modification is easy, since a multi-solution oracle $\hat{U}$  with solutions $\mathbf{s}_1, \mathbf{s}_2, \ldots, \mathbf{s}_M$ is just a product of the single-solution oracles:

<img src="pics/multi-oracle.svg">

We will just plop this new multi-solution oracle into the original circuit for a single Grover step:

<img src="pics/multi-oracle-circuit.svg" width="600px">

Let's start by coding up this new oracle.

---

***Codercise G.5.1.*** Create an oracle for a random solution set of a given size using the [``MultiControlledX``](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.MultiControlledX.html) gate. Remember that this takes a string for `control_values` (e.g.,``"11011"``) as a parameter rather than a list of bits.
