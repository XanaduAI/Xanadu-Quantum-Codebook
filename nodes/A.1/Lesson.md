---

**Learning outcomes**
- *Explain why quantum superposition does not automatically imply exponential speedups.*
- *Write a uniform superposition over multiple qubits as a tensor
product.*

---

Classical computers run on binary digits, or bits, which can be either $0$ or $1$ but not both. Suppose we have a combination lock with bits rather than digits in its combination. As the number of bits, $n$, increases, the number of
possible combinations grows exponentially as $2^n$. If you want to break the lock by trial and error, it will take you a very long time! To give a sense of how long, let's take the world's most powerful "supercomputer", the distributed computing network [Folding@home](https://foldingathome.org/) for simulating protein folding. This can perform about $10^{16}$ floating point operations per second, about twice the processing power of the [Fugaku](https://en.wikipedia.org/wiki/Fugaku_(supercomputer)), the world's most powerful individual supercomputer. Let's assume it can check a single combination with each such operation. For a $100$-bit lock, there are $2^{100} \approx 10^{30}$ combinations, and our supercomputer will need around

$$
  \frac{2^{100}}{10^{16}} \text{ s} \approx 4 \text{ million years}
$$

to break it by brute force. This is a long time by human standards!

![](pics/lock.svg)

Quantum computers use qubits, which are like regular bits except that they can be in a superposition of quantum states $\vert 0\rangle$ and $\vert 1\rangle$:

$$
  \vert \psi\rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle.
$$

This suggests the following scheme for breaking the $n$-bit lock with
a quantum computer: take $n$ qubits and put each into an even superposition,

$$
  \vert +\rangle = \frac{1}{\sqrt{2}} (\vert 0\rangle + \vert 1\rangle).
$$

The total state of the system will be an even superposition over every $n$-bit string $\mathbf{x} \in \{0, 1\}^n$:

$$
\begin{align*}
  \vert \psi\rangle & = \vert +\rangle \otimes \vert +\rangle \otimes \cdots\otimes
  \vert +\rangle \\
  & = \vert +\rangle^{\otimes n} \\
  & = \frac{1}{\sqrt{2^n}} \sum_{\mathbf{x} \in \{0, 1\}^n}
  \vert \mathbf{x}\rangle,\label{eq:had0} \tag{1}
\end{align*}
$$

where $\otimes$ indicates the tensor product. Note that when we take tensor products of basis states, we will usually omit the tensor product symbol, so for instance $\vert 0\rangle \otimes \vert 1\rangle = \vert 01\rangle$.
If we could somehow test this state on our lock, then we will test the correct answer at the same time as everything else, and open the lock on the first go! It appears that we have turned an exponentially hard classical task into something we can perform in a single shot on a quantum computer.

---

***Exercise A.1.1.*** Prove Eq. (\ref{eq:had0}) by showing that the
   tensor product $\vert +\cdots + \rangle$ does indeed give the
   uniform superposition.

<details>
  <summary><i>Hint.</i></summary>
Consider expanding a product of polynomials in ordinary
algebra.
</details>

<details>
  <summary><i>Solution.</i></summary>

It's a bit like ordinary algebra, where expanding a product

$$
(a + b)(x + y) = ax + ay + bx + by
$$

gives us all products of terms in the first factor with terms in the second. Similarly,

$$
(\vert 0\rangle + \vert 1\rangle)\otimes (\vert 0\rangle + \vert 1\rangle) = \vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle
$$

gives us all tensor products of things in the first factor with things in the second. We can extend this to additional factors:

$$
\begin{align*}
(\vert 0\rangle + \vert 1\rangle) \otimes(\vert 0\rangle + \vert 1\rangle)\otimes(\vert 0\rangle + \vert 1\rangle) & = (\vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle)\otimes(\vert 0\rangle + \vert 1\rangle) \\
& = \vert 000\rangle + \vert 001\rangle + \vert 010\rangle + \vert 011\rangle + \vert 100\rangle + \vert 101\rangle + \vert 110\rangle + \vert 111\rangle.
\end{align*}
$$

We can continue on in this way for $n$ factors, and generate an even superposition of all $n$-bit strings, labelled by $\mathbf{x} \in \{0, 1\}^n$. The factors of $1/\sqrt{2}$ come along for the ride. Thus,

$$
\frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) \otimes \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) \otimes \cdots \otimes \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) = \frac{1}{\sqrt{2^n}} \sum_{\mathbf{x} \in \{0, 1\}^n}
  \vert \mathbf{x}\rangle.
$$

as required. ▢
</details>

---

A uniform superposition will include the solution string
$\vert \mathbf{s}\rangle$. But by itself, this doesn't help us break
the lock, since the superposition includes everything else as well!
Once we open the quantum computer and look inside, we may observe the correct
lock combination, but we might also see an incorrect combination, due to the
probabilistic nature of quantum computation. Let's draw a cartoon of the case for the single-bit lock:

![](pics/peril.svg)

We still only have a $50\%$ chance of landing on the correct answer
when the computation finishes. More generally, if we start in the even
superposition Eq. (\ref{eq:had0}) for $n$ bits, our chance of observing
the correct answer is $1/2^n$. These are the same odds as a random
*classical* guess! So, we see the basic dilemma (or rather,
di${}^n$lemma). A quantum superposition may look like it can result in
an exponential number of things being done at once, but once we take a
measurement, we will only get a random snapshot of what it's done.

Quantum algorithms are all about shuffling around this exponential collection of terms in the superposition so that, when we observe the system, our random snapshot has a high probability of showing us the thing we are looking for. And given that our algorithms involve randomness, we also should be comparing them to *random classical algorithms*, like guessing the combination.
