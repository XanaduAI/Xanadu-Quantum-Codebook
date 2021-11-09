(b) Now implement the second-order approximation to $e^{tU}$,

$$
I + tU + \frac{1}{2}t^2U^2 = U^0 + t\left(U^1 + \frac{1}{2}tU^2\right).
$$

Now ``aux = [0, 1]`` and ``main = 2``. The trick here is to create a circuit corresponding to the term in brackets:

<img src="pics/lcu-nest2.svg" width="650px">

In other words, we have a *controlled subcircuit* realizing this second term.

*Tip.* You can create controlled subcircuits using [``qml.ctrl``](https://pennylane.readthedocs.io/en/stable/code/api/pennylane.ctrl.html). Unfortunately, we can't specify the control string, so we need to put an $X$ on either side of the control node.
