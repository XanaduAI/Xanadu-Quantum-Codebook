---

**Learning outcomes**:
    
 - *Identify the different components of a quantum circuit (qubits, gates, and measurements).*
 - *Translate between sequences of instructions and a quantum circuit.*
 - *Define and calculate the depth of a quantum circuit.*
 
---

Now that we've seen what qubits are, an important next step is to discuss how
quantum computations are expressed. Quantum computation involves manipulating
and measuring these qubits in a meaningful way. But first, we need a way of
writing down quantum algorithms and protocols, ideally in a way that is portable
and not specific to any particular hardware or programming language.

**Quantum circuits** are a way to visually depict the sequence of operations
  that are performed on qubits throughout the course of a computation. You can
  think of quantum circuits like a recipe, or set of instructions that tells you
  what to do to each qubit, and when to do it. By placing and performing the
  operations in a certain way, we can realize different quantum algorithms.

The following is an example of a real quantum circuit:

<img src="pics/sample-circuit.svg" alt="" width="400px">

(If you've ever studied Boolean logic circuits in a computer science course,
you'll find that quantum circuits look quite similar.)

In this section, we'll take a look at quantum circuits in general. We'll learn
how to read them, and how to build them from a set of abstract operations. The
next section will show you an example of a circuit being used as part of a
quantum algorithm, focusing on the well-known quantum teleportation
protocol. Following that, you'll learn more details about what the operations
actually look like and what they do to the qubits.

## Wires and registers

A circuit starts with a collection of **wires** that represent a set of
qubits. Qubits are ordered from top to bottom, and typically labelled
numerically in the same order. We will label starting from 0 to match most quantum programming frameworks.
A group of qubits together is called a **quantum
register**.

<img src="pics/sample-circuit-empty.svg" alt="" width="400px">

The qubits have to start somewhere, in the sense that they must be initialized
to some state at the beginning of a computation. A typical choice is for all
qubits to start in state $\vert 0\rangle$, but this may not always be the
case. Therefore, it is common in circuit diagrams to indicate the initial states
explicitly, like so:

<img src="pics/sample-circuit-initial-states.svg" alt="" width="300px">

*Tip*. If the initial state is not given explicitly, it is typically safe to
 assume that all qubits start in state $\vert 0\rangle$.

## Gates and operations

Operations on qubits are often called **gates**. There are many different types
of gates, which have different effects on the qubits. Some gates affect only one
qubit at a time, whereas others might affect two (or more!) qubits.

As a starting point, in the circuits below, we'll represent different types of
gates by different shapes. A shape on a wire indicates a gate acting on the
specified qubit at that point in time. On that note, *quantum circuits are read
from left to right*. For example, in the diagram below we are first applying a
triangle gate to each of qubits 0 and 2, followed by a rectangle gate that acts
on both qubits 0 and 1 while a circle gate acts on qubit 2, etc.

<img src="pics/sample-circuit-shape-gates.svg" alt="" width="400px">

Quantum operations that act on separate qubits can be applied in *parallel*. For
example, note that the pentagon on qubit 0 can be "pushed" to the left, and
applied at the same time as the rectangle on qubits 1 and 2:

<img src="pics/sample-circuit-shape-gates-push-left.svg" alt="" width="600px">

We can do this when there is empty space in a circuit, provided that we maintain
the chain of dependency of the gates. For example, we could not move the
rectangle on qubits 0 and 1 any earlier, because the triangle on qubit 0 has to
occur first, even though qubit 1 is not doing anything in the meantime. We can
thus visualize a circuit as a sequence of layers.

<img src="pics/sample-circuit-layers.svg" alt="" width="400px">

This brings us to a very important measure of quantum circuits: the **circuit
depth**. The depth of a quantum circuit is the minimum number of non-overlapping
layers. (For the readers who enjoy graph theory, circuits are typically
represented in software by directed, acyclic graphs where the nodes are the
gates, and edges represent the qubits involved in each gate. The longest path in
this graph is the circuit depth.)

A more fun way to visualize depth is to think of the circuit gates as lego
bricks, and consider what would happen if we were to build the corresponding
structure. The length of that structure would be the depth of the circuit! For
example, building the circuit from the set of gates shown below allows us to
clearly see that it has depth 6.

<img src="pics/lego-circuit.svg" alt="" width="600px">

## Measurements

The final step of any quantum computation is a measurement of one or more of the
qubits - after all, we need to get the answer out somehow. A measurement is
depicted in a circuit as a box with a dial, as shown below.

<img src="pics/sample-circuit-shape-gates-measurements.svg" alt="" width="400px">

While the measurements look like a "layer" of the circuit, they are not counted
in the calculation of depth.

---

***Exercise I.2.1.*** Draw the circuit diagram for a 4-qubit circuit from the following set of instructions:
 - Initialize all the qubits in $\vert 0\rangle$
 - Apply a circle operation to qubit 0
 - Apply a circle operation to qubit 2
 - Apply a triangle operation to qubit 2
 - Apply a triangle operation to qubit 3
 - Apply a rectangle operation between qubits 0 and 1
 - Apply a rectangle operation between qubits 1 and 2
 - Apply a rectangle operation between qubits 2 and 3
 - Measure all the qubits

<details>
  <summary><i>Solution.</i></summary>

This is what the circuit will look like in its most compact form.


<img src="pics/exercise-circuit.svg" alt="" width="400px">

<div align="right"> ▢ </div>

</details>

---

***Exercise I.2.2.*** What is the depth of the circuit in the previous exercise?


<details>
  <summary><i>Solution.</i></summary>

The depth of this circuit is 4. ▢

</details>

---