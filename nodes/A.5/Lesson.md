---

**Learning outcomes**

- *Define the Hadamard transform.*
- *Understand the effect of applying an oracle between Hadamard transforms.*

---

Now that we've warmed up with our simple test-in-pairs algorithm, we can try for something more ambitious. Instead of testing in pairs, we might wonder how to gather information from *every* basis state and make it globally accessible. Earlier, we showed that the test-in-pairs algorithm could be implemented by starting with the superposition

$$
  \vert \psi_{\tilde{\mathbf{x}}}\rangle = \frac{1}{\sqrt{2}}(\vert \tilde{\mathbf{x}}0\rangle+\vert \tilde{\mathbf{x}}1\rangle),
$$

where we label the pair with $\tilde{\mathbf{x}}$, an $(n-1)$-bit string. We apply the oracle $U_f$ and then a Hadamard $H_n$ on the last qubit to carry the phase information back into the computational basis. In circuit notation:

![](pics/pair-circuit.svg)

A simple way to generalize is to start with the uniform superposition on *all* states, apply the oracle, and then apply a Hadamard to *each* qubit, $H^{\otimes n} U_f \vert \psi\rangle$, where $\vert \psi\rangle$ is the uniform superposition

$$
\vert \psi\rangle= \frac{1}{\sqrt{2^n}}\sum_{\mathbf{x}\in\{0,1\}^n} \vert \mathbf{x}\rangle = H^{\otimes n} \vert \mathbf{0}\rangle.
$$

Here is the circuit:

![](pics/all-circuit.svg)

Applying a Hadamard to each qubit constitutes a big, multi-qubit operation called the
**Hadamard transform**. Mathematically speaking, the result of applying the transform is a bit
messy, but by linearity we only need to worry about what the Hadamard
transform does to an individual basis state $\vert
\mathbf{x}\rangle$. Let's denote the action of the Hadamard on the
single-qubit basis states by $H\vert x\rangle = \vert
\hspace{-1pt}\pm^x\rangle$, with the new notation

$$
\begin{align*}
\vert \pm^0\rangle & = \vert +\rangle = \frac{1}{\sqrt{2}}(\vert
0\rangle + \vert 1 \rangle) \\
\vert \pm^1\rangle & = \vert -\rangle = \frac{1}{\sqrt{2}}(\vert
0\rangle - \vert 1 \rangle),
\end{align*}
$$

which we can summarize as

$$
\vert \pm^x\rangle = \frac{1}{\sqrt{2}}(\vert 0\rangle + (-1)^x\vert 1 \rangle).
$$

Notice also that, for $x, y \in \{0, 1\}$, and a single-qubit basis state $\vert y\rangle$,

$$ 
\begin{equation}
  \langle y \vert  \hspace{-1pt}\pm^{x}\rangle = \frac{1}{\sqrt{2}}(\langle y\vert 0\rangle +
  (-1)^x \langle y\vert 1\rangle) =
  \frac{1}{\sqrt{2}}(-1)^{xy},\label{eq:had-overlap} \tag{1}
\end{equation}
$$

since $y = 0$ yields the first overlap and $y = 1$ the second. The result for two qubits is just a product of the one-qubit result:

$$ 
\begin{align*}
  (\langle y_1\vert  \otimes \langle y_2\vert ) (\vert  \hspace{-1pt}\pm^{x_1}\rangle \otimes \vert  \hspace{-1pt}\pm^{x_2}\rangle) & = (\langle y_1 \vert  \hspace{-1pt}\pm^{x_1}\rangle)(\langle y_2 \vert  \hspace{-1pt}\pm^{x_2}\rangle) \\ & = \frac{1}{2}(-1)^{x_1y_1}(-1)^{x_2y_2}.
\end{align*}
$$

This two-qubit example makes it clear that we can generalize to $n$ qubits simply by taking a product of $n$ terms. The Hadamard transform of a basis state is

$$
  H^{\otimes n} \vert \mathbf{x}\rangle = \vert \hspace{-1pt}\pm^{x_1}\rangle
  \vert \hspace{-1pt}\pm^{x_2}\rangle \cdots \vert \hspace{-1pt}\pm^{x_n}\rangle.
