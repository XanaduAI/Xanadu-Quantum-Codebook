The probability of observing $\mathbf{0}$ appears to be $1$ when there are no solutions, and decreases until it hits zero at the halfway point. It then climbs symmetrically back up again to hit $1$ when all the combinations are solutions. The probability to observe $\mathbf{0}$ turns out to be $\vert \mathcal{A}_{\mathbf{0}} \vert^2$, where

$$
 \mathcal{A}_{\mathbf{0}} =  \frac{1}{2^n}(\vert T \vert - \vert S\vert ),
$$

for a set of solutions $S$ and non-solutions $T$. If half the combinations are solutions, $\vert S\vert = \vert T \vert  = 2^{n-1}$, then $\vert \mathcal{A}_{\mathbf{0}}\vert ^2 = 0$. We call such a function (or lock, in our analogy) *balanced*. If all or none are solutions, $\vert S\vert  = 0$ or $\vert S\vert  = 2^n$, then $\vert \mathcal{A}_{\mathbf{0}}\vert ^2 = 1$, and we call the function *constant*, since it always outputs the same bit.

Because of this nice pattern in the probability of observing $\mathbf{0}$, we can take a lock which is either constant or balanced and use our circuit to tell which it is! More formally, suppose we are given a promise that the function $f$ is either constant or balanced. From the circuit above, we can conclude that 

 1. if we measure $\mathbf{0}$, $f$ is constant (either side of the graph)
 2. if we don't measure $\mathbf{0}$, $f$ is balanced (middle of the graph). 
 
 This is called the **Deutsch-Jozsa algorithm**.

---

***Codercise A.6.2.*** Implement the Deutsch-Jozsa algorithm. Choose a constant or balanced function based on the ``promise_var`` flag, then implement the circuit from above to determine which.
