Now that we know how to apply the Grover operator, we'd like to know how many iterations are optimal. By "optimal", we mean a *local peak* in the probability of observing the correct answer. For instance, in the list

$$
[0, 5, 1, 2, 2, 3],
$$

the local peak is $5$, since it is larger than its neighbours $0$ to the left and $1$ to the right. We would like to know the position of the first local peak as we iterate the Grover operator, since too many steps will rotate us *past* the solution and away from it:

<img src="pics/rotate2.gif">

In fact, the probability of observing the solution varies sinusoidally. Given an $n$-bit combo, we are searching through a space of $N = 2^n$ possibilities. Let us assume that the optimal number of steps $S$ required is proportional to a *power* of $N$:

$$
S = C N^p = C 2^{np}.
$$

For different system sizes $n$, we can run the algorithm and find the smallest number of steps $S$ that maximize our chances of finding the solution. To make a guess at $p,$ the easiest thing to do is take the binary logarithm of the power law relationship:

$$
\log_2 S = np + \log_2 C.
$$

Thus, if $S$ is indeed proportional to a power $p$ of $N$, $\log_2 S$ should be a straight line of slope $p$ and intercept $\log_2 C,$ as a function of $n.$ To generate the needed data, we will loop over different system sizes and build a circuit for each.

---

***Codercise G.4.1.*** (a) Complete the function below, which implements Grover search for a given secret combination and number of Grover steps. The oracle, Hadamard transform and diffusion operator are provided as ``oracle(combo)``, ``hadamard_transform(my_wires)``, and ``diffusion(n_bits)``.

*Note.* The inner circuit is required since we are going to be changing the number of qubits, which is implicitly specified by the length of the secret combination.
