---

**Learning outcomes**

- *Write down a mathematical description of a qubit state in two different notations.*
- *Define and give examples of what it means for a quantum system to be in a superposition of states.* 
- *State the relationship between amplitudes and measurement outcome probabilities, and what it means for a state to be normalized.*
- *Explain how operations are mathematically applied to qubit states.*
 
---

Quantum computers are an emerging technology with amazing potential to solve
problems that are intractable even on today's biggest supercomputers. Regular
computers, which we will refer to as **classical computers**, represent
information as *bits*. A bit is a binary value. It can be either 0 or 1, and
this is associated to something physical being in two different states. For
example, a voltage passing through an electronic component can be used to
represent bits. We can choose a threshold value of the voltage, and denote any
voltage over that threshold as a bit in state 1, and similarly any voltage below
as a bit in state 0.

<img src="pics/voltage_threshold.svg" width="700px">

The power of quantum computers comes from the different way in which they
represent and manipulate information. Quantum computers use special bits, called
quantum bits, or **qubits**. As with bits, qubits also correspond to something
physical, but our focus here will be on the theory from a software and
algorithms perspective.

Quantum computing is the manipulation of qubits to solve problems. Before we
can delve into quantum computation, we need a framework for describing qubits and the
things we can do to them. In this node, you will learn about the mathematical
underpinnings of quantum computing. The key ingredients we need are:

 - a mathematical representation of a qubit's *state*
 - a means of measuring a qubit to determine what state it is in
 - a way of manipulating the state to perform computation

## Mathematical representation of qubits 

Under the hood, the mathematical framework of quantum computing is **linear
algebra**. A qubit is represented by a **state**, which is a column vector of
two elements. The two most basic ones are the analogues of a bit's "0" and "1"
state, which are represented by the following two vectors:

$$
\begin{equation}
 \hbox{qubit state 0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad  \hbox{qubit state 1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \tag{1}
\end{equation}
$$

This is tedious to write, though, so in quantum computing (and more generally,
in quantum mechanics) we use a type of shorthand notation called **Dirac
notation**, or **bra-ket notation**. The state vector of a qubit is called a
**ket**, the notation for which is $\vert \cdot \rangle$. What goes in between
the $\vert$ and $\rangle$ is a label to denote particular state. The two states
above, in bra-ket notation, are expressed like so:

$$
\begin{equation}
 \vert 0 \rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad  \vert 1 \rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \tag{2}
\end{equation}
$$

Quite often, we will see the notation $\vert \psi \rangle$, which represents a
qubit in some arbitrary state labelled by $\psi$.

Bra-ket notation gets its name for a reason: for every ket, there is an associated
**bra**. A bra is like a ket turned on its side. It is a row vector, where each
element in the vector is the complex conjugate of the corresponding element in the ket.
(More formally, a bra is the conjugate transpose of a ket.) The notation for bras
is the reverse of the notation for kets:

$$
\begin{equation}
 \langle 0 \vert = \begin{pmatrix} 1 & 0 \end{pmatrix}, \quad  \langle 1 \vert = \begin{pmatrix} 0 & 1 \end{pmatrix}. \tag{3}
\end{equation}
$$

These two states, $\vert 0 \rangle$ and $\vert 1 \rangle$, are particularly
important because they form a basis. In linear algebra, a basis is a set of
vectors that spans a vector space; you can write anything else in that space as
a **linear combination** of those basis vectors. Bases must consist of linearly
independent vectors. A special case of this is when the basis vectors are
**orthogonal**. Orthogonality can be checked by taking the **inner product**
between two vectors, which is defined by the dot product. The same holds true
for qubit states (with a bit of a twist).

The inner product between two qubit states is computed by taking the dot
product between the bra of one, and the ket of the other (they
combine to form a "bra-ket" expression). We can do so to check that 
$\vert 0 \rangle$ and $\vert 1 \rangle$ are orthogonal:

$$
\begin{align*}
\langle 0\vert \vert 1\rangle = \langle 0\vert  1\rangle
&=~\begin{pmatrix} 1 & 0 \end{pmatrix} \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix} \\
&= ~1 \cdot 0 + 0 \cdot 1 \\
&= ~0. 
\end{align*} \tag{4}
$$

Notice how we simplify the notation when combining a bra and a ket by
eliminating one of the vertical lines. Thus, $\vert 0 \rangle$ and $\vert 1 \rangle$
are orthogonal, and form a basis. This is a special basis called the **computational
basis**, and it is the most commonly-used basis in which to express quantum states.

Another feature of the computational basis is that its states are **normalized**
to have length 1. You can compute the length of a qubit state vector just like
you compute the length of a regular 2-dimensional vector; by computing its inner
product with itself, and then taking the square root. For example, 

$$
\begin{align*}
\sqrt{\langle 1\vert 1\rangle} 
& = \sqrt{\begin{pmatrix} 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix}} \\
& = \sqrt{0 \cdot 0 + 1 \cdot 1} \\
& = 1.
\end{align*} \tag{5}
$$

