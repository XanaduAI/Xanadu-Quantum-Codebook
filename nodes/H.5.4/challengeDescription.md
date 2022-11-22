---

To Trotterize, we can use
<a href="https://docs.pennylane.ai/en/stable/code/api/pennylane.ApproxTimeEvolution.html" target="_blank"><tt>qml.ApproxTimeEvolution</tt></a>, which simply takes a Hamiltonian, a time to evolve, and a number of steps for the Trotterization.

---

***Codercise H.5.4.*** Use the function ``ham_close_spins(B, J)`` from
   the previous exercise, along with the
   <a href="https://docs.pennylane.ai/en/stable/code/api/pennylane.ApproxTimeEvolution.html" target="_blank"><tt>qml.ApproxTimeEvolution</tt></a>
   method, to simulate evolution under couplings $\mathbf{J} = (J_X, J_Y, J_Z)$ and a
   magnetic field of strength $B$ in the $z$-direction.
