Now that you've run your very first quantum algorithm, you might be wondering
whether there's a cleaner way of representing things than vectors and matrix
multiplication. In the next few exercises, we'll abstract away the linear
algebra, and explore how to use PennyLane to implement quantum algorithms. In
tandem, you'll start playing with quantum circuits.

**Quantum circuits** are a common means of visually representing the sequence of
operations that are performed on qubits during a quantum computation.  They
consist of a set of operations, or **gates**, applied to a set of qubits (or
more generally, **wires**). Each wire in the diagram represents a
qubit. Circuits are read from left to right, and this is the order in which
operations are applied. Quantum circuits end in a **measurement** of one or more
qubits. For example, the circuit below has 3 qubits that start in state $\vert
0\rangle$, applies 5 operations, and measures every qubit at the end.

<img src="pics/circuit_i-2-1.svg" alt="" width="400px">

In PennyLane, a quantum circuit is represented by a **quantum function**. These
are just regular Python functions, with some special properties: they must apply
one or more quantum operations, and return one or more quantum measurements.
Expressing quantum circuits as quantum functions allows us to represent circuits
compactly, and use regular programming concepts such as subroutines
(subcircuits), loops, and input parameters.

Suppose we would like to write a circuit for 2 qubits. By default in PennyLane,
qubits (wires) are ordered numerically starting from 0 (which corresponds to the
top qubit in the circuit). In pseudocode, a quantum function looks something
like this:

<code>

    import pennylane as qml

    def my_quantum_function(params):

        # Single-qubit operations with no input parameters
        qml.Gate1(wires=0)
        qml.Gate2(wires=1)

        # A single-qubit operation with an input parameter
        qml.Gate3(params[0], wires=0)

        # Two-qubit operation with no input parameter on wires 0 and 1
        qml.TwoQubitGate1(wires=[0, 1])
    
        # Two-qubit operation with an input parameter on wires 0 and 1
        qml.TwoQubitGate2(params[1], wires=[0, 1])

        # Return the result of a measurement
        return qml.Measurement(wires=[0, 1])

</code>

You can see how operations on qubits are applied one per line. Each
operation indicates which qubits it acts on, and some operations also
take input parameters.

<i>Tip.</i> PennyLane uses the term `wires` rather than `qubits` because
it also supports continuous-variable quantum computing, for which a wire
in a circuit does not correspond to a qubit.

---

***Codercise I.2.1.*** The code below is a quantum function with all the gates
   from the above circuit (which we reproduce here for convenience). However,
   the gates are out of order! Re-arrange the lines of the function to match the
   order of operations in the circuit.

<img src="pics/circuit_i-2-1.svg" alt="" width="400px">


<details>
  <summary><i>Hint.</i></summary>

Deduce which line of code corresponds to which gate by looking at the labels in the
circuit diagram, and the wires each gate acts on.

</details>