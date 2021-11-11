Recall that a single Grover step consists in applying the oracle and
then the diffusion operator:

```python
grover_op_matrix = np.dot(diffusion_matrix(), oracle_matrix(combo))
```
<br>

We would like to choose the number of Grover steps which, applied to
the uniform superposition $\vert \psi\rangle$, maximizes the amplitude
of the solution state $\vert\mathbf{s}\rangle$.
To help us figure this out, we can reason about Grover search in a two-dimensional
geometry spanned by the uniform superposition $\vert \psi\rangle$ and
our target state $\vert \mathbf{s}\rangle$, i.e., with states of the
form

$$
\alpha \vert \psi\rangle  + \beta \vert\mathbf{s}\rangle.
$$

In this geometry, orthogonal vectors $\vert u\rangle$ and $\vert
v\rangle$, i.e., with zero overlap $\langle u \vert v \rangle = 0$,
are at right angles:

<img src="pics/grover-space.svg"  width="250px">

We plot $\vert \mathbf{s}\rangle$ on the vertical axis and the uniform superposition
$\vert \psi\rangle$ to the right.
Since $\vert\psi\rangle$ is not orthogonal to $\vert
\mathbf{s}\rangle,$ but has overlap $1/\sqrt{2^n}$, the uniform
superposition will not quite lie on the horizontal axis.
Let's run our Grover operator multiple times and see its effect in
this new geometry!

---

***Codercise G.2.1.*** Create a circuit which runs $G = DU_f$ some
specified number of times, and manually set the step number
``my_steps``.
The results in the two-dimensional geometry will be displayed for
``combo = [0, 0, 0, 0, 0]``.
The oracle and diffusion matrices are
defined below, and available by calling ``oracle_matrix(combo)`` and ``diffusion_matrix()``.
From the plots, confirm that applying the Grover operator
*rotates* the state vector, and determine the optimal number of
Grover steps for $n = 5$.