When a basis consists of two normalized, orthogonal vectors, is it called an
**orthonormal basis**.

## Superposition

Of course, $\vert 0 \rangle$ and $\vert 1 \rangle$ are not the only possible states for
a qubit (otherwise, they wouldn't be any different than bits!). What makes qubits so
special is that they can exist in a **superposition** state somewhere "between"
$\vert 0\rangle$ and $\vert 1\rangle$.  Mathematically, the state of a qubit in
superposition is a linear combination of the basis states,

$$
\begin{equation}
\vert \psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}
\end{equation} \tag{6},
$$

where $\alpha$ and $\beta$ are complex numbers such that

$$
\alpha \alpha^* + \beta \beta^* = 1, \tag{7}
$$

and the $*$  indicates the complex conjugate. These $\alpha$ and $\beta$ are
called **amplitudes**, or **probability amplitudes**. The amplitudes carry
information about the relative strength of $\vert 0\rangle$ and $\vert 1\rangle$
in the state.

*Tip*. A common misconception is that a qubit in a superposition of two states
 is *in* both states at the same time. This is false; the qubit is only ever
 *in* one state. It's just that sometimes, that state may be a linear
 combination of the basis states.

Now that we have complex numbers in the mix, we have to be a bit more
careful. Let's suppose we have two states

$$
\begin{equation}
\vert \psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle \quad \text{and} \quad \vert \phi\rangle = \gamma\vert 0\rangle + \delta\vert 1\rangle
\end{equation} \tag{8}
$$

and we would like to take the inner product between them, $\langle \phi \vert
\psi \rangle$.  First, we must compute the bra of $\vert \phi \rangle$. When a qubit is in a
superposition of the basis states, we can compute the bra by taking the bra of
each basis state one at a time, remembering to take the *conjugate* of the amplitudes:

$$
\begin{equation}
\langle \phi \vert  = \gamma^* \langle 0 \vert + \delta^* \langle 1 \vert = \begin{pmatrix} \gamma^* & \delta^* \end{pmatrix}.
\end{equation} \tag{9}
$$


With more interesting quantum states, the inner product tells us something about
the overlap, or, in a sense, similarity between two states. The result of the
inner product is a complex number. If it's 0, the two states are orthogonal, and
if it is 1, they are the same and the state is normalized (as we observed when we computed the inner product of
$\vert 1 \rangle$ with itself). There are two ways to compute the inner
product of two superposition states. You could write out the matrices:

$$
\begin{equation}
\langle \phi \vert  \psi \rangle = \begin{pmatrix} \gamma^* & \delta^* \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}.
\end{equation} \tag{10}
$$


Alternatively, you can work purely in bra-ket notation. The inner product is
**linear**, and we can compute the inner product by expanding out the expression,
much like we would a polynomial in algebra:

$$
\begin{equation}
\langle \phi \vert  \psi \rangle = (\gamma^*\langle 0\vert  + \delta^* \langle 1\vert ) \cdot (\alpha\vert 0\rangle + \beta\vert 1\rangle) = \gamma^* \alpha \langle 0\vert 0\rangle + \delta^* \alpha \langle 1\vert 0\rangle + \gamma^* \beta \langle 0\vert 1\rangle + \delta^* \beta \langle 1\vert 1\rangle 
\end{equation}. \tag{11}
$$

