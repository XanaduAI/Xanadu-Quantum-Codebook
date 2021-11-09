---

**Learning outcomes**

- *Explain how global information and promises are useful for algorithm design.*

---

Our little speedup in the previous node depended on a special fact about the function $f$ encoding the lock: there was only one secret combination $\mathbf{s}$.
But if we test a pair of combinations $|\tilde{\mathbf{x}}0\rangle, |\tilde{\mathbf{x}}1\rangle$ which both open the lock, we generate an undetectable phase once more:

$$
\begin{align*}
    \vert \tilde{\mathbf{x}}\rangle\otimes \frac{1}{\sqrt{2}}\left(\vert 0\rangle+\vert 1\rangle\right) & \mapsto
  \vert \tilde{\mathbf{x}}\rangle\otimes \frac{1}{\sqrt{2}}\big((-1)\vert 0\rangle+(-1)\vert 1\rangle\big) \\ & = -\vert \tilde{\mathbf{x}}\rangle\otimes \frac{1}{\sqrt{2}}\left(\vert 0\rangle+\vert 1\rangle\right).
\end{align*}
$$

Is our algorithm now useless? To open the lock, we just need a single solution. Our strategy of testing in pairs is still guaranteed to work (eventually), provided there are an *odd* number of solutions. Even if we miss the solutions that come in pairs, there will always be one left over! But on the other hand, if the number of solutions is even, we might get unlucky, with solutions pairing up into a bunch of unobservable phases.

![](pics/odd.svg)

There are two ways to view this algorithmic quirk. First, if we are told in advance that our lock has an odd
number of solutions, we can test in pairs, confident we will eventually encounter a solution. But if we don't know the **parity** of the number (i.e., whether it is odd or even), we can test in pairs and discover it! Each time we observe a phase change, we know we have encountered a single solution, and otherwise, we have encountered either two or zero solutions, which are equal modulo $2$.
So we simply test in pairs and count the number of phase changes we were able to observe. The parity of the solution set is the parity of this count. Once again, this is twice as fast as the classical algorithm, which must separately test each combination. This gives a circuit for determining the parity:

![](pics/flowchart2.svg)

Our pair-testing algorithm suggests that quantum computers might be good at determining *global information* about a function, like the parity of the solution set. Although we can't produce the observation we want from the exponentially many possibilities, we might be able to gather global information from *all* the different branches and combine them in an observable way. The pair-testing algorithm also tells us that, conversely, global assumptions about the function (e.g., that the number of solutions is odd) can lead to very different performance guarantees for our algorithms. These global assumptions about $f$ are called **promises**, and play an important role in quantum algorithms.
