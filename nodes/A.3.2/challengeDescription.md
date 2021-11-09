---

With this circuit at our disposal, we can crack the lock by simply iterating over the labels $\tilde{\mathbf{x}}$ until we detect the solution. Let's see how long this takes on average.

---

***Codercise A.3.2.*** Complete the function below to see how many attempts it takes to break the lock using our quantum circuit. You should find an improvement over the brute force approach, which takes around $9$ guesses (on average) for $4$ qubits. Note that ``pair_circuit`` is available.

*Tip.* Use [``np.isclose(a, b)``](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html) to test the probabilities coming from ``pair_circuit(x_tilde, combo)``.
