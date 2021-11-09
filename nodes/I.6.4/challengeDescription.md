Completing the previous exercise shows that $RY$ is quite similar to $RX$ and
allows us to adjust the relative sizes of the amplitudes, but without the
complex portion. You can infer part of its matrix representation from the plot in the
previous exercise; the full matrix is

$$
RY(\theta) = \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & - \sin \left(\frac{\theta}{2} \right) \\ \sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)   \end{pmatrix},
$$

and its action on the basis states is

$$
\begin{align*}
RY(\theta) \vert 0\rangle &= \cos(\theta/2) \vert 0\rangle - \sin(\theta/2) \vert 1\rangle,\\
RY(\theta) \vert 1\rangle &= \sin(\theta/2) \vert 0\rangle + \cos(\theta/2) \vert 1\rangle.
\end{align*}
$$

Finally, just like $RX$ and $RZ$, there is a special name for the case where
$\theta =\pi$: the $Y$ gate (or Pauli $Y$), which is implemented in PennyLane as
[`qml.PauliY`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.PauliY.html).
