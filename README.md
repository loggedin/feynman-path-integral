# machine-learning

This repository contains scripts that demonstrate various machine learning algorithms.

## gradient-descent.py

This script produces a plot and text illustrating the different behaviours of the gradient descent method when finding the minimum of Rosenbrock's Banana Function. It also gives where the minimum of the function occurs.

	python3 gradient-descent.py

Example output:

![gradient-descent](https://user-images.githubusercontent.com/97130665/150395299-323108c2-81fc-4962-9516-a9455b838d50.png)

When the step size parameter is too small, convergence is very slow. Indeed, despite 10,000 gradient descent steps, the plotted trajectory for this case does not reach the minimum. When the step size is too large, the GD method is unstable as the trajectory either overshoots the minimum or never reaches it at all. Indeed, the plotted trajectory for this case reaches the valley of the function but does not approach the minimum.

## chemotaxis.py

This script produces a simulation of Chemotaxis, a modified random walk used by some bacteria to find food sources.

	python3 chemotaxis.py

Example output:

![chemotaxis](https://user-images.githubusercontent.com/97130665/150395515-b0a66fa5-00b0-4ca2-8a0d-14a7bc5d47b2.png)

The sensitivity of the bacteria, k, cannot be too big. Indeed, when k is very large, the bacteria behave very similarly to the case where k = 0.2: they reach the position of maximum energy density in around fifty seconds. When k is too small, the bacteria take longer to reach the position of maximum energy density. This is because the bacteria are less likely to tumble when the energy density is decreasing.

## newton-raphson.py

This script demonstrates the chaotic behaviour of the Newton-Raphson method.

	python3 newton-raphson.py

Example output:

![newton-raphson](https://user-images.githubusercontent.com/97130665/150395723-2d24309d-741f-494f-8325-bacee6ef067a.png)

The left-hand diagrams show the identified roots for different ranges of seed points; the right-hand diagrams show the number of iterations, or convergence time, to locate the identified roots for these seed points. Both sets of diagrams demonstrate the chaotic behaviour of the respective aspect of the Newton-Raphson method because they are extremely complex. This shows that, although they are completely deterministic, both aspects are highly sensitive to the initial conditions and exhibit topological mixing. Furthermore, the images in the diagrams are said to be fractal in nature because they have self-similarity, that is, they look the same at difference scales. This is shown by the lower diagrams which have different scales to the corresponding diagrams above.

## markov-chain-monte-carlo.py

	python3 markov-chain-monte-carlo.py

Example output:

![markov-chain-monte-carlo](https://user-images.githubusercontent.com/97130665/150395856-b7ace4db-ffda-4710-97bd-8e31ac810dbb.png)

TEXT
