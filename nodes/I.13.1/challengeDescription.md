In this node we'll meet a number of other common controlled operations. We start
with the **controlled-$Z$** operation; this behaves just like $CNOT$, except
we apply a $Z$ on a target qubit instead of an $X$. In a circuit, it's
represented like so (the first is more common):

<img src="pics/cz.svg" width="200px">

In PennyLane, it's available as [`qml.CZ`](https://docs.pennylane.ai/en/stable/code/api/pennylane.CZ.html),
and can be called in the same way as `qml.CNOT`.

```python
def circuit():
    qml.CZ(wires=[control, target])
```

---

***Codercise I.13.1.*** Earlier we learned how to create a $Z$ gate using $X$
   and $H$. A similar circuit identity can be constructed for the controlled-$Z$ gate,
   using the controlled-$X$ ($CNOT$) and $H$ gates. Complete the function `imposter_cz`
   below to reveal the relationship.