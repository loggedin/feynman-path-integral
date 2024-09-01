# metropolis-algorithm

In the Feynman Path Integral formulation of quantum mechanics, the value of the quantum mechanical propagator can be evaluated numerically by discretising time.

If the $t$-axis is split into $N$ slices and the endpoints of the paths are held fixed as $x$, then the quantum mechanical propagator can be rewritten as

$$
\langle \ x | e^{-\hat{H}(t_f - t_i)} | x \ \rangle = A \int_{-\infty}^{\infty} dx_1 \dots dx_{N-1} e^{- \frac{t_f - t_i}{N} E[x]},
$$

where $E$ denotes the summed energy along the path and $A$ is a normalisation constant.

A Markov Chain Monte Carlo method can be used to evaluate the multi-dimensional integral above. Specifically, the Metropolis-Hastings algorithm:

1. Generate a uniformly random number, $\zeta$, between $-\epsilon$ and $\epsilon$;
2. Perturb the first path element by $\zeta$;
3. Calculate the resulting change in energy along the path, $\Delta E$;
4. If $\Delta E < 0$: accept change;
5. If $\Delta E > 0$: generate a uniformly random number, $\eta$, between $0$ and $1$ and only accept the change if $e^{−∆E} > \eta$;
6. Repeat the above steps for all path elements.

This script simulates a particle of mass $m = 1$ constrained to the $x$-axis and subject to the potential $V(x) = x^2 / 2$.
