---

A more realistic Hamiltonian for two nearby electrons involves
interactions proportional to $Y_1Y_2$ and $Z_1Z_2$ in addition to $X_1X_2$:

$$
\hat{H} = -\frac{\hbar Be}{2 m_e}(Z_1 + Z_2) + \frac{\hbar^2}{4}(J_X
X_1X_2 + J_Y Y_1Y_2 + J_Z Z_1Z_2). \label{J3} \tag{2}
$$

For a case like this, we can use a generalization of the Trotter-Suzuki formula for a sum of $L$ terms:

$$
e^{A_1+A_2 + \cdots + A_L} = \lim_{n\to\infty} \left(e^{A_1/n}e^{A_2/n}\cdots e^{A_L/n}\right)^n.
$$

Thus, for a Hamiltonian $\hat{H} = \hat{H}_1 + \cdots + \hat{H}_L$, we can replace the unitary $U(t)$ with a circuit

<img src="pics/trotterL.svg" width="500px">

Although we can code this time evolution by hand, it quickly becomes
tedious. Thankfully, in PennyLane we can input the Hamiltonian and
automatically Trotterize.

To start with, let's enter a Hamiltonian using the
<a href="https://pennylane.readthedocs.io/en/stable/code/api/pennylane.Hamiltonian.html" target=_"blank"><tt>Hamiltonian</tt></a>
method, which builds $\hat{H}$ by pairing a list of terms (assumed to
be products of Pauli operators on different qubits) and coefficients
for those terms.
In fact, for reasons to be explained in a moment, we will enter $\hbar
\hat{H}$, the Hamiltonian multiplied by Planck's constant.
For instance, the Hamiltonian for two non-interacting electrons would be encoded as

```python
coeffs = [-alpha, -alpha]
obs = [qml.PauliZ(0), qml.PauliZ(1)]
H = qml.Hamiltonian(coeffs, obs)
```

Note the offset in wire labels, e.g., $Z_1$ is entered as
``qml.PauliZ(0)``.

---

***Codercise H.5.3.*** Enter the Hamiltonian (\ref{J3}) for two
   interacting electrons using the ``Hamiltonian`` method.
