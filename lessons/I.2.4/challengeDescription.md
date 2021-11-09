---

Quantum circuits are algorithms. Just like how we profile code, and study the
complexity and resource requirements of regular algorithms and software, we can
do the same for quantum circuits to make sure we implement them as efficiently
as possible. The number of gates, and the type of gates, are useful
metrics. However, one particularly important metric is that of **circuit
depth**. Loosely, the depth is the number of time steps it takes for a circuit to
run, if we do things as in-parallel as possible. Alternatively, you can think of
it as the number of layers in a circuit.

For example, remember our circuit from the previous section:

<img src="pics/circuit_i-2-2.svg" alt="" width="400px">

---

***Codercise I.2.4.*** What is the depth of the circuit in the picture above?


<details>
  <summary><i>Hint.</i></summary>

If you're not sure, try using the `qml.specs` function to compute some useful
properties of your circuit:

<code>

    # resource_calculator will compute the resources of the QNode `my_qnode`
    resource_calculator = qml.specs(my_qnode)

    # we pass it the same parameters as the original QNode
    theta, phi, omega = 0.1, 0.2, 0.3
    print(resource_calculator(theta, phi, omega))

</code>

</details>