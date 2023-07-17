
    
def predict(tick):
    import yfinance as yf
    import pandas as pd
    import math
    ticker = yf.Ticker(tick)
    data = ticker.history(period="10y")
    data = data.loc["1990-01-01":].copy()
    del data["Dividends"]
    del data["Stock Splits"]
    data["Tomorrow"] = data["Close"].shift(-1)
    data["Target"] = (data["Tomorrow"]>data["Close"].astype(int))
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100,min_samples_split=100,random_state=1)
    train=data.iloc[:-1]
    test = data.iloc[-1:]
    train_acc=data.iloc[:-100]
    test_acc = data.iloc[-100:]
    predictors= ["Close","Volume","Open","High","Low"]
    model.fit(train_acc[predictors],train_acc["Target"])
    preds = model.predict(test_acc[predictors])
    preds=pd.Series(preds,index=test_acc.index)
    from sklearn.metrics import precision_score
    acc = precision_score(test_acc["Target"],preds)
    acc*=100
    model.fit(train[predictors],train["Target"])
    tomorrow = model.predict(test[predictors])
    ans=tomorrow[0]
    acc=math.floor(acc)
    return ans,acc

def accuracy(tick):
    import yfinance as yf
    import pandas as pd
    import math
    ticker = yf.Ticker(tick)
    data = ticker.history(period="10y")
    data = data.loc["1990-01-01":].copy()
    del data["Dividends"]
    del data["Stock Splits"]
    data["Tomorrow"] = data["Close"].shift(-1)
    data["Target"] = (data["Tomorrow"]>data["Close"].astype(int))
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100,min_samples_split=100,random_state=1)
    train=data.iloc[:-100]
    test = data.iloc[-100:]
    predictors= ["Close","Volume","Open","High","Low"]
    model.fit(train[predictors],train["Target"])
    preds = model.predict(test[predictors])
    preds=pd.Series(preds,index=test.index)
    from sklearn.metrics import precision_score
    acc = precision_score(test["Target"],preds)
    acc*=100
    return math.floor(acc)