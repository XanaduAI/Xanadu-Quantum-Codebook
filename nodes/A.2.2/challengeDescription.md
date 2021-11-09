---

Let's add the oracle to our circuit and see if we fare better than just creating the uniform superposition. Here is the circuit we want to implement:

![](pics/uniform-oracle.svg)

---

***Codercise A.2.2.*** Write a circuit which applies the oracle to the uniform superposition.
The oracle matrix function from the previous exercise is available for you as `oracle_mat`. 
The supplied code will plot the resulting probability distribution. Has applying the oracle helped us break the lock?

*Tip.* Use PennyLane's [``QubitUnitary()``](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.QubitUnitary.html) operation.
