---

It is possible to complete the above exercise using only four gates!
To see how, let's first take our original circuit

<img src="pics/circuit_i-7-2_solution_1.svg" alt="" width="400px">

and decompose each gate into a product of $RX$ and $RZ$ (note that for $Y$, we can
write $Y = i XZ = i RX(\pi) RZ(\pi)$).

<img src="pics/circuit_i-7-2_solution_2.svg" alt="" width="750px">

Next, we can simplify this circuit by grouping together rotations of the same type.

<img src="pics/circuit_i-7-2_solution_3.svg" alt="" width="750px">

Then, since subsequent rotations of the same type are equivalent
to performing one rotation with the cumulative angle, we can 
group together all the $RZ$ in the middle into a single one.

<img src="pics/circuit_i-7-2_solution_4.svg" alt="" width="500px">

---

***Codercise I.7.3.*** The two gates $H$ and $T$ are also a **universal gate
   set**. By combining just these two gates, we can approximate to arbitrary
   precision *any* single-qubit operation (just like we can do with $RZ$ and
   $RY$)! Write a PennyLane circuit that applies the unitary matrix

$$
U = \frac{1}{\sqrt{2}^3} \begin{pmatrix} 
 1 + e^{i\pi/4} + i (1 - e^{i\pi/4}) &  1 - e^{i\pi/4} + i (1 +e^{i\pi/4}) \\ 
 1 + e^{i\pi/4} - i (1 - e^{i\pi/4}) &  1 - e^{i\pi/4} - i (1 +e^{i\pi/4})
\end{pmatrix}
$$


using 6 $H$ and $T$ gates altogether. Recall that the matrix form of
$T$ can be written up to a global phase as 

$$
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}.
$$


<details>
  <summary><i>Hint.</i></summary>

Consider that the Hadamard is its own inverse. This limits the ordering of how the
two operations can be applied in sequence.

</details>


<details>
  <summary><i>Hint.</i></summary>

The common denominator of all the terms holds information about
 the number of Hadamards you have to use. The largest cumulative phase, and
 number of terms in the sum should also give you a hint as to how many $T$s are
 necessary.

</details>

*Tip*. This process is called **quantum circuit synthesis** and is part of the
 broader subject of **quantum compilation**. As you will no doubt appreciate
 after working out this small exercise, designing high-quality, automated
 compilation tools is an active area of research.