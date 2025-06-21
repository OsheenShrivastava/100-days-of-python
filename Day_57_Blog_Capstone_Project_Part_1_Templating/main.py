
# Hi all this code is exactly same as that of tutor since the code written by me (which was working) was not optimized.
# I did not use jinja for multiline statements which was the task. So this was the ideal code which I wanted to share.

# TODO-1 - Import requests, render_template and Flask modules. Import post class from post.py

from flask import Flask, render_template
from post import Post
import requests


# TODO-2 - Get all json data from blog_url given below

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
all_posts = response.json()


# TODO-3 - Pass these parameters to Post class - post_id, title, subtitle, body and create attributes

# TODO-4 - Pass parameters - id,title,subtitle and body to class Post using FOR loop in order to create them as
#  attributes of the class. These attributes will be called directly in the code using Post object.
#  Append them to a list.

Post_objects = []
for blog_post in all_posts:
    post_obj = Post(blog_post["id"], blog_post["title"], blog_post["subtitle"], blog_post["body"])
    Post_objects.append(post_obj)


# TODO-5 - Initialize Flask

app = Flask(__name__)

# TODO-6 - Create home route and pass Post_objects list as a parameter

# TODO-7 - Inside index.html create a for loop using jinja multiline statements and pass title and subtitle by accessing
#  attributes of Post class. Each item of FOR loop consists of list of all elements of a post in the form of dictionary.
#  So access title and subtitle form it. Additionally call blog_post function and pass id from index.html to this
#  function.


@app.route('/')
def home():
    # Passing a list
    return render_template("index.html", all_posts=Post_objects)

# TODO-8 - Accept the variable blog_id and compare it with data from the list Post_Objects using FOR loop. If blog_id
#   matches any one of Post_Objects id's then pass the entire post to post.html file.

# TODO-9 - Since we had created attributes of Post class now we can directly access them using "post" variable passed
#   in to post.html file. Insert title,subtitle and body in post.html file.


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    post_requested = None
    for post in Post_objects:
        if post.id == blog_id:
            post_requested = post

    return render_template("post.html", post=post_requested)

# TODO-10 - Finally run the app


if __name__ == "__main__":
    app.run(debug=True)