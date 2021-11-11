Let's now consider two electrons in a magnetic field. If they are far away from each other, then the total Hamiltonian (energy) will just be a sum of Hamiltonians:

$$
\hat{H} = \hat{H}_1 + \hat{H}_2 = -\frac{e\hbar B}{2 m_e}(Z_0 + Z_1),
$$

where $Z_0 = Z \otimes I$ is the Pauli $Z$ acting on the first
electron, and $Z_1 = I \otimes Z$ acts on the second. We've indexed
these in the same way wires are indexed in PennyLane. Since the electrons are independent, the unitary which evolves this two-electron system in time is two copies of the unitary $e^{i\alpha t Z}$, $\alpha= Be/2m_e$. In circuit form:

<img src="pics/prod-circ.svg" width="400px">

---

***Codercise H.5.1.*** Complete the function below for simulating two distant electrons in a magnetic field.
