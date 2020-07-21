from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title_page(request, title):


    if util.get_entry(title) is None:
        return render(request, "encyclopedia/error.html",{
        "message": "Title does not exist."
        })
    else:
        return render(request, "encyclopedia/title_page.html",{
            "entry":markdown2.markdown(util.get_entry(title)),
            "title":title
        })

def random_title(request):

    entries = util.list_entries();
    count = len(entries)
    num = random.randint(0,count-1)
    return render(request, "encyclopedia/title_page.html",{
        "entry":markdown2.markdown(util.get_entry(entries[num])),
        "title":entries[num]
    })

def search(request):
    if request.method == "POST":
        entries = util.list_entries()

        title = request.POST.get("title")
        res = [string for string in entries if title.lower() in string.lower()]

        if util.get_entry(request.POST.get("title")):
            return render(request, "encyclopedia/title_page.html",{
                "entry":markdown2.markdown(util.get_entry(request.POST.get("title"))),
                "title":title
            })
        elif res:
            return render(request, "encyclopedia/index.html", {
                "entries": res
            })
        else:
            return render(request, "encyclopedia/error.html",{
            "message": "Title does not exist."
            })

def edit(request,title):
    return render(request, "encyclopedia/edit.html",{
        "content":util.get_entry(title),
        "title":title
    })

def update(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(title, content)
        return render(request, "encyclopedia/title_page.html",{
            "entry":markdown2.markdown(util.get_entry(title)),
            "title":title
        })

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html",{
            "message": "Title already exist."
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/title_page.html",{
                "entry":markdown2.markdown(util.get_entry(title)),
                "title":title
            })
    else:
        return render(request, "encyclopedia/add.html")
