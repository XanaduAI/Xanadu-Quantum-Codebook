---

Let's consider again an arbitrary state of a qubit:

$$
\vert \psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle. \tag{6}
$$

We know that $\vert \alpha\vert ^2 + \vert \beta\vert ^2 = \alpha \alpha^* + \beta \beta^* = 1$, but *why* must this be the case?

Quantum computing is all about manipulating states of qubits by 
modifying their state vectors in some way. But at the end of the day, we need to be
able to extract an answer from our quantum computer: we need to be able to
measure.

**Measurement** in quantum computing is probabilistic. When we measure a qubit,
  we can't see that it's in a superposition; we observe the qubit either in
  state $\vert 0\rangle$ or state $\vert 1\rangle$. If we think back to the
  coin analogy, measuring a qubit that is in superposition would be like
  spinning the coin on its edge, slamming your hand down over it, then checking
  to see whether it is "heads" or "tails".
  
The amplitudes $\alpha$ and
  $\beta$ contain the information about the probabilities of the possible outcomes:

$$
\begin{align*}
 \hbox{Prob(measure and observe } \vert 0\rangle) &= \vert \alpha\vert ^2, \\
 \hbox{Prob(measure and observe } \vert 1\rangle) &= \vert \beta\vert ^2. \\ \tag{7}
\end{align*}
$$

Since the qubit must be found in one of those two states, the probabilities must
sum to $1$.

Measuring a qubit once gets us effectively a single bit of information: which
state we observed the qubit in. This doesn't tell us very much about the state,
only that this particular basis state is involved in the superposition. In order to
get a clearer picture, we have to measure many times, and look at the
distribution of outcomes.

---

***Codercise I.1.3.*** The function below takes a quantum state vector as
   input. Complete the function to simulate the outcomes of an arbitrary number
   of quantum measurements, i.e., return a list of samples $0$ or $1$ based on
   the probabilities given by the input state.

<details>
  <summary><i>Example.</i></summary>

  Suppose we are given two states

  <pre>
  state = np.array([0.8, 0.6])</pre>

  If we measure a qubit in this state, we'll observe $\vert 0 \rangle$ 64% of the time ($|0.8|^2 = 0.64$),
  and $\vert 1 \rangle$ 36% of the time. Therefore, an example set of 10 measurement outcomes might be

  <pre>[0, 1, 1, 1, 0, 1, 0, 0 ,0 ,0]</pre>

</details>

<details>
  <summary><i>Hint.</i></summary>

The function <a href="https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html" target="_blank"><tt>np.random.choice</tt></a> will be helpful here.

</details>