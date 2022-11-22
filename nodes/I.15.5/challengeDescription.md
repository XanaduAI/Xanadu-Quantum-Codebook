---

Something looks funny here — the output state we see here is a 3-qubit
state. How can we determine the state of the third qubit to check whether
it was correctly teleported?

---

***Codercise I.15.5.*** By working through the theoretical action of the circuit
   (see the accompanying text node for details), you can show that the combined
   state of the three qubits together after the procedure is

$$
\begin{equation}
\frac{1}{2} (\vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle) (\alpha\vert 0\rangle + \beta\vert 1\rangle) 
\end{equation}
$$

With this knowledge, write a function that takes a state vector as input, and
outputs the state of the third qubit as a two-element vector. Does it match the
original state above?