from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def project_list(request):
    context = return_covid_data()
    return(render(request, "projects/index.html", context))

def return_covid_data():
    covid_url='https://api.covid19india.org/data.json'
    r = requests.get(covid_url)
    # print(pprint(r.json()['statewise']))
    statewise=r.json()
    return(statewise)