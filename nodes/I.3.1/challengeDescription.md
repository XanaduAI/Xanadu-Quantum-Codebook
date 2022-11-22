Earlier, we learned that performing quantum operations
involves multiplication by matrices that send valid, normalized quantum states
to other normalized quantum states. We even saw an example,

\begin{equation}
U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1& 1 \\ 1 & -1 \end{pmatrix}. \tag{1}
\end{equation}

Surely, such matrices have some special properties in order to work properly on
quantum states. These matrices are called **unitary**. Unitary matrices are
complex-valued matrices with the property that $ U U^\dagger = U^\dagger U =
I_n$, where $I_n$ is the $n$-dimensional identity matrix. $U^\dagger$ is the
notation for the conjugate transpose of $U$ (i.e., take the transpose of the
matrix, and replace each entry with its complex conjugate).

In PennyLane, unitary operations specified by a matrix can be implemented in a
quantum circuit using the <a href="https://docs.pennylane.ai/en/stable/code/api/pennylane.QubitUnitary.html" target="_blank"><tt>QubitUnitary</tt></a> operation. `QubitUnitary` is a parametrized
gate, and can be called like so:

<code>

    qml.QubitUnitary(U, wires=wire)
    
</code>

---

***Codercise I.3.1.*** Complete the quantum function below to create a circuit
   that applies `U` to the qubit and returns its *state*. (Compare this to the
   earlier function `apply_u` that you wrote — isn't it nice to not have to
   worry about the matrix arithmetic?)