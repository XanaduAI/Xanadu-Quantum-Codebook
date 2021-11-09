---

**Learning outcomes**

- *Understand the distinction between the behaviour of deterministic, random, and quantum systems*

---

What makes quantum computing fundamentally different from classical computing?
In a word, the physics going on inside the computer.
To help understand this, it's useful to abstract from specific computational models, and instead think about physical systems in general as black boxes where initial conditions go in, we wait for some time, and then observe. In between, physics happens. The job of a physicist is to work out the laws of Nature which govern the "in between", also called the *time evolution* or *dynamics* of the system.

<img src="pics/nature.svg" width="700px">

Often, even knowing the laws of physics does not allow us to predict what the black box will do to some input, at least with pen and paper. The math is just too hard. An example is the three-body problem. If three planets interact gravitationally, they perform a do-si-do so complex that there is no explicit mathematical formula for it! In this case, we can do something more radical than math. We can use our knowledge of the laws of physics to make our own black box, one that imitates or *simulates* the black box of Nature. We call these human-made black boxes *computers*.

<img src="pics/computer.svg" width="450px">

Most physical laws are continuous, in the sense that they act on systems that cannot be split into a finite set of components. In contrast, most computers (though not all, e.g., a slide rule) are *discrete*, acting only on a finite number of components. So to turn continuous laws into discrete computations, we need to *approximate*. The better we want our approximation to be, the more computing power we will need, measured either in computing steps or memory allocation. Computing power therefore turns out to be a major limiting factor in how well we can understand the complicated physical systems around us.

Let's talk about some broad classes of black boxes. The first is **classical deterministic systems**, where a given input always produces the same output. "Classical" here refers to "classical physics", the set of Natural laws governing the macroscopic world and with which we are most familiar. Most of classical physics, from mechanics to electromagnetism to gravity, takes the form a classical deterministic box.

<img src="pics/deterministic.svg" width="450px">

Our model problem will involve coins, though really, this is just a colorful way to talk about binary digits. So, let's consider a system of $n$ coins lying on a table. Each coin can be in one of two states: heads ($0$) or tails ($1$). We will describe the state of the system by a vector of $n$ bits, $\mathbf{x} = (x_1, x_2, \ldots, x_n) \in \{0, 1\}^n.$

---

***Exercise H.1.1.*** (a) How many variables do we need to describe the state of the $n$-coin system before it passes through the box? How many different configurations does this system have?

(b) How many different rules are there for deterministically evolving the $n$-coin system into a new configuration of $n$ coins?

<details>
<summary><i>Solution.</i></summary>

(a) The classical value of the coin $j$, $x_j \in \{0, 1\}$, is a variable, so there are $n$ variables altogether. Since each variable can have $2$ values, the total number of configurations is $2 \times 2 \cdots \times 2 = 2^n$.

(b) For classical deterministic systems, there are $2^n$ possible inputs $\mathbf{x}$. Each of these may be associated with any other configuration $\mathbf{y} \in \{0, 1\}^n$. That leads to $2^n \times 2^n \times \cdots \times 2^n = (2^n)^{2^n}$ different deterministic black boxes. ▢

</details>

---

