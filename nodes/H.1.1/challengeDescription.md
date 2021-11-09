Fundamentally, quantum computing is different from classical computing
because of the physical laws working "under the hood" of the
computer. To understand quantum computing in this light, it's useful
to treat Nature as a sort of black box.
It takes an initial condition as an input,
evolves it using physical laws, and outputs experimental data (aka
*measurements*) at the end. We can try to infer the laws of Nature
from looking at the pattern of input conditions and output
measurements. 

<img src="pics/nature.svg" width="700px">

Let's start with a simple *deterministic* warm-up example, where the same input always leads to the same output.

<img src="pics/deterministic.svg" width="450px">

In the code box below, you can print the result of applying the box to
an aribtrary input using ``secret_box(bits)``.

---

***Codercise H.1.1.*** Generate some examples using the provided code and guess the secret deterministic rule.
