In module **A**, we sped up the lock-breaking process by testing
states in pairs. This told us when the solution was present, but not
which state it was. Our goal now will be to try and figure out the
state $\vert \mathbf{s}\rangle$ directly, and our broad strategy will
be to start in the uniform superposition and somehow "pump" amplitude
from the other states into $\vert\mathbf{s}\rangle$, so that we
measure the solution $\mathbf{s}$ with high probability. This strategy
is called **amplitude amplification**. Let's start by exploring what
happens to amplitudes when we apply the oracle.

---

***Codercise G.1.1.*** Complete the following code for returning the
   amplitudes after applying the oracle to the uniform superposition. The oracle is accessible as
   ``oracle_matrix(combo)``, where ``combo`` is the secret combination. Amplitudes will be plotted for ``combo =
   [0, 0, 0, 1]``.

<details>
<summary><i>Hint.</i></summary>
Since the oracle is encoded as
   a matrix, you will need to use the
   <a href="https://pennylane.readthedocs.io/en/stable/code/api/pennylane.QubitUnitary.html" target="_blank">``QubitUnitary()``</a>
   method in PennyLane.
</details>
