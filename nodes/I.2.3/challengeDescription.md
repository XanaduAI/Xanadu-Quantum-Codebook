---

*Tip*. At this point, you might be wondering what these operations are being
 applied *to*; after all, quantum functions are simply a list of operations, and
 there is no quantum state present like there was in our single-qubit simulator
 from earlier. All the linear algebra, and maintenance of state, happens under
 the hood in PennyLane on the devices. This enables you to focus more on your
 quantum algorithm, and less on the implementation details!

The second way to construct a QNode in PennyLane is using a
**decorator**. Decorating a quantum function with ``@qml.qnode(dev)`` will
automatically produce a QNode with the same name as your function that can be
run on the device `dev`. Try it below!

---

***Codercise I.2.3.*** The quantum function below implements the circuit from
   the previous exercise. Apply a decorator to the quantum function to construct
   a QNode, then run it using the provided input parameters.