(b) For $n = 5$ and $M \in \{2^0, 2^1, 2^2\}$, determine the optimal number of steps for Grover search. Once again, the optimal number of steps does not depend on the strings themselves, so we will simply choose the first $m$ binary strings. The function ``local_max_arg(num_list)`` once again picks out the location of the first maximum if it exists. The function ``grover_iter_multi(combos, num_steps)`` is available from the previous exercise.

<details>
<summary><i>Hint.</i></summary>

The probability of observing a solution in $S$ is the sum of probabilities of observing any solution $\mathbf{s} \in S$.

</details>
