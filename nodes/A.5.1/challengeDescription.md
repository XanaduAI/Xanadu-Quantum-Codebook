By testing in pairs, we managed to halve the run time of our lock breaking algorithm. We might hope that testing more states at the same time will reduce the number of steps required even further. Testing in pairs involved applying a Hadamard, the oracle, and then another Hadamard to the last qubit:

![](pics/pair-test-circuit.svg)

We can simply generalize this strategy by doing the same thing to every qubit! Here is the circuit diagram:

![](pics/hadamard.svg)

The layer of Hadamards is called the **Hadamard transform**. Let's see what this circuit does for the case of a single solution.

---

***Codercise A.5.1.*** Implement the circuit above, consisting of a Hadamard transform, an oracle, and a Hadamard transform. The oracle is provided as ``oracle_matrix(combo)``, which you can invoke using the [``QubitUnitary()``](https://docs.pennylane.ai/en/stable/code/api/pennylane.QubitUnitary.html) function.

*Tip*. To implement the Hadamard transform, apply PennyLane's [``broadcast()``](https://docs.pennylane.ai/en/stable/code/api/pennylane.broadcast.html) function instead of a ``for`` loop. This applies a unitary multiple times according to a given pattern, and for a specified set of wires.
