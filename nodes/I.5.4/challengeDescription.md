---

***Codercise I.5.4.*** The $T$ gate plays an important role in more advanced
   quantum computing topics; specifically, it is a required operation in some
   fault-tolerant frameworks. However, it is much more resource intensive to
   implement in those frameworks than other gates, and therefore a common task
   in quantum circuit design is minimization of the $T$-count and $T$-depth
   (i.e., the number of layers of depth in a circuit which contain a
   $T$ or $T^\dagger$). Many such tools for optimizing quantum circuits are
   automated, however we can work out a simple example by hand. Suppose that we
   want to implement the following circuit:


<img src="pics/t-optimization-before.svg" alt="" width="500px">

That’s an awful lot of $T$s! Implement this same circuit in PennyLane as a QNode
`just_enough_ts`, but minimize the number of $T$ gates by replacing sequences of
them with other gates that have the same effect. Using the gates you learned
before, how much can you simplify this circuit?

Then, answer the following questions:

 - What are the original $T$-count, $T$-depth, and regular depth? 
 - What is the optimal $T$-count? 
 - What are the optimal depth and $T$-depth of the resulting circuit?

Record your answers in the variables provided in the code block below.

*Tip*. Recall that operations can be applied to different qubits by specifying
 the desired index in the `wires` variable.

<details>
  <summary><i>Hint.</i></summary>

If you're not sure where to start making simplifications, consider the
following. $T$, $S$, and $Z$ are all special cases of a rotation. Their rotation
angles are $\pi/4$, $\pi/2$, and $\pi$ respectively. Given these angles, what
would happen if you apply $T$ twice? Or $S$ twice?

</details>