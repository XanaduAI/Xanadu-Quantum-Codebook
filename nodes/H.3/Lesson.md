---

**Learning outcomes**

- *Define a Hamiltonian and explain what it means with respect to a quantum system.*
- *Compute unitary evolution for a simple, single-qubit physical system.*

---

The unitary operators $U$ don't appear out of nowhere, but arise in a
principled way from physical properties of a quantum system. As a
concrete example, let's consider magnets. These have a north and a
south pole.
The magnet points in a direction (from south to north pole) which we
will call $\mathbf{S}$:

<img src="pics/magnet.svg" width="200px">

This is a vector in $3$-dimensional space.
We're used to big magnets, like the bar magnets you might have played
around with in high school, but most subatomic particles, e.g.,
electrons, are also magnets!
In this case, $\mathbf{S}$ gets the special name of **spin vector**
(since we can explain the magnetic behaviour by pretending that the
particle spins).

Interestingly, electrons can also be described as qubits $\alpha\vert
0\rangle + \beta\vert 1\rangle$.
The spin vector, telling us which way the little electron magnet
points, is related in a simple way to Pauli operators:

$$
\mathbf{S} = (S_x, S_y, S_z) \propto (\langle X\rangle, \langle Y\rangle, \langle Z\rangle).
$$

Now that we have this connection between magnets and qubits, we can do
some physics.
If we put a little magnet in the vicinity of a much bigger magnet
(one from your fridge for instance), it will want to align itself with
the big field:

<img src="pics/field.svg" width="450px">

Why do little magnets like to align with the big magnets? For the same reason that balls roll downhill, namely, that it *reduces potential energy*. If we imagine the potential energy of the little bar magnet as an undulating energy landscape, valleys are where it aligns with the big magnetic field, and hills where it *anti-aligns*, i.e. points in the opposite direction:

<img src="pics/potential.svg" width="420px">

(For historical reasons, the magnetic field is called $B$.) So, we
expect that if we place an electron in the field of a big magnet, it
will try to align itself somehow. Thus, the unitary $U$ associated to
time evolution should somehow be connected to the *energy* of the
electron considered as a little magnet. For simplicity, let's imagine
that the magnetic field $B$ points in the $Z$ direction:

<img src="pics/magnets.svg" width="200px">

The classical potential energy for the electron is

$$
E = -\frac{e B}{m_e}S_z, \tag{1} \label{magnet}
$$

where $e$ is the electron charge, $m_e$ is its mass, and $S_z$ is the
$z$-component of the spin vector. We picture this below:

<img src="pics/Sz.svg" width="150px">

The energy is smallest (a valley)
when $S_z$ is largest, which corresponds to the spin lining up with
the field in the positive $z$ direction. Similarly, the energy is
largest (a hill) when $S_z$ is smallest, and the spin anti-aligns with
the field, in the negative $z$ direction.

<img src="pics/Sz-hill.svg" width="420px">

So far, all of this is classical. In quantum mechanics, energy is not
a number but a *measurement*, e.g., the Pauli $X$, $Y$ and $Z$ gates,
or any other Hermitian operator. The observable which measures energy
is called the **Hamiltonian** $\hat{H}$, with a hat to distinguish it
from the Hadamard gate, and it plays a central role in the black boxes
of quantum physics.

Our first task is to turn the expression
(\ref{magnet}) into an observable. This turns out to be easy. The
length of the spin vector $\mathbf{S}$ is just how much **spin** the
electron carries. This turns out to be $\hbar/2$, where $\hbar \approx
10^{-34} \text{ J} \cdot\text{s}$ is *Planck's (reduced)
constant*. (You can learn more about "quantization" of spin in a
course on quantum mechanics.) We still need an operator, and the fact
that this is the $z$ component of the spin gives us a clue to
associate it with the Pauli $Z$:

$$
S_z \mapsto \frac{\hbar}{2}Z.
$$

So, the resulting Hamiltonian is

$$
\hat{H} = -\frac{e \hbar B}{2m_e} Z = -\alpha \hbar Z, \tag{2} \label{magham-Z}
$$

where $\alpha - Be/2m_e$. Our physical picture of the electron is
simply related to the measurement outcomes for $Z$:

<img src="pics/align.svg" width="350px">

There's nothing mysterious about this operator. If we had a circuit
which prepared an electron in some state, then put it in the magnetic
field, we would simply make a $Z$ measurement and multiply by $-e\hbar
B/2m_e:$

<img src="pics/ham-z.svg" width="500px">

