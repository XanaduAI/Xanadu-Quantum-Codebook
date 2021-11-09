---

We can use a similar approach for the diffusion operator $\hat{D}$. This operator flips the (orthogonal complement of) the uniform superposition $\vert \psi\rangle$ rather than a computational basis state, but we can work in the computational basis simply by using a Hadamard transform. The circuit for performing diffusion is then:

<img src="pics/diffusion.svg">

---

***Codercise G.3.2.*** Implement the diffusion operator in terms of the multi-controlled $X$. Note that ``query_register``, ``aux`` and ``all_wires`` refer to the wires in the query register, the auxiliary qubit, and all wires respectively. The Hadamard transform has been defined (using PennyLane's [``broadcast()``](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.broadcast.html) function) for you.
