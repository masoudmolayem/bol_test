from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    """
        View to retrieve a list of tasks with 'Completed' status.
    """
    url="https://legendary-toffee.herokuapp.com/search?queryId=31&userId=dummyuser"
    response = requests.get(url).json()
    return render(request, "sample.html", response)
