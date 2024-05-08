# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:45:38 2024

@author: abaloraerika
"""

import seaborn as sns
import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt

sns.set(style="darkgrid", palette="muted")


np.random.seed(42)
X = np.linspace(0, 10, 100)
Y_true = 1.0 + 2.0 * X
Y = Y_true + np.random.normal(0, 0.5, size=100)

with pm.Model() as model:
    sigma = pm.HalfCauchy('sigma', beta=10, testval=1.)
    intercept = pm.Normal('Intercept', mu=0, sd=20)
    slope = pm.Normal('slope', mu=0, sd=20)
    
    
    likelihood = pm.Normal('y', mu=intercept + slope * X, sd=sigma, observed=Y)
    
    
    trace = pm.sample(1000, tune=3000, cores=2, return_inferencedata=True)
    

pm.plot_trace(trace)
plt.show()

