# machine-learning-theoretical

This repository contains scripts that demonstrate the inner workings of various machine learning algorithms.

## markov-chain-monte-carlo.py

In the Feynman Path Integral formulation of quantum mechanics, the value of the quantum mechanical propagator can be evaluated numerically by discretising time.

If the t-axis is split into N slices and the endpoints of the paths are held fixed as x, then the quantum mechanical propagator can be rewritten as

![equation](https://user-images.githubusercontent.com/97130665/150843644-0c135e37-6f42-4ec1-9168-e565dbc9c63b.png)

where E denotes the summed energy along the path.

A Markov Chain Monte Carlo method can be used to evaluate the multi-dimensional integral above. Specifically, the Metropolis-Hastings algorithm:

1. Generate a uniformly random number, ζ, between −ε and ε;
2. Perturb the first path element by ζ;
3. Calculate the resulting change in energy along the path, ∆E;
4. If ∆E < 0: accept change;
5. If ∆E > 0: generate a uniformly random number, η, between 0 and 1 and only accept the change if e^(−∆E > η);
6. Repeat the above steps for all path elements.

This script simulates a particle of mass m = 1 constrained to the x-axis and subject to the potential V(x) = x^2 / 2.

	python3 markov-chain-monte-carlo.py

Example output:

![markov-chain-monte-carlo](https://user-images.githubusercontent.com/97130665/150395856-b7ace4db-ffda-4710-97bd-8e31ac810dbb.png)
