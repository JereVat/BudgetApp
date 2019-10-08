import numpy as np
from decimal import Decimal

def calculate(net_income, saving_time, target_wealth, beginning_wealth, target_interest):
    inflation = 0.011
    beginning_wealth = int(beginning_wealth)
    target_wealth = int(target_wealth)
    target_interest = 5 / 100 - inflation
    saving_time_m = int(saving_time) * 12
    target_intereset_m = float(target_interest) / 12
    result = abs(np.pmt(target_intereset_m, saving_time_m, beginning_wealth, target_wealth, 1))
    # result = target_intereset_m / ((1 + target_intereset_m)**saving_time_m - 1) * (beginning_wealth * (1 + target_intereset_m)**saving_time_m + target_wealth) / (1 + target_intereset_m)
    result = Decimal(result)
    result = round(result, 2)
    return result