---

***Exercise I.1.1.*** Starting from the previous expression, and using what
   you've learned so far about the basis states $\vert 0\rangle$ and $\vert
   1\rangle$, finish evaluating the inner product $\langle \phi \vert \psi
   \rangle$ and express the results in terms of the amplitudes $\alpha, \beta,
   \gamma, \delta$.

<details>
  <summary><i>Solution.</i></summary>

The orthogonality of the basis states means that $\langle 0 \vert 0 \rangle =
\langle 1 \vert 1 \rangle = 1$, while $\langle 1 \vert 0 \rangle = \langle 0
\vert 1 \rangle = 0$. Thus, we obtain that

$$
\langle \phi \vert  \psi \rangle = \gamma^*\alpha + \delta^* \beta.
$$

<div align="right"> ▢ </div>

</details>


---

***Exercise I.1.2.*** Verify that the superposition state

$$
\vert \psi\rangle = \frac{3}{5} \vert 0\rangle - \frac{4}{5} e^{\frac{\pi}{6} i} \vert 1\rangle
$$

is normalized. 

<details>
  <summary><i>Solution.</i></summary>

To verify this, we can take the inner product of the state with itself and check
that the result is 1. We can simplify the calculation using the tricks from the
previous exercise to quickly eliminate half of the terms:

$$
\begin{align*}
\langle \psi \vert \psi \rangle 
& = \left( \frac{3}{5} \langle 0 \vert - \frac{4}{5} e^{-\frac{\pi}{6} i} \langle 1 \vert  \right) \left(  \frac{3}{5} \vert 0\rangle - \frac{4}{5} e^{\frac{\pi}{6} i} \vert 1\rangle \right)\\
& = \frac{9}{25}  + \frac{16}{25} \\
& = 1.
\end{align*} 
$$

<div align="right"> ▢ </div>

</details>

---

## Measurement outcome probabilities

Creating qubit states and putting them in superposition happens at the beginning
of an algorithm. In order to perform a meaningful quantum computation, we'll
need a way to get information *from* the qubits at the end of an algorithm. That
is, we need a way to measure qubits. Measurement in quantum computing is
probabilistic. When we measure, we can't see whether a qubit is in a
superposition, rather we observe the qubit either in state $\vert 0\rangle$ or
state $\vert 1\rangle$. The amplitudes $\alpha$ and $\beta$ contain the
information about the probability of each of those outcomes:

\begin{eqnarray}
 \hbox{Prob(measure and observe } \vert 0\rangle) &=& \vert \alpha\vert ^2, \\
 \hbox{Prob(measure and observe } \vert 1\rangle) &=& \vert \beta\vert ^2. \\ \tag{12}
\end{eqnarray}

This notation, $\vert \cdot\vert ^2$ is called the "mod squared", and is simply
multiplication of a number by its complex conjugate, i.e., $\vert \alpha\vert ^2
= \alpha \alpha^*$. Since there are only two possible outcomes for the
measurement, it must be that these probabilities sum to $1$ for a valid qubit
state; this is why quantum states must be *normalized* ($\vert \alpha\vert ^2 +
\vert \beta\vert ^2 = 1$).

Colloquially, we often refer to observing the qubit in state $\vert 0\rangle$
after measurement as a "measurement outcome of 0", and similarly for $\vert
1\rangle$.  In other words, if we measure a $\vert 0\rangle$ we can map that to
a classical "0" and if we measure a $\vert 1\rangle$ we can map that to a
classical "1". After measurement, the qubit itself remains in the observed
state. This means we can't tell right away what some original state $\vert \psi
\rangle = \alpha \vert 0 \rangle + \beta \vert 1 \rangle$ might have
been. Measurement has given us just a single bit of information, 0 or 1, that we
associate with the corresponding outcome. In order to determine the full state,
we must take many, many measurements in order to estimate the
outcome probabilities, and thus $\alpha$ and $\beta$.

---

***Exercise I.1.3.*** Suppose you have a qubit in the state

