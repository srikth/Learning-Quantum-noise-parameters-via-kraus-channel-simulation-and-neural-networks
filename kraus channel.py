import numpy as np

def amplitude_damping(rho, gamma):
    """
    Apply amplitude damping channel using Kraus operators.
    rho: 2x2 density matrix
    gamma: damping probability (0 to 1)
    """

    E0 = np.array([[1, 0],
                   [0, np.sqrt(1 - gamma)]])

    E1 = np.array([[0, np.sqrt(gamma)],
                   [0, 0]])

    rho_new = E0 @ rho @ E0.conj().T + E1 @ rho @ E1.conj().T
    return rho_new
