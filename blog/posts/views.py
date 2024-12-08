from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
posts = [
    {
        "id": 1,
        "title": "Python",
        "content": "Used by companies like Google, Microsoft, etc."
    },
    {
        "id": 2,
        "title": "JavaScript",
        "content": "Popular for web development, used by Facebook, Google, etc."
    },
    {
        "id": 3,
        "title": "Django",
        "content": "A Python framework used to build scalable web applications."
    },
    {
        "id": 4,
        "title": "React",
        "content": "A JavaScript library for building user interfaces, maintained by Facebook."
    },
    {
        "id": 5,
        "title": "Node.js",
        "content": "JavaScript runtime built on Chrome's V8 engine, used for backend development."
    }
]

def home(request):
    html= ""
    for post in posts:
        html += f'''<div>
              <a href= ../{post["id"]} >
              <h1>{post["id"]} - {post["title"]},</h1></a>
              <p>{post["content"]}</p>
        </div>'''
    return HttpResponse(html)

def post(request, id):
    html = ""
    valid_id = False
    for post in posts:
        if id == post["id"]:
            html=f'''<h1>{post["id"]} {post["title"]}</h1>
                      <p>{post["content"]}<p>'''
            valid_id = True
            break
    if(valid_id):    
     return HttpResponse(html)
    else:
     return HttpResponseNotFound("Post Not Found Error(404)")