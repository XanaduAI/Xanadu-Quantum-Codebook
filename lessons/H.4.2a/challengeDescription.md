---

If finding all the eigenvalues is too hard, we might hope to identify a *single* eigenvalue, such as the lowest energy level $E_\Omega$ and the corresponding **ground state** $\vert \Omega\rangle$. To see how this can be useful for solving computational problems, suppose we want to determine if a graph $G$ is **bipartite**, i.e., whether its nodes can be coloured red and blue so that edges always connect distinct colours. We give an example of a bipartite and a non-bipartite graph below:

<img src="pics/bipartite.svg" width="400px">

Physically speaking, this setup naturally arises if we have a lattice of electrons which interact only with each other and not with a background magnetic field.
Sometimes, the interaction means they want to *anti-align*, i.e., the energy will be lowered when adjacent electrons have spins in opposite directions.
Thus, the graph problem is a natural generalization of a single tiny bar magnet!

In general, for any graph $G$, we can associate a qubit to each node, a colour to a qubit state, an interaction to each edge, and put together a Hamiltonian whose ground state tells us if the graph is bipartite. For instance, let's use the graph on the left with qubit labels as follows:

<img src="pics/test-graph.svg" width="200px">

The Hamiltonian for the bipartiteness problem is:

$$
\hat{H} = Z_1 Z_2 + Z_2Z_3 + Z_2 Z_4 + Z_4Z_5.
$$

---

***Codercise H.4.2a.*** Complete the following code to measure the Hamiltonian above in a given basis state. It uses <a
 href="https://pennylane.readthedocs.io/en/latest/code/api/pennylane.ExpvalCost.html"
 target=_"blank"><tt>qml.ExpvalCost</tt></a> to evaluate the Hamiltonian, so you may want to look at the documentation to see how it works!
