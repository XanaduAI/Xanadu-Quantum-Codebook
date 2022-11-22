In the previous exercise, you will have found that applying $Z$ to $\vert + \rangle$
produces the $\vert - \rangle$ state,

$$
\begin{equation}
\vert - \rangle = \frac{1}{\sqrt{2}} \left( \vert 0 \rangle - \vert 1 \rangle \right).
\end{equation}  \tag{2}
$$

Despite the difference in sign on the amplitude of the $\vert 1 \rangle$
state, $\vert + \rangle$ and $\vert - \rangle$ have the same measurement outcome
probabilities in the computational basis!

---

The operation $Z$ is a special case of a more general operation that modifies
the phase of an amplitude, known as a **$Z$ rotation**, or $RZ$. Given some
arbitrary $\vert \psi \rangle = \alpha \vert 0\rangle + \beta \vert 1\rangle$
and angle of rotation $\omega$ (in radians),

$$
\begin{equation}
RZ(\omega) \vert \psi \rangle = e^{-i\frac{\omega}{2}} \alpha \vert 0\rangle + \beta e^{i\frac{\omega}{2}} \vert 1\rangle. 
\end{equation} \tag{3}
$$

However, this prefactor of $ e^{-i\frac{\omega}{2}}$ is also a **global phase**,
and can thus be factored out. This means that $RZ(\omega)$ produces

$$
\begin{equation}
RZ(\omega) \vert \psi \rangle = e^{-i\frac{\omega}{2}} \alpha \vert 0\rangle + \beta e^{i\frac{\omega}{2}} \vert 1\rangle =  e^{-i\frac{\omega}{2}} \left( \alpha \vert 0\rangle + \beta e^{i\omega} \vert 1\rangle \right) \sim  \alpha \vert 0\rangle + \beta e^{i\omega} \vert 1\rangle.
\end{equation} \tag{4}
$$

 In PennyLane,
this operation is accessible as <a
href="https://docs.pennylane.ai/en/stable/code/api/pennylane.RZ.html"
target="_blank"><tt>qml.RZ</tt></a>. `qml.RZ` is a parametrized operation,
and so we must specify not only a wire, but an angle of rotation:


<code>

    qml.RZ(angle, wires=wire)
    
</code>

---

***Codercise I.5.2.*** Write a QNode that uses `qml.RZ` to simulate a `qml.PauliZ`
   operation and return the state. Apply it to the $\vert +\rangle$ state to
   check your work.


<details>
  <summary><i>Hint.</i></summary>

The internal representation of $RZ$ in PennyLane yields a state with the
$e^{-i\frac{\omega}{2}}$/$e^{i\frac{\omega}{2}}$ phase prefactors. Use the global
phase relationships above to help determine if you have the correct
implementation.

</details>