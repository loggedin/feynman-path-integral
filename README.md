# machine-learning

This repository contains scripts that demonstrate various machine learning algorithms.

## gradient-descent.py

This module produces a plot illustrating the different behaviours of the gradient descent method when finding the minima of Rosenbrocks Banana Function. It also gives where the minimum of the function occurs.

	python3 gradient-descent.py

Example output:

![gradient-descent](https://user-images.githubusercontent.com/97130665/150220262-e714bb9e-edc6-4083-984a-7e195fc07ded.png)

When the step size parameter is too small, convergence is very slow. Indeed, despite 10,000 gradient descent steps, the plotted trajectory for this case does not reach the minimum. When the step size is too large, the GD method is unstable as the trajectory either overshoots the minimum or never reaches it at all. Indeed, the plotted trajectory for this case reaches the valley of the function but does not approach the minimum.

## chemotaxis.py

This module produces a simulation of Chemotaxis, a modified random walk used by some bacteria to find food sources.

	python3 chemotaxis.py

Example output:

![chemotaxis](https://user-images.githubusercontent.com/97130665/150219755-7b9ce3e3-cd9a-4bab-a01e-4983051be5be.png)

The sensitivity of the bacteria, k, cannot be too big. Indeed, when k is very large, the bacteria behave very similarly to the case where k = 0.2: they reach the position of maximum energy density in around fifty seconds. When k is too small, the bacteria take longer to reach the position of maximum energy density. This is because the bacteria are less likely to tumble when the energy density is decreasing.
