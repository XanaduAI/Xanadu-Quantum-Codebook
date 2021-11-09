---

In the previous exercise, you saw that

$$
\begin{align*}
 H|0\rangle &= \frac{1}{\sqrt{2}} (|0\rangle + |1\rangle), \\
 H|1\rangle &= \frac{1}{\sqrt{2}} (|0\rangle - |1\rangle).
\end{align*} \tag{3}
$$

The first in particular is known as a uniform superposition because the
amplitudes are the same. These two states occur so often that they have special
labels based on the sign of the amplitudes:
    
$$
\begin{align*}
 |+\rangle &= \frac{1}{\sqrt{2}} (|0\rangle + |1\rangle), \\
 |-\rangle &= \frac{1}{\sqrt{2}} (|0\rangle - |1\rangle).
\end{align*} \tag{4}
$$ 

If you compute their inner product, you'll find that these states are
*normalized*, and *orthogonal*, thus forming a basis (the "Hadamard basis") for
a qubit state!  This result also tells us something interesting about unitary
matrices: the result of applying a unitary to each state of a pair of orthogonal
states produces a pair of states that is also orthogonal. Unitary matrices
preserve both the normalization of quantum state vectors, as well as the angles
between them!

---

***Codercise I.4.4.*** Now let's combine what we've just learned. Create a
   device with one qubit. Then, write a QNode (from scratch!) that applies the
   following circuit and returns the state.


<img src="pics/hxh.svg" alt="" width="400px">

Determine its effect on the two basis states. What do you think this operation
does? (We'll discuss this further in the next node).

The signature of your function should be:

```python
def apply_hxh(state):
    ...
    return qml.state()

```

where as in the previous exercises, `state` is an integer that indicates
which basis state to prepare.