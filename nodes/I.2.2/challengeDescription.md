---

While quantum circuits are represented as quantum functions, a quantum function
alone isn't enough to run and execute a circuit. For this we need two extra
parts:

 - a device to run the circuit on
 - a QNode, which binds the circuit to the device, and executes it

In this book, our devices will be **quantum simulators**, but PennyLane provides
**plugins** that enable us to run on real quantum hardware as well! To construct
a device in PennyLane, we need to know the name or type of the device, and the
number of qubits (wires) it has:

<code>

    dev = qml.device('device.name', wires=num_qubits)

</code>


In this section, we will always be using the `default.qubit` device, which is a
standard quantum simulator. You can also give string labels to the wires on a
device.

<code>

    dev = qml.device('default.qubit', wires=["wire_a", "wire_b"])

</code>

Once we have a device, we can construct a [`QNode`](https://docs.pennylane.ai/en/stable/code/api/pennylane.QNode.html). QNodes are the main unit of
quantum computation in PennyLane. 

<img src="pics/qnode.svg" alt="" width="600px">

There are two ways to construct a QNode from a device and a quantum function. The
first, which you will see in the next exercise, is using the `qml.QNode` function:

<code>

    my_qnode = qml.QNode(my_circuit, my_device)

</code>

Once a QNode is created, it can be called like a function using the same
parameters as the quantum function upon which it's built.

---

***Codercise I.2.2.*** Complete the quantum function in the PennyLane code below
   to implement the following quantum circuit. We'll then construct a QNode, and
   run the circuit on the provided device.

<img src="pics/circuit_i-2-2.svg" alt="" width="400px">

<details>
  <summary><i>Hint.</i></summary>

The mapping between the parameters in the circuit diagram and the parameters
of the circuit in the code are $\theta \rightarrow$ `theta`, $\varphi \rightarrow$ `phi`,
and $\omega \rightarrow$ `omega`.

</details>