$$

This means that the Hadamard transform of the post-oracle state is

$$
  H^{\otimes n} U_f \vert \psi\rangle = \frac{1}{\sqrt{2^n}}\sum_{\mathbf{x}\in\{0,1\}^n}
  (-1)^{f(\mathbf{x})}\vert \hspace{-1pt}\pm^{x_1}\rangle \vert \hspace{-1pt}\pm^{x_2}\rangle \cdots \vert \hspace{-1pt}\pm^{x_n}\rangle.
$$

We would like to write this in the computational basis, since this is the basis in which we will measure. You can see what the computational basis elements look like in the next exercise.

---

***Exercise A.5.1.*** Using Eq. (\ref{eq:had-overlap}), show that

$$
\begin{align*}
      \langle\mathbf{y}\vert H^{\otimes n} U_f \vert \psi\rangle %& = \frac{1}{2^n}\sum_{\mathbf{x}\in\{0,1\}^n}                                                        (-1)^{f(\mathbf{x})}(-1)^{x_1y_2 + \cdots + x_n y_n}\\
                                                       &  = \frac{1}{2^n}\sum_{\mathbf{x}\in\{0,1\}^n} (-1)^{f(\mathbf{x})+\mathbf{x}\cdot\mathbf{y}}.
    \end{align*}
    $$
    
Conclude that, in the computational basis,

$$
   H^{\otimes n} U_f \vert \psi\rangle = \frac{1}{2^n}\sum_{\mathbf{x},
     \mathbf{y}\in\{0,1\}^n}
   (-1)^{f(\mathbf{x})+\mathbf{x}\cdot\mathbf{y}}\vert
   \mathbf{y}\rangle.\label{eq:DJ-state} \tag{2}
 $$

<details>
<summary><i>Solution.</i></summary>

Consider a bit string $\mathbf{y} = (y_j)$, $1 \leq j \leq
n$. Applying Eq. (\ref{eq:had-overlap}) to multiple qubits gives

$$
\begin{align*}
\langle\mathbf{y}\vert \hspace{-1pt}\pm^{x_1}\rangle
  \vert \hspace{-1pt}\pm^{x_2}\rangle \cdots \vert \hspace{-1pt}\pm^{x_n}\rangle & = \frac{1}{\sqrt{2^n}}(-1)^{x_1y_1} (-1)^{x_2y_2} \cdots (-1)^{x_ny_n} \\ & = \frac{1}{\sqrt{2^n}} (-1)^{\mathbf{x}\cdot\mathbf{y}}.
\end{align*}
$$

By linearity,

$$
\begin{align*}
\langle\mathbf{y}\vert H^{\otimes n} U_f \vert \psi\rangle & = \frac{1}{\sqrt{2^n}}\sum_{\mathbf{x}\in\{0,1\}^n}
  (-1)^{f(\mathbf{x})}\langle\mathbf{y} \vert\big(\vert \hspace{-1pt}\pm^{x_1}\rangle \vert \hspace{-1pt}\pm^{x_2}\rangle \cdots \vert \hspace{-1pt}\pm^{x_n}\rangle\big) \\ & = \frac{1}{2^n}\sum_{\mathbf{x}\in\{0,1\}^n} (-1)^{f(\mathbf{x})+\mathbf{x}\cdot\mathbf{y}}
\end{align*}
$$

as required. Since $\vert \mathbf{y}\rangle$ labels states in the computational basis, these overlaps are simply coefficients of $H^{\otimes n} U_f \vert \psi\rangle$ in that basis. Hence,

$$
   H^{\otimes n} U_f \vert \psi\rangle = \frac{1}{2^n}\sum_{\mathbf{x},
     \mathbf{y}\in\{0,1\}^n}
   (-1)^{f(\mathbf{x})+\mathbf{x}\cdot\mathbf{y}}\vert \mathbf{y}\rangle
 $$

as claimed. ▢

</details>

---

