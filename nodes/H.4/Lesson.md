---

**Learning outcomes**

- *Describe the utility of diagonalizing a Hamiltonian for simulation, and diagonalize a simple case.*
- *See how nontrivial computational problems can be encoded in ground states.*

---

You might wonder if understanding the physics of a Hamiltonian will
give us some shortcuts for simulating the corresponding system. This
turns out to be true! We can generalize the observation that $Z$, when
exponentiated, acts simply on eigenvectors of $Z$, for instance,

$$
e^{i\alpha t Z} \vert 0\rangle = e^{i\alpha t} \vert 0\rangle,
$$

We can perform the same trick with any Hamiltonian!
Recall that the Hamiltonian $\hat{H}$ measures energy. It is an
observable, and it has some associated eigenvectors $\vert E\rangle$
with eigenvalues $E$:

$$
\hat{H}\vert E \rangle = E\vert E \rangle.
$$

These are called the **energy eigenstates** of the system, and $E$ the **energy levels**. In the basis $(\vert E_1 \rangle, \vert E_2 \rangle, \ldots, \vert E_N \rangle)$ comprised of $N$ eigenstates, the Hamiltonian takes a particularly simple diagonal form:

$$
\hat{H} =
\begin{bmatrix}
E_1 & & & \\
 &E_2 & & \\
 & & \ddots & \\
  & & & E_N
\end{bmatrix}.
$$

To evolve the system for a time $t$ in this basis, we exponentiate as usual. But the exponential of a diagonal matrix is simply the exponential of the diagonal entries, as we can immediately show from the Taylor series:

$$
\begin{align*}
e^{-it\hat{H}/\hbar} & = \sum_{k=0}^\infty \frac{(-it/\hbar)^k}{k!}\hat{H}^k \\
& = \sum_{k=0}^\infty \frac{(-it/\hbar)^k}{k!}\begin{bmatrix}
E_1^k & & & \\
 &E_2^k & & \\
 & & \ddots & \\
  & & & E_N^k
\end{bmatrix} \\
& =  \begin{bmatrix}
\sum_{k=0}^\infty\frac{(-it/\hbar)^k}{k!}E_1^k & & & \\
 & \sum_{k=0}^\infty\frac{(-it/\hbar)^k}{k!}E_2^k & & \\
 & & \ddots & \\
  & & &\sum_{k=0}^\infty\frac{(-it/\hbar)^k}{k!} E_N^k
\end{bmatrix} \\
& = \begin{bmatrix}
e^{-itE_1/\hbar} & & & \\
 &e^{-itE_2/\hbar} & & \\
 & & \ddots & \\
  & & & e^{-itE_N/\hbar}
\end{bmatrix}.
\end{align*}
$$

So, it seems like all we need to do is figure out the energy levels and associated eigenstates, and simulation becomes trivial! And you probably learned how to find eigenvalues in your linear algebra class, so it seems like a straightforward problem. As a simple example, suppose our Hamiltonian is a simple coupling

$$
\hat{H} = \alpha Z \otimes Z.
$$

Our goal is to find the eigenvectors and eigenvalues. Since $Z|x\rangle = (-1)^x |x\rangle$, it follows that there are four eigenvectors, $\vert x y\rangle$ for $x, y \in \{0, 1\}$, with associated eigenvalues $(-1)^{x+y}$, since

$$
(Z \otimes Z) \vert x y \rangle = (-1)^{x+y}\vert x y \rangle.
$$

Time evolution just puts these eigenvalues in the exponential:

$$
U(t) \vert xy \rangle = \exp\left[-\frac{i\alpha t}{\hbar} (-1)^{x+y}\right]\vert xy \rangle. \tag{1} \label{diag-zz}
$$

Since we know the eigenvalues and eigenstates, it should be easy to
simulate right? Well, here we run into our first snag: we are trying
to do this on a quantum computer! We have a limited palette of gates
available to implement (\ref{diag-zz}). In this case it turns out to
be doable, since we can "mock up" the right eigenvalue $(-1)^{x+y}$ by
acting with a $Z$ rotation on a *single qubit* state $\vert x + y\rangle$.
More precisely,

$$
e^{-(i\alpha t/\hbar) Z}\vert x + y\rangle = \exp\left[-\frac{i\alpha t}{\hbar} (-1)^{x+y}\right]\vert x + y\rangle.
$$

We now need to think about how to produce the single-qubit state $\vert x +
y\rangle$ starting with the two-qubit state $\vert xy\rangle$.
This turns out to be straightforward: we simply apply the CNOT gate to
$\vert x y\rangle$, since

$$
\text{CNOT} \vert xy\rangle = \vert x\rangle \otimes \vert x + y\rangle,
$$

so the state we want lives on the second qubit.
We perform a $Z$ rotation on this qubit, and restore our original
state $\vert xy\rangle$ using another CNOT. As a circuit:

<img src="pics/diag-zz-2.svg" width="350px">

where $\theta = 2\alpha t/\hbar$.

---

***Exercise H.4.1.*** Write a circuit for simulating a system with Hamiltonian $\hat{H} = \alpha X \otimes X$.

<details>
<summary><i>Hint.</i></summary>
Use $HZH = X$, where $H$ is the Hadamard gate.
</details>

<details>
<summary><i>Solution.</i></summary>

Since $HZH = X$, we can convert the $X \otimes X$ Hamiltonian into the $Z \otimes Z$ Hamiltonian we just solved:

$$
\hat{H} = \alpha (H \otimes H)(Z \otimes Z)(H \otimes H).
$$

