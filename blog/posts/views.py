from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
posts = [
    {
        "id": 1,
        "title": "Getting Started with Java",
        "author": "John Smith",
        "p_date": "2024-11-01",
        "content": """Java is a powerful, object-oriented programming language that is widely used in a variety of applications, from mobile apps to large-scale enterprise systems. 
                      This post is designed for beginners who are just starting their journey with Java. We will walk through the installation of the Java Development Kit (JDK), 
                      setting up your environment, and writing your first "Hello, World!" program. You'll also learn about basic concepts like variables, data types, 
                      operators, and control flow in Java. By the end of this post, you should have a good understanding of the fundamentals of Java programming."""
    },
    {
        "id": 2,
        "title": "Python for Beginners",
        "author": "Jane Doe",
        "p_date": "2024-11-05",
        "content": """Python is one of the most popular programming languages in the world, known for its simplicity, readability, and versatility. 
                      Whether you’re interested in web development, data science, or automation, Python is the language for you. 
                      In this blog post, we’ll start from the very basics, including how to install Python, understand Python syntax, and write your first Python script. 
                      You'll also learn about Python’s powerful libraries that make it easy to handle complex tasks. If you're a beginner, this post will help you lay a solid foundation."""
    },
    {
        "id": 3,
        "title": "Introduction to Node.js",
        "author": "Michael Brown",
        "p_date": "2024-11-10",
        "content": """Node.js is a runtime environment that allows developers to run JavaScript on the server side. This means that you can use JavaScript for both front-end and back-end development. 
                      In this post, we’ll discuss how to set up Node.js, the basics of writing a simple server, and introduce you to the concept of non-blocking, asynchronous programming in Node.js. 
                      We’ll also explore the advantages of using Node.js for building fast and scalable network applications, and how its event-driven architecture is ideal for I/O-heavy tasks."""
    },
    {
        "id": 4,
        "title": "Advanced Java Concepts",
        "author": "Alice Green",
        "p_date": "2024-11-15",
        "content": """This post is intended for Java developers who want to dive deeper into more advanced concepts. We’ll cover topics such as multithreading, 
                      which allows you to perform multiple tasks simultaneously, memory management, and garbage collection in Java. 
                      You’ll also learn about the Java Virtual Machine (JVM) and how it manages the execution of Java programs. 
                      By understanding these advanced concepts, you’ll be able to write more efficient and optimized code, especially for large-scale applications."""
    },
    {
        "id": 5,
        "title": "Python Libraries for Data Science",
        "author": "Sophia White",
        "p_date": "2024-11-20",
        "content": """Python is widely used in the field of data science, thanks to its rich ecosystem of libraries. In this post, we’ll introduce some of the most essential Python libraries for data science, including NumPy, Pandas, and Matplotlib. 
                      You’ll learn how to manipulate large datasets using Pandas, perform complex mathematical operations with NumPy, and visualize your data with Matplotlib. 
                      Whether you’re cleaning data, performing analysis, or building machine learning models, these libraries are indispensable tools for any data scientist."""
    },
    {
        "id": 6,
        "title": "Building REST APIs with Node.js",
        "author": "David Lee",
        "p_date": "2024-11-25",
        "content": """RESTful APIs are a crucial part of modern web applications, and Node.js makes it easy to build scalable APIs. In this post, we’ll show you how to set up a REST API using Node.js and Express.js. 
                      You’ll learn about HTTP methods such as GET, POST, PUT, and DELETE, and how to implement these in your API to handle CRUD (Create, Read, Update, Delete) operations. 
                      We’ll also discuss how to manage routing, handle incoming data, and connect your API to a database for persistent data storage."""
    },
    {
        "id": 7,
        "title": "Java Design Patterns",
        "author": "Ethan Scott",
        "p_date": "2024-11-30",
        "content": """Design patterns are a crucial part of software development, and understanding them will make you a better Java programmer. In this post, we’ll cover some of the most important design patterns in Java, 
                      including Singleton, Factory, Observer, and Strategy patterns. We’ll explain the purpose of each pattern and provide examples of how to implement them in Java. 
                      By using design patterns, you can write more maintainable and scalable code, and handle recurring design problems with proven solutions."""
    },
    {
        "id": 8,
        "title": "Web Scraping with Python",
        "author": "Emma Davis",
        "p_date": "2024-12-01",
        "content": """Web scraping allows you to extract data from websites, and Python provides several libraries to help you with this task. 
                      In this post, we’ll introduce you to BeautifulSoup and Scrapy, two of the most popular web scraping libraries in Python. 
                      You’ll learn how to set up a basic web scraper, parse HTML content, and extract specific information from web pages. 
                      We’ll also discuss ethical considerations when scraping websites and how to avoid getting blocked by sites."""
    },
    {
        "id": 9,
        "title": "Asynchronous Programming in Node.js",
        "author": "Olivia Martinez",
        "p_date": "2024-12-05",
        "content": """One of the key strengths of Node.js is its ability to handle asynchronous programming. This means that you can perform tasks without blocking the main thread, making your applications more efficient and scalable. 
                      In this post, we’ll explore different asynchronous patterns in Node.js, including callbacks, promises, and async/await. 
                      We’ll also discuss how to avoid common pitfalls, such as callback hell, and how to use async/await to write cleaner, more readable code."""
    }
]



def home(request):
    # print(reverse('home'))
    # html= ""
    # for post in posts:
    #     html += f'''<div>
    #           <a href= ../{post["id"]} >
    #           <h1>{post["id"]} - {post["title"]},</h1></a>
    #           <p>{post["content"]}</p>
    #     </div>'''
    # return HttpResponse(html)
    return render(request, "posts/index.html", {"posts":posts})

def post(request, id):
    # html = ""
    valid_id = False
    for post in posts:
        if id == post["id"]:
            # html=f'''<h1>{post["id"]} {post["title"]}</h1>
            #           <p>{post["content"]}<p>'''
            valid_id = True
            break
    if(valid_id):    
     return render(request, "posts/blog.html", {"post":post})
    else:
     return HttpResponseNotFound("Post Not Found Error(404)")
    
def google(request, id):
      url = reverse("post", args = [id])
      return HttpResponseRedirect(url)

# def global1(request):
#    return render(request , "global.html")