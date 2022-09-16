---

**Learning outcomes**:

 - *Describe the action of the RX gate and its matrix representation.*
 - *Describe the action of the RY gate and its matrix representation.*
 - *Represent qubit states in 3-dimensional space using the Bloch sphere.*
 
---

Qubits bear a special relationship with 3-dimensional space. We saw in the
previous node that the most general form of a qubit is

$$
\begin{equation}
 \vert \psi\rangle = a \vert 0\rangle + b e^{i\phi} \vert 1\rangle, \tag{1}
\end{equation}
$$

where $a$ and $b$ are two real numbers. The normalization requirements of the
state also tell us something else: that $a^2 + b^2 = 1$. We can thus make
the natural association of $a$ and $b$ to two trigonometric functions that have
the same relationship: $a = \cos(\theta/2)$ and $b = \sin(\theta/2)$. Then,


$$
\begin{equation}
 \vert \psi\rangle = \cos \left(\frac{\theta}{2} \right) \vert 0\rangle + \sin \left(\frac{\theta}{2} \right) e^{i\phi} \vert 1\rangle. \tag{2}
\end{equation}
$$


We have a single-qubit state parametrized by two angles, $\theta$ and $\phi$, with
length 1. This suggests that we could make associations between qubit states,
and unit vectors in 3-dimensional space expressed in *spherical
coordinates*. $Z$ rotations correspond to rotations around the vertical
"Z-axis". There are thus two other ways in which we can rotate: about "X" and
"Y".

Now, calling single-qubit operations "rotations" like this can seem very
abstract. What *are* "X", and "Y"? Fortunately, there is a visualization tool
that can be helpful for understanding the structure and behaviour of single-qubit
states and operations: the **Bloch sphere**.

The Bloch sphere is a spherical representation of the state of a single
qubit. Each qubit state vector corresponds to a *real* vector on the surface of
the sphere in a 3-dimensional space.

<img src="pics/bloch_state.svg" alt="" width="300px">

There are the usual three axes: $x$, $y$, and $z$. Along the $z$ axis, the
top-most state corresponds to $\vert 0 \rangle$, and the bottom to $\vert 1\rangle$;
these are the eigenvectors of the Pauli $Z$ operator. Similarly, along the $x$
axis are the $\vert + \rangle$ and $\vert - \rangle$ states, which are the
eigenvectors of the Pauli $X$ operator. (You will meet Pauli $Y$ later in node,
but the same holds for it and its eigenvectors.)


<img src="pics/bloch.svg" alt="" width="400px">

$RX$, $RY$, and $RZ$ rotate the qubit's state vector about the appropriate axis.

<img src="pics/bloch_rotations.svg" alt="" width="700px">

This can help you visually understand some of the rotation angles you saw
previously for $RZ$, namely $Z$, $S$, and $T$. Consider the starting state
$\vert + \rangle$.  If we apply $Z = RZ(\pi)$, we end up at the opposite pole of
the circle at $\vert - \rangle$, which is precisely a 3-dimensional rotation of
$\pi$. The same goes for $S$ and $T$; they are quarter- and eighth-turns
respectively.

<img src="pics/bloch_zst.svg" alt="" width="500px">

## RX and RY

Now that we have some intuition about what these rotations are, we can
begin to express $RX$ and $RY$ in terms of matrices and describe how they
act on the basis states.

The matrix representation of an $X$ rotation is

$$
    RX(\theta) = \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\ -i\sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)   \end{pmatrix}. \tag{3}
$$

---

***Exercise I.6.1.*** Determine $\theta$ for which $RX(\theta) = X$ (up to a global phase). 


<details>
  <summary><i>Solution.</i></summary>

We need an angle such that $\cos\left(\theta/2\right) = 0$, and
 $\sin(\theta/2) = 1$. The angle $\pi$ satisfies these requirements; there is a
 global phase of $-i$ present, but as in the previous node, global phases have
 no effect and can be safely removed.

$$
\begin{align*}
RX(\pi) &= \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix} \\
&= -i X.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

---

The matrix representation of a $Y$ rotation looks very similar to that of $RX$,
however there is no complex component:

