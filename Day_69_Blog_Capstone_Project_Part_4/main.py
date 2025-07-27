from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, Register_Form, Login_Form, Comment_Form
from sqlalchemy import ForeignKey


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
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))

    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="posts")

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    blog_post_comment = relationship("Comment", back_populates="comment_for_blog_post")


# TODO: Create a User table for all your registered users.
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")

    comment = relationship("Comment", back_populates="comment_author")


# TODO: Create a Comment table to store comments of users
class Comment(UserMixin, db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))

    # "comment" refers to the comment property in the User class.
    comment_author = relationship("User", back_populates="comment")


    blog_post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))

    comment_for_blog_post = relationship("BlogPost", back_populates="blog_post_comment")


    text: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()


# Create a decorator function to protect edit,post and delete route from users except for admin.
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function



# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = Register_Form()

    if register_form.validate_on_submit():
        Name = register_form.name.data
        Email = register_form.email.data
        Password = register_form.password.data

        # Find the user using email to realize where user exists.
        user = db.session.execute(db.select(User).where(User.email == Email))
        Final_user = user.scalar()

        if Final_user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        Hashed_Password = generate_password_hash(Password, method='pbkdf2:sha256', salt_length=8)

        new_user = User(
           name = Name,
           email = Email,
           password = Hashed_Password,
        )

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user
        login_user(new_user)

        return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=register_form, current_user=current_user)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Login_Form()

    if login_form.validate_on_submit():
        Email = login_form.email.data
        Password = login_form.password.data

        user = db.session.execute(db.select(User).where(User.email == Email))
        Final_user = user.scalar()

        if not Final_user:
            flash("The email does not exist. Please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(Final_user.password, Password):
            flash("Password incorrect, please try again.")
            return redirect(url_for('login'))
        else:
            # Log in and authenticate user
            login_user(Final_user)
            return redirect(url_for('get_all_posts'))

    return render_template("login.html", form=login_form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    comment_form = Comment_Form()
    requested_post = db.get_or_404(BlogPost, post_id)


    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for('login'))

        new_comment = Comment(
            text=comment_form.comment_body.data,
            comment_author=current_user,
            comment_for_blog_post=requested_post
        )

        db.session.add(new_comment)
        db.session.commit()

    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True, port=5002)


