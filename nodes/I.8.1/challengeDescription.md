Now that you've learned all about single-qubit gates, you have the tools to
perform arbitrary **quantum state preparation** of a single qubit! State
preparation takes place at the start of many algorithms. There is some target
state we would like the qubit to be in, and we need to figure out the sequence
of operations that, acting on $\vert 0 \rangle$, produces the desired state. Furthermore,
we ideally want this sequence of operations to be as small as possible.

***Codercise I.8.1.*** Write a circuit that prepares the quantum state

$$
\vert \psi \rangle = \frac{1}{\sqrt{2}} \vert 0\rangle +  \frac{1}{\sqrt{2}}  e^{\frac{5}{4}i \pi} \vert 1\rangle
$$

up to a global phase using as few gates as possible.


<details>
  <summary><i>Hint.</i></summary>

First look at the amplitudes of the target state, ignoring the complex
phase. What operation sends $\vert 0 \rangle$ to the state with the correct
amplitudes? Then, determine which operation(s) would add the correct phase.

</details>
