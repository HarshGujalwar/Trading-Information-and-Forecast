from django.shortcuts import render

from .predictors import predict,accuracy

def Welcome(request):
    return render(request,'Webpage.html')
def User(request):
    ticker = request.GET['ticker']
    tomorrow=False
    tomorrow,acc= predict(ticker)
    if tomorrow:
        ans = "UP"
    else:
        ans = "DOWN"
    return render(request,'user.html',{'ticker':ans,'accuracy':acc})