$$
    RY(\theta) = \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & - \sin \left(\frac{\theta}{2} \right) \\ \sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)   \end{pmatrix}. \tag{4}
$$


---

***Exercise I.6.2.*** Just like how Pauli $X$ and $Z$ are special cases of $RX$
   and $RZ$, Pauli $Y$ is the special case of $RY(\theta)$ when $\theta =
   \pi$. Typically, it is written as

   $$
   Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}.
   $$

   Furthermore, there is a nice relationship between $X$, $Y$, and $Z$. Show
   that $Y = iXZ = iRY(\pi)$.


<details>
  <summary><i>Solution.</i></summary>

For this exercise, let's use matrix multiplication to prove the
 identity. First,

$$
\begin{align*}
i XZ &= i \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \\
&= i \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \\
&= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \\
\end{align*}.
$$

Now if we use instead the $RY$ rotation,
$$
\begin{align*}
i RY(\pi) &= i \begin{pmatrix} \cos \left(\frac{\pi}{2} \right) & - \sin \left(\frac{\pi}{2} \right) \\ \sin \left(\frac{\pi}{2} \right)& \cos \left(\frac{\pi}{2} \right)   \end{pmatrix}. \\
&= i \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \\
&= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

---


***Exercise I.6.3.*** Evaluate the action of $RX(\theta)$ and $RY(\theta)$ on
 $\vert 0 \rangle$ and $\vert 1 \rangle$. Express your results as linear combinations
of these computational basis states.


<details>
  <summary><i>Solution.</i></summary>

This can be worked out easily enough using matrix multiplication. For $RX$, we have

$$
\begin{align*}
 RX(\theta)\vert 0\rangle &=  \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\ -i\sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)  \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} \\
 &= \begin{pmatrix} \cos \left( \frac{\theta}{2} \right) \\ -i \sin \left( \frac{\theta}{2} \right) \end{pmatrix} \\
 &= \cos \left( \frac{\theta}{2} \right) \vert 0 \rangle -i \sin \left( \frac{\theta}{2} \right) \vert 1 \rangle,
\end{align*}
$$

and 

$$
\begin{align*}
 RX(\theta) \vert 1\rangle  &=  \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\ -i\sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)  \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} \\
 &= \begin{pmatrix}  -i \sin \left( \frac{\theta}{2} \right) \\ \cos \left( \frac{\theta}{2} \right) \end{pmatrix} \\
 &= -i \sin \left( \frac{\theta}{2} \right)  \vert 0 \rangle + \cos \left( \frac{\theta}{2} \right) \vert 1 \rangle.
\end{align*}
$$

You can follow the same steps for $RY$ to obtain

$$
\begin{align*}
 RY(\theta) \vert 0 \rangle &=  \cos \left( \frac{\theta}{2} \right) \vert 0 \rangle + \sin \left( \frac{\theta}{2} \right) \vert 1 \rangle, \\
 RY(\theta) \vert 1 \rangle &=  -\sin \left( \frac{\theta}{2} \right) \vert 0 \rangle + \cos \left( \frac{\theta}{2} \right) \vert 1 \rangle. \\
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

---


***Exercise I.6.4.*** There are many other relationships you can derive between
   these three types of rotation. Such relationships are often useful for
   simplifying sequences of quantum operations in circuits.  For example, what
   is the result of applying $X$ both before and after an application of
   $RY(\theta)$?

   
<img src="pics/x_ry_x.svg" alt="" width="400px">


<details>
  <summary><i>Solution.</i></summary>

Let's work through the math in bra-ket notation; recall we need only
 see how the operations affect the computational basis states to know how they
 act in general.

$$
\begin{align*}
X RY(\theta) X \vert 0 \rangle &= X RY(\theta) \vert 1 \rangle  \\
&= X \left( -\sin \left( \frac{\theta}{2} \right) \vert 0 \rangle + \cos \left( \frac{\theta}{2} \right) \vert 1 \rangle \right) \\
&=  \cos \left( \frac{\theta}{2} \right) \vert 0 \rangle -\sin \left( \frac{\theta}{2} \right) \vert 1 \rangle.
\end{align*}
$$