# TODO-1 - Create a class Register_Form in forms.py using WT forms consisting of name,email,password and submit button.
# TODO-2 - Render the form in register.html {{ render_form(form, novalidate=True) }}.
# TODO-3 - Import class Register_Form from forms.py.
# TODO-4 - Add GET,POST methods to register route and create object form from Register_Form class like
#  register_form = Register_Form()
# TODO-5 - Create db table User for storing name,email and password for a registering a new user
#  class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(integer, primary_key=True)
#     email: Mapped[str] = mapped_column(String(100), unique=True)
#     password: Mapped[str] = mapped_column(String(100))
#     name: Mapped[str] = mapped_column(String(1000))
# TODO-6 - Check if form submit button is click, if yes then retrieve name,email and password from form. Create a
#  hashed password from current password.
# TODO-7 - Add the new user to User db with name,email and hashed password and redirect to "/get_all_posts" page.
# TODO-8 - Add methods to login route , methods=['GET', 'POST'].
# TODO-9 - Add {{ render_form(form, novalidate=True) }} to login.html file.
# TODO-10 - Create a class Login_Form in forms.py using WT forms consisting of email,password and submit button.
# TODO-11 - Import class Login_Form from forms.py.
# TODO-12 - Create object form from Login_Form class like login_form = Login_Form().
# TODO-13 - Configure Flask-Login
#  login_manager = LoginManager()
#  login_manager.init_app(app)
# TODO-14 - Create a user_loader callback
#  @login_manager.user_loader
#  def load_user(user_id):
#     return db.session.get(User, user_id)
# TODO-15 - Check if form submit button is click, if yes then retrieve email and password from form.
# TODO-16 - Find the user in the database using email retrieved from form.
# TODO-17 - If user exists then verify password of form from to that of database using check_password_hash() function.
# TODO-18 - Log in and authenticate user using login_user(Final_user) and redirect to home page.
# TODO-19 - Add login_user(new_user) in register route so that when users successfully register they are taken back to
#  the home page and are logged in with Flask-Login.
# TODO-20 - Inside register route find the user by email and if the user exists then flash a message that it already
#  exists and rdirect to login page.
# TODO-21 - Add the code below to login.html to display a flash message.
#   {% with messages = get_flashed_messages() %}
#       {% if message %}
#           {% for message in messages %}
#               <p class="flash"> {{ message }} </p>
#           {% end_for %}
#       {% endif %}
#   {% end with %}
# TODO-22 - We need to show Login and Register on navigation bar if user is logged out. Once logged in we need to show
#  Logout. So we will pass current_user=current_user as a parameter to all routes except delete and logout.
# TODO-23 - Add logout_user() in logout route to clear the session for currently logged-in user / logs out the current
#  user and redirect it to home page.
# TODO-24 - Add {% if not current_user.is_authenticated %} in header.html for Login and Register and {% else %}
#  condition for Logout. It will display Login and Register if the user is logged out. Add {% endif %} to end if
#  condition.
# TODO-25 - The first registered user will be the admin. The admin user will be able to create new blog posts,
#  edit posts and delete posts. So add {% if current_user.id == 1 %} to check if current user's id is equal to 1. Add
#  it in index.html for Delete and Create New Post button. Add it in post.html for Edit Post button.
# TODO-26 - from functools import wraps to create a decorator function similar to @login_required to protect the
#  routes /edit-post or /new-post or /delete to user other than admin.
# TODO-27 - from flask import abort. Create decorator function named admin_only.
# TODO-28 - Check if current_user.id != 1, if yes then return abort(403).
#  def login_required(f):
#      @wraps(f)
#      def decorated_function(*args, **kwargs):
#          if current_user.id != 1:
#              return abort(403)
#          return f(*args, **kwargs)
#      return decorated_function
# TODO-28 - Add them just below the app.route of new-post,edit-post and delete.
# TODO-29 - Import from sqlalchemy import ForeignKey
# TODO-30 - We will define a relationship between tables using a ForeignKey and a relationship() method. The
#  relationship will be One-to-Many. Here we will have 1 class as Parent and the other as Child. In our case User db
#  will be Parent and Blogpost db will be a Child. So add: posts = relationship("BlogPost", back_populates="author") in
#  User db creating it as a Parent
# TODO-31 - Add this in Blogpost db: author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
#  This links each blog post to a user. "users.id" means the id field in the users table.
# TODO-32 - Add this in Blogpost db: author = relationship("User", back_populates="posts"). This sets up the connection
#  to the User class. It allows you to access blog_post.author to get the user object. back_populates="posts" must
#  match the corresponding field in the User class.
# TODO-33 - Add this to User db: posts = relationship("BlogPost", back_populates="author").Creates a one-to-many
#  relationship. One user can write many blog posts. You can use user.posts to get all the blog posts that a user has
#  written.
# TODO-34 - Delete both the db User and Blogpost since we are adding a new field author_id. If we don't do this then we
#  get error.
# TODO-35 - Once deleted then run the code again. Register the first user who will also be the admin.
#  Add a new blogpost. Now if you check the database you will see a new field author.id added in it.
# TODO-36 - Author name wont be seen in the post, you will see <User 1>. So to show author name replace post.author
#  with post.author.name in index.html and post.html.
# TODO-37 - Create a Comment_Form in the form.py file it will only contain a single CKEditorField for users to write
#  their comments.
# TODO-38 - Import from flask_ckeditor import CKEditor, CKEditorField.
# TODO-39 - Initialize CKEditor with Flask: ckeditor = CKEditor(app).
# TODO-40 - body = CKEditorField('Blog Comment', validators=[DataRequired()]) - Add this to Comment_Form in form.py
#  file.
# TODO-41 - Add submit = SubmitField("SUBMIT COMMENT") in Comment_Form class in forms.py.
# TODO-42 - Import Comment_Form class, initialize it in post route like this: comment_form = Comment_Form() and pass it
#  in post.html.
# TODO-43 - Add {% from "bootstrap5/form.html" import render_form %} then add{{ ckeditor.load() }},
#  {{ ckeditor.config(name='comment_body') }} and {{ render_form(form) }} to post.html file.
# TODO-44 - Create a Comment db. Name the table "comments", add id and text enterted from CKEditor Field.
# class  Comment(UserMixin, db.Model):
#     __tablename__ = "comments"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     text: Mapped[str] = mapped_column(Text, nullable=False)
# TODO-45 - Establish a One to Many relationship Between the User Table (Parent) and the Comment table (Child). Where
#  One User is linked to Many Comment objects. Add the lines below to Comment db.
#  # Create Foreign Key, "users.id" the users refers to the tablename of User.
#  author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
#  # "comment" refers to the comment property in the User class.
#  comment_author = relationship("User", back_populates="comment")
# TODO-46 - Add the code below to User to link it with Comment db.
#  comment = relationship("Comment", back_populates="comment_author")
# TODO-47 - Establish a One to Many relationship between each BlogPost object (Parent) and Comment object (Child).
#  Where each BlogPost can have many associated Comment objects. Add the code below to BlogPost db.
#  blog_post_comment = relationship("Comment", back_populates="comment_for_blog_post")
# TODO-47 - Add the code below to Comment db.
#  blog_post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
#  comment_for_blog_post = relationship("BlogPost", back_populates="blog_post_comment")
# TODO-48 - Delete all posts and users. Run the application again. Register an admin user and add a post.
# TODO-49 - Add another user / blog reader.
# TODO-50 - Only allow registered and logged-in users (users that have been authenticated) to comment on posts.
#  Otherwise, they should see a flash message telling them to log in and redirect them to the /login route. Add methods
#  to post route methods=['GET', 'POST'].
# TODO-51 - After the user comments on the post check if form is submitted. If yes then check if user is logged in or
#  authenticated, if not then redirect to login page and display message "You need to login or register to comment."
# TODO-52 - If form is submitted and user is logged in then store the comment in Comment db like this:
#  new_comment = Comment(
#             text=comment_form.body.data,
#             comment_author=current_user,
#             comment_for_blog_post=requested_post
#         )
#         db.session.add(new_comment)
#         db.session.commit()
# TODO-53 - Add FOR Loop in post.html under <ul class="commentList"> - {% for comment in post.blog_post_comment: %}
#  Since we have created relational database between BlogPost and Comment db so we can retrieve all the comments for
#  that blog post.
# TODO-54 - To retrieve comment text use {{ comment.text|safe }} in post.html. The |safe filter in Jinja2
#  (Flask's templating engine) is used to mark a string as safe HTML, meaning: It prevents auto-escaping of HTML
#  content.
# TODO-55 - To retrieve author name add {{ comment.comment_author.name }} in post.html. Since we have created
#  relational database between User and Comment db so we can retrieve author name from User db using foreign key
#  created for Comment db.
# TODO-56 - from flask_gravatar import Gravatar.
# TODO-57 - Initialize flask application with Gravatar and insert default parameters.
# gravatar = Gravatar(app,
#                     size=100,
#                     rating='g',
#                     default='retro',
#                     force_default=False,
#                     force_lower=False,
#                     use_ssl=False,
#                     base_url=None)
# TODO-58 - In post.html under image source add {{ 'comment.comment_author.email' | gravatar }} to display image.