We've focused so far on locks with a single solution $\mathbf{s}$, and in this case, testing in pairs is guaranteed to detect the solution when it is present. But what happens if there are multiple solutions, or our function is a more general one with multiple output bits? Can we still use a quantum computer to find the solution? This seems like it would be problematic, because if we superpose a pair of solutions, the oracle once more produces an undetectable phase:

$$
\begin{align*}
    \vert \mathbf{s}_1 \rangle + \vert \mathbf{s}_2 \rangle \overset{U}{\longrightarrow} -(\vert \mathbf{s}_1 \rangle + \vert \mathbf{s}_2\rangle).
\end{align*}
$$

But not all hope is lost! If there are an *odd* number of solutions, then even if we miss a number of pairs of solutions, there is guaranteed to be one left over. This guarantee about the number of solutions is called a **promise**, and like promises in real life, it helps us make decisions about how to design our algorithms.

On the other hand, if we don't know the number of solutions, then we can test in pairs and tally up the number of times we detect one. This tally will have the same parity (i.e., odd or even) as the total number of solutions, since we can only miss solutions in pairs of two. Thus, we can learn a *global property* about the function that we didn't know beforehand! We use the same circuit as before:

![](pics/pair-test-circuit.svg)

---

***Codercise A.4.1.*** Implement the circuit above, but now for ``how_many`` solutions instead of one. You will first need to implement the multi-solution version of the oracle matrix, ``multisol_oracle_matrix(combos)``, which takes a list of bit strings (representing different solutions) and returns the associated oracle in matrix form.
