---

We'll define the PREPARE oracle as the Householder transformation
of the state

$$
\vert 0 - \alpha\rangle  =\frac{\vert 0\rangle - \vert
\alpha \rangle}{\vert \vert 0\rangle - \vert
\alpha \rangle \vert}.
$$

This requires a little explanation. First, $\vert \alpha\rangle$ is a
vector of coefficients which has been normalized and can therefore be
interpreted as a state.
Then $\vert 0\rangle - \vert \alpha\rangle$ is a difference of states,
and is normalized by the denominator.
You can implement this in the next exercise.

---

***Codercise H.7.2.*** (a) Implement the PREPARE oracle using the
   Householder transformation; this is available from the previous exercise. For simplicity, we work with a sum of $2^k$
   unitaries. This means our auxiliary register will have $k$ qubits,
   and the state $\vert 0\rangle$ is the all-zero state (usually
   denoted $\vert \mathbf{0}\rangle$).