The Eq. (\ref{eq:DJ-state}) outcome of our superposition-oracle-Hadamard transform circuit is a bit messy, but perhaps we can tailor a measurement to determine
the secret lock combination. For this to work, we would need different solutions to correspond to
*orthogonal* states of the form given in
Eq. (\ref{eq:DJ-state}). Unfortunately, most of them overlap!  For
instance, if $n  =1$, then the end result of $HU_f$ is the same state
$\pm \vert -\rangle$ for either solution. In fact, it's possible to
show that for distinct solutions $\vert \mathbf{s}_1\rangle$ and
$\vert \mathbf{s}_2\rangle$,

$$
\left(\langle \mathbf{0}\vert - \frac{2}{\sqrt{2^n}} \langle\mathbf{s}_2\vert H^{\otimes n}\right) \left(\vert \mathbf{0}\rangle - \frac{2}{\sqrt{2^n}} H^{\otimes n}\vert \mathbf{s}_1\rangle\right) = 1 - \frac{4}{2^n}. \label{eq:overlap} \tag{3}
$$

Thus, for $n \neq 2$ qubits, we cannot learn the lock combination from
a clever measurement since the outcomes are not orthogonal. (See the
bonus exercise below if you don't believe it.) But even if we can't
learn the lock combination from the circuit, something interesting
happens! Let's look at a particularly simple measurement outcome,
$\mathbf{y} = \mathbf{0}$. The amplitude for observing this follows
immediately from Eq. (\ref{eq:DJ-state}):

$$
\begin{align*}
   \mathcal{A}_{\mathbf{0}} & = \langle \mathbf{0}\vert H^{\otimes n}
   U_f \vert \psi\rangle \\ & = \frac{1}{2^n}\sum_{\mathbf{x},\mathbf{y}\in\{0,1\}^n}
   (-1)^{f(\mathbf{x})+\mathbf{x}\cdot\mathbf{y}}\langle\mathbf{0}\vert \mathbf{y}\rangle \\ & = \frac{1}{2^n}\sum_{\mathbf{x}\in\{0,1\}^n}
   (-1)^{f(\mathbf{x})}.
\end{align*}
$$

This sum clearly doesn't depend on what the solution is, so it won't help us find the lock combination. But it does tell us something about the global properties of $f$! In the next node, we will use this to design our first nontrivial quantum algorithm.

---

***Exercise A.5.2 (bonus).*** Confirm Eq. (\ref{eq:overlap}).

<details>
<summary><i>Solution.</i></summary>

Expanding the LHS gives four terms:

$$
\begin{align*}
\left(\langle \mathbf{0}\vert 
    - \frac{2}{\sqrt{2^n}} \langle\mathbf{s}_2\vert H^{\otimes n}\right) \left(\vert \mathbf{0}\rangle
    - \frac{2}{\sqrt{2^n}} H^{\otimes n}\vert \mathbf{s}_1\rangle\right) & =
    \langle\mathbf{0}\vert \mathbf{0}\rangle - \frac{2}{\sqrt{2^n}} \langle\mathbf{s}_2\vert H^{\otimes n}\vert \mathbf{0}\rangle \\ & \qquad - \frac{2}{\sqrt{2^n}}\langle \mathbf{0}\vert  H^{\otimes n}\vert \mathbf{s}_1\rangle + \frac{4}{2^n} \langle\mathbf{s}_2\vert H^{\otimes n}\cdot H^{\otimes n}\vert \mathbf{s}_1\rangle.
\end{align*}
$$

The first term on the RHS gives $1$ since the state is
normalized. Since $H^{\otimes n}\cdot H^{\otimes n} = I,$ the last term is proportional to $\langle\mathbf{s}_2\vert \mathbf{s}_1\rangle,$ which vanishes for distinct solutions, i.e., $\mathbf{s}_2\neq\mathbf{s}_1$. Finally, we have the middle terms. Since $H^{\otimes n}\vert \mathbf{0}\rangle = \vert \psi\rangle$ is the uniform superposition, the overlap with any computational basis state is $1/\sqrt{2^n}$. Thus, our final answer for the overlap is

$$
\begin{align*}
1 - \frac{2}{2^n} - \frac{2}{2^n} + 0 = 1 - \frac{4}{2^n}
\end{align*}
$$

as claimed. ▢

</details>

---
