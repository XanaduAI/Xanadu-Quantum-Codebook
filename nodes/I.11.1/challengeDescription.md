We've worked a couple of times now with circuits that have more than one qubit,
but we haven't yet really gone into detail about how this all works. The
single-qubit computational basis consists of $|0\rangle$ and $|1\rangle$. When
we deal with multiple qubits, their states combine using the *tensor
product* (see the accompanying textbook page for details about how this works
mathematically). The multi-qubit computational basis is the set of multi-qubit
states that contain all possible combinations of $|0\rangle$ and $|1\rangle$. For
example, for the 2-qubit case, we have $|00\rangle, |01\rangle, |10\rangle,
|11\rangle$.

You may notice that these correspond to the numbers $\{0,1,2,3\}$ in binary; this is not
an accident! It is common to write out the integer values, especially for a large
number of qubits, e.g., $|10\rangle \rightarrow |2\rangle$, $|111\rangle
\rightarrow |7\rangle$.

**Important: qubit-ordering convention.** In PennyLane, qubits are indexed
  numerically from left to right. Therefore, a state such as $|10100\rangle$
  indicates that the first and third qubit (or wires `0` and `2`) are in state
  $|1\rangle$, and the second, fourth, and fifth qubit are in state
  $|0\rangle$. When drawing quantum circuits, our convention is that the
  leftmost (first) qubit is at the *top* of the circuit, such that qubits
  starting in state $|10100\rangle$ corresponds to the circuit below:

<img src="pics/qubit_ordering.svg" alt="" width="200px">

A different convention, where qubit `0` is the rightmost qubit in the ket, is
used in a number of other quantum computing software frameworks and
resources. Always check the qubit ordering when you start using a new software
library!

---

***Codercise I.11.1.*** Write a circuit in PennyLane that accepts an integer
   value, then prepares and returns the corresponding computational basis state
   vector $|n\rangle$. (Assume a 3-qubit device). Try a few examples; does the
   appearance of the state vector match what you expect given the integer?


<details>
  <summary><i>Hint.</i></summary>

You will find the `numpy` function [`np.binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html)
helpful for this codercise.

</details>

<details>
  <summary><i>Hint.</i></summary>

 There are two ways to solve this challenge. The first is to manipulate the
 individual qubits based on the bit values. The second is to use a built-in
 state preparation template.  Check out the [PennyLane template
 library](https://docs.pennylane.ai/en/stable/introduction/templates.html)
 and see if there are any predefined functions that will help you.

</details>