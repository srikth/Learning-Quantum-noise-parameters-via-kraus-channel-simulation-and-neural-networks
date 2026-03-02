import numpy as np
from kraus_channel import amplitude_damping

def random_pure_state():
    """Generate random 1-qubit pure state density matrix."""
    psi = np.random.randn(2) + 1j * np.random.randn(2)
    psi = psi / np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    return rho

def generate_dataset(samples=2000):
    X = []
    y = []

    for _ in range(samples):
        rho = random_pure_state()
        gamma = np.random.uniform(0, 0.5)

        rho_noisy = amplitude_damping(rho, gamma)

        # Use real + imaginary parts flattened
        features = np.hstack([
            rho_noisy.real.flatten(),
            rho_noisy.imag.flatten()
        ])

        X.append(features)
        y.append(gamma)

    return np.array(X), np.array(y)
