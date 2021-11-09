
To solve the general case, start with the solution for the three-controlled version:

<img src="pics/4cx_solution_2.svg" width="400px">

First, we store the result of $(ab)$ on the auxiliary qubit by applying the first
Toffoli. Then, we incorporate $c$ with an additional Toffoli, which adds the result
to the target qubit. We then undo the computation on the auxiliary qubit by applying
the Toffoli again, because it is its own inverse.

We can do something similar for the case where there are four control qubits,
but we will need one additional auxiliary qubit. The process is largely the
same: first we perform a Toffoli to get the result $(ab)$ on an auxiliary qubit;
then we use that result and $c$ to obtain $(abc)$. Finally, we incorporate $d$ to
obtain $(abcd)$ on the target qubit, then we undo the first two Toffolis to
return the auxiliary qubits to $\vert 0\rangle$. 

<img src="pics/5cx_solution.svg" width="700px">

From this, it should be clear how to generalize to larger cases. For $n$ control qubits,
we need $n - 2$ auxiliary qubits, and a nice cascade of $2n - 3$ Toffoli gates.