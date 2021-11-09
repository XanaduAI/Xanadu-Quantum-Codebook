With our answers stored in ``opt_steps``, we can plot them on a
logarithmic scale and look for a trend. In fact, we will add another
data point for $n = 7$, with the optimal number of Grover steps for $n
\in \{3,4,5,6, 7\}$ given by

$$
S \in \{2, 3, 4, 6, 8\}.
$$

You can plot a line of best fit for $\log_2 S$ below. The data points have a slope $p \approx 0.5$ or $S \propto N^{0.5} = \sqrt{N}$, suggesting that instead of scaling linearly with the number of items to search through, quantum computers can search through lists in a time which scales as the *square root* $\sqrt{N}$. The intercept for our data, plotted logarithmically, is $-0.47 = \log_2 C$ or $C \approx 0.72$. Thus, our empirical estimate for the optimal number of steps is

$$
S \approx 0.72 \sqrt{N}.
$$

With even more data, this will converge to $C = \pi/4 \approx 0.79$, so

$$
S \approx \frac{\pi}{4} \sqrt{N}.
$$

You can prove this scaling mathematically.
Since the best classical algorithm is *linear*
in $N$, Grover search yields a *quadratic* improvement. While not an exponential improvement, this is still sizable.

