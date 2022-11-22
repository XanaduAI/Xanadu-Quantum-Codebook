*(b)* Now that we know how to produce the two basis states, we can perform a
measurement in that basis. To do so, we must apply the adjoint of these
operations to rotate back from that basis to the computational one. Using your
quantum function from the previous exercise, perform the basis rotation and
return determine the measurement outcome probabilities.

You can call the two functions, `prepare_psi` and `y_basis_rotation`, directly.
You do not need to redefine them here.

<details>
  <summary><i>Hint.</i></summary>

Recall that you can take the adjoint in PennyLane using [`qml.adjoint()`](https://docs.pennylane.ai/en/latest/code/api/pennylane.adjoint.html)
like so,

```python
def my_circuit():
    qml.adjoint(function)(params)
```

where `function` can be a single quantum gate, or an entire quantum function.

</details>