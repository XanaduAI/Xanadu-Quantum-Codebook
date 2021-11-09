*Solution*. Unsurprisingly, you'll find that as you increase the number of
 shots, the results will approach the true value of -0.707.

---

What happens under the hood in the exercise above is that the circuit is run
multiple times, and a measurement is made, yielding one of the two eigenvalues
($1$ or $-1$). We can use the results of these samples to compute the
expectation value in the same way as we would normally take a *weighted
average*, i.e.,

$$
\langle Y \rangle = \frac{1 \cdot (\text{num. 1s}) + (-1) \cdot (\text{num. -1s})}{\text{num_shots}}. \tag{1}
$$

In PennyLane, we can access samples directly by returning `qml.sample`
rather than `qml.expval`.

```python
@qml.qnode(dev)
def my_circuit():
    # ...    
    return qml.sample(qml.PauliZ(wires=0))
```

---

***Codercise I.10.3.*** Using the circuit from earlier, replace the `qml.expval`
   measurement with `qml.sample`. Then, write a function to compute an estimate of the
   expectation value based on the samples.