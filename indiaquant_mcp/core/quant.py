import numpy as np
from scipy.stats import norm

class Quant:
    def calculate(self, S, K, days, sigma, r):
        if days <= 0 or sigma <= 0: return {"error": "Invalid days/vol"}
        T = days / 365.0
        d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        
        # Define the variables here so the dictionary can see them
        delta = norm.cdf(d1)
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        theta = -(S*norm.pdf(d1)*sigma)/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2)
        vega = S * norm.pdf(d1) * np.sqrt(T)
        
        return {
            "delta": round(float(delta), 3), 
            "gamma": round(float(gamma), 4), 
            "theta_per_day": round(float(theta/365), 3), 
            "vega_per_1pct": round(float(vega/100), 3)
        }
