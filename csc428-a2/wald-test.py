# Written by Chat GPT. It looks simple enough so I think it's correct?
import pandas as pd
import statsmodels.api as sm

# Load the Excel file
data = pd.read_csv("sim_data.csv")

# Define the dependent (Y) and independent (X) variables
Y = data['attempted']
X = data['received_email']

# Add a constant for the intercept in the logistic regression
X = sm.add_constant(X)

# Fit the logistic regression model
model = sm.Logit(Y, X).fit()

# Perform the Wald test (by inspecting p-values of coefficients)
print(model.summary())
