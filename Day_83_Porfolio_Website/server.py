
# TODO-1 - Import Flask, render_template, redirect, url_for from flask module
# TODO-2 - Initialize Flask with app and create a home route.
# TODO-3 - Render template index.html.
# TODO-4 - Run the app.
# TODO-5 - Add Bootstrap CDN links since we will be using Templates.
# TODO-6 - Create Section 1 using table. Add table rows and then insert table data. Profile pic along with name and
#  designation is added. One line intro is added too.
# TODO-7 - Add a divider of your choice. I have taken ready made dividers you can choose your own. Add the divider
#  after every section except for the last one.
# TODO-8 - For Section 2 I have used built-in Bootstrap template called Carousel and edited my data.
# TODO-9 - For Section 3 I have used another Bootstrap template called Product and edited my data.
# TODO-10 - I have add a footer using Bootstrap template for footers and edited my data.
# TODO-11 - I have added a header using Bootstrap template which consists of contact button. When clicked it redirects
#  to contact page.
# TODO-12 - Import FlaskForm from flask_wtf. Import StringField, SubmitField from wtforms. Import DataRequired from
#  wtforms.validators. Import Bootstrap5 from flask_bootstrap. Import SMTP from smtplib.
# TODO-13 - Create ContactForm using FlaskForm. Create email,message and submit firlds with validators = required.
# TODO-14 - create a secret key for flask application to generate CRSF (Cross-Site Request Forgery) tokens. It’s an
#  attack where a malicious site tricks a user into submitting a request (like a form) to your website without their
#  knowledge.
# TODO-15 - Initialize Bootstrap5. In contact.html add {% from 'bootstrap5/form.html' import render_form %}. Load
#  {{ bootstrap.load_css() }} in head section. Render form {{ render_form(form) }} in body section.
# TODO-16 - Create an object contact_form from ContactForm class. On submit retrieve the data i.e., email and message
#  from the form. Using SMTP send email to yourself with the user's email and message. Once done redirect to home page.
# TODO-17 - Create a link to "Osheen Tech" in index.html and create a route "/osheentech_page" which renders
#  "osheentech.html".
# TODO-18 - I have used Bootstrap template Cover to create Navbar & Hero and to display "Osheen Tech" and info about it.
# TODO-19 - Features template for About Section.
# TODO-20 - Album template for Services and Footer section.
# TODO-21 - Do add Bootstrap CDN links.
# TODO-22 - Back button redirects to home page.



from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from smtplib import SMTP

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField(label="Submit")

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)

my_email = "pythontestmail123456@gmail.com"
password  = "tjjw wylh iski ptxp"


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print("Successfully submitted form")

        Final_Email = contact_form.email.data
        Final_Message = contact_form.message.data

        print(Final_Email)
        print(Final_Message)

        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Contact Msg \n\n Email:{Final_Email} \n Message:{Final_Message}"
            )
        return redirect(url_for('home'))

    return render_template("contact.html", form=contact_form)

@app.route("/osheentech_page")
def osheentech_page():
    return render_template("osheentech.html")


if __name__ == '__main__':
     app.run(debug=True)