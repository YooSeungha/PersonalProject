from re import template
from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

def connect_db():
    client = MongoClient(host='192.168.0.138', port=27017)
    db = client['restaurants']
    return db, client


def check_data(col):
    count = 0
    data_list = []
    for data in col.find().sort("_id").limit(10):
        name = data.get("name")
        addr = data.get("info")[2]
        count +=1
        data_list.append([name,addr])
    return data_list, count
    # print(count)


def index(request):
    #template = loader.get_template("index.html")
    db, client = connect_db()
    col = db["info_list"]
    data_list, count = check_data(col)
    context = {

        'data_list': data_list,
        'count': count,
    }
    return render(request, "index.html", context)
    #return HttpResponse(template.render({}, request))


def detail(request):
    
    context = {
    }
    return render(request, "detail.html", context)


def favors(request):
    
    context = {   
    }
    return render(request, "favors.html", context)