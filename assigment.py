from bond import Bond

def task1a(bond: Bond):
    print("Bond price:", bond.price())

def task1b(bond: Bond):
    print("Bond duration", bond.macaulay_duration())

def task1c(bond: Bond):
    print("Bond modified duration", bond.modified_duration())


if __name__ == "__main__":
    bond = Bond(maturity=6.0, ytm =0.03,nominal_amount=12000, coupon_rate=0.05 ) 
    task1a(bond)
    task1b(bond)
    task1c(bond)