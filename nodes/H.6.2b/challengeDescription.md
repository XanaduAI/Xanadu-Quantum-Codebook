(b) Write a circuit to apply

$$
\begin{align*}
X\otimes H + H \otimes Z & = X \otimes X + Z \otimes Z + X \otimes Z + Z
\otimes X \\ & = U_0 + U_1 + U_2 + U_3
\end{align*}
$$

to the $\vert 01\rangle$ state on the ``main`` register. You can access the auxiliary wires
as ``aux``, and the `SELECT_uniform` function from the previous exercise is available. Note that 

$$
U_0 + U_1 + U_2 + U_3 \propto H \otimes H.
$$

Are the results what you expect?
