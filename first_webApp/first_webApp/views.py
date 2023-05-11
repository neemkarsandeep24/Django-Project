from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    # data={
    #     't':'Welcome Home!',
    #     'b':"Khan Academy!",
    #     'details':[
    #     {'name':'aarya','ph':123},
    #     {'name':'jain','ph':456}
    #     ],
    #     'numbers':[1,2,3,4,5,6,7,8,9],

    # }
    return render(request,"index.html")

def tictac(request):
    return render(request,"tictactoe.html")

def album(request):
    return render(request,"album.html")

def wordle(request):
    return render(request,"wordle.html")