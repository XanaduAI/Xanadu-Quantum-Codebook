---

**Learning outcomes**:

 - *Define what it means for a gate set to be universal for quantum computing.*
 - *State two universal gate sets for single-qubit quantum computation.*

---

Recall that the most general expression of a single-qubit unitary matrix looks like this:

$$
U(\phi, \theta, \omega) = \begin{pmatrix} e^{-i(\phi + \omega)/2} \cos(\theta/2) & -e^{i(\phi - \omega)/2} \sin(\theta/2) \\ e^{-i(\phi - \omega)/2} \sin(\theta/2) & e^{i(\phi + \omega)/2} \cos(\theta/2)  \end{pmatrix}. \tag{1}
$$

It's possible to find a set of angles $\phi, \theta, \omega$ for all the
gates we encountered in previous nodes, such that $U(\phi, \theta, \omega)$
is equivalent to the gate up to a global phase. However, $U$ can actually
be expressed in a simpler way.

---

***Exercise I.7.1.*** Prove that 

$$
U(\phi, \theta, \omega) = \begin{pmatrix} e^{-i(\phi + \omega)/2} \cos(\theta/2) & -e^{i(\phi - \omega)/2} \sin(\theta/2) \\ e^{-i(\phi - \omega)/2} \sin(\theta/2) & e^{i(\phi + \omega)/2} \cos(\theta/2)  \end{pmatrix}.
$$

can be expressed using only 3 gates from the set $\{RZ, RY\}$.

<details>
  <summary><i>Hint.</i></summary>

Recall that their matrix forms are 

$$
RY(\theta) = \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & - \sin \left(\frac{\theta}{2} \right) \\ \sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)   \end{pmatrix}, \quad 
RZ(\theta) = \begin{pmatrix} e^{-i \frac{\theta}{2}} & 0 \\ 0 & e^{i \frac{\theta}{2}}. \end{pmatrix}
$$

</details>

<details>
  <summary><i>Solution.</i></summary>

First, knowing that we need 3 $RZ$ and $RY$ operations, consider how they can be
combined. If we put two $RZ$ next to each other, that would be equivalent to applying
an $RZ$ with the sum of the angles (the same goes for $RY$). Thus, if we are using only
3 gates, they must alternate, so our options are $RZ$, $RY$, $RZ$, or $RY$, $RZ$, $RY$.

Looking at the form of the matrix representation above, we see that the portion of
the matrix that depends on $\theta$ looks exactly like a $Y$ rotation. Furthermore, the
phase in the exponential contains two of the angles. This suggests that we need $RY(\theta)$,
and then $RZ(\omega)$ and $RZ(\phi)$. Indeed, if you work through the matrix multiplication,
you will find that

$$
U(\phi, \theta, \omega) = RZ(\omega) RY(\theta) RZ(\phi)
$$

as desired. ▢

</details>

---


***Exercise I.7.2.*** Prove that 

$$
U(\phi, \theta, \omega) = \begin{pmatrix} e^{-i(\phi + \omega)/2} \cos(\theta/2) & -e^{i(\phi - \omega)/2} \sin(\theta/2) \\ e^{-i(\phi - \omega)/2} \sin(\theta/2) & e^{i(\phi + \omega)/2} \cos(\theta/2)  \end{pmatrix}.
$$

can be expressed using only 3 gates from the set $\{RZ, RX\}$.


<details>
  <summary><i>Hint.</i></summary>

You already know how to express this in terms of $RZ$ and $RY$, so the
question is whether we can turn the $RY$ into $RZ$ and $RX$. There is a
convenient circuit identity that relates $Y$ and $X$: $Y = -SXS^\dagger$. Use this
as starting point for expressing $RY(\theta) = e^{-i\frac{\theta}{2}Y}$ in terms
of $RX$ and $RZ$. 

</details>

<details>
  <summary><i>Solution.</i></summary>

Let's take advantage of the hint. If $Y = -S X S^\dagger$, then

$$
\begin{align*}
RY(\theta) &= e^{-i\frac{\theta}{2}Y} \\
 &= \cos \frac{\theta}{2} I - i \sin \frac{\theta}{2} Y \\
 &= \cos \frac{\theta}{2} I + i \sin \frac{\theta}{2} SXS^\dagger \\
 &= S \left( \cos \frac{\theta}{2} I + i \sin \frac{\theta}{2} X \right) S^\dagger \\
 &= S RX(-\theta) S^\dagger.
\end{align*}
$$

Now, since $S = RZ(\frac{\pi}{2})$, we can recover $U$ by writing

$$
\begin{align*}
U(\phi, \theta, \omega) &= RZ(\omega) RY(\theta) RZ(\phi) \\
&= RZ(\omega)  RZ\left(\frac{\pi}{2} \right) RX(-\theta)  RZ\left(-\frac{\pi}{2}\right) RZ(\phi) \\
&= RZ\left(\omega + \frac{\pi}{2}\right) RX(-\theta) RZ\left(\phi - \frac{\pi}{2}\right).
\end{align*}
$$

<div align="right"> ▢ </div>


*Tip*. If you have experience with 3D computer graphics, or flying planes, you
 might notice that there are a lot of similarities here to Euler angle
 decompositions for rotations in 3-dimensional space. There are 12 different
 ways to decompose an arbitrary single-qubit operation into a sequence of 3 $RX,
 RY, RZ$ gates; a combination of $RZ$ and $RY$ is the most commonly encountered.

</details>

---

These two exercises have led us to something very interesting: with just two
types of rotations, we can implement *any* single-qubit unitary operation! This
is great news, especially in terms of building actual quantum hardware: the
hardware only needs to be able to do these two things well, rather than having
to implement a large set of gates.

This idea has a name: any two rotations of $\{RX, RY, RZ\}$ gates are a
**universal gate set** for single-qubit operations. A gate set is universal if
combinations of the gates therein can be used to approximate any unitary matrix
up to arbitrary precision. More formally, for *any* $U$, we can find $V$
composed only of gates from the universal set such that

$$
|| U - V || \leq \epsilon \tag{2}
$$

for $\epsilon$ arbitrarily small. Finding the sequence of gates that make up $V$
is called **quantum circuit synthesis**.


In the case of $RX$ and $RZ$, or $RZ$ and $RY$, the precision can be taken for
granted, since we can rotate by arbitrary angles. However, there are also
universal gate sets that do not contain any parametrized rotations: a
particularly famous one is the set $\{H, T\}$. For *any* single-qubit operation,
you can approximate it up to arbitrary precision with just $H$ and $T$. That
sequence of $H$ and $T$ might be absolutely enormous, should you want to obtain
a particularly precise approximation, but it can always be found (and for the
single-qubit case, can be found quite efficiently).