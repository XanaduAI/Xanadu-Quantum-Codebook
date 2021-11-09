This state is proportional to $\vert +\rangle \otimes \vert-\rangle = (H \otimes H)\vert 01\rangle$, as we expect.

---

So far, we have only dealt with equally weighted unitaries. To perform an unequally weighted linear combination,

$$
\tilde{U} = \kappa U + V,
$$

we require the slightly more involved circuit:

<img src="pics/vk-circuit.svg" width="400px">

where we have replaced the Hadamard gate with a more complicated gate

$$
V_\kappa =
\frac{1}{\sqrt{\kappa+1}}\begin{bmatrix}
\sqrt{\kappa} & -1 \\
1 & \sqrt{\kappa}
\end{bmatrix}.
$$

Once again, we apply the weighted sum if we observe $0$ on the
auxiliary qubit. It turns out that this two-unitary circuit is all you need to implement a general linear combination of unitaries, since you can iteratively *nest* this circuit to perform a weighted sum of multiple unitaries. We can finally revisit our original goal of approximating a Taylor series. The case for exponentiating a Hamiltonian which is itself a linear combination of unitaries is very similiar, just more complicated, so we'll just focus on $e^{tU}$.

---

***Codercise H.6.3.*** Consider the matrix exponential of a unitary operator $U$:

$$
e^{tU} = I + tU + \frac{1}{2}t^2 U^2 + \cdots.
$$

(a) Code up the circuit to non-deterministically implement the first-order approximation to this Taylor series,

$$
I + tU = U^0 + tU^1.
$$

This is given by the circuit:

<img src="pics/lcu-nest1.svg" width="400px">

The auxiliary qubit is on wire ``aux = 0`` and
   the main qubit on ``main = 1``.  As with ``add_two_unitaries``, don't initialize the state just
yet.

*Tip.* The controlled identity is simply the identity, which can be
 omitted from the circuit. Since $V_t$ is a real matrix, you can take
 its adjoint using
 [``np.tranpose``](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html).
