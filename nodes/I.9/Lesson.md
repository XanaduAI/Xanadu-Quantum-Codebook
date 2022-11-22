---

**Learning outcomes**

 - *Define a projective measurement.*
 - *Perform a projective measurement in the computational basis.*
 - *Perform measurements in an alternative measurement basis.* 
 
---

Having studied unitary operations, we've now learned about how quantum computers
are manipulated. But if we want to tackle a real problem, we need a way of
getting information *out* of the system after we've done something to it! We
need methods to measure our qubits and interpret those results so that we can
relate them back to the problem at hand.

In earlier nodes, you may recall that we alluded to the idea of **measurements**
when discussing superposition, and the probability of different measurement
outcomes after applying certain quantum operations. In the next two sections, we
will formalize and expand on those ideas. First, we will explore **projective
measurements**.

## Projective measurements

Suppose we have a qubit in the state

$$
 \vert \psi\rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle.
$$

Earlier we learned that, if we measure this qubit, we will observe it in state
$\vert 0\rangle$ with probability $\vert \alpha\vert ^2 = \alpha \alpha^*$, and
in state $\vert 1\rangle$ with probability $\vert \beta\vert ^2$.

A more formal way of expressing the measurement outcome probabilities is using
the *inner product*. Given a quantum state $\vert \psi\rangle$, the probability
that we observe it in state $\vert \varphi\rangle$ when we measure it with
respect to a basis that includes $\vert \varphi\rangle$ is equal to

$$
\hbox{Pr}(\varphi) = \vert \langle \varphi \vert  \psi \rangle\vert ^2.
$$


---

***Exercise I.9.1.*** Try it yourself - compute $\hbox{Pr}(0)$ and
   $\hbox{Pr}(1)$ for $\vert \psi\rangle = \alpha \vert 0\rangle + \beta \vert
   1\rangle$ using the inner product method.

<details>
  <summary><i>Solution.</i></summary>

Evaluating the inner products gives us:

$$
\begin{align*}
\hbox{Pr}(0) &= \vert \langle 0 \vert  \psi \rangle \vert ^2 =  \vert  \alpha \langle 0 \vert  0\rangle + \beta \langle 0 \vert  1 \rangle \vert ^2 = \vert \alpha\vert ^2, \\
\hbox{Pr}(1) &= \vert \langle 1 \vert  \psi \rangle \vert ^2 =  \vert  \alpha \langle 1 \vert  0\rangle + \beta \langle 1 \vert  1 \rangle \vert ^2 = \vert \beta\vert ^2.
\end{align*}
$$

Note how the calculation gets simplified on account of the basis states being
orthogonal! ▢

</details>

---

This type of measurement is known as a projective measurement. We are
essentially asking "how much does each basis vector contribute to a given
state"? The name relates to the fact that we are computing an overlap of the two
state vectors with their inner product, which is just like projections in linear
algebra, as illustrated below.

![](pics/projection.svg)
 
One step that differs from the standard linear algebra example, however, is that
we take the modulus squared of the inner product to obtain a real-valued
probability.

*Tip*. You might be wondering something: after the qubit in a superposition is
 measured, is it still in that superposition? The answer to this is, surprisingly,
 *no*. Once a quantum state has been measured, and we observe its output state,
 it will remain in that state until further processing is done. Or, in briefer
 terms, *what you see is what you get*.

## Bases

So far, we've discussed measurement outcome probabilities of a state expressed
in the computational basis, i.e., a linear combination of $\vert 0\rangle$ and
$\vert 1\rangle$. When we make a measurement, we obtain one of those two states
as a result. But it is not always the case that we're interested in finding out
whether the system is in $\vert 0\rangle$ or $\vert 1\rangle$. In fact,
sometimes measuring in the computational basis makes it impossible to tell
quantum states apart! Measurement in quantum computing is performed with respect
to a *basis*, and as you will see, the choice of basis can lead to very
different results.

*Tip*. If the measurement basis is not specified, it is usually safe to assume
 that it is taken with respect to the computational basis.


---

***Exercise I.9.2.*** A basis consists of vectors that are *orthonormal* (i.e.,
   *normalized* and *orthogonal*). The normalization criteria ensures that the
   basis states are valid qubit states, and the orthogonality condition ensures
   linear independence so that we can write any other qubit state in terms of
   the basis. Earlier, we saw the pair of states

