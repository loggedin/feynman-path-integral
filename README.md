# machine-learning

This repository contains scripts that demonstrate various machine learning algorithms.

## gradient-descent.py

This module produces a plot illustrating the different behaviours of the gradient descent method when finding the minima of Rosenbrocks Banana Function. It also gives where the minimum of the function occurs.

	python3 gradient-descent.py

Example output:



When the step size parameter is too small, convergence is very slow. Indeed, despite 10,000 gradient descent steps, the plotted trajectory for this case does not reach the minimum. When the step size is too large, the GD method is unstable as the trajectory either overshoots the minimum or never reaches it at all. Indeed, the plotted trajectory for this case reaches the valley of the function but does not approach the minimum.
