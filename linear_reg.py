from scipy import stats
import numpy as np
import pandas as pd 
import collections
import matplotlib.pyplot as plt
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loanlength = loansData['Loan.Length'].map(lambda x: x.strip('months'))
loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: x.split('-'))
loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: int(x[0]))

loansData['FICO.Score'] = loansData['FICO.Range']

print loansData['FICO.Score'][0:5]
print loansData['Interest.Rate'][0:5]
print loansData['Amount.Requested'][0:5]

intrate = 	loansData['Interest.Rate']
loanamt = 	loansData['Amount.Requested']
fico = 		loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()

# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

#put the two columsn together to create an input matrix
x = np.column_stack([x1,x2])

#create a linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print "summary"
print f.summary()

print "other stuff"

print 'Coefficients: ', f.params[1:]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared
print "Final model: 'Interest Rate = " + str(round(f.params[0])) + " + " + str(f.params[1]) + "*fico" + ' + ' + str(f.params[2]) + "*loanamt"



