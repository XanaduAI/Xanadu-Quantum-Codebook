---

**Learning outcomes**

- *Describe and manipulate the geometry of Grover search.*

---

Our picture of shuffling amplitudes is hard to reason about. Luckily, there is a beautiful alternative representation which makes things clearer. Only two states have made an appearance so far: the solution $\vert \mathbf{s}\rangle$, and the uniform superposition $\vert\psi\rangle$.
We can simply focus on the two-dimensional space spanned by $\vert \mathbf{s}\rangle$ and $\vert \psi\rangle$, drawing them as below:

<img src="pics/grover-space.svg"  width="250px">

The states $\vert \psi\rangle$ and $\vert \mathbf{s}\rangle$ are not at right angles since they have some non-zero overlap. Our goal will be to start with the uniform superposition, and try to rotate our state towards the solution using the Grover operator discussed in the last node:

<img src="pics/rotate.svg"  width="250px">

First, let's visualize the effect of the oracle in this two-dimensional space. In the oracle $U_f = I - 2 \vert \mathbf{s}\rangle \langle \mathbf{s}\vert $, we can view the projector $\vert \mathbf{s}\rangle \langle \mathbf{s}\vert $ as identifying the part of the state which lies on the $\vert \mathbf{s}\rangle$ axis. The $-2$ then *flips* it:

<img src="pics/flip.svg"  width="300px">

The oracle by itself does not get us closer, in the sense that the oracle can *never* increase the overlap with the solution for any state $\vert \phi\rangle$, but merely changes the sign. We can prove this using the matrix representation of $U_f$:

$$
\langle \mathbf{s}\vert U_f \vert \phi\rangle = \langle \mathbf{s}\vert (I - 2 \vert \mathbf{s}\rangle \langle \mathbf{s}\vert ) \vert \phi\rangle = \langle \mathbf{s}\vert \phi\rangle - 2 \langle\mathbf{s}\vert \mathbf{s}\rangle\langle\mathbf{s}\vert \phi\rangle = -\langle \mathbf{s}\vert \phi\rangle.
$$

We need the diffusion operator $D = 2 \vert \psi\rangle \langle
\psi\vert  - I$ to get the ball rolling. You can see how it works
geometrically in the next exercise.

---

***Exercise G.2.1.*** Show that $D$ flips a vector representing the state $\vert\phi\rangle$ of the system *around* the axis of $\vert \psi\rangle$, represented by the purple arrow in the image below:

<img src="pics/flip-psi.svg"  width="300px">

<details>
<summary><i>Hint.</i></summary>
Use geometry! To start with, suppose the vector representing the state of the system $\vert\phi\rangle$ makes an angle $\pi/2 - \varphi$ to $\vert \psi\rangle$. You can assume that $-D = I - 2\vert \psi\rangle\langle\psi\vert $ reflects parallel to $\vert \psi\rangle$, and go from there.
</details>

<details>
<summary><i>Solution.</i></summary>

Applying $-D$ reflects across the dotted red line orthogonal to $\vert \psi\rangle$. This gives a total rotation by $2\varphi$, as shown below middle:

<img src="pics/flip-psi-sol.svg" width="700px">

We now apply $-I$, so that the total effect is $-D \cdot -I = D$. This reflects the vector to the other side of the circle. But it's easy to see that the angle from the $\vert \psi\rangle$ axis is now

$$
\pi - 2\varphi - \left(\frac{\pi}{2} - \varphi\right) = \frac{\pi}{2} - \varphi,
$$

so that the final vector is indeed flipped around the $\vert
\psi\rangle$ axis, i.e., makes the same angle as the initial vector
but on the other side. ▢

</details>

---

***Exercise G.2.2. (Bonus)*** If you prefer algebra, show that the overlap of the state of the system $\vert\phi\rangle$ with $\vert \psi\rangle$ is unchanged after applying $D$, but reflected in the orthogonal subspace.

<details>
<summary><i>Solution.</i></summary>

Algebraically, let's write our arbitrary state $\vert \phi\rangle = \alpha \vert \psi\rangle + \beta \vert \phi_\perp\rangle$, where $\vert \phi_\perp\rangle$ is the projection onto the subspace orthogonal to $\vert \psi\rangle$. Then

$$
D\vert \phi\rangle = \alpha (2 \vert \psi\rangle\langle \psi\vert  - I)\vert \psi\rangle + \beta (2 \vert \psi\rangle\langle \psi\vert  - I)\vert \phi_\perp\rangle = \alpha \vert \psi\rangle - \beta \vert \phi_\perp\rangle.
$$

Hence, $\langle\psi\vert D\vert \phi\rangle = \alpha = \langle\psi\vert \phi\rangle$, while $\langle\phi_\perp\vert D\vert \phi\rangle = -\beta = -\langle\phi_\perp\vert \phi\rangle$. So the overlap is unchanged, and state is reflected in the orthogonal subspace, as required. ▢

</details>

---

Let's draw a picture of what happens when we iterate $U_f$ and $D$ together a number of times:

<img src="pics/zigzag.svg"  width="300px">

Applying $DU_f$ performs a single "zigzag" on our circle. If we do this the right number of times, it will get us close to $\vert \mathbf{s}\rangle$! But if we continue zigzagging, we will overshoot the solution and end up on the other side of the circle:

<img src="pics/overshoot.svg"  width="300px">

In the next node, we will discuss how to implement the zigzag as a circuit on a quantum computer:

<img src="pics/grover-iter.svg" width="300px">

Clearly, there is some optimal number of times to zigzag before we overshoot the solution. From our sloppy amplitude shuffling argument in the last node, we correctly guessed that it scales as $\sqrt{N}$. With our newfound geometric representation of Grover search, we will be able to verify this!
