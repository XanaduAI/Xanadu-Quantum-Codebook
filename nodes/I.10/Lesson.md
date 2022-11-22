---

**Learning outcomes**

 - *Define an observable, and compute its possible measurement outcomes.*
 - *Compute the expectation value of an observable.*
 
---

## Observables

While obtaining measurement outcome probabilities gives us useful information
about a qubit's state, we're often interested in other measurable quantities
that correspond to something physical, such as its energy. In quantum mechanics,
and consequently quantum computing, physical quantities are related to a special
type of object called an **observable**. Observables correspond to [Hermitian
matrices](https://en.wikipedia.org/wiki/Hermitian_matrix) whose eigenvalues
represent the possible values of the measurement outcome.

*Tip*.  A matrix $B$ is **Hermitian** if $B = B^\dagger$. Hermitian matrices
have real eigenvalues, which is a sensible property for measurable physical
quantities to have.

As an example, let us consider the Pauli $Z$ operation. You can check that

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

is Hermitian, and has eigenvalues $1$ and $-1$ with corresponding eigenvectors,
or eigenstates, $\vert 0\rangle$ and $\vert 1\rangle$. Similarly, the Pauli $X$ matrix is
Hermitian and has eigenvalues $1$ and $-1$, but the associated eigenstates are
$\vert +\rangle$ and $\vert -\rangle$. If we were to "measure the observable
Pauli $Z$" (or Pauli $X$) for a given qubit state, we would obtain one of the
two possible eigenvalues. (This is why, in earlier nodes, we computed the
eigenvalues of some of these operations!) Furthermore, following the
measurement, the qubit's state will be that of the eigenvector of the
corresponding measurement outcome.

In order to get a clearer picture of the value of an observable for a given
qubit state, we need to measure its **expectation value**. This is essentially
the weighted average of what we would see over many experiments.

---

***Exercise I.10.1.*** Suppose we measure an observable $B$ for which there is a
   $70\%$ chance we obtain eigenvalue $1$, and $30\%$ chance we obtain the
   eigenvalue $-1$. What is the expectation value of $B$?

<details>
  <summary><i>Solution.</i></summary>

The expectation value of $B$ is

$$
\langle B \rangle = 0.7 \times 1 + 0.3 \times (-1) = 0.4.
$$

While in each individual experiment we see $1$ or $-1$, we'll see $1$ more
often, and so the expected value is closer to $1$ than it is to $-1$. ▢

</details>

---

Expressed mathematically, the expectation value of some observable $B$ for a state
$\vert \psi\rangle$ is given by

$$
\langle B \rangle = \langle \psi \vert  B \vert  \psi \rangle. \tag{1}
$$

Namely, we first compute the result of the matrix $B$ applied to $\vert
\psi\rangle$ followed by its inner product with $\vert \psi\rangle$.

---

***Exercise I.10.2.*** Let 

$$
\begin{equation}
 \vert \psi\rangle = \frac{4}{5} \vert 0\rangle - \frac{3}{5} e^{i \pi/3} \vert 1\rangle
\end{equation},
$$

and suppose we want to measure the observable 

$$ 
B = \begin{pmatrix} 1 & -2i \\ 2i & 2 \end{pmatrix}.
$$

 *(a)* What are the possible outcomes of the measurement?


<details>
  <summary><i>Tip.</i></summary>

*Tip*. It is common to specify a measurement by saying "measure in the $X$
 basis", or "measure $X$". These statements relate directly back to projective
 measurements and observables respectively. Measuring in the $X$ basis means to
 take a projective measurement with respect to the basis composed of the
 eigenvectors of $X$ (these happen to be $\vert +\rangle$ and $\vert
 -\rangle$). The output of this measurement is either $\vert +\rangle$, or
 $\vert -\rangle$. Measuring $X$, on the other hand, means to measure the
 observable $X$, which has eigenvalues $+1$ and $-1$, corresponding to those
 same eigenstates $\vert +\rangle$ and $\vert -\rangle$. The output of this
 measurement is then either $+1$, or $-1$. While the two measurements are
 ultimately the same, the context and language indicate what the output value
 should look like.

</details>

<details>
  <summary><i>Solution.</i></summary>

To determine the possible measurement outcomes, we must compute the eigenvalues of $B$. They are
$\lambda_1 = 3.56155281$ and $\lambda_2=-0.56155281$.  ▢
 </details>


*(b)* For each outcome, what state is the qubit in after the measurement? Express
this in the computational basis.

<details>
  <summary><i>Solution.</i></summary>

The possible outcomes are the associated eigenvectors,

$$
\begin{align*}
\vert v_1\rangle &= -0.61541221i \vert 0 \rangle + 0.78820544 \vert 1\rangle, \\
\vert v_2\rangle &= 0.78820544 \vert 0 \rangle - 0.61541221i \vert 1 \rangle.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

*(c)* What is the expectation value of $B$, computed analytically?

<details>
  <summary><i>Solution.</i></summary>

The analytical expectation value is 
 $$ 
 \begin{equation}
  \langle \psi \vert B \vert \psi \rangle = \frac{1}{25} \begin{pmatrix} 4 & -3 e^{-i\pi/3} \end{pmatrix} \begin{pmatrix} 1 & -2i \\ 2i & 2 \end{pmatrix} \begin{pmatrix} 4 \\ -3 e^{i\pi/3} \end{pmatrix} = 3.022769.
 \end{equation}
 $$

<div align="right"> ▢ </div>

</details>

*(d)* Suppose we prepared this state and measured $B$ 1000 times. 816 of the trials yielded the larger of the two possible measurement outcomes, and the remaining tries yielded the smaller one. What is the experimentally-obtained expectation value of $B$?  


<details>
  <summary><i>Solution.</i></summary>

 To compute the experimentally obtained eigenvalue, we take the weighted average:
 $$
 \langle \tilde{B} \rangle = \frac{816 \cdot 3.56155281 + 184 \cdot (-0.56155281)}{1000} = 2.802901.
 $$
 The experimentally obtained value does not exactly match the analytically obtained one in this case, but will do so in the limit of an infinite number of trials. ▢

</details>