This looks almost like $RY(\theta) \vert 0\rangle = \cos \left( \frac{\theta}{2}
\right) \vert 0 \rangle + \sin \left( \frac{\theta}{2} \right) \vert 1 \rangle$
, but with a negative sign. Let's check what it does to $\vert 1 \rangle$:

$$
\begin{align*}
X RY(\theta) X \vert 1 \rangle &= X RY(\theta) \vert 0 \rangle  \\
&= X \left(  \cos \left( \frac{\theta}{2} \right) \vert 0 \rangle -\sin \left( \frac{\theta}{2} \right) \vert 1 \rangle \right) \\
&= -\sin \left( \frac{\theta}{2} \right) \vert 0 \rangle +   \cos \left(\frac{\theta}{2} \right)\vert 1 \rangle.
\end{align*}
$$

We can see that, again, that we're *close* to $RY(\theta) \vert 1\rangle$ but
have a negative sign on the $\sin$ term. However, recall that $- \sin
\left(\theta \right) = \sin(-\theta)$. We can simply absorb the negative sign
into the argument, meaning that we obtain the "backwards" rotation by $-\theta$:

$$
X RY(\theta) X = RY(-\theta). 
$$

Or, expressed as a circuit,

<img src="pics/x_ry_x_solution.svg" alt="" width="400px">

Whenever we see such a pattern of three gates in a circuit, we can perform
this small optimization to replace them by a single gate! You can show
that similar relationships exist among the other $RX, RY, RZ$ and $X, Y, Z$ too. ▢

</details>

---

***Exercise I.6.5.*** Show that $RX$,
   $RY$, and $RZ$ can be represented as follows:

$$
\begin{align*}
 RX(\theta) &= e^{-i\theta X/2}, \\
 RY(\theta) &= e^{-i\theta Y/2}, \\
 RZ(\theta) &= e^{-i\theta Z/2}.
\end{align*}
$$


(While this may look unusual, this representation is actually very important in
applications of quantum computing such as *Hamiltonian simulation*.)


<details>
  <summary><i>Hint.</i></summary>

Start by taking the [matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential), and
then consider what are some special properties of powers of $X, Y$, and $Z$.

</details>

<details>
  <summary><i>Solution.</i></summary>

 We show the case of $RX$; the other gates have similar proofs. We
 can exponentiate a matrix by expanding the exponential out as a series:

$$
\begin{align*}
e^{-i\theta X/2} &= I + \left(-i\frac{\theta}{2} X\right) + \frac{1}{2!}\left(-i \frac{\theta}{2} X\right)^2 + \frac{1}{3!}\left(-i \frac{\theta}{2} X\right)^3 + \frac{1}{4!}\left(-i \frac{\theta}{2} X\right)^4 + \cdots \\
&= I - i\frac{\theta}{2} X -\frac{1}{2} \left(\frac{\theta}{2}\right)^2 X^2 + \frac{1}{3!}i \left( \frac{\theta}{2}\right)^3 X^3+ \frac{1}{4!} \left(\frac{\theta}{2}\right)^4 X^4 + \cdots
\end{align*}
$$

However, consider what happens when we apply $X$ more than once - all it does is
flip the bit, so applying it twice brings us right back to where we started!
Therefore, all even powers in this expansion will reduce to $I$, and all odd ones
to $X$:

$$
\begin{align*}
&= \left(1 - \frac{1}{2}\left(\frac{\theta}{2}\right)^2 + \frac{1}{4!} \left(\frac{\theta}{2}\right)^4 - \cdots  \right)I - i\left(\left(\frac{\theta}{2}\right) - \frac{1}{3!}\left(\frac{\theta}{2}\right)^3 + \cdots \right) X .
\end{align*}
$$

These expressions in the parentheses are simply the expansions of cosine and
sine, so we can write this in closed form, and recover the matrix expression.

$$
\begin{align*}
&= \cos \left(\frac{\theta}{2} \right) I - i \sin \left(\frac{\theta}{2} \right) X \\
&= \cos \left(\frac{\theta}{2} \right) \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} -i  \sin \left(\frac{\theta}{2} \right)  \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \\
&= \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\ -i\sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)   \end{pmatrix}.
\end{align*}
$$

<div align="right"> ▢ </div>

</details>

---

