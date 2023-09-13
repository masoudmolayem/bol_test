from django.shortcuts import render
import requests
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    """
        View to retrieve a list of tasks with 'Completed' status.
    """
    url="https://legendary-toffee.herokuapp.com/search?queryId=31&userId=dummyuser"
    response = requests.get(url).json()

    rendered_html = render_to_string("sample.html", response)
    # Save the rendered HTML to a file
    # with open("rendered_sample.html", "w") as file:
    #     file.write(rendered_html)
    return render(request, "sample.html", response)
