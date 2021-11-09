---

**Learning outcomes**

 - *Define what it means for a matrix to be unitary.*
 - *Express a single-qubit unitary operation in terms of 3 real parameters.*
 
---

Now that we know what qubits are, and how to express computations on them,
it's time to make an important transition: what exactly are we *doing* to the
qubits? What are the different possible gates, and how do they work?


<img src="pics/circuit-shapes-to-gates.svg" alt="" width="600px">

Recall that qubit states are represented by 2-dimensional vectors that live in a
mathematical space called the *Hilbert space*. We know already that single qubit
operations must take valid qubit states to other valid qubit states, and this is
done using matrix-vector multiplication by a $2 \times 2$ matrix. Given an
initial qubit state $\vert \psi\rangle$, a single-qubit operation $U$ sends

$$
\vert \psi \rangle \rightarrow \vert \psi^\prime \rangle = U \vert \psi \rangle, \tag{1}
$$

where $\vert \psi^\prime \rangle$ is the new state.

However, recall that qubit state vectors have some special properties - in
particular, they are normalized, i.e., have length 1. Thus, any matrix that
operates on qubits is going to require a structure that preserves this property.
Matrices of this type are called **unitary matrices**. More formally, an $n
\times n$ complex-valued matrix $U$ is unitary if
  
$$
U U^\dagger = U^\dagger U = I_n, \tag{2}
$$
   
where $I_n$ is the $n$-dimensional identity matrix. $U^\dagger$ is the notation
for the conjugate transpose or adjoint of $U$ (i.e., take the transpose of the matrix, and
replace each entry with its complex conjugate). 

## Unitary parametrization

As a consequence of this definition, unitary matrices have a very particular
structure. Upon seeing a $2 \times 2$ matrix of complex numbers, you might think
that we need 8 real numbers to specify it (i.e., 1 complex number per entry,
giving 2 real numbers per entry). By working through the exercises in this
section, you'll see how consequences of this definition enable us to specify
them with only 3 real numbers. This will provide insight into the form of some
of the operations you'll see in the upcoming sections.

---

***Exercise I.3.1.*** Suppose we write

$$
U = \begin{pmatrix} a & b \\ c & d \end{pmatrix},
$$

where $a, b, c, d$ are complex numbers. Evaluate the matrix product $U
U^\dagger$ and write down the set of equations that must be satisfied for $U$ to
be unitary. What does this tell you about the rows of $U$? Do the same for
$U^\dagger U$, and check what this tells you about the columns of $U$.


<details>
  <summary><i>Solution.</i></summary>

Evaluating $U U^\dagger$ gives us

$$
U U^\dagger = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} a^* & c^* \\ b^* & d^* \end{pmatrix} = 
 \begin{pmatrix} \vert a\vert ^2 + \vert b\vert ^2 & a c^* + b d^* \\ a^*c + b^*d & \vert c\vert ^2 + \vert d\vert ^2 \end{pmatrix}.
$$

Setting this equal to the identity gives 4 equations:

$$
\begin{align*}
\vert a\vert ^2 + \vert b\vert ^2 &= 1, \\
a c^* + b d^* &= 0, \\
a^*c + b^*d &= 0, \\
\vert c\vert ^2 + \vert d\vert ^2 &= 1.
\end{align*}
$$

This shows us that the lengths of both rows are 1. 

Doing the same for $U^\dagger U$ produces a similar set of equations that tells
us the columns also have length 1. In both cases, products of rows with other
rows gives a result of 0, thus different rows are orthogonal to each other. We
say that $U$ has **orthonormal** rows and columns, i.e., its rows and columns are
orthogonal and normalized (they have length 1 just like state vectors). ▢

</details>

---

Having learned about the rows and columns of $U$, we can see that there are
relationships between $a, b, c$ and $d$ that can simplify how we express unitary
operations.

---

***Exercise I.3.2.*** Starting from 

$$
U = \begin{pmatrix} a & b \\ c &  d  \end{pmatrix},
$$

where $a, b, c, d$ are complex numbers, show that $U$ can be expressed as 

$$
U = \begin{pmatrix} a & -e^{i\beta} c^* \\ c &  e^{i \beta} a^*  \end{pmatrix},
$$

where $\beta$ is a real number (and we refer to the complex value $e^{i\beta}$ as a **phase**).

<details>
  <summary><i>Hint.</i></summary>

 The condition of unitarity, $U U^\dagger = I$, tells you something about
 both the inverse and the determinant of $U$. This can be applied to decrease
 the amount of complex numbers needed to describe $U$.
</details>

<details>
  <summary><i>Solution.</i></summary>

Since $U U^\dagger = I$, this means that $U^{-1} =
 U^\dagger$. Inverting the matrix tells us that

$$
U^\dagger = \begin{pmatrix} a^* & c^* \\ b^* & d^*  \end{pmatrix} = \frac{1}{\hbox{det}(U)} \begin{pmatrix} d & -b \\ -c & a  \end{pmatrix}.
$$

This allows us to re-express both $d$ and $b$ in terms of $a$ and $c$
respectively:

$$
d = \hbox{det}(U)a^*, \quad b = -\hbox{det}(U) c^*.
$$

This gives us the form 

$$
U = \begin{pmatrix} a & -\hbox{det}(U) c^* \\ c &  \hbox{det}(U) a^*  \end{pmatrix}.
$$

Since determinants are multiplicative, $\hbox{det}(U U^\dagger) = \hbox{det}(U)
\hbox{det}(U^\dagger) = 1$. Therefore, the determinant of $U$ must be a complex
number with modulus 1 (i.e., a <a
href="https://en.wikipedia.org/wiki/Circle_group" target="_blank"> unit complex
number</a>). Let's write $\hbox{det}(U) = e^{i \beta}$ so that