Now we have a Hamiltonian, let's return to the problem of how our
electron bar magnet changes with time. We know that, for a time $t$,
there is some unitary operator $U$ that realizes the time-evolution
for the state of the electron, $\vert \psi(t)\rangle = U(t)\vert
\psi(0)\rangle$, where $\vert \psi(0)\rangle$ is the initial
state. What is the unitary $U(t)$? This question was answered in
general by Erwin Schrödinger in 1926, so it is called **Schrödinger's
equation**:

$$
U(t) = e^{-it\hat{H}/\hbar}. \tag{3} \label{schro}
$$

In our case,

$$
U(t) = e^{i\alpha t Z} = R_z(-2\alpha t).
$$

This is just a $Z$ rotation! Once again, we've already seen this in
the context of quantum computing. We can implement the time evolution
of an electron state $\vert \psi\rangle$ as a circuit:

<img src="pics/expz.svg" width="350px">

Let's see what this does to our electron in the simple case where the
qubit starts in state $\vert 0\rangle$. This is aligned with
the field in the $z$ direction, a claim we can check by evaluating the
vector $(\langle X\rangle, \langle Y\rangle, \langle Z\rangle)$:

$$
\langle Z\rangle = \langle 0\vert Z\vert 0\rangle = \langle 0\vert 0\rangle = 1, \quad \langle 0\vert X\vert 0\rangle = \langle 0\vert 1\rangle = 0, \quad \langle 0\vert Y\vert 0\rangle = -i\langle 0\vert 1\rangle = 0.
$$

(We shouldn't be surprised that $\vert 0\rangle$ is associated with
the positive $z$ direction, because it's an eigenvector of the $Z$
operator with positive eigenvalue; we will see a more general
relationship between spins and eigenvectors below.) But the effect of
$U(t)$ on this state is kind of boring! We can expand $e^{i\alpha t
Z}$ as a Taylor series in $Z$, by analogy with the Taylor series for
the ordinary exponential:

$$
e^{i\alpha t Z} = I + i\alpha t Z + \frac{(i\alpha t)^2}{2!} Z^2 + \cdots = \sum_{k=0}^\infty \frac{(i\alpha t)^k}{k!}Z^k.
$$

Acting on $\vert 0\rangle$ with any number of powers of $Z$ just gives us $\vert 0\rangle$ back, so

$$
e^{i\alpha tZ}\vert 0\rangle = \sum_{k=0}^\infty \frac{(i\alpha t)^k}{k!}Z^k\vert 0\rangle = \sum_{k=0}^\infty \frac{(i\alpha t)^k}{k!}\vert 0\rangle = e^{i\alpha t}\vert 0\rangle.
$$

All we get is a phase! Making the time-dependence a bit more explicit, if $\vert \psi (0)\rangle = \vert 0\rangle$, then $\vert \psi(t)\rangle = e^{iBet/2m_e}\vert 0\rangle$.

---

***Exercise H.3.1.*** Show that $e^{i\alpha t Z}\vert 1\rangle = e^{-i\alpha t}\vert 1\rangle$.

<details>
<summary><i>Solution.</i></summary>

Now we use $Z^k\vert 1\rangle = (-1)^k\vert 1\rangle$:

$$
e^{i\alpha tZ}\vert 1\rangle = \sum_{k=0}^\infty \frac{(i\alpha t)^k}{k!}Z^k\vert 1\rangle = \sum_{k=0}^\infty \frac{(-i\alpha t)^k}{k!}\vert 1\rangle = e^{-i\alpha t}\vert 1\rangle.
$$

This is also a phase, but rotating in the opposite direction. ▢

</details>

---

Let's try a more interesting case, where instead of starting in an
eigenstate of the $Z$ operator, we start in state $\vert
\psi(0)\rangle = \vert +\rangle$. As before, we will evaluate the
expectations $(\langle X\rangle, \langle Y\rangle, \langle Z\rangle)$
to see where the spin is pointing.
It's easy to verify that the initial state corresponds to a spin
pointing in the positive $x$ direction, since $\langle X\rangle = 1$
and $\langle Y\rangle=\langle Z\rangle = 0$.
To see how it changes with time, let's write out the $Z$ rotation more explicitly:

$$
U = e^{i\alpha tZ}  = \cos(\alpha t) \cdot I + i \sin (\alpha t) \cdot Z.  \tag{4} \label{expZ}
$$

Hence, the state of the qubit is

$$
\vert \psi\rangle = U\vert +\rangle = \left[\cos(\alpha t) \cdot I + i \sin(\alpha t) \cdot Z\right]\vert +\rangle = \cos(\alpha t) \vert +\rangle + i \sin(\alpha t) \vert -\rangle \tag{5} \label{gyro}
$$

since $Z\vert +\rangle = \vert -\rangle$. This corresponds to a spin pointing in the direction 

$$
(\langle X\rangle, \langle Y\rangle, \langle Z\rangle) = (\cos(2\alpha t), \sin(2\alpha t), 0).
$$

