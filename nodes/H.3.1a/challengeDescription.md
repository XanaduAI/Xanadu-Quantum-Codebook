We want to understand how physical, and in particular quantum, systems
evolve with time, and we also know that the "black box" behaviour of
quantum systems is constrained to be unitary.
But we can look inside the black box and see where these unitaries
come from!
This is necessary if we want to *simulate* the system based on its
physics.

More specifically, the unitaries $U$ evolving a quantum system arise
from a special operator $\hat{H}$ called the **Hamiltonian**, which
measures the system's energy. According to **Schrödinger's equation**,
for a system with Hamiltonian $\hat{H}$, the corresponding unitary
evolving it for a time $t$ is

$$
U = e^{-it\hat{H}/\hbar}, \tag{1} \label{schro}
$$

where $\hbar \approx 10^{-34} \text{ J} \cdot\text{s}$ is Planck's
(reduced) constant.
A simple example comes from a single qubit, which physically
corresponds to a tiny magnet whose axis points in direction $\mathbf{S}$:

<img src="pics/magnet.svg" width="200px">

If we place this tiny magnet in a big external magnetic field $B$
pointing in the $z$ direction, the little magnet likes to align with
the big field:

<img src="pics/magnets.svg" width="200px">

When we say the little magnet "likes to align", what we really mean is
the energy of the system is lower when the little magnet is aligned.
This is captured by the Hamiltonian

$$
\hat{H} = -\frac{\hbar eB}{2m_e} Z = \alpha \hbar Z, \tag{2} \label{ham-z}
$$

where $Z$ is the Pauli $Z$, $e = 1.6 \times 10^{-19}$ C is the charge
of the electron, and $m_e = 9.1 \times 10^{-31}$ kg its mass.
We've lumped some of the constants into $\alpha = eB/2m_e$ for
convenience.
The $Z$ operator has eigenvalue $+1$ when the magnet is aligned, and
$-1$ when anti-aligned, so the energy is indeed lower in the first
case:

<img src="pics/align.svg" width="350px">

To get the unitary according to
(\ref{schro}), we must exponentiate (\ref{ham-z}), which is simply a
$Z$ rotation:

$$
\begin{align*}
e^{-it\hat{H}/\hbar} & = e^{i\alpha t Z} \\
& = \cos(\alpha t) \cdot I + i
\sin(\alpha t) \cdot Z \tag{3} \label{ham} \\
& =
\begin{bmatrix}
\cos(\alpha t) - i \sin (\alpha t) & \\
& \cos(\alpha t) + i \sin (\alpha t)
\end{bmatrix}.
\end{align*}
$$

---

***Codercise H.3.1.*** (a) Complete the code to build the unitary
   (\ref{ham}). We can verify the output is unitary using
   ``unitary_check``.