\begin{equation}
 \vert \psi \rangle = \frac{1}{2} \vert 0\rangle - \frac{\sqrt{3}i}{2} \vert 1\rangle.
\end{equation}

Is this state normalized? If so, what is the probability of observing the qubit
in state $\vert 1\rangle$ after measuring it?

<details>
  <summary><i>Solution.</i></summary>
  Yes, the state is normalized because:
 \begin{equation}
    \bigg|\frac{1}{2}\bigg|^2 + \bigg|\frac{\sqrt{3}i}{2}\bigg|^2 = 1
\end{equation}
  
  The probability of observing it in $\vert 1 \rangle$ is 

\begin{equation}
-\frac{\sqrt{3}i}{2} \times \frac{\sqrt{3}i}{2} = \frac{3}{4}.
\end{equation}

<div align="right"> ▢ </div>

</details>

---

## Operations on qubit states

Now that we have the starting and ending components of a quantum algorithm, we
need the final ingredient that happens in between: the manipulation of qubit
states. Qubit states are vectors, so we need a mathematical means of modifying a
vector $\vert \psi\rangle$ to produce another vector $\vert \psi^\prime\rangle$:

\begin{equation}
 \vert \psi\rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle \rightarrow \vert \psi^\prime\rangle = \alpha^\prime \vert 0\rangle + \beta^\prime \vert 1\rangle. \tag{13}
\end{equation}

What sends a 2-dimensional vector to another 2-dimensional vector?
Multiplication by a $2 \times 2$ matrix, $U$:

\begin{equation}
\vert \psi^\prime \rangle = U \vert \psi\rangle. \tag{14}
\end{equation}

But not just any matrix will do. The matrix must preserve the normalization of
the state. Even after an operation, the measurement outcome probabilities must
sum to 1, i.e., $\vert \alpha^\prime\vert ^2 + \vert \beta^\prime\vert ^2 =
1$. There is a special class of matrices that preserves the length of quantum
states: **unitary matrices**. Their defining property is that $U U^\dagger = I$,
where the $\dagger$ indicates the taking complex conjugate of all elements in
the transpose of $U$, and $I$ is the $2 \times 2$ identity matrix. As you
progress through the rest of this module, you will become familiar with
many common unitary operations.

---

***Exercise I.1.4.*** Suppose we have a qubit in state 

\begin{equation}
 \vert \psi \rangle = \frac{1}{2} \vert 0\rangle - \frac{\sqrt{3}i}{2} \vert 1\rangle,
\end{equation}

and we want to apply the operation 

\begin{equation}
 U = \begin{pmatrix} 0 & i \\ -i & 0 \end{pmatrix}.
\end{equation}

Compute the state of the qubit after applying $U$. Then, compute the measurement
outcome probabilities of 0 and 1, and verify that the state is normalized

<details>
  <summary><i>Solution.</i></summary>

$$
U \vert \psi\rangle = \begin{pmatrix} 0 & i \\ -i & 0 \end{pmatrix} \begin{pmatrix} \frac{1}{2} \\ \frac{-\sqrt{3}i}{2} \end{pmatrix} = \begin{pmatrix} \frac{\sqrt{3}}{2} \\ \frac{-i}{2} \end{pmatrix} = \frac{\sqrt{3}}{2} \vert 0\rangle - \frac{i}{2}\vert 1\rangle
$$

The probabilities of outcomes 0 and 1 are 3/4 and 1/4 respectively. Since they sum to 1,
we know that the state is normalized. ▢

</details>

---

## Quantum computation in a nutshell

With that, you now know enough to perform simple computations on a single qubit!
Everything is linear algebra: qubit states are linear combinations of basis
vectors $\vert 0\rangle$ and $\vert 1\rangle$, and operations on them are
performed by matrices. Furthermore, the coefficients of those linear
combinations tell us about the likelihood of a qubit being in one of those two
states after measurement. Preparing states, performing operations, and taking
measurements are the building blocks of all quantum algorithms. In the next few
sections, we will formalize these ideas, and you will be introduced to a wide
variety of common operations and a more formal description of measurement. But
first, we'll explore a different representation of quantum computation: quantum
circuits.