$$
U = \begin{pmatrix} a & -e^{i\beta} c^* \\ c &  e^{i \beta} a^*  \end{pmatrix}.
$$

<div align="right"> ▢ </div>

</details>

---

***Challenge Exercise I.3.3.*** Starting from the expression for $U$ obtained in
   the previous exercise, show that any unitary matrix can be expressed as

$$
U(\phi, \theta, \omega) = \begin{pmatrix} e^{-i(\phi + \omega)/2} \cos(\theta/2) & -e^{i(\phi - \omega)/2} \sin(\theta/2) \\ e^{-i(\phi - \omega)/2} \sin(\theta/2) & e^{i(\phi + \omega)/2} \cos(\theta/2)  \end{pmatrix},
$$

where $\phi$, $\theta$, and $\omega$ are real numbers.


<details>
  <summary><i>Hint.</i></summary>

Start by expressing the complex numbers $a$ and $c$ in polar form to
 uncover the $\theta$ dependence. Then, find a way to re-express the phases involving $\phi$, $\omega$ to
 match the result.

</details>

<details>
  <summary><i>Hint.</i></summary>

  In quantum computing, $U$ and $e^{i\theta} U$ are effectively the same operation. You can
  thus factor out complex numbers with modulus 1 from any unitary matrix.

</details>


<details>
  <summary><i>Solution.</i></summary>

 As per the first hint, let's write our complex numbers in polar form, $a =
 r e^{i\alpha}$ and $c = s e^{i\gamma}$. Since $U$ is orthonormal, it must be
 that $\vert a\vert ^2 + \vert c\vert ^2 = r^2 + s^2 = 1$. So without loss of
 generality, we can set $r = \cos(\theta / 2)$, $s = \sin(\theta / 2)$ to obtain

$$
U = \begin{pmatrix} e^{i\alpha} \cos(\theta/2) & -e^{i(\beta-\gamma)} \sin (\theta/2) \\ e^{i\gamma} \sin(\theta/2) &  e^{i (\beta - \alpha)} \cos(\theta/2)  \end{pmatrix}.
$$

The next step is to massage the phases. The second hint tells us that we can factor out complex
numbers from our matrix. We start by removing a factor of $e^{i\beta/2}$ from each element:

$$
U = \begin{pmatrix} e^{i \left( \alpha - \frac{\beta}{2} \right)} \cos(\theta/2) & -e^{i\left(\frac{\beta}{2}-\gamma\right)} \sin (\theta/2) \\ e^{i\left(\gamma - \frac{\beta}{2}\right)} \sin(\theta/2) &  e^{i \left(\frac{\beta}{2} - \alpha\right)} \cos(\theta/2)  \end{pmatrix}.
$$

Next, let's adjust the signs to match:

$$
U = \begin{pmatrix} e^{-i\left(\frac{\beta}{2} - \alpha\right)} \cos(\theta/2) & -e^{i\left(\frac{\beta}{2}-\gamma\right)} \sin (\theta/2) \\ e^{-i\left( \frac{\beta}{2} - \gamma\right)} \sin(\theta/2) &  e^{i \left(\frac{\beta}{2} - \alpha\right)} \cos(\theta/2)  \end{pmatrix}.
$$

Now notice that in the desired expression, each phase contains both $\phi$ and
$\omega$. This suggests that all our phases should contain some combination of
$\alpha$, $\beta$, and $\gamma$. To ensure this, we both add and subtract
$\frac{\alpha}{2}$ to the upper right and lower left corners, and similarly add
and subtract $\frac{\gamma}{2}$ to the two diagonal elements. We'll also rewrite
the existing $\alpha$ and $\gamma$ as a combination of two $\frac{\alpha}{2}$
(or $\frac{\gamma}{2}$):

$$
U = \begin{pmatrix} 
e^{-i\left(\frac{\beta}{2} - \frac{\alpha}{2} - \frac{\alpha}{2} - \frac{\gamma}{2} + \frac{\gamma}{2}\right)} \cos(\theta/2) & -e^{i\left(\frac{\beta}{2}- \frac{\gamma}{2} - \frac{\gamma}{2} + \frac{\alpha}{2} - \frac{\alpha}{2}\right)} \sin (\theta/2) \\ 
e^{-i\left( \frac{\beta}{2} - \frac{\gamma}{2} - \frac{\gamma}{2} - \frac{\alpha}{2} + \frac{\alpha}{2}\right)} \sin(\theta/2) &  e^{i \left(\frac{\beta}{2} - \frac{\alpha}{2} - \frac{\alpha}{2} - \frac{\gamma}{2} + \frac{\gamma}{2}\right)} \cos(\theta/2)  
\end{pmatrix}.
$$

The final step is to make the substitution

$$
\begin{align*}
\phi &= \frac{\beta}{2} - \frac{\alpha}{2} - \frac{\gamma}{2}, \\
\omega &= \frac{\gamma}{2} - \frac{\alpha}{2}, \\
\end{align*}
$$

to obtain 

$$
U(\phi, \theta, \omega) = \begin{pmatrix} e^{-i(\phi + \omega)/2} \cos(\theta/2) & -e^{i(\phi - \omega)/2} \sin(\theta/2) \\ e^{-i(\phi - \omega)/2} \sin(\theta/2) & e^{i(\phi + \omega)/2} \cos(\theta/2)  \end{pmatrix}.
$$

While this is the most general parametrization of a unitary matrix, many common
single-qubit operations are actually much simpler than this. In the next few
sections, we will explore a number of the most-used unitary operations and see
how they affect qubit states. ▢

</details>

