from django.shortcuts import render
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from django.http import JsonResponse
from django.core import serializers

import statistics
import numpy as np
from pmdarima import auto_arima
from statsmodels.tsa.stattools import adfuller
from .models import (
    BlogPost
)

# Create your views here.


def index(request):
    dd =  BlogPost.objects.all()

    context = {
        'blog':dd
    }
    

    return render(request,'index.html',context)


def map_filter(request):
    df  =  pd.read_csv('terraclimate.csv')
    print(str(df.head()))
    # group panda for ploting because the data was too large
    grouped_data = (df.groupby(['Year'], as_index=False).mean())
    grouped_data.head()
    all_dat = df.iloc[:,:3]
    all_dat.head()
    all_dat['date'] = all_dat['Year'].astype(str)+"-"+all_dat['Month'].astype(str)+"-"+"1"
    all_dat.head()
    all_data = all_dat.iloc[:,2:]
    all_data['date'] = all_data['date'].astype('datetime64[ns]')
    all_data.head()
    arima_model_tmax = ARIMA(np.array(all_dat['tmax']), order=(2,0,2))
    model2 = arima_model_tmax.fit()

    # request.session['model_2'] = model2


    index_future_prediction = pd.date_range(start="2020-12-1",end="2022-01-30")
    print(len(index_future_prediction))

    pred2 = model2.predict(start=len(all_dat['tmax']),end=len(all_dat['tmax'])+ 425,typ='levels')

    changed = pd.DataFrame(pred2, columns = ['Generated_tmax'])
    changed.index = index_future_prediction
    ln = changed.tail(30)
    m = []
    for a in ln.index:
        m.append(str(a.strftime('%Y-%m-%d')))
        print(a.strftime('%Y-%m-%d'))
    print(m)


    context = {
        'y_data':list(ln['Generated_tmax']),
        'x_data':m
       
    }

    if request.method == "POST":
        print(request.POST)
        lenth = request.POST.get('lenth')
        start_date =  request.POST.get('startdate')
        end_date = request.POST.get('enddate')

        df  =  pd.read_csv('terraclimate.csv')
        print(str(df.head()))
        # group panda for ploting because the data was too large
        grouped_data = (df.groupby(['Year'], as_index=False).mean())
        grouped_data.head()
        all_dat = df.iloc[:,:3]
        all_dat.head()
        all_dat['date'] = all_dat['Year'].astype(str)+"-"+all_dat['Month'].astype(str)+"-"+"1"
        all_dat.head()
        all_data = all_dat.iloc[:,2:]
        all_data['date'] = all_data['date'].astype('datetime64[ns]')
        all_data.head()
        arima_model_tmax = ARIMA(np.array(all_dat['tmax']), order=(2,0,2))
        model2 = arima_model_tmax.fit()

        # request.session['model_2'] = model2


        index_future_prediction = pd.date_range(start=start_date,end=end_date)
        print(len(index_future_prediction))
        cc = len(index_future_prediction) -1

        pred2 = model2.predict(start=len(all_dat['tmax']),end=len(all_dat['tmax'])+ cc,typ='levels')

        changed = pd.DataFrame(pred2, columns = ['Generated_tmax'])
        changed.index = index_future_prediction
        ln = changed.tail()
        m = []
        for a in ln.index:
            m.append(str(a.strftime('%Y-%m-%d')))
            print(a.strftime('%Y-%m-%d'))
        print(m)


        context = {
            'y_data':list(ln['Generated_tmax']),
            'x_data':m
        
        }
        return render(request,'map_page.html',context)
    

    return render(request,'map_page.html',context)





def precipitation_prediction(request):
    df  =  pd.read_csv('terraclimate.csv')
    print(str(df.head()))
    # group panda for ploting because the data was too large
    grouped_data = (df.groupby(['Year'], as_index=False).mean())
    grouped_data.head()
    all_dat = df.iloc[:,:5]
    all_dat.head()
    all_dat['date'] = all_dat['Year'].astype(str)+"-"+all_dat['Month'].astype(str)+"-"+"1"
    all_dat.head()
    all_data = all_dat.iloc[:,2:]
    all_data['date'] = all_data['date'].astype('datetime64[ns]')
    all_data.head()
    arima_model_tmax = ARIMA(np.array(all_dat['ppt']), order=(2,0,2))
    model2 = arima_model_tmax.fit()

    # request.session['model_2'] = model2


    index_future_prediction = pd.date_range(start="2020-12-1",end="2022-01-30")
    print(len(index_future_prediction))

    pred2 = model2.predict(start=len(all_dat['ppt']),end=len(all_dat['ppt'])+ 425,typ='levels')

    changed = pd.DataFrame(pred2, columns = ['Generated_tmax'])
    changed.index = index_future_prediction
    ln = changed.tail(30)
    m = []
    for a in ln.index:
        m.append(str(a.strftime('%Y-%m-%d')))
        print(a.strftime('%Y-%m-%d'))
    print(m)


    context = {
        'y_data':list(ln['Generated_tmax']),
        'x_data':m
       
    }

    if request.method == "POST":
        print(request.POST)
        lenth = request.POST.get('lenth')
        start_date =  request.POST.get('startdate')
        end_date = request.POST.get('enddate')

        df  =  pd.read_csv('terraclimate.csv')
        print(str(df.head()))
        # group panda for ploting because the data was too large
        grouped_data = (df.groupby(['Year'], as_index=False).mean())
        grouped_data.head()
        all_dat = df.iloc[:,:5]
        all_dat.head()
        all_dat['date'] = all_dat['Year'].astype(str)+"-"+all_dat['Month'].astype(str)+"-"+"1"
        all_dat.head()
        all_data = all_dat.iloc[:,2:]
        all_data['date'] = all_data['date'].astype('datetime64[ns]')
        all_data.head()
        arima_model_tmax = ARIMA(np.array(all_dat['ppt']), order=(2,0,2))
        model2 = arima_model_tmax.fit()

        # request.session['model_2'] = model2


        index_future_prediction = pd.date_range(start=start_date,end=end_date)
        print(len(index_future_prediction))
        cc = len(index_future_prediction) -1

        pred2 = model2.predict(start=len(all_dat['ppt']),end=len(all_dat['ppt'])+ cc,typ='levels')

        changed = pd.DataFrame(pred2, columns = ['Generated_tmax'])
        changed.index = index_future_prediction
        ln = changed.tail()
        m = []
        for a in ln.index:
            m.append(str(a.strftime('%Y-%m-%d')))
            print(a.strftime('%Y-%m-%d'))
        print(m)


        context = {
            'y_data':list(ln['Generated_tmax']),
            'x_data':m
        
        }
        return render(request,'ppt.html',context)
    

    return render(request,'ppt.html',context)
