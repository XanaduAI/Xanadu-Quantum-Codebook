The oracle simply adds a phase to the solution:

$$
\vert \mathbf{s}\rangle \longrightarrow -\vert \mathbf{s}\rangle.
$$

This doesn't change the probability of observing $\vert \mathbf{s}\rangle$. But we can observe a *relative* phase change if $\vert \mathbf{s}\rangle$ is combined with a non-solution $\vert \mathbf{t}\rangle:$

$$
\vert \mathbf{t}\rangle + \vert \mathbf{s}\rangle \longrightarrow \vert \mathbf{t}\rangle -\vert \mathbf{s}\rangle.
$$

Thus, the oracle $U_f$ provides a way to test for the presence of the
solution in a superposition of computational basis states. This
suggests the following strategy. We can iterate through all $n$-bit strings in pairs $(\tilde{\mathbf{x}}0, \tilde{\mathbf{x}}1)$, labelled by an $(n-1)$-bit string $\tilde{\mathbf{x}}$, and apply the oracle $U_f$ to the superposition:

$$
    \frac{1}{\sqrt{2}} (\vert \tilde{\mathbf{x}}0\rangle +
    \vert \tilde{\mathbf{x}}1\rangle) = \vert \tilde{\mathbf{x}}\rangle \otimes \vert +\rangle.
$$

If the solution is present, there will be a relative phase change, which (up to a global phase) gives a state $\vert -\rangle$ on the last qubit:

$$
\vert \tilde{\mathbf{x}}\rangle \otimes \vert +\rangle \longrightarrow \vert \tilde{\mathbf{x}}\rangle \otimes \vert -\rangle.
$$

We can determine whether the last qubit is in the state $\vert +\rangle$ or $\vert -\rangle$ by applying the Hadamard operator $H$. Similarly, we can create the state $\vert \tilde{\mathbf{x}}\rangle\otimes \vert +\rangle$ by applying the Hadamard to $\vert \tilde{\mathbf{x}}0\rangle$. Thus, for each pair labelled by $\tilde{\mathbf{x}},$ we implement the following computation:

![](pics/pair-test-circuit.svg)

where the top line stands for $n-1$ qubits. The last qubit will be in state $\vert 1\rangle$ if the solution is present, and $\vert 0\rangle$ if it is not.

---

***Codercise A.3.1.*** Implement this circuit and return the
   probabilities on the last qubit. The function ``oracle_matrix`` is
   defined for you. You can expand the box below to see the docstring
   and implementation.

<details>
<summary class><i>Details.</i></summary>

```python
def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.
    
    Args:
        combo (list[int]): A list of bits representing a secret combination.
         
    Returns: 
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2]*len(combo)) # Index of solution
    my_array = np.identity(2**len(combo)) # Create the identity matrix
    my_array[index, index] = -1
    return my_array
```
</details>