A second, more general class is **classical random systems**. Here, an input sometimes results in one output, sometimes in another, with the output varying randomly. One way this randomness can arise is from dynamics which are in fact determistic, but where we ignore (or don't have access to) certain details of the system. The most famous example is *statistical mechanics*, the mathematical formalism underlying thermodynamics. It turns out that it is not just impossible, but useless and unnecessary, to keep track of the precise deterministic evolution of each of the $\sim 10^{26}$ particles in a handful of dust. It is much better to talk about the statistical tendencies of this handful!

<img src="pics/random.svg" width="450px">

Suppose that we are now allowed to *flip* our $n$ coins, and introduce random outcomes. In particular, we'll assume that black boxes can be described by conditional probabilities,

$$
p(\mathbf{y}\vert \mathbf{x}) = \text{probability of observing } \mathbf{y} \text{ given input } \mathbf{x}.
$$

Let's explore how this differs from the class of deterministic systems!

---

***Exercise H.1.2.*** (a) How many variables are needed to describe the current state of the system?

(b) Since probabilities are continuous, there are now an infinite number of black boxes. Show that $2^{2n} - 2^n$ independent probabilities are required to specify a black box.

<details>
<summary><i>Solution.</i></summary>

(a) We still only need to specify the value $x_j$ of each coin, so $n$ variables remain sufficient.

(b) It seems at first as if each $p(\mathbf{y}\vert \mathbf{x})$ is independent, which would give a total of $(2^{n})^2 = 2^{2n}$ parameters. But for a given $\mathbf{x}$, $p(\mathbf{y}\vert \mathbf{x})$ must be a probability distribution over $\mathbf{y}$, so the $p(\mathbf{y}\vert \mathbf{x})$ must add up to $1$. This gives us a set of $2^n$ constraints (one for each configuration $\mathbf{x}$) so the total number is

$$
2^{2n} - 2^n
$$

as claimed. ▢

</details>

---

The class of **quantum systems** is of most interest to us. Like random classical systems, in a quantum system, different inputs can lead to different, random observations. But these outcomes have some curious features that cannot be explained by classical randomness.

<img src="pics/quantum.svg" width="450px">

Let's imagine that our set of $n$ coins are now quantum, i.e., we now have $n$ qubits described by a state $\vert \psi\rangle$. There is an important difference in simulating the state of the classical and quantum system.

---

***Exercise H.1.3.*** How many classical deterministic variables are needed to describe the state of the system? Explain from this perspective why a quantum computer might be useful.

<details>
<summary><i>Solution.</i></summary>

The state of the system is described by a state vector $\vert \psi\rangle$, which now has $2^n$ complex amplitudes $\langle\mathbf{x}\vert \psi\rangle = \psi(\mathbf{x})$. In a classical computer, we need to list all $2^n$ components. In a quantum computer, we need only $n$ qubits to store and manipulate the state of the system. That seems exponentially better! ▢

</details>

---

We will imagine we have the ability to prepare the system in some specific configuration $\vert \mathbf{x}\rangle$, and observe in the computational basis after applying the black box, with probabilities

$$
p(\mathbf{y}\vert \mathbf{x}) = \text{probability of observing } \mathbf{y} \text{ given input } \mathbf{x}
$$

as above. This looks very similar to the classical random case, and it's tempting to conclude that we could just simulate the $n$-qubit system using $n$ random bits. In the next exercise, you'll see why this doesn't work!

---

***Exercise H.1.4.*** (a) Consider a single-qubit quantum circuit consisting of a single Hadamard gate $H$. Write down the conditional probabilities $p(y\vert x)$ for measurement outcome $y$ after applying this "black box" to input $x$, where $x, y \in \{0, 1\}$.

(b) If this black box was classically random, call it $\tilde{H}$, what would be the result of applying it twice? What is the probability distribution after applying two Hadamard gates?

<details>
<summary><i>Solution.</i></summary>

(a) The Hadamard gate takes

$$
\vert x\rangle \overset{H}{\to} \frac{1}{\sqrt{2}}(\vert 0\rangle + (-1)^x \vert 1\rangle).
$$

Although there is a difference in sign, the amplitude squared for both outcomes $y = 0, 1$ is $1/2$. Hence $p(y\vert x) = 1/2$ for all $x, y \in \{0, 1\}$.

(b) If our black box is the classically random $\tilde{H}$, specified only by the conditional probabilities, then the result of applying it twice gives the same thing back. If $p_{1}$ denotes the result of applying one $\tilde{H}$ gate, and $p_2$ two, then conditioning on the intermediate value $y'$ gives a probability distribution

$$
p_{2}(y\vert x) = \sum_{y' = 0, 1} p_1(y \vert  y')p_1(y'\vert x) = \frac{1}{2}\cdot \frac{1}{2} + \frac{1}{2}\cdot \frac{1}{2} = \frac{1}{2}.
$$

This is the same as $\tilde{H}$, so $\tilde{H}^2 = \tilde{H}$. In sharp contrast, the Hadamard gate is its own inverse, so $H^2 = I$! ▢

</details>

---

We can summarize the results of the last exercise as follows:

<img src="pics/repete.svg">

Two Hadamard gates $H$ gives us a *deterministic* result, while repeating the random gate $\tilde{H}$ looks just like doing a single random gate $\tilde{H}$. Clearly, the nature of time evolution in quantum systems is very different even from classical random systems. In the next section, we'll explore this time evolution in much greater detail!
