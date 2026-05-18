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


if __name__ == "__main__":
    bond = Bond(maturity=6.0, ytm =0.03,nominal_amount=12000, coupon_rate=0.05 ) 
    var = VaR(bond, sigma = 0.04, mu = 0)
    task1a(bond)
    task1b(bond)
    task1c(bond)
    tasl1d(bond)
    task2(var, 1.645)