$$
\begin{eqnarray}
\vert +\rangle = \frac{1}{\sqrt{2}} \left( \vert 0\rangle + \vert 1 \rangle \right), \\
\vert -\rangle = \frac{1}{\sqrt{2}} \left( \vert 0\rangle - \vert 1 \rangle \right).
\end{eqnarray}
$$

Do these states form a basis?

<details>
  <summary><i>Solution.</i></summary>

  Yes - the inner product $\langle + \vert - \rangle = 0$, and
 similarly $\langle - \vert + \rangle = 0$ which tells us that the states are
 orthogonal. Also, $\langle + \vert + \rangle = 1$ and $\langle - \vert -
 \rangle = 1$, which tells us that each state is normalized. We hence have a
 basis, one that is commonly known as the **Hadamard basis**, or the
 **plus-minus** basis.  ▢

</details>

---

There is an *infinite* number of bases you can use to represent a qubit
state. However, by far the most common ones are the computational basis and the
Hadamard basis. In what follows, you'll learn how to perform measurements in
different bases.

## Changing things up: basis rotations

Suppose we have a state expressed in the computational basis,

$$
\vert \psi \rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle,
$$

and we would like to perform a change of basis, or *basis rotation*, to convert
this to the Hadamard basis. One way to accomplish this is to re-express the
computational basis states in terms of the Hadamard basis states, which we can
do since they are a proper orthonormal basis. With a bit of algebra, you'll find
that

$$
\begin{align*}
 \vert 0\rangle &= \frac{1}{\sqrt{2}} \left(\vert +\rangle + \vert -\rangle \right), \\
 \vert 1\rangle &= \frac{1}{\sqrt{2}} \left(\vert +\rangle - \vert -\rangle \right).
\end{align*}
$$

We can substitute this into the expression for $\vert \psi\rangle$ and simplify to obtain

$$
\begin{align*}
\vert \psi \rangle &= \alpha \vert 0\rangle + \beta \vert 1\rangle \\
  &= \alpha \frac{1}{\sqrt{2}} \left(\vert +\rangle + \vert -\rangle \right) + \beta  \frac{1}{\sqrt{2}} \left(\vert +\rangle - \vert -\rangle \right) \\
  &= \left( \frac{\alpha + \beta}{\sqrt{2}} \right) \vert +\rangle + \left( \frac{\alpha - \beta}{\sqrt{2}}  \right)\vert -\rangle.
\end{align*}
$$

Now that this state is expressed in the Hadamard basis, we can take a
measurement with respect to it. This measurement is also a projective
measurement, it's just that now, we're projecting onto different basis, as
illustrated below.

![](pics/basis-rotation.svg)

---

***Exercise I.9.3.*** Use the inner product method (as in Exercise I.9.1) to
   compute the measurement outcome probabilities of measuring $\vert \psi
   \rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle$ in the Hadamard basis
   $(\vert +\rangle, \vert -\rangle)$.

<details>
  <summary><i>Solution.</i></summary>

 We are looking for the measurement outcome probabilities
 $\hbox{Pr}(+)$ and $\hbox{Pr}(-)$. We can compute these using the inner product
 method above, but with the state expressed in the Hadamard basis. This makes
 things more convenient, because many terms in the inner product will cancel out
 due to orthogonality.

$$
\begin{align*}
\hbox{Pr}(+) &= \vert \langle + \vert  \psi \rangle \vert ^2 =  \vert  \left( \frac{\alpha + \beta}{\sqrt{2}} \right) \langle + \vert +\rangle + \left( \frac{\alpha - \beta}{\sqrt{2}}  \right) \langle + \vert -\rangle \vert ^2 = \frac{\vert \alpha + \beta\vert ^2}{2}, \\
\hbox{Pr}(-) &= \vert \langle - \vert  \psi \rangle \vert ^2 =  \vert  \left( \frac{\alpha + \beta}{\sqrt{2}} \right) \langle - \vert +\rangle + \left( \frac{\alpha - \beta}{\sqrt{2}}  \right) \langle - \vert -\rangle \vert ^2 = \frac{\vert \alpha - \beta\vert ^2}{2}.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>