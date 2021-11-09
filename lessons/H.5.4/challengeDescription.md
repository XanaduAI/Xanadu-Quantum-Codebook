---

To Trotterize, we can use
<a href="https://pennylane.readthedocs.io/en/stable/code/api/pennylane.templates.subroutines.ApproxTimeEvolution.html" target=_"blank"><tt>templates.subroutines.ApproxTimeEvolution</tt></a>, which simply takes a Hamiltonian, a time to evolve, and a number of steps for the Trotterization.

---

***Codercise H.5.4.*** Use the
   <a href="https://pennylane.readthedocs.io/en/stable/code/api/pennylane.Hamiltonian.html" target="_blank"><tt>Hamiltonian</tt></a>
   and
   <a href="https://pennylane.readthedocs.io/en/stable/code/api/pennylane.templates.subroutines.ApproxTimeEvolution.html" target="_blank"><tt>ApproxTimeEvolution</tt></a>
   methods to simulate evolution under couplings $J_X, J_Y, J_Z$ and a
   magnetic field of strength $B$ in the $z$-direction.
