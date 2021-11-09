---

**Learning objectives**

- *Implement the Deutsch-Jozsa algorithm.*
- *Compare the algorithmic performance of Deutsch-Jozsa to deterministic and classically random strategies.*

---

As discussed in the last section, our Hadamard-oracle circuit doesn't tell us the lock combination. But the amplitude for observing $\mathbf{0}$ has a particularly simple form:

$$
   \mathcal{A}_{\mathbf{0}} = \langle \mathbf{0}\vert H^{\otimes n}
   U_f \vert \psi\rangle = \frac{1}{2^n}\sum_{\mathbf{x}\in\{0,1\}^n}
   (-1)^{f(\mathbf{x})}.
$$

Let's return to the scenario where our lock has multiple secret combinations, with a set of solution strings $S$ and non-solution strings $T$. Each solution $\mathbf{s} \in S$ contributes $-1$ in the sum, and each non-solution $\mathbf{t} \in T$ contributes $+1$, so that

$$
  \mathcal{A}_{\mathbf{0}} = \frac{1}{2^n} (\vert T\vert  - \vert S\vert ). \tag{1} \label{amp}
$$

Deutsch and Jozsa noticed something very clever. Call the situation where $\vert S\vert  = \vert T\vert $ "balanced", i.e., there are just as many solutions as non-solutions. Then the amplitude (\ref{amp}) vanishes, and you will never observe
$\mathbf{0}$! But if $f$ is "constant", with $S = \varnothing$ or $T = \varnothing$, then
$\mathcal{A}_{\mathbf{0}} = \pm 1$ and you will always observe $\mathbf{0}$! This leads to the **Deutsch-Jozsa algorithm**. If we are given the promise that $f$ is either balanced or constant, then applying the same set of gates and observing will tell us which it is. It just depends on whether we see $\mathbf{0}$ or not! The circuit is the same as the last node:

![](pics/dj-circuit-2.svg)

where we now make a decision based on the measurement outcomes, like the test-in-pairs algorithm.

We'll end by seeing how the Deutsch-Jozsa algorithm compares to classical algorithms in terms of the number of "basic steps" required. We can count these steps in different ways. We could compare calls to the function $f$, which are either classical evaluations such as $f(\mathbf{x})$, or oracle calls $U_f$ on a quantum computer. We could also choose to count the number of gates in the quantum circuit, but a slightly better analogue to the "time" required is the minimum circuit depth, i.e., the smallest number of layers of gates in the circuit, since each layer is like a time step.

Note that we can make a distinction between two types of classical algorithms: *deterministic*, where given fixed inputs, the (classical) computer always produces the same output, and *probabilistic*, where the computer can choose outputs randomly. You'll find that Deutsch-Jozsa takes fewer steps than the best deterministic classical algorithm, but more than the probabilistic one!

---

***Exercise A.6.1.*** Let's compare the Deutsch-Jozsa algorithm to deterministic and probabilistic classical algorithms, and see how they do.

(a) What is the total number of layers needed for the Deutsch-Jozsa algorithm on $n$ qubits? How many oracle calls?

(b) To determine *with certainty* whether $f$ is constant or balanced on a classical computer, how many function calls do we need? Compare this to the answer in (a).

(c) Finally, consider a *probabilistic* classical algorithm, which simply tests $k$ random elements $\mathbf{x}_i \in \{0, 1\}^n$, and guesses the function is constant if all $f(\mathbf{x}_i)$ are the same. Assuming $2^n \gg k$ (or equivalently, sampling with replacement) argue that for a given probability of error $\epsilon$, the algorithm runs in a constant number of steps. So Deutsch-Jozsa is comparable to a random classical algorithm, with both running in "constant time".

<details>
<summary><i>Solution.</i></summary>

(a) We need to create a uniform superposition, using a Hadamard transformation, which is a single layer. We then make a single oracle call. Finally, we apply another layer of Hadamards. Thus, the circuit for the Deutsch-Jozsa algorithm has depth $3$ and makes a single oracle call.

(b) On a classical computer, we need to test the function on over half of the bit strings $\{0, 1\}^n$ before we can conclude *with certainty* that it is constant or balanced. This requires $2^{n-1} + 1$ function calls, which is exponentially worse than Deutsch-Jozsa!

(c) If the function is balanced, the probability of selecting a solution is $1/2$, and similarly for a non-solution. Thus, the probability of selecting $k$ of the same type (with replacement, or when $2^n \gg k$) is $1/2^k$. Since there are two types we can choose, the probability of randomly selecting $k$ instances of the same type is $1/2^{k-1}$. This is our probability of error, since in this case our algorithm incorrectly concludes that the function is constant. Thus, for an allowable error $\epsilon$, the number of random calls needed is

$$
\epsilon = \frac{1}{2^{k-1}} \quad \Longrightarrow \quad k = 1 - \log_2 \epsilon.
$$

This has no dependence on $n$, so the random algorithm runs in a constant number of steps for a fixed error probability. Deutsch-Jozsa is mild improvement, in the sense that it requires only a single oracle call, and gives the correct answer with probability $1$. ▢

</details>

---
