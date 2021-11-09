So far, what we've learned about measurements is that the different outcome
probabilities are related to the amplitudes of a qubit's state vector. More
generally though, measurement in quantum computing is performed with respect to
a *basis*. Such **projective measurements** determine the probability of each
basis state outcome by computing the inner product between the basis state
$\vert \varphi\rangle$ and a target state $\vert \psi\rangle$:

$$
\hbox{Pr}(\varphi) = \vert \langle \varphi \vert  \psi \rangle\vert ^2.
$$

This inner product provides us with a measure of overlap between the states.

If no measurement basis is specified, you can generally assume that measurement
is done in the computational basis; this is the default in PennyLane.
Outcome probabilities of the basis states can be returned directly in PennyLane.
Rather than putting 

```python
return qml.state()
```

at the end of our QNodes, we can swap it out for 

```python
return qml.probs(wires=...)
```

where note that we must explicitly specify the wire labels
of the qubits we would like to measure.

---

***Codercise I.9.1.*** Write a simple circuit that applies a Hadamard gate to
   either $\vert 0\rangle$ or $\vert 1\rangle$, and returns the measurement
   outcome probabilities.  What do you notice about these probabilities?