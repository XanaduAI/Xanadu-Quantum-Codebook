(c) Finally, consider the combination of unitaries

$$
\begin{align*}
\tilde{U} & = \sum_j \alpha_j U_j \\
& = X \otimes X + \frac{1}{2}Z \otimes Z + \frac{1}{2} X \otimes Z + Z \otimes X \\
& = H \otimes
\begin{bmatrix}
1/2 & 1 \\
1 & -1/2
\end{bmatrix}.
\end{align*}
$$

Create a circuit which applies this to $\vert 11\rangle$. Note that

$$
\begin{align*}
H \otimes
\begin{bmatrix}
1/2 & 1 \\
1 & -1/2
\end{bmatrix} \vert 11\rangle & \propto \vert 00\rangle - \frac{1}{2}\vert 01\rangle - \vert 10\rangle + \frac{1}{2} \vert 11\rangle,
\end{align*}
$$

so the unnormalized amplitudes should be proportional to this.
