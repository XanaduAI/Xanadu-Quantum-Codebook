---

*Tip*. You can also specify a custom observable using
[`qml.Hermitian`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.Hermitian.html). For
example,

```python
# Single-qubit Hermitian observable   
O = np.array([[3, 4i], [-4i, 3]])

@qml.qnode(dev)
def circuit():
    # ...
    return qml.expval(qml.Hermitian(O, wires=0)) 

```

However, one must be careful as specifying an arbitrary observable may make your
circuit incompatible with some simulators and hardware.


In the previous sections, we computed measurement outcome probabilities and
expectation values analytically. Of course, this is impossible to do on
hardware. When we run a circuit and take a measurement, we get a single data
point that tells us in which state we observed a qubit for a particular
run. Since this process is random, in order to get a clearer picture of the
statistics we must perform the experiment many, many times. Each time is
typically called a *shot*, or a *sample*. We can sample from the output
distribution in order to estimate expectation values and measurement outcome
probabilities in situations where it isn't possible to do so analytically.

In PennyLane, the number of shots to take during an experiment is specified upon
device construction:

```python
dev = qml.device('default.qubit', wires=1, shots=1000)
```

---

***Codercise I.10.2.*** In the code below is a list of possible numbers of
   shots.  For each value, initialize a device, then create and QNode that runs
   circuit from the previous exercise (reproduced below for convenience). What
   happens to the expectation value as you increase the number of shots?

<img src="pics/exercise_i101.svg" width="400px">