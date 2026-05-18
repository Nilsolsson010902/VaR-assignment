from bond import Bond
import numpy as np

class VaR:

    def __init__(self, bond: Bond, sigma: float, mu: float):
        self.bond = bond
        self.sigma = sigma
        self.mu = mu

    def delta(self):
        return self.bond.modified_duration()*self.bond.get_ytm()
    
    def gamma(self):
        return self.bond.convexity() * self.bond.get_ytm()**2
    
    def delta_normal(self, Z: float):
        return abs((-self.delta())*self.sigma*Z* self.bond.price())
    
    def simulate_y_tilde(self, n=1000):
        return np.random.normal(self.mu, self.sigma, n)
    
    
    def simulated_delta_var(self, confidence=0.95, n=1000):
        y_tilde = self.simulate_y_tilde(n)
        x = -self.delta() * y_tilde
        threshold = np.percentile(x, (1 - confidence) * 100)
        return abs(threshold) * self.bond.price()
    
    def simulated_delta_gamma_var(self, confidence=0.95, n=1000):
        y_tilde = self.simulate_y_tilde(n)
        x = -self.delta() * y_tilde + 0.5 * self.gamma() * y_tilde**2
        threshold = np.percentile(x, (1 - confidence) * 100)
        return abs(threshold) * self.bond.price()