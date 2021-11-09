In a previous codercise, we learned about arbitrary unitary rotations, and you
applied a parametrized operation using the `Rot` gate in PennyLane. It's time to
learn a bit more about what's happening under the hood. `Rot` is actually applying
a sequence of three operations:

```python
def decomposed_rot(phi, theta, omega):
    qml.RZ(phi, wires=0)
    qml.RY(theta, wires=0)
    qml.RZ(omega, wires=0)
```

Even though `Rot` is the most general single-qubit operation, under the hood
it's just `RZ` and `RY` gates! This begs the question of whether we actually
need `RX` - essentially, the answer is no. In fact, in general, as long as we
have two rotations out of the set `[RX, RY, RZ]`, we can implement any
single-qubit operation; it's just a matter of finding the angles that work,
which could be mathematically cumbersome. Together, `RZ` and `RY` form a
universal gate set for single-qubit operations (as do `RZ` and `RX`, or `RY` and
`RX`)

***Codercise I.7.1*** Can you find a set of angles `phi, theta, omega` such that
  the sequence of gates

```python
    qml.RZ(phi, wires=0)
    qml.RX(theta, wires=0)
    qml.RZ(omega, wires=0)
```

acts the same as a Hadamard gate (up to a global phase)?

<details>
  <summary><i>Hint.</i></summary>

For convenience, here are the matrix forms for $H$ and $RX$:

$$
H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad
    RX(\theta) = \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\ -i\sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)   \end{pmatrix}.
$$

Start by determining which angle of the $RX$ will give you the correct magnitude
of the elements, then use the $RZ$ to adjust the signs to give $H$ up to a
global phase.

</details>