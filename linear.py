from scipy import stats
import pandas as pd 
import collections
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate

loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length

loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range

intLoans = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

loanlength = loansData['Loan.Length'].map(lambda x: x.strip('months'))

loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: x.split('-'))
##loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: x.strip('['))
##loansData['FICO.Range']  = [str(x) for x in loansData['FICO.Range']]
loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: int(x[0]))

print loansData['FICO.Range'][0:5]
