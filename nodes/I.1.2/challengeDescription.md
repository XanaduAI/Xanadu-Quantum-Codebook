---

All qubit state vectors have a dual vector, known as a **bra**. It is obtained by
taking the conjugate transpose of the ket vector:

$$
\langle\psi\vert  = \begin{pmatrix} \alpha^* & \beta^* \end{pmatrix}. \tag{4}
$$  

Together, we can combine a bra and a ket to define an **inner product**.  Given two states $\vert \psi\rangle = \alpha \vert 0\rangle + \beta
\vert 1\rangle$ and $\vert \phi\rangle = \gamma \vert 0\rangle + \delta \vert
1\rangle$, the inner product between them is

$$
\begin{equation}
\langle \phi \vert  \psi \rangle = \begin{pmatrix} \gamma^* & \delta^* \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \gamma^* \alpha + \delta^* \beta. \tag{5}
\end{equation}
$$

The value of the inner product is just a complex number. Loosely, this number tells 
us how much one state overlaps with another. States between which the inner
product is 0 are called **orthogonal**. The maximum value of the inner product
is 1, corresponding to the inner product of a normalized state with itself,
$\langle \psi \vert \psi\rangle = 1$.

---

***Codercise I.1.2*** Write a function to compute the inner product between two
   arbitrary states. Then, use it to verify that $\vert 0\rangle$ and $\vert
   1\rangle$ form an **orthonormal basis**, i.e., the states are normalized and
   orthogonal.

<details>
  <summary><i>Example.</i></summary>

  Suppose we are given two states

  <pre>
  state_1 = np.array([0.8, 0.6])
  state_2 = np.array([1 / np.sqrt(2), 1j / np.sqrt(2)]) </pre>

  Your function should compute and return the value of the inner product:

  <pre> 0.56568542-0.42426407j</pre>

</details>