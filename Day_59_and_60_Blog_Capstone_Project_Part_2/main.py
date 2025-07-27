# TODO-1 - Import Flask module
# TODO-4 - Import render_template
from flask import Flask, render_template, request
import requests
from smtplib import SMTP

API_ENDPOINT = "Your Endpoint"

MY_EMAIL = "Your Email"
PASSWORD = "Your Password"

response = requests.get(url=API_ENDPOINT)
print(response.raise_for_status())
data = response.json()
print(data)

# TODO-2 - Initialize Flask with the root file
app = Flask(__name__)


# TODO-3 - Add the decorator function for home page / home route

@app.route("/")
def home():
    # TODO-5 - Return the render_template index.html
    return render_template("index.html", all_posts=data)


# TODO-13 - Add a decorator function for about page

@app.route("/about")
def about():
    return render_template("about.html")


# TODO-14 - Add a decorator function for contact page

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        Name = data["name"]
        Email = data["email"]
        Phone = data["phone"]
        Message = data["message"]

        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            Email_message = f"Subject:New Message\n\n Name: {Name} \n Email: {Email} \n Phone: {Phone} \n Message: {Message}"
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="Your Email", msg=Email_message)

        return render_template("contact.html", message_sent=True)
    else:
        return render_template("contact.html", message_sent=False)


@app.route("/post/<int:id_no>")
def get_post(id_no):
    for post in data:
        if post["id"] == id_no:
            print(post)
            return render_template("post.html", post=post)


# @app.route('/form-entry', methods=["POST"])
# def receive_data():
#     data = request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phone"])
#     print(data["message"])
#     return f"<h1> Successfully sent your message </h1>"


# TODO-6 - Run the app
if __name__ == "__main__":
    app.run(debug=True)

# TODO-7 - Remove the <head> & navigation code from index.html and place it in the header.html file.
# TODO-8 - Remove the <footer> from index.html and place it in the footer.html file.
# TODO-9 - Use {% include "header.html" %} and {% include "footer.html" %} to add files in index.html
# TODO-10 - Fix the header in HEADER.html so that the styling and bootstrap all appear.
#  Add {{ url_for('static', filename='css/styles.css') }} in the head section link. We are adding 'static' since it is
#  under static folder and we need to run a dynamic url.
# TODO-11 - Fix the footer resources so that the Javascript works. The navbar disappears off the top of the page when
#  you scroll down, but it reappears as soon as you start scrolling upwards - and it stays there until you scroll down
#  again i.e., the white division with header should get highlighted when moving to top from bottom. Add
#  <script src=" {{ url_for('static', filename='js/scripts.js') }}"></script> to footer.html.
# TODO-12 - Add background image to page header section in index.html using
#   style="background-image: url('static/assets/img/home-bg.jpg')"
# TODO-15 - Add url link for about and contact pages in header.html as {{ url_for('about') }} and
#  {{ url_for('contact') }}. If you directly try adding about.html or contact.html in header.html file then error will
#  occur.
# TODO-16 - Include {% include "header.html" %} and {% include "footer.html" %} so that both pages have similar
#  properties as that of main page i.e., index.html
# TODO-17 - Create your own JSON bin with npoint.io. Click on "Create JSON Bin".
# TODO-18 - Paste below data to the bin
# [
#     {
#         "id": 1,
#         "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
#         "title": "The Life of Cactus",
#         "subtitle": "Who knew that cacti lived such interesting lives.",
#         "image_url": "https://i1.wp.com/blog.plantdelights.com/wp-content/uploads/2015/08/Ferocactus-wislizeni-A3AZ-028-in-flower.jpg",
#         "date":"June 30th 2025",
#         "author":"Osheen Shrivastava",
#     },
#     {
#         "id": 2,
#         "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.",
#         "title": "Top 15 Things to do When You are Bored",
#         "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
#         "image_url": "https://c2.staticflickr.com/4/3026/2838434910_d770a0bb94_z.jpg?zz=1",
#         "date":"July 7th 2025",
#         "author":"Osheen Shrivastava",
#     },
#     {
#         "id": 3,
#         "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.",
#         "title": "Introduction to Intermittent Fasting",
#         "subtitle": "Learn about the newest health craze.",
#         "image_url": "https://dinnerthendessert.com/wp-content/uploads/2019/11/Fruit-Cake-Muffins-16x9.jpg",
#         "date":"July 12th 2025",
#         "author":"Osheen Shrivastava",
#     }
# ]
# TODO-19 - Save the file and copy the endpoint given below. Save it.
# TODO-20 - Import requests module, copy your API endpoint and save it in a variable.
# TODO-21 - Using requests module get hold of the JSON data at the above API endpoint in main.py and pass it to
#  index.html.
# TODO-22 - Use the data from the API to render the home page, replacing the title, subtitle, author and dates of each
#  blog post with the data from the API. (Add fields as necessary to your document.) Keep only 1 post structure and
#  delete the rest. Add FOR loop to the post structure and extract data from all_posts. Add title,subtitle,date and
#  author.
# TODO-23 - Add the background image home_2-bg.jpg to page header in index.html or you can just add the image url.
#  Change the heading and subheading as given.
# TODO-24 - Delete head,navigation and footer from post.html and include it from header and footer html files.
# TODO-25 - Add url for get_post function and pass id in index.html using {{ url_for('get_post', id_no=post.id) }}.
# TODO-26 - Add a decorator function for post,accept variable id_no from index.html and pass it in get_post() function.
# TODO-27 - Run FOR loop and find out the post referring to the id_no from data. Once found pass it in post.html file.
# TODO-28 - In post.html replace title,subtitle,author,date and body using post variable passed i.e., post.title,
#  post.subtitle,post.author,post.date and post.body.
# TODO-29 - Add image for all post by extracting image url form data and adding it as background image using
#  url('{{ post.image_url }}')
# TODO-30 - Add background image for about and contact pages using url('static/assets/img/about-bg.jpg') and
#  url('static/assets/img/contact-bg.jpg' in the header section of background image.
# TODO-31 - Replace the below form tag with current form tage of contact.html

