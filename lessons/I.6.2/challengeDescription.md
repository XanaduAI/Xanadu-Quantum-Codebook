---

In the previous exercise, you should have noticed that for this special case,
$RX(\pi) = X$ up to a global phase of $-i$. But what does $RX$ do more generally?



---


***Codercise I.6.2.*** The matrix representation of $RX$ is

$$
\begin{equation}
RX(\theta) = \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\ -i\sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)  \end{pmatrix}.
\end{equation}
$$

How does this affect the amplitudes when we apply it to a quantum state?
Implement a QNode that applies the `qml.RX` operation with parameter $\theta$ to a
specified basis state. Then, run the code to plot the amplitudes
of the $\vert 0 \rangle$ and $\vert 1 \rangle$ after applying $RX(\theta)$ to the
$\vert 0 \rangle$ state.