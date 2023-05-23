from django.shortcuts import render
import joblib
import pickle
from sklearn import *

def home(request):
    return render(request,"home.html")

def getPrediction(age,menopause,tumorSize,invNodes,nodeCaps,degMalig):
    model = pickle.load(open("predition.sav", "rb"))
    prediction = model.predict([[age,menopause,tumorSize,invNodes,nodeCaps,degMalig]])

    if prediction == 0:
        return "No recurrence"
    else:
        return "Recurrence"

def index(request):
    return render(request,"index.html")

def result(request):

    age = float(request.GET['age'])
    menopause = int(request.GET['menopause'])
    tumorSize = int(request.GET['tumorSize'])
    invNodes = int(request.GET['invNodes'])
    nodeCaps = int(request.GET['nodeCaps'])
    degMalig = int(request.GET['degMalig'])

    result = getPrediction(age,menopause,tumorSize,invNodes,nodeCaps,degMalig)
    list = [age,tumorSize,invNodes,nodeCaps,degMalig]

    print(list)
    return render(request,"result.html",{'result':result,'list':list})
