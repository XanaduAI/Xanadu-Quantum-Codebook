Let's briefly recap what we've achieved. We had a lock with solution
$\mathbf{s}$, and in the quantum context, we landed on the strategy of
amplifying the amplitude of the state $\vert \mathbf{s}\rangle$,
starting in the uniform superposition $\vert\psi\rangle$. The easiest
way to do this was to apply first the oracle, and then the diffusion
operator. Grover search simply consists of applying this a number of
times. In order to implement this as a real circuit using elementary gates, we added an
auxiliary qubit and used the phase kickback trick. Finally, we
generalized to the context of multiple solutions, simply by using the
multi-solution oracle.

The result is a practically useful quantum algorithm which
quadratically outperforms its classical counterpart, i.e., taking
$O(\sqrt{N})$ steps to break a lock with $N = 2^n$ possible
combinations, instead of $O(N)$.
In the multi-solution cases, we've just empirically demonstrated that
the running time is $O(\sqrt{N/M})$.
We really can break locks with our quantum computer now!