Since $(H \otimes H)^2 = I$, any number of powers of $\hat{H}$ can be written

$$
\hat{H}^k = [\alpha (H \otimes H)(Z \otimes Z)(H \otimes H)]^k = (H \otimes H)[\alpha (Z \otimes Z)]^k(H \otimes H).
$$

Plugging this into exponential gives

$$
e^{-it\hat{H}/\hbar} = (H\otimes H)e^{-it\alpha Z \otimes Z/\hbar}(H\otimes H).
$$

Thus, we simply bookend our circuit for exponentiating $\alpha Z \otimes Z$ with Hadamard gates, giving a new circuit:

<img src="pics/diag-xx-2.svg" width="400px">

<div align="right">▢</div>

</details>

---

We can see that, even when we know the energy levels for a simple Hamiltonian like (\ref{diag-zz}), implementing it on a quantum computer takes work. But even discovering the energy levels is in general very hard! The reason is simply that the matrices we are dealing with are huge. For an $N \times N$ matrix, general-purpose numerical algorithms for finding the eigenvalues and eigenvectors take a polynomial number of steps in $N$. If we have a Hamiltonian acting on $n$ qubits, then $N = 2^n$, and hence the number of steps is exponential! This is the sort of exponential cost Feynman was thinking about when he proposed computers built using quantum-mechanical principles.

<img src="pics/diag-steps.svg" width="500px">

If finding all the energy levels is overambitious, what about a single energy level? The lowest energy $E_\Omega$ and the associated **ground state** $\vert \Omega\rangle$ are usually of great interest. This is the state the system likes to relax to when given the opportunity, and we can even design Hamiltonians so that their ground state and energy solves a hard mathematical problem.

A rich class of examples comes from graph theory, which in turn are
connected to real-world optimization problems. For instance, in route
planning, circuit design, scheduling, and even web searches, graph
theory is an essential component.
A graph $G = (V, E)$ has two parts, a set of points $V$ called the
**vertices** and some **edges** $E$ connecting them.
In quantum computing, we usually
associate each node in $V$ to a quantum system, edges to interactions,
and design a Hamiltonian so that the ground state gives us an optimal
solution to problem we would like to solve on the graph.

As a concrete
example, suppose we want to check if a graph
$G$ is **bipartite**, meaning that we can colour the nodes red and
blue so that no two nodes connected by an edge have the same
colour. Below, the graph on the left is bipartite while the graph on
the right is not, since there is no way to colour the triangle so that
red and blue never share an edge:

<img src="pics/bipartite.svg" width="400px">

We would like our Hamiltonian to tell us if the graph is bipartite or not. Let's associate different qubit states to different colours, say blue to $\vert 0\rangle$ and red to $\vert 1\rangle$. If the graph is bipartite, then there is some basis state where each edge $e = (u, v)$ has a $\vert 0\rangle$ state on one end, and a $\vert 1\rangle$ state on the other. We can measure this using the combination of Pauli operators $Z_u Z_v$, since (just focusing on the states at nodes $u$ and $v$)

$$
Z_u Z_v \vert x_u \rangle \otimes \vert x_v\rangle = (-1)^{x_u + x_v}\vert x_u \rangle \otimes \vert x_v\rangle.
$$

Thus, a valid colouring of $e = (u, v)$ will pick up an eigenvalue $-1$ when we apply $Z_u Z_v$. This motivates our choice of Hamiltonian:

$$
\hat{H} = \sum_{(u, v) \in E} Z_u Z_v. \tag{2} \label{bipartite}
$$

The ground state will correspond to an assignment of red and blue such that each edge contributes $-1$, so we know the graph is bipartite if the ground state energy $E_\Omega = -|E|$, where $|E|$ denotes the size of edge set. As an example, let's consider the graph on the left, and label the nodes as follows:

<img src="pics/test-graph.svg" width="200px">

The Hamiltonian is then

$$
\hat{H} = Z_0 Z_1 + Z_1Z_2 + Z_1 Z_3 + Z_3Z_4.
$$

To actually generate a good guess at the ground state $\vert
\Omega\rangle$ is difficult and beyond our scope for the moment. But
if you are *given* a candidate ground state, it's easy to check if the
graph is bipartite! One way is to measure the energy directly.

---

***Exercise H.4.2.*** Consider the Hamiltonian (\ref{bipartite}). If
   an energy measurement gives $E = -|V|$, argue that the graph is
   bipartite and the system is in the ground state.

<details>
<summary><i>Solution.</i></summary>

Let's draw an example for our graph above:

<img src="pics/ground-state.svg" width="200px">

The expectation of each term $\langle Z_uZ_v\rangle$, for any state, is at least $-1$, since

$$
\vert\langle Z_uZ_v\rangle \vert \leq \vert\langle Z_u\rangle\vert \cdot \vert\langle Z_v\rangle \vert \leq 1
$$

by the Cauchy-Schwarz inequality. Thus, $E = -|V|$ is achieved
precisely when $\langle Z_uZ_v\rangle = -1$ for each term, which is a
minimum. Hence, this is the ground state.
Moreover, since each $|\langle Z\rangle| \leq 1$, this requires
$|\langle Z_u\rangle| = |\langle Z_v\rangle| = 1$, so that the state
is diagonal in the $Z$ basis, i.e., a computational basis state, with
an assignment of eigenvalues $\pm 1$ to each qubit. Finally, this
assignment can only achieve $E = -|V|$ if the graph is bipartite. ▢

</details>

---
