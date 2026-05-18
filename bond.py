class Bond:
    def __init__(self, maturity: float, ytm: float,  nominal_amount: float, coupon_rate = 0.0):
        self.T = maturity
        self.ytm = ytm
        self.c = coupon_rate
        self.N = nominal_amount

    def get_ytm(self):
        return self.ytm

    def price(self):
        coupon_payment = self.N * self.c

        coupon_price = 0
        for t in range(1, int(self.T )+ 1):
            coupon_price += coupon_payment / ((1 + self.ytm) ** t)

        nominal_price = self.N / ((1 + self.ytm) ** self.T)

        return coupon_price + nominal_price
    
    def macaulay_duration(self):
        P = self.price()
        duration = 0
        coupon = self.N * self.c

        for t in range(1, int(self.T) + 1):
            cf = coupon
            if t == self.T:
                cf += self.N 

            
            duration += t * ( cf / (1 + self.ytm) ** t)

        return duration / P
    
    def modified_duration(self):
        return self.macaulay_duration() / (1 + self.ytm)
    
    def convexity(self):
        P = self.price()
        coupon = self.N * self.c
        convexity_sum = 0

        for t in range(1, int(self.T) + 1):
            cf = coupon

            if t == int(self.T):
                cf += self.N

            convexity_sum += t * (t + 1) * cf / ((1 + self.ytm) ** (t + 2))

        return convexity_sum / P