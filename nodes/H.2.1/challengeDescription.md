In the last code challenge, you will have noticed that the quantum black box could be described by a Hadamard gate. This has the peculiar behaviour that applying it twice leads to the trivial box:

<img src="pics/repete2.svg" width="550px">

This is in sharp contrast to the random classical black box, which
applied twice gives the same random outcome, since it simply flips a
fair coin and tells you the result. Clearly, more is possible in quantum mechanics! The most general quantum black box is a **unitary** operator $U$, defined by the property that applying $U$, and then the *adjoint* $U^\dagger$, does nothing:

<img src="pics/twonitary.svg" width="550px">

The adjoint is shorthand for the complex conjugate of each matrix entry, followed by the transpose, $U^\dagger = (U^*)^T$.

---

***Codercise H.2.1.*** Write a function which checks if an array of complex numbers is unitary.

*Tip.* You will find the
[``np.identity``](https://numpy.org/doc/stable/reference/generated/numpy.identity.html),
[``np.allclose``](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html),
[``np.conjugate``](https://numpy.org/doc/stable/reference/generated/numpy.conjugate.html)
and
[``np.transpose``](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
methods useful.
