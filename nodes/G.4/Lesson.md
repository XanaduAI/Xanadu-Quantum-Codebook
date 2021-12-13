---

**Learning outcomes**

- *Understand the exact geometry of a Grover step.*
- *Compute the scaling of the optimal number of Grover steps for a single solution.*

---

Let's analyze Grover search more formally. Imagine we have a list of $N = 2^n$ items labelled by distinct bit strings $\mathbf{x} \in \{0,1\}^n$, and a single marked item $\mathbf{s}$ (for instance, the correct combination for the lock). A brute force classical search will take $O(N)$ steps, since if we move randomly through the list, we will need to look at half the combinations on average. To see how Grover search performs in comparison, we'll need to think about the geometry of the Grover step and compute the optimal number of iterations.

Our initial state $\vert \psi\rangle$ will be the uniform superposition over all $\mathbf{x} \in \{0,1\}^n$. This is completely symmetric between the different bit strings, which is appropriate if we know nothing about the marked item. Because it is uniform, the probability of observing any given string $\mathbf{s}$ is $1/N$, and hence the amplitude is $1/\sqrt{N}$, where we choose $\vert \psi\rangle$ so that the phase is positive. From the inner product between $\vert \psi\rangle$ and $\vert\mathbf{s}\rangle$, we can compute the angle $\alpha$ between them:

$$
\cos\alpha = \langle\mathbf{s}\vert \psi\rangle = \frac{1}{\sqrt{N}}.
$$

We'll actually find the complementary angle $\theta = \pi/2 - \alpha$ more useful, so let's include this in our picture:

<img src="pics/angle.svg" width="300px">

Recall that the oracle operator $U_f$ has the effect of reflecting the state parallel to $\vert \mathbf{s}\rangle$. The first time we apply this, it flips us across the horizontal axis. We can also view this as a clockwise rotation of $2\theta$.

<img src="pics/flip-angle.svg" width="300px">

Next, we apply the diffusion operator, which flips around the state $\vert \psi\rangle$. The has the effect of a counter-clockwise (ccw) rotation by $4\theta$:

<img src="pics/psi-angle.svg" width="300px">

Thus, the total effect is a ccw rotation by $2\theta$:

<img src="pics/grover-angle.svg" width="300px">

In fact, you can check that *each* application of the *Grover operator* $G = DU_f$ rotates ccw by $2\theta$.

---

***Exercise G.4.1.*** Consider the space spanned by $\vert
   \mathbf{s}\rangle$ and $\vert \psi\rangle$.
   If the coefficients are real, let us define the vector space

$$
V = \{\alpha \vert \mathbf{s}\rangle + \beta \vert
\psi\rangle: \alpha, \beta \in \mathbb{R} \},
$$

where the angle $\vartheta$ between two vectors $\vert u\rangle, \vert
v\rangle \in V$ is given by
   
   $$
   \cos\vartheta = \langle u \vert v\rangle.
   $$

(a) Let $U$ be a unitary acting on the space $V$. Argue that it does
not change the angle between any two vectors.

(b) The only transformations of the plane which leave relative angles
unchanged between vectors are rotations by some fixed angle around a
point, and reflections. Explain why the Grover operator $G = DU_f$
is a rotation around the origin.

(c) Finally, argue that the Grover operator rotates all vectors in the
space ccw by $2\theta$.

<details>
<summary><i>Hint.</i></summary>
You can assume that a unitary acting on this two-dimensional space
acts as a rotation by some angle (possibly followed by a reflection)
around the origin, and rotates every vector by the same amount.
From considering the initial Grover step, what is this angle?
</details>

<details>
<summary><i>Solution.</i> (a)</summary>
Acting on $\vert u\rangle$ and $\vert v\rangle$ with unitaries, we
find the inner product is unchanged,

$$
(U \vert u\rangle)^\dagger \vert U v\rangle = \langle u\vert U^\dagger U
\vert v\rangle = \langle u \vert v\rangle,
$$

since $U^\dagger U = I$ from the definition of unitary. It follows
that the angle is unchanged.
</details>

<details>
<summary>(b)</summary>
We know that both the oracle $U_f$ and diffusion operator $D$ are
<i>reflections</i> in this two-dimensional space. If we perform two
reflections, we go to the mirror image, and then back to the original un-mirrored
image, so the end result is a rotation by some angle. Since states are
vectors of unit length, and unitary operators must preserve this
length, it is a rotation around the origin.
</details>

