from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):               #Home page
    return HttpResponse("This is a bad request. Start from the music root")
def music(request):     #List of artists
    return HttpResponse("List of Artist: \nProject Pat \nTommy Wright III \nThree 6 Mafia")
def ProP(request):  #Artist1
    return HttpResponse("Project Pat is the G.O.A.T")
def TW(request):  #artist2
    return HttpResponse("This guy here is the godfather of trap music.")
def Three6(request): #artist3
    return HttpResponse("Won an Oscar. Legacy of music in Memphis. What more can you say?")