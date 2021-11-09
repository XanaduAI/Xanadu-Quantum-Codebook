Each time you run this code block, you'll obtain a different set of samples, and
thus a different estimate for the expectation value. An interesting question,
then, is given a certain number of shots, how close should we expect to get? You
can gain some intuition for this by completing the exercise below.

---

***Codercise I.10.4.*** Using the code below as a starting point, explore how
   the accuracy of the expectation value depends on the number of shots. For
   example, if we run 100 experiments with 100 shots each, what are the mean and
   variance of the distribution of expectation values obtained? How does this
   variance scale with the number of shots?

   To accomplish this, we will use a very simple circuit that consists of a
   Hadamard and a measurement of the `qml.PauliZ` observable, which will allow
   us to directly extract the dependence of the variance on the number of
   shots. We will plot your results; based on the plot, complete the
   `variance_scaling` function below to define the relationship between variance
   and shots.