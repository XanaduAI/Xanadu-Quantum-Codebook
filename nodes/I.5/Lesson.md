---

**Learning outcomes**:
    
 - *Describe the action of the RZ gate and its matrix representation.*
 - *Identify 3 special cases of RZ.*
 
---

Both the $X$ and the $H$ gate of the previous node affected which basis states
appeared in the superposition. We know how to flip the states using $X$, and how
to create uniform superpositions. But, how can we change the amplitudes more
generally? How do we change their relative magnitudes? In this section, we will
learn about operations that change the *phase* of the amplitudes of a
superposition.

## Global and relative phases

Let's consider an arbitrary quantum state 

$$
\vert \psi \rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle, \tag{1}
$$

and separate out the real and complex components of the amplitudes by writing
them in polar form, i.e., $\alpha = a e^{i\theta}$, $\beta = b e^{i\varphi}$. We
can factor out the complex part:

$$
\vert \psi \rangle = a e^{i\theta} \vert 0\rangle +b e^{i\varphi} \vert 1\rangle = e^{i\theta} ( a\vert 0\rangle + b e^{i(\varphi-\theta)} \vert 1\rangle). \tag{2}
$$


Notice how the term $e^{i\theta}$ out front doesn't affect the measurement
outcome probabilities *at all*! Without loss of generality, we can totally
ignore this **global phase**, and describe exactly the same quantum state:

$$
\begin{equation}
\vert \psi \rangle = a\vert 0\rangle + b e^{i(\varphi-\theta)} \vert 1\rangle = a\vert 0\rangle + b e^{i\phi} \vert 1\rangle. \tag{3}
\end{equation}
$$

This remaining complex value, $e^{i\phi}$ is known as a **relative phase**. If
you look at the measurement outcome probabilities of $\vert 0\rangle$ and $\vert
1\rangle$, you might notice that this phase doesn't affect them either; we will
learn later, though, that it *can* affect the measurement outcomes if the
measurements are performed in a different way.

## Z rotations

The $RZ$ gate, or "$Z$ rotation" is a quantum gate that modifies the relative
phase between $\vert 0\rangle$ and $\vert 1\rangle$. Given some initial state
$\vert \psi \rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle$, a $Z$
rotation by the amount $\omega$ (an angle in radians) is

$$
\begin{equation}
RZ(\omega) \vert \psi \rangle = \alpha \vert 0\rangle + \beta e^{i\omega} \vert 1\rangle. \tag{4}
\end{equation}
$$

The matrix representation of $RZ$ is a bit counter-intuitive at first:

$$
\begin{equation}
 RZ(\omega) = \begin{pmatrix} e^{-i \frac{\omega}{2}} & 0 \\ 0 & e^{i \frac{\omega}{2}} \end{pmatrix}. \tag{5}
\end{equation}
$$

---

***Exercise I.5.1.*** Evaluate the action of the $RZ(\omega)$ matrix on an
   arbitrary state $\vert \psi \rangle = \alpha \vert 0\rangle + \beta \vert
   1\rangle$. Explain why this is equivalent to the matrix representation

\begin{equation}
 RZ^\prime(\omega) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i \omega} \end{pmatrix}.
\end{equation}


<details>
  <summary><i>Solution.</i></summary>

  Let's work this out using matrix-vector multiplication.

$$
\begin{align*}
 RZ(\omega) \begin{pmatrix} \alpha \\ \beta \end{pmatrix} 
 &= \begin{pmatrix} e^{-i \frac{\omega}{2}} & 0 \\ 0 & e^{i \frac{\omega}{2}} \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \\
 &\equiv \begin{pmatrix} e^{-i \frac{\omega}{2}} \alpha \\ e^{i \frac{\omega}{2}} \beta \end{pmatrix} \\
 &= e^{-i \frac{\omega}{2}} \alpha \vert 0 \rangle + e^{i \frac{\omega}{2}} \beta \vert 1 \rangle.
\end{align*}
$$

We can factor out the complex part of the amplitude on $\vert 0 \rangle$, as it
is a global phase. Doing so, we obtain:

$$
\begin{align*}
e^{-i \frac{\omega}{2}} \alpha \vert 0 \rangle + e^{i \frac{\omega}{2}} \beta \vert 1 \rangle
 &= e^{-i \frac{\omega}{2}} \left( \alpha \vert 0 \rangle + e^{i \omega} \beta \vert 1 \rangle \right) \\
&\equiv  \alpha \vert 0 \rangle + e^{i \omega} \beta \vert 1 \rangle \\
&=  \begin{pmatrix} 1 & 0 \\ 0 & e^{i \omega} \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, 
\end{align*}
$$

demonstrating that these matrix representations are equivalent. ▢

</details>

---

***Exercise I.5.2.*** What is the inverse (i.e., conjugate transpose) of
   $RZ(\omega)$? Express the result as a function of $\omega$.


<details>
  <summary><i>Solution.</i></summary>

If $RZ(\omega)$ rotates us forward by an angle $\omega$, we should
 be able to undo it by rotating backwards. You can check that indeed
 $RZ^\dagger(\omega) = RZ(-\omega)$. ▢

</details>

---

## Z, S, and T

There are three special cases of $RZ(\omega)$ that correspond to very
commonly-used quantum gates: $Z$, $S$, and $T$.


<img src="pics/zst.svg" alt="" width="300px">


The case where $\omega = \pi$ is known as a Pauli $Z$ operation.

---

***Exercise I.5.3.*** Determine the matrix representation of $Z$ (and factor out
   the global phase). What are its eigenvalues and normalized eigenvectors
   expressed in the computational basis? What happens when you apply $Z$ twice?

<details>
  <summary><i>Solution.</i></summary>

The matrix representation of $Z$ without its global phase is

$$
\begin{equation}
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
\end{equation}
$$

Its eigenvectors $\vert 0 \rangle$ and $\vert 1 \rangle$, with respective
eigenvalues $1$ and $-1$ (the same as Pauli $X$). Applying $Z$ twice gives us
back our original state; $Z$ is its own inverse. ▢

</details>

---

Another well-known case is $\omega=\pi/2$. This gate is known colloquially as
the phase gate and is denoted by $S$.

---

***Exercise I.5.4.*** Determine the matrix representation of $S$ (and factor out
   the global phase). What are its eigenvalues and eigenvectors? What happens
   when you apply $S$ twice?


<details>
  <summary><i>Solution.</i></summary>

 Filling in the value of $\pi/2$, we obtain 

$$
\begin{align*}
 S &= \begin{pmatrix} e^{-i \frac{\pi}{4}} & 0 \\ 0 & e^{i \frac{\pi}{4}} \end{pmatrix} \\
 &=  e^{-i \frac{\pi}{4}} \begin{pmatrix} 1 & 0 \\ 0 & e^{i \frac{\pi}{2}} \end{pmatrix} \\ 
 &\equiv \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}.
\end{align*}
$$

Its eigenvalues are $1$ and $i$ with eigenvectors $\vert 0\rangle$ and $\vert 1
\rangle$ respectively. If we apply $S$ twice, we obtain

$$
\begin{align*}
 S^2 &=  \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \\
 &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \\
 &= Z.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

---

Finally, the case where $\omega=\pi/4$ is known as the $T$ gate. The $T$ gate is
sometimes referred to as the "pi over 8 gate" due to how its matrix
representation looks.

---

***Exercise I.5.5.*** How can you implement the adjoint of $S$, $S^\dagger$,
   using only $S$ gates? Similarly, implement the adjoint of $T$, $T^\dagger$,
   using only $T$ gates.

<details>
  <summary><i>Solution.</i></summary>

 We know from the previous exercises that $SS = Z$, and that $ZZ =
 I$. Therefore, $SSSS = I$. Since we know $S S^\dagger = I$, it must be that
 $S^\dagger = SSS$. You can also reason this using the rotation angles. We're
 dealing with complex exponentials, which have a period of $2\pi$. Since $S$ is
 a rotation of $\pi/2$, we would need to do that 3 more times to get to a full
 rotation, which due to the periodicity, would be equivalent to doing nothing
 (i.e., the identity). You can use a similar argument for the $T$ gate. $T$ is a
 $\pi/4$ rotation, meaning that we would need to apply $7$ of them to get to a
 full $2\pi$. Thus, $T^\dagger = T^7$. ▢

</details>