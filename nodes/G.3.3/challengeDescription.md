---

Finally, we can assemble these into an honest-to-goodness circuit which initializes the state and applies the Grover operator once:

<img src="pics/grover-iter-2.svg">

You will see in the exercise below that this circuit increases the
amplitude for the solution, as we expect.
But the next question is: can we do even better?

---

***Codercise G.3.3.*** In the code below, create a circuit which
   prepares the uniform superposition in the query register, places
   the auxiliary qubit in the $\vert -\rangle$ state, and applies a
   single Grover iteration using ``MultiControlledX``. We will plot
   the output for ``combo = [0, 0, 0, 0, 0]``. Note that the
   subcircuits ``oracle(combo)``, ``hadamard_transform(my_wires)`` and
   ``diffusion()`` are provided for you and do not need to be reimplemented.
