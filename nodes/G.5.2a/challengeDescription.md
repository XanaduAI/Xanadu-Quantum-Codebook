---

Let's attempt to empirically determine how the optimal number Grover
steps scales with the number of solutions, $M$ . For simplicity, let us consider the case where $M$ is a power of 2, i.e., $M = 2^m$. Assume that the number of steps is a power law of the form $S = C_N M^q = C_N 2^{mq}$, where all the $N$-dependence now lives in the constant $C_N$. Taking binary logs, we get

$$
\log_2 S = mq + \log_2 C_N.
$$

Thus, for a power law, $\log_2 S$ is linear in $m$, with a slope $q$ and an intercept $\log_2 C_N$. Most of the code to generate the list ``opt_steps`` of optimal Grover iterations is the same as the single solution case.

---

***Codercise G.5.2.*** (a) Below, we've provided the routine for
   regular Grover search, except for the oracle. Using the 
   oracle from the previous exercise, construct the circuit for multi-solution Grover search!