The tiny bar magnet is just spinning around in the $xy$-plane! Let's check the $x$ component, for instance. Using the fact that $X\vert \pm\rangle = \pm \vert \pm\rangle$, we find that

$$
\begin{align*}
\langle \psi \vert X \vert \psi\rangle & = \left(\cos(\alpha t) \langle +\vert  - i \sin(\alpha t) \langle-\vert \right) X \left(\cos(\alpha t) \vert +\rangle + i \sin(\alpha t) \vert -\rangle\right) \\
& = \left(\cos(\alpha t) \langle +\vert  - i \sin(\alpha t) \langle -\vert \right) \left(\cos(\alpha t) \vert +\rangle - i \sin(\alpha t) \vert -\rangle\right) \\
& = \cos^2(\alpha t) \langle +\vert +\rangle - \sin^2(\alpha t) \langle -\vert -\rangle + i \cos(\alpha t)\sin(\alpha t)  (\langle-\vert +\rangle - \langle +\vert -\rangle) \\ & = \cos^2(\alpha t) - \sin^2(\alpha t) = \cos(2\alpha t).
\end{align*}
$$

Similar manipulations show $\langle Y\rangle = \sin(2\alpha t)$ and
$\langle Z\rangle =0$, with the angle changing at a rate $2\alpha$. A
stronger field won't align the spin any better, but it will rotate the
spin vector faster! This is called *Larmor precession*:

<img src="pics/precess.svg" width="500px">

In general, the spin vector $\mathbf{S}$ of the electron will simply rotate around the $z$-axis with angular velocity $Be/m_e$, as you can check in the next exercise. It may seem odd that the magnetic field doesn't push the spin into alignment, but it turns out that in quantum as in classical physics, a *uniform* magnetic field cannot cause tiny magnets to align. Iron filings only arrange themselves along field lines because the strength of the field at the top and bottom of the filing is different!

---

***Exercise H.3.2.*** Suppose that $\vert \psi(0)\rangle$ has expectations

$$
(\langle X\rangle_0, \langle Y\rangle_0,\langle Z\rangle_0) = (x, y, z).
$$

Show that $\vert \psi(t)\rangle = U(t)\vert \psi(0)\rangle$ has expectations

$$
(\langle X\rangle_t, \langle Y\rangle_t,\langle Z\rangle_t) = (\cos(2\alpha t) x - \sin(2\alpha t) y, \sin(2\alpha t) x + \cos(2\alpha t) y, z),
$$

where for an operator $\mathcal{O}$, $\langle\mathcal{O}\rangle_t =
\langle\psi(t)\vert \mathcal{O}\vert \psi(t)\rangle$. This means a
qubit starting in any state will simply precess clockwise around the
$z$-axis with angular rate of change $2\alpha$.

<details>
<summary><i>Solution.</i></summary>

We'll do $\langle X\rangle_t$ and leave the rest to the diligent
reader. We will need to take the adjoint of $U(t)$ in order to apply
it to the bra version of the state we use in the expectations. Making
use of (\ref{expZ}) and the identity

$$
U(t)^\dagger = \left(\cos(\alpha t) \cdot I + i \sin (\alpha t) \cdot Z\right)^\dagger = \cos(\alpha t) \cdot I - i \sin (\alpha t) \cdot Z,
$$

we obtain after some algebra

$$
\begin{align*}
\langle X\rangle_t & = \langle \psi(t)\vert  X \vert \psi(t)\rangle \\
& = \langle \psi(0)\vert U(t)^\dagger X U(t) \vert \psi(0)\rangle \\
& = \langle \psi(0)\vert  (\cos(\alpha t) \cdot I - i \sin (\alpha t) \cdot Z)X (\cos(\alpha t) \cdot I + i \sin(\alpha t) \cdot Z) \vert \psi(0) \\
& = \cos^2(\alpha t) \langle X\rangle_0 + i\cos(\alpha t)\sin(\alpha t) (\langle XZ\rangle_0 - \langle ZX\rangle_0) + \sin^2(\alpha t) \langle ZXZ\rangle_0.
\end{align*}
$$

From the algebra of Pauli matrices, $ZX = -XZ = iY$ and $ZXZ = iYZ = -X$, and hence

$$
\langle X\rangle_t = \big(\cos^2(\alpha t) - \sin^2(\alpha t)\big)\langle X_0\rangle - 2\cos(\alpha t)\sin(\alpha t) \langle Y \rangle_0 = \cos(2\alpha t) x - \sin(2\alpha t) y.
$$

This is what we wanted! The other components are similar. ▢

</details>

---

We now have a nice simple example where the unitary evolution is
connected to the physics. Time to consider something more interesting!