<details>
<summary>(c)</summary>
From its effect on the initial vector, we learn it must
rotate <i>every</i> vector by the same amount, i.e., ccw by $2\theta$. ▢
</details>

---

We can now determine the optimal number of iterations for Grover search. We'll give a rough estimate, taking $N = 2^n \gg 1$ to be large, and finesse this in the exercises. The initial angle between the state $\vert \psi\rangle$ and our target element $\vert \mathbf{s}\rangle$ is $\alpha$, where

$$
\begin{align*}
\cos \alpha & = \frac{1}{\sqrt{N}} \\
& = \cos \left(\frac{\pi}{2} - \theta\right) \\
& = \sin\theta
\end{align*}
$$

For large $N$, the small angle approximation gives

$$
\theta \approx \frac{1}{\sqrt{N}}.
$$

For each Grover step, we rotate by $2\theta$. Thus, the optimal number of Grover iterations is roughly

$$
\begin{align*}
S & = \frac{\alpha}{2\theta} \\
& = \frac{\tfrac{\pi}{2} - \theta}{2\theta} \\
& \approx \frac{\tfrac{\pi}{2} - N^{-1/2}}{2N^{-1/2}} \\
& \approx \frac{\pi}{4} \sqrt{N}.
\end{align*}
$$

In the next exercise, you can check this scaling a little more carefully.

---

***Exercise G.4.2.*** We've argued that a Grover iteration rotates the
   state in the two-dimensional space by $2\theta$, and it starts an
   angle $\alpha = \pi/2 - \theta$ away.

(a) Using this result, argue that after $k$ iterations, the overlap with the solution is

$$
\langle \mathbf{s} \vert  G^k \vert \psi\rangle = \sin[(2k+1)\theta].
$$

(b) Treating $k$ as a *continuous* parameter, where does the first maximum of probability occur, in terms of $\theta$? Show that for $N \gg 1$, this is consistent with our argument above.

<details>
<summary><i>Solution.</i></summary>

(a) After $k$ iterations, the angle between the state and the solution is

$$
\frac{\pi}{2} - \theta - 2k\theta = \frac{\pi}{2} - (2k+1)\theta.
$$

From the geometry, the overlap is then

$$
\cos\left[\frac{\pi}{2} - (2k+1)\theta\right] = \sin[(2k+1)\theta].
$$

(b) Since $\sin$ is real and initially positive, we can simply maximize the amplitude $g(k) = \sin[(2k+1)\theta]$ in order to maximize the probability. The first maximum occurs when the argument equals $\pi/2$, so

$$
\begin{align*}
\frac{\pi}{2} & = (2k+1)\theta \\ \Longrightarrow \quad k & = \frac{\pi}{4\theta} - \frac{1}{2}.
\end{align*}
$$

When $N \gg 1$, we have $\theta \approx 1/\sqrt{N}$, so probability is maximized for

$$
\begin{align*}
k & \approx \frac{\pi}{4}\sqrt{N} - \frac{1}{2} \\ & \approx \frac{\pi}{4}\sqrt{N},
\end{align*}
$$

as above. ▢

</details>

---

Let's pause and reflect on the square-root scaling. This is a huge deal! We said above that the best classical algorithm for searching an unstructured list runs in $O(N)$ time. Here, we have *quadratic improvement*. It's not exponential, but it can still have huge practical implications, since searching is a ubiquitous task.

<img src="pics/biglock.svg">

For example, looking up websites, accessing data on our computers, and breaking locks all involve searching through a list of candidate items.

---

***Exercise G.4.3.*** In module **A** we calculated that a classical
   supercomputer, performing $10^{16}$ operations per second, takes
   around $4$ millions years to crack a $100$-bit lock. How long does
   it take a "quantum supercomputer", implementing gates at the same
   speed? We're assuming that each Grover iteration is one step, and
   rather than the elementary gates we would deconstruct a Grover step
   into in a real circuit.

<details>
<summary><i>Solution.</i></summary>

Now $N = 2^{100}$. Since Grover search requires around $\sqrt{N} = 2^{50}$ iterations, the time our quantum supercomputer requires is

$$
\frac{2^{50}}{10^{16}} \text{ s} \approx 0.1 \text{ s}.
$$

Our hypothetical quantum computer would take less than a second! ▢

</details>

---
