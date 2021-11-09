---

***Codercise I.11.2.*** Use PennyLane to create the state $|+1\rangle =
   |+\rangle \otimes |1\rangle$. Then, return two measurements:

 - the expectation value of $Y$ on the first qubit 
 - the expectation value of $Z$ on the second qubit
 
In PennyLane, you can return measurements of multiple observables as a tuple, as
long as they don't share wires.