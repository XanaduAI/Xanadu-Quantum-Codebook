---

Having done this manually a few times, you might wonder whether there are any
automated tools to perform such state preparation. PennyLane contains a library
of
[**templates**](https://pennylane.readthedocs.io/en/stable/introduction/templates.html),
some of which perform state preparation. Templates are subroutines that can be
used in quantum circuits just like any other gate:

```python
def my_circuit():
    qml.MyTemplate(parameters, wires)
```

PennyLane contains a template called
[`MottonenStatePreparation`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.MottonenStatePreparation.html),
which will automatically prepare any normalized qubit state vector, up to a
global phase. You need only pass the template a normalized state vector, and a
set of wires.  This is especially convenient for multi-qubit systems, where it
would be challenging to find state preparation circuits by hand.

***Codercise I.8.3.*** Write a QNode that uses `qml.MottonenStatePreparation`
 to prepare the state

$$
\vert v\rangle = (0.52889389-0.14956775i) \vert 0 \rangle + (0.67262317+0.49545818i) \vert 1 \rangle.
$$

Return the state of system. In addition, we'll print the circuit using `qml.draw` to
investigate which operations were actually used under the hood.