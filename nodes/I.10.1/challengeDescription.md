Rather than simply measuring outcome probabilities, when solving physical
problems, we need to compute a measurable quantity that relates to some property
of the system. Such properties are called **observables**. Mathematically,
observables correspond to Hermitian matrices, i.e., matrices $B$ such that
$B=B^\dagger$. Each observable has some set of possible measurement outcomes,
corresponding to their real eigenvalues. However, since measurement is
probabilistic, we usually want to look for the **expectation value**, denoted by
$\langle B \rangle$, of that physical property.


It is very straightforward to compute expectation values in PennyLane. We can
simply replace the
[`qml.probs`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.probs.html)
of the previous sections with
[`qml.expval`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.expval.html),
and specify the observable to be measured. Common choices are
[`qml.PauliX`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.PauliX.html),
[`qml.PauliY`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.PauliY.html),
and
[`qml.PauliZ`](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.PauliZ.html),
as many algorithms that solve physical problems require computing the
expectation values of the Pauli operators. The possible outcomes of measuring
any Pauli-based expectation value are either $1$ or $-1$, as these are their
eigenvalues.

*Tip.* These three Pauli operators are unitary *and* Hermitian. They
can therefore be used both as gates in circuits, and considered as observables.

To measure an expectation value in PennyLane, we must specify which observable
we are measuring, and which wires it acts on.  For example, if we wanted to
return a measurement of the `PauliZ` observable acting on a single qubit, we
would write

```python
@qml.qnode(dev)
def my_circuit():
    # ...    
    return qml.expval(qml.PauliZ(wires=0))
```

*Tip*. It is usually more convenient to use the shorthand `qml.PauliZ(0)` 
when specifying expectation values. Otherwise, the lines of code will get
quite long when you get to the multi-qubit case!



---

***Codercise I.10.1.*** Design and run a PennyLane circuit that performs the
   following, where $\langle Y \rangle$ indicates measurement of the `PauliY`
   observable.

<img src="pics/exercise_i101.svg" width="400px">