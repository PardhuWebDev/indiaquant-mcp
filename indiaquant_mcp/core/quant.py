import numpy as np
from scipy.stats import norm

class Quant:
    def get_greeks(self, S, K, days, sigma, r):
        # Prevent crash if days or volatility is 0
        if days <= 0 or sigma <= 0:
            return {"delta": 0, "gamma": 0, "theta": 0, "vega": 0}

        T = days / 365.0
        # Math for d1 and d2
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        
        # Calculate Greeks
        delta = norm.cdf(d1)
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)
        vega = S * norm.pdf(d1) * np.sqrt(T)
        
        return {
            "delta": round(float(delta), 3),
            "gamma": round(float(gamma), 4),
            "theta": round(float(theta / 365), 3),
            "vega": round(float(vega / 100), 3)
        }