from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'
Bootstrap5(app)

ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class CreatePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired()])
    body = CKEditorField('Blog Content')
    submit = SubmitField('Submit Post')


@app.route('/')
def get_all_posts():
    # TODO-1 - Query the database for all the posts. Convert the data to a python list.

    # READ RECORDS
    read_all_posts = db.session.execute(db.select(BlogPost))
    posts = read_all_posts.scalars().all()

    return render_template("index.html", all_posts=posts)


# TODO-2 - Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO-3 - Retrieve a BlogPost from the database based on the post_id

    # READ A PARTICULAR RECORD
    requested_post = db.session.get(BlogPost, post_id)

    return render_template("post.html", post=requested_post)


# TODO-8 - add_new_post() to create a new blog post. Add url_for add_new_post() in index.html. Render form in
#  make-post.html.
@app.route('/new_post', methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()

    if form.validate_on_submit():
        # CREATE RECORD
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            author = form.author.data,
            img_url = form.img_url.data,
            body = form.body.data,
            date = date.today().strftime("%B %d,%Y"),
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    # TODO-4 - Add this ckeditor = CKEditor(app) to initialize ckeditor.
    # TODO-5 - Create a class called CreatePostForm and add all the fields of form.
    # TODO-6 - Add body using CKEditor like this: body = CKEditorField('Body')
    # TODO-7 - Add {{ ckeditor.config(name='body') }} in make-post.html to load body.
    # TODO-8 - Once the form is submitted then create a new record in db with the form data and save it.
    # TODO-9 - Add date in the format: August 31, 2019 <full month name> <date number>, <full year> using datetime
    #  module.

    return render_template("make-post.html", form=form)


# TODO-10 - edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # READ A PARTICULAR RECORD
    post = db.session.get(BlogPost, post_id)

    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )

    # UPDATE RECORDS
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data

        db.session.commit()

        return redirect(url_for('show_post', post_id=post_id))

    # TODO-11 - Add {{ url_for('edit_post', post_id=post.id) }} in post.html in <a> tag for Edit Post.
    # TODO-12 - Add a route for edit-post and pass post_id in it
    # TODO-13 - Get the post for the requested post_id passed.
    # TODO-14 - Render make-post.html and pass "edit_post" as True to change the heading to edit post.
    # TODO-15 - Add the code below to distinguish between adding new post or editing a particular blog bost.
    #  {% if edit_post: %}
    #   <h1>Edit Post</h1>
    #  {% else: %}
    #   <h1>New Post</h1>
    # {% endif %}
    # TODO-16 - When we want to edit a form add the code to auto-populate the fields in the WTForm with the blog post's
    #  data. This way the user doesn't have to type out their blog post again. So add below to edit_post route:
    #  edit_form = CreatePostForm(
    #         title=post.title,
    #         subtitle=post.subtitle,
    #         img_url=post.img_url,
    #         name=post.author,
    #         body=post.body
    #     )
    # TODO-17 - Once edited formed is submitted then we will assign the changes to current post in database and return
    # the same post.


    return render_template("make-post.html", form=edit_form, edit_post=True)

# TODO-18 - Add <a href=" {{ url_for('delete_post', post_id=post.id) }} ">✘</a> after date for each post in index.html.
# TODO-19 - In the main.py create a DELETE route at the path /delete/<post_id> to remove a blog post from the database.
# TODO-20 - Delete the record from the database obtained using id.

@app.route("/delete/<int:post_id>")
def delete_post(post_id):

    # DELETE RECORD
    delete_post = db.get_or_404(BlogPost, post_id)
    db.session.delete(delete_post)
    db.session.commit()

    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
