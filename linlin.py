from scipy import stats
import numpy as np
import pandas as pd 
import collections
import matplotlib.pyplot as plt
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


def clean_data(df):
    print("Cleaning data")
    df['Interest.Rate'] = df['Interest.Rate'].str.replace('%', '').astype('float')
    df['Loan.Length'] = df['Loan.Length'].str.replace(' months', '').astype('int')
    df['FICO.Score'] = df['FICO.Range'].str.split('-').apply(itemgetter(0)).astype('int')


def linear_regression(loansData):
    print("Extracting series for regression")
    intrate = loansData['Interest.Rate']
    loanamt = loansData['Amount.Requested']
    fico = loansData['FICO.Score']

    # The dependent variable
    print("Creating dependent variable")
    y = np.matrix(intrate).transpose()

    # The independent variables shaped as columns
    print("Creating independent variables")
    x1 = np.matrix(fico).transpose()
    x2 = np.matrix(loanamt).transpose()

    # Put the two columns together to create an input matrix 
    print("Stacking independent variables")
    x = np.column_stack([x1, x2])

    # Create a linear model
    print("Creating linear model")
    X = sm.add_constant(x)
    model = sm.OLS(y, X)
    f = model.fit()
    
    print(dir(f))
    
    # Print results
    print("Printing results")
    print(f.summary())


