---

From this last exercise, both the matrix representation and plot show that

$$
\begin{equation}
RX(\theta) \vert 0\rangle = \cos(\theta/2) \vert 0\rangle - i \sin(\theta/2) \vert 1\rangle.
\end{equation}
$$

Similarly, you could work out that

$$
RX(\theta) \vert 1\rangle = -i \sin(\theta/2) \vert 0\rangle + \cos(\theta/2) \vert 1\rangle.
$$

The way the operation acts on the amplitudes is periodic, and is described by
simple trigonometric functions. $RX$ is simply rotating the state in its
two-dimensional space, with some extra complex phases! But, what if we want to
change the relative sizes of the amplitudes *without* adding in the complex
components? 

---

***Codercise I.6.3.*** Repeat the above exercise, but using `qml.RY`. From the
amplitudes you obtain for $RY\vert 0 \rangle$, can you start deducing the
matrix form of $RY$?

