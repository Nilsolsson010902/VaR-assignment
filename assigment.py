from bond import Bond
from var import VaR

def task1a(bond: Bond):
    print("Bond price:", bond.price())

def task1b(bond: Bond):
    print("Bond duration", bond.macaulay_duration())

def task1c(bond: Bond):
    print("Bond modified duration", bond.modified_duration())

def tasl1d(bond: Bond):
    print("Bond convexity:", bond.convexity())

def task2(var: VaR, Z: float):
    print( var.delta_normal(Z))

def task3(var: VaR):
    print("\n--- Monte Carlo Simulation VaR ---")

    delta_var = var.simulated_delta_var(confidence=0.95,n=1000)

    delta_gamma_var = var.simulated_delta_gamma_var(confidence=0.95, n=1000)

    print("Simulated delta VaR:", delta_var)
    print("Simulated delta-gamma VaR:", delta_gamma_var)


if __name__ == "__main__":
    bond = Bond(maturity=6.0, ytm =0.03,nominal_amount=12000, coupon_rate=0.05 ) 
    var = VaR(bond, sigma = 0.02, mu = 0)
    task1a(bond)
    task1b(bond)
    task1c(bond)
    tasl1d(bond)
    task2(var, 1.645)
    task3(var)
