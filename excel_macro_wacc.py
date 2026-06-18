pip install yfinance
import pandas as pd
import numpy as np
import yfinance as yf
#weights
b=input("Which companies WACC do you want to calculate? : ")
a=yf.Ticker(b)
equity=(a.info['previousClose']*a.info['sharesOutstanding'])
debt=(a.info['totalDebt'])
marketcap=debt+equity
c=equity/marketcap
d=debt/marketcap
#Cost of equity
riskfreerate=0.0686
beta=a.info['beta']
q="^NSEI"
n=yf.Ticker(q)
erm=n.info['previousClose']
capm=0.4349
#cost of debt
t=0.2517
pretax=0.1
wacc=round((c*capm)+(d*pretax*(1-t))*100,2)
print("The WACC for",b,"is",wacc,"%")
