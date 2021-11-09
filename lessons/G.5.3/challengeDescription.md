---

Once again, we can work out how the optimal number of solutions scales
with $M$. As you've just shown, for $n = 5$ and $M \in \{2^0, 2^1,
2^2\}$, the optimal number of Grover steps is

$$
S \in \{4, 3, 2\}.
$$

Again, you can fiddle with the line of best fit for $\log_2 S$ below. The gradient is $-0.5$, suggesting that the optimal number of steps scales as $M^{-1/2} = 1/\sqrt{M}$. The intercept $\log_2 C_N \approx 2.03$ is consistent with the scaling $S \approx \tfrac{\pi}{4}\sqrt{N}$ for a single solution, since

$$
\log_2 \left(\frac{\pi}{4} \sqrt{N}\right) = \log_2 \left(\frac{\pi}{4} \sqrt{2^5}\right) \approx 2.15.
$$

We therefore guess that for $M$ solutions, the optimal number of steps scales as

$$
S \approx \frac{\pi}{4}\sqrt{\frac{N}{M}}.
$$

This is indeed the scaling for Grover search with multiple solutions!
