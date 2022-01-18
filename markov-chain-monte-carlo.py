from __future__ import division
import numpy
import numpy.random
import matplotlib.pyplot as pyplot

# Set the values of the following constants
m = 1							# Mass of the particle
T = 4							# Time interval
N = 7							# Number of time steps
a = T / N
epsilon = 1.4					# Maximum changes to a path element
N_cf = 1000						# Number of saved paths
N_cor = 20						# Number of intervening sweeps
x_min, x_max = 0, 2				# Bounds of x-axis
x_spacing = 0.1					# x-axis spacing

def E(path):
	'''This function returns the summed energy along a path.'''
	# Initialise the path energy
	path_energy = 0
	for i in range(1, N + 1):
		# Calculate the energy at the i-th time step
		kinetic_energy = m / 2 * ((path[i] - path[i - 1]) / a) ** 2
		potential_energy = 1 / 2 * ((path[i] + path[i - 1]) / 2) ** 2
		step_energy =  kinetic_energy + potential_energy
		# Add this to the path energy
		path_energy = path_energy + step_energy
	return path_energy

def update(path):
	'''This function applies the Metropolis Algorithm to a path.'''
	# Create an array which is exactly the same as path
	updated_path = numpy.zeros((len(path)))
	for i in range(len(updated_path)):
		updated_path[i] = path[i]
	for i in range(1, N):
		# Store the initial path and corresponding path energy
		initial_xi = updated_path[i]
		initial_path_energy = E(updated_path)
		# Replace the i-th element of the path
		updated_path[i] = updated_path[i] + numpy.random.uniform(-epsilon, epsilon)
		# Store the new path and corresponding path energy
		new_xi = updated_path[i]
		new_path_energy = E(updated_path)
		# Calculate the change in path energy
		d_path_energies = new_path_energy - initial_path_energy
		# Retain or discard i-th element of the path
		if d_path_energies > 0:
			if numpy.exp(-d_path_energies) < numpy.random.uniform(0, 1):
				updated_path[i] = initial_xi
	return updated_path

def G(x):
	'''This function uses the Metropolis Monte Carlo algorithm to return the value of the propagator. It also returns the associated error.'''
	# Initialise the path
	path = numpy.random.uniform(x_min, x_max, N + 1)
	path[0] = x
	path[-1] = x
	# Thermalise the path
	for i in range(10 * N_cor):
		path = update(path)
	# Store N_cf paths
	stored_paths = numpy.zeros((N_cf, N + 1))
	for i in range(N_cf):
		stored_paths[i, :] = path
		# Keep only every N_cor-th path
		for j in range(N_cor):
			path = update(path)
	# Calculate the mean value of the integrand and its associated error
	integrands = numpy.zeros((N_cf))
	for i in range(N_cf):
		integrands[i] = numpy.exp(- a * E(stored_paths[i, :]))
	mean_integrand = numpy.mean(integrands)
	err_integrand = numpy.std(integrands) / (N_cf) ** 0.5
	# Calculate the value of G and its associated error
	G = (x_max - x_min) ** (N - 1) * mean_integrand
	G_err = (x_max - x_min) ** (N - 1) * err_integrand
	return numpy.array([G, G_err])

def schrodinger_solution(x):
	'''This function returns the Scroedinger probability distribution function for a 1D harmonic oscillator in the ground state.'''
	return (numpy.exp(- 0.5 * x ** 2) / numpy.pi ** 0.25) ** 2

pyplot.figure()
pyplot.title("Ground State of the 1D Harmonic Oscillator")
pyplot.ylabel("PDF")
pyplot.xlabel("x")

# Discretise the x-axis
x_values = numpy.arange(x_min, x_max + x_spacing, x_spacing)

# Calculate the corresponding values of G and their associated errors
G_values = numpy.zeros((len(x_values), 2))
for i in range(len(x_values)):
	G_values[i, :] = G(x_values[i])
# Calculate the value of Z and its associated error
Z = 0
for i in range(len(x_values)):
	Z = Z + x_spacing * G_values[i, 0]
Z_err = (numpy.sum(G_values[:, 1] ** 2)) ** 0.5
# Calculate the corresponding values of the probability distribution function and their associated errors
pdf_values = numpy.zeros((len(x_values), 2))
pdf_values[:, 0] = G_values[:, 0] / (2 * Z)
for i in range(len(x_values)):
	pdf_values[i, 1] = pdf_values[i, 0] * ((G_values[i, 1] / G_values[i, 0]) ** 2 + (Z_err / Z) ** 2) ** 0.5
y_values = pdf_values[:, 0]
y_err = pdf_values[:, 1]
pyplot.errorbar(x_values, y_values, yerr = y_err, capsize = 3, elinewidth = 1, markeredgewidth = 1, color = "blue", label = "path integral solution")

pyplot.plot(x_values, schrodinger_solution(x_values), color = "grey", label = "Schroedinger solution")

print("The value of the PDF at x = 1 is {}.".format(pdf_values[int((len(x_values) - 1) / 2), 0]))

pyplot.legend()
pyplot.show()