# Current Form tag
# <form id="contactForm" data-sb-form-api-token="API_TOKEN">
#     <div class="form-floating">
#         <input class="form-control" id="name" type="text" placeholder="Enter your name..." data-sb-validations="required" />
#         <label for="name">Name</label>
#         <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
#     </div>
#     <div class="form-floating">
#         <input class="form-control" id="email" type="email" placeholder="Enter your email..." data-sb-validations="required,email" />
#         <label for="email">Email address</label>
#         <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
#         <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
#     </div>
#     <div class="form-floating">
#         <input class="form-control" id="phone" type="tel" placeholder="Enter your phone number..." data-sb-validations="required" />
#         <label for="phone">Phone Number</label>
#         <div class="invalid-feedback" data-sb-feedback="phone:required">A phone number is required.</div>
#     </div>
#     <div class="form-floating">
#         <textarea class="form-control" id="message" placeholder="Enter your message here..." style="height: 12rem" data-sb-validations="required"></textarea>
#         <label for="message">Message</label>
#         <div class="invalid-feedback" data-sb-feedback="message:required">A message is required.</div>
#     </div>
#     <br />
#     <!-- Submit success message-->
#     <!---->
#     <!-- This is what your users will see when the form-->
#     <!-- has successfully submitted-->
#     <div class="d-none" id="submitSuccessMessage">
#         <div class="text-center mb-3">
#             <div class="fw-bolder">Form submission successful!</div>
#             To activate this form, sign up at
#             <br />
#             <a href="https://startbootstrap.com/solution/contact-forms">https://startbootstrap.com/solution/contact-forms</a>
#         </div>
#     </div>
#     <!-- Submit error message-->
#     <!---->
#     <!-- This is what your users will see when there is-->
#     <!-- an error submitting the form-->
#     <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3">Error sending message!</div></div>
#     <!-- Submit Button-->
#     <button class="btn btn-primary text-uppercase disabled" id="submitButton" type="submit">Send</button>
# </form>

# New form tag which needs to be replaced with current one
# <form id="contactForm" name="sentMessage">
#     <div class="form-floating">
#       <input class="form-control" id="name" name="name" type="text" placeholder="Enter your name..."required/>
#       <label for="name">Name</label>
#     </div>
#     <div class="form-floating">
#       <input class="form-control" id="email" name="email" type="email" placeholder="Enter your email..." required/>
#       <label for="email">Email address</label>
#     </div>
#     <div class="form-floating">
#       <input class="form-control" id="phone" name="phone" type="tel" placeholder="Enter your phone number..." required/>
#       <label for="phone">Phone Number</label>
#     </div>
#     <div class="form-floating">
#       <textarea class="form-control" id="message" name="message" placeholder="Enter your message here..." required style="height: 12rem"></textarea>
#       <label for="message">Message</label>
#     </div>
#     <br />
#     <button class="btn btn-primary text-uppercase" id="submitButton" type="submit"> Send </button>
# </form>

# TODO-32 - Add a "/form-entry" route in main.py to receive data from the form from contact.html.
# TODO-33 - In contact.html add action="/form-entry" method="post" to post data at "/form-entry" route.
# TODO-34 - In main.py for "/form-entry" route add methods=["POST"] to post data at the route. Return a string to check
#  the function.
# TODO-35 - Once you have tested the "post" method then combine the /contact route with /form-entry so that they are
#  both under the route "/contact" but depending on which method (GET/POST) that triggered the route. Modify
#  action="/contact" in contact.html inside form tag.
# TODO-36 - Use request.method to check which method triggered the route. if request.method == 'POST': then return the
#  form data else return contact.html file.
# TODO-37 - Instead of returning a <h1> that says "Successfully sent message", update the contact.html file so that the
#  <h1> on the contact.html file becomes "Successfully sent your message". Pass a parameter message_sent as True when
#  form is filled else pass it as False to contact.html.
# TODO-38 - In contact.html add this
#   {% if message_sent: %}
#       <h1>Successfully sent your message</h1>
#   {% else %}
#       <h1>Contact Me</h1>
#   {% endif %}
#   where originally <h1>Contact Me</h1> is placed.
# TODO-39 - Import smtplib. If the form is filled then send an email with all the information.
