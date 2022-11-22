When our unitary is $e^{i\alpha t Z}$, and it acts on an eigenvector
$\vert 0\rangle$ or $\vert 1\rangle$ of $Z$, then we simply pick up a
phase, replacing $Z$ with the corresponding eigenvalue. For instance,

$$
e^{i\alpha t Z} \vert 0\rangle = e^{i\alpha t} \vert 0\rangle.
$$

To generalize this observation, suppose we know the eigenvalues
$\lambda_i$ and eigenvectors $\vert \lambda_i\rangle$ of an operator
$\Lambda$, with $i = 1, 2, \ldots, N$.
Then, in the basis of eigenvectors, $\Lambda = \mbox{diag}(\lambda_1,
\lambda_2, \ldots, \lambda_N)$ is simply a diagonal
matrix with eigenvalues along the diagonal, and the exponential is
also diagonal:

$$
\begin{align*}
e^{\alpha\Lambda} & = \begin{bmatrix}
e^{\alpha\lambda_1} & & & \\
 &e^{\alpha\lambda_2} & & \\
 & & \ddots & \\
  & & & e^{\alpha \lambda_N}
\end{bmatrix}.
\end{align*}
$$

Thus, if we know the eigenvalues or **energy levels** $E_i$, and
**energy eigenstates** $\vert E_i\rangle$ of a Hamiltonian $\hat{H}$,
we can easily exponentiate it:

$$
\begin{align*}
e^{-it\hat{H}/\hbar} & = \begin{bmatrix}
e^{-itE_1/\hbar} & & & \\
 &e^{-itE_2/\hbar} & & \\
 & & \ddots & \\
  & & & e^{-itE_N/\hbar}
\end{bmatrix}.
\end{align*}
$$

There are two reasons diagonalization is not the magical hack it first
appears to be. First, $\hat{H}$ is an $N \times N$ matrix, where $N = 2^n$
for $n$ qubits. This is exponential in the number of qubits, and
finding its eigenvalues takes an exponentially long time. But even
when we know the diagonal form of the Hamiltonian, implementing the
evolution in a quantum circuit can take ingenuity. For instance,
consider a simple Hamiltonian coupling two qubits:

$$
\hat{H} = \alpha Z \otimes Z.
$$

The eigenvectors are just the computational basis states $\vert xy\rangle$, with eigenvalues $\alpha(-1)^{x+y}$. To implement the unitary $U(t)$ which evolves by time $t$, we need to build a gate with the following action on basis states:

$$
U(t) \vert xy \rangle = \exp\left[-\frac{i\alpha t}{\hbar} (-1)^{x+y}\right] \vert xy \rangle.
$$

As you will check in a moment, this can be done using the following (non-trivial) circuit involving CNOTs and a $Z$ rotation:

<img src="pics/diag-zz-2.svg" width="350px">

where $\theta = 2\alpha t/\hbar$.

---

***Codercise H.4.1.*** Implement the circuit drawn above, allowing for the specification of an initial computational basis state.

*Tip.* Try using 
<a href="https://docs.pennylane.ai/en/stable/code/api/pennylane.BasisState.html" target="_blank"><tt>qml.BasisState</tt></a> 
to prepare the basis state.
