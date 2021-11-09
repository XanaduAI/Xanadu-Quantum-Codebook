---

***Codercise I.11.4.*** Implement the following circuit twice. For one version,
   measure the observables $Z$ on the first qubit (i.e., $Z\otimes I$), and $Z$
   on the second qubit ($I \otimes Z$). For the other version, measure the
   observable $Z \otimes Z$. How do think the results of the first circuit will
   relate to those of the second? Plot the results as a function of $\theta$ to
   test your hypothesis.

<img src="pics/circuit_i-11-4.svg" width="400px">

*Tip*. In PennyLane, you don't need to specify the identity portion of
 observables. For example, $I \otimes Z$ is simply `qml.PauliZ(1)` rather than
 `qml.Identity(0) @ qml.PauliZ(1)`.


<details>
  <summary><i>Hint.</i></summary>

Consider how the observables themselves are related. If you have $Z \otimes I$ and $I \otimes Z$,
can you produce $Z \otimes Z$?

</details>