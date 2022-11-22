This circuit performs something interesting. The set of three Hadamards serves to
put the first three qubits in a linear superposition of all 3-qubit basis states:

$$
(H \otimes H \otimes H) \vert 000 \rangle = \frac{1}{\sqrt{2}^3} \left(
 \vert 000 \rangle + \vert 001 \rangle + \cdots + \vert 111 \rangle \right). \tag{3}
$$

Together with the fourth qubit, the state before the multi-controlled gate is

$$
(H \otimes H \otimes H \otimes I) \vert 0000 \rangle = \frac{1}{\sqrt{2}^3} \left(
 \vert 0000 \rangle + \vert 0010 \rangle + \cdots + \vert 1110 \rangle \right). \tag{4}
$$

The multi-controlled gate only triggers in the case where the first three qubits
are in the state $\vert 001\rangle$. Therefore, the state of the fourth qubit
will only be flipped for that particular term in the superposition:

$$
MCX (H \otimes H \otimes H \otimes I) \vert 0000 \rangle = \frac{1}{\sqrt{2}^3} \left(
 \vert 0000 \rangle + \vert 0011 \rangle + \cdots + \vert 1110 \rangle \right). \tag{5}
$$

Since you can apply any gate in a multi-controlled fashion like this, this is a
nice trick for applying operations to only certain parts of a
superposition. Furthermore, different controlled operations can be applied to
different terms simply by tinkering with the control values.

---

***Codercise I.13.5.*** Consider the 3-controlled-NOT below. Can you implement
   this gate using only Toffolis? You'll need one extra qubit to do so; this is
   called an *auxiliary* qubit, and note that it both starts and ends in the
   state $\vert 0 \rangle$.

<img src="pics/4cx.svg" width="500px">


<details>
  <summary><i>Hint.</i></summary>

  Only 3 Toffolis are required.

</details>

<details>
  <summary><i>Hint.</i></summary>

 We need to compute the AND of three bits, but we can only do two at a
 time; the auxiliary qubit gives us space to store intermediate results. To
 return the auxiliary qubit back to its initial state, recall that the Toffoli
 is a reversible gate.

</details>

*Challenge*. Once you figure out the solution, try and do the 4-controlled case
 (you'll need one additional auxiliary qubit). Can you see how this generalizes
 to larger and larger gates?