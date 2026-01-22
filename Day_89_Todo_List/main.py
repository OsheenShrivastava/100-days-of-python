
# main.py file
# TODO-1 - Import Flask, render_template, redirect, url_for, flash and request from flask.
# TODO-2 - Import FlaskForm from flask_wtf.
# TODO-3 - Import Bootstrap5 from flask_bootstrap.
# TODO-4 - Import DataRequired, Email and Length from wtforms.validators.
# TODO-5 - Import StringField, SubmitField and PasswordField from wtforms.
# TODO-6 - Import SQLAlchemy from flask_sqlalchemy.
# TODO-7 - Import DeclarativeBase, Mapped and mapped_column from sqlalchemy.orm.
# TODO-8 - Import UserMixin, login_user, LoginManager, current_user, logout_user and login_required from flask_login.
# TODO-9 - Import generate_password_hash and check_password_hash from werkzeug.security.
# TODO-10 - Import date from datetime.
# TODO-11 - Import SMTP from smtplib.
# TODO-12 - Import EmailMessage from email.message.
# TODO-13 - Import load_dotenv from dotenv. Import os.
# TODO-14 - Import URLSafeTimedSerializer from itsdangerous.
# TODO-15 - Initialize Flask with app. Add secret key for Cross-Site Request Forgery (CSRF) attcks protection.
# TODO-16 - Initialise Bootstrap5.
# TODO-17 -  Initialize serializer. URLSafeTimedSerializer comes from itsdangerous, a library Flask relies on for secure
#  token generation. Its job is to: 1) Sign data so it cannot be tampered with. 2) Attach a timestamp so tokens can
#  expire. 3) Make the token safe to use in URLs. app.secret_key is used to 1) Sign the data cryptographically.
#  2) Ensure only your app can create or verify tokens.
# TODO-18 - Create a home route. Create a function home() and render "index.html" file.
# TODO-19 - Run the app. Check if the name of the file is "main" -->if __name__ == '__main__':. If true, then run the
#  app set debug=True which auto-reloads server when code changes,shows detailed error pages (stack traces) and enables
#  interactive debugger. Set the port to 5000.
# TODO-20 - Create a folder named "static". Add another folder named "img" and add all the required images in it.
# TODO-21 - Create style.css file inside "static" folder.
# TODO-22 - Add requirements.txt file and install the given versions - WTForms==3.0.1, Flask_WTF==1.2.1, Flask==3.0.2,
#  Flask-SQLAlchemy==3.1.1, SQLAlchemy==2.0.28, Werkzeug==3.0.1 and Bootstrap-Flask==2.3.3.
# TODO-23 - Create a function named generate_reset_token and pass email in it. This function turns an email into a
#  secure, expiring password-reset token that can be safely sent in a URL.
# TODO-24 - Create another function named verify_reset_token. This function verifies a password-reset token and
#  extracts the email from it but only if the token is valid and not expired. Pass token and expiration time in it.
#  Serializer loads token, salt with which taken has been created and checks if token is expired. If all conditions are
#  true, then it returns original data stored in the token i.e., email string else none.
# TODO-25 - Load env file using load_dotenv() function. Create .env file and store email and password in it.
#  Retrieve the email and password from .env file and save to SMTP_EMAIL and SMTP_PASSWORD respectively.
# TODO-26 - Configure Flask-Login using LoginManager() and initialise the app. Add login_manager.login_view = "login"
#  line. If a user tries to access a protected page without being logged in, redirect them to this route.” Here "login"
#  is the function name, not the URL string. When user visits:/my_saved_list_page And is not logged in, Flask-Login
#  does: redirect(url_for("login")).
# TODO-27 - @login_manager.user_loader registers this function with Flask-Login. Flask-Login will automatically call it
#  when needed. def load_user(user_id):user_id comes from the session cookie.Stored as a string by Flask-Login. Finally
#  returns the user id.
# TODO-28 - Initialize db by creating class Base(DeclarativeBase): and add pass inside it. DeclarativeBase is a base
#  class provided by SQLAlchemy. It creates a base class for all ORM (Object-Relational Mapping) models.
# TODO-29 - Define path for users.db using app.config --> app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'.
# TODO-30 - Create an object db from SQLAlchemy(model_class=Base) like this --> db = SQLAlchemy(model_class=Base). This
#  is used to read and write data to db.
# TODO-31 - Now db exists, but it is NOT yet connected to any Flask app. So, add db.init_app(app) which is a
#  Flask-SQLAlchemy initialization step that connects your database object (db) with your Flask app (app).
# TODO-32 - Now we will create a db model which matches the existing users.db table. Create class
#  User(UserMixin, db.Model) where db.Model is the base ORM class provided by Flask-SQLAlchemy. __tablename__ = 'users'
#  sets the table name in the database.
# TODO-33 - Define the database column, define its Column data type. Here we will define the data type as Integer for
#  id. Set primary_key=True as this column uniquely identifies each row. It means Values must be unique, Values cannot
#  be NULL,Database automatically indexes it and Usually auto-increments.
# TODO-34 - Define column datatype String for email,password and name. Add unique=True for email means this column
#  must have distinct values across all rows. No two records are allowed to store the same value in that column.
# TODO-35 - Define one-to-many relationship between a User and their TodoList items in SQLAlchemy. one-to-many
#  relationship between a User and their TodoList items in SQLAlchemy.
# TODO-36 - Similarly create another db model to store todolist options, name the table as 'todolists'. Define the
#  database column, define its data type. Define the data type as Integer for id. Set primary_key=True. Set String for
#  task and keep nullable=False i.e., every row must have a value for this column.
# TODO-37 - Map due_date with date|None which says that it can be a date or it can be None. Set nullable=True.
# TODO-38 - Set priority datatype as Integer and add nullable=False along with default value as 0. Set is_important
#  datatype as Boolean and add nullable=False along with default value as False.
# TODO-39 - Set completed datatype as Boolean and add nullable=False along with default value as False.
# TODO-40 - Similarly, set user_id datatype as Integer. Now user_id is used to define a foreign-key relationship
#  between a TodoList item and a User. Each list item belongs to exactly one user, and this link works both in the
#  database and in Python. Set nullable=False.
# TODO-41 - Add this --> user = db.relationship("User", back_populates="lists"). This creates a Python-level object
#  relationship i.e., links it with 'users' table.
# TODO-42 - Create form LoginForm(FlaskForm) to create flask form to enable user login functionality. Use StringField
#  function for email, add label which will be seen by user and validators=[DataRequired()] to validate form input
#  alongwith Email() to check if email is valid or not. Use PasswordField for password along with
#  validators=[DataRequired()]. Use SubmitField for submit button.
# TODO-43 - Create form RegisterForm(FlaskForm) to create flask form to enable register new user functionality. Use
#  StringField function for name, add label which will be seen by user and validators=[DataRequired()]. Use
#  StringField and PasswordField for email and password similar to that of LoginForm. Use SubmitField for submit button.
# TODO-44 - Create form AccountForm(FlaskForm) to create flask form to enable user to edit data and change password.
#  Use StringField function for name, add label which will be seen by user and validators=[DataRequired()]. Add
#  validators=[DataRequired() for all fields except submit button. Use StringField and PasswordField for email,
#  new_password and confirm_new_password similar to that of LoginForm except in this add 'Length(min=6)' for both
#  passwords in the validator row. Use SubmitField for submit button.
# TODO-45 - Create form ForgotPasswordForm(FlaskForm) to create flask form to enable to add email when user clicks on
#  forgot password. UseStringField for email same as that of LoginForm. Use SubmitField for submit button. This function
#  sends a password reset link to user on email.
# TODO-46 - Create form ResetPasswordForm(FlaskForm) to create flask form to enable to change password when user clicks
#  on the reset password link provided on email. Use PasswordField for new_password and confirm_new_password similar to
#  that of AccountForm. Use SubmitField for submit button.
# TODO-47 - Create a function send_email to send list via email. Pass to_email,subject and message to this function.
#  Create an object from class EmailMessage(). Assign msg['From'] = SMTP_EMAIL, msg['To'] = to_email and
#  msg['Subject'] = subject. Set message as content. Using SMTP open a connection, starttls(), login via SMTP_EMAIL and
#  SMTP_PASSWORD and finally send message.
# TODO-48 - Inside 'home' route check if current_user is logged in. if yes then redirect to 'my_saved_list_page' else
#  render 'index.html'.
# TODO-49 - Create another route '/register' to register the user and add function register() in it. Add GET and POST
#  methods to accept data from form and add it to db.
# TODO-50 - Inside register() function, create form object from RegisterForm() class and pass form and redirect to
#  'register.html' page. Check if submit button is pressed using if form.validate_on_submit():. If yes, then check if
#  user email exists in db if true flash message that user exists and redirect to login page. if not then generate hash
#  and salted password using generate_password_hash() function.
# TODO-51 - Create new_user and save name,email and password from form to User() db. Add login_user(new_user) to login
#  user immediately after registration and redirect to 'my_saved_list_page'.
# TODO-52 - Create another route '/login' to enable user login and add function login() in it. Add GET and POST
#  methods to accept data from form and add it to db.
# TODO-53 - Inside login() function, create form object from LoginForm() class and pass form and redirect to
#  'login.html' page.. Check if submit button is pressed using if form.validate_on_submit():. If yes, then check if
#  email exists in db if not, then flash message that user does not exist and redirect to login page. Else check if
#  password entered by user matches the one stored in db, if false then flash password incorrect message and redirect
#  to login page. Finally if everything is smooth then user will be logged in using login_user(user) and redirected to
#  my_saved_list_page.
# TODO-54 - Create another route '/my_saved_list_page' to display all the saved lists and add function
#  my_saved_list_page() in it. Add GET and POST methods to accept data from form and add it to db. Add @login_required
#  to display the page only when a user is logged in.
# TODO-55 - Filter TodoList by user_id. Then order it first by is_important in descending order, then by priority in
#  descending order and then finally by due_date in ascending order. Get all the lists and store then in lists variable.
# TODO-56 - Request edit id and store it in edit_id. Request edit card id and store it in edit_card_id.
# TODO-57 - Pass lists,edit_id, edit_card_id and date.today() [today's date] to my_saved_list.html and render it.
# TODO-58 - Inside my_saved_list_page() function, check if request is 'POST'. If yes then request the current task from
#  form and store it in task variable.
# TODO-59 - Create a new list and add the current task obtained,due_date as today's date and user_id as current_user.id.
#  Add the new list to db and redirect to my_saved_list_page.
# TODO-60 - Create another route '/star_task_as_imp/<int:list_id>' to enable user to mark a task as priority and add
#  function star_task_as_imp() in it. Add POST method set a task as important and add it to db. Add @login_required
#  to display the page only when a user is logged in. Pass list_id in the route as well as in the function.
# TODO-61 - Inside star_task_as_imp() function, fetch a single TodoList record from the database using its list_id and
#  store it in task variable. Check if task exists and task belongs to the logged-in user, if true then toggle
#  is_important and save the changes. Finally redirect to my_saved_list_page.
# TODO-62 - Create another route '/set_priority/<int:list_id>' to enable user to label the task with color and add
#  function set_priority() in it. Add POST method. Add @login_required to display the page only when a user is logged
#  in. Pass list_id in the route as well as in the function.
# TODO-63 - Inside set_priority() function, fetch a single TodoList record from the database using its list_id and
#  store it in task variable. Check if task exists and task belongs to the logged-in user, if true then request
#  'priority' field data from form, set default as 0(normal) convert it to integer and save it in task.priority. Save
#  the changes to db. Finally redirect to my_saved_list_page.
# TODO-64 - There are total 4 options to set color to tasks. 0:default(background color), 1:low(Green), 2:medium(Yellow)
#  and 3:high(Red).
# TODO-65 - Create another route '/edit_task/<int:list_id>' to enable user to edit the task details and add function
#  edit_task() in it. Add POST method. Add @login_required to display the page only when a user is logged in. Pass
#  list_id in the route as well as in the function.
# TODO-66 - Inside edit_task() function, fetch a single TodoList record from the database using its list_id and
#  store it in task variable. Check if task exists and task belongs to the logged-in user, if true then request
#  task and due_date field data from form. Save them to task.task and due_date_str respectively.
# TODO-67 - Convert date to iso format. Check if due_date_str exists, if true then save it in task.due_date else save
#  none. Save the changes to db. Finally redirect to my_saved_list_page.
# TODO-68 - Create another route '/toggle-complete/<int:list_id>' to enable user to mark the task as completed and add
#  function toggle_complete() in it. Add POST method. Add @login_required to display the page only when a user is
#  logged in. Pass list_id in the route as well as in the function.
# TODO-69 - Inside toggle_complete() function, fetch a single TodoList record from the database using its list_id and
#  store it in task variable. Toggle completed field and save the changes. Finally redirect to my_saved_list_page.
# TODO-70 - Create another route '/share_list' to enable user to share the task list via email and add function
#  share_list() in it. Add POST method. Add @login_required to display the page only when a user is logged in.
# TODO-71 - Inside share_list() function, fetch all TodoList task records from the database using current_user.id and
#  store it in task variable. Request email from form and store it in email variable.
# TODO-72 - Create a full URL of my_saved_list_page by adding _external=True in url_for() function. Save it in
#  list_link. Add another variable email_body and clear it.
# TODO-73 - Run a FOR loop on task list. Add task,due_date and completed fields to email_body for each task enclosed in
#  F-string. Finally add list_link to email_body.
# TODO-74 - Call function send_email() [already created above] and pass email,subject and email_body to its
#  corresponding variables. An email will be sent when this function is called. Once the email is sent flash success
#  message and redirect to my_saved_list_page.
# TODO-75 - Create another route '/account_settings' to enable user to change user account details such as name,email
#  and password. Add function account_settings() in it. Add GET and POST methods. Add @login_required to display the
#  page only when a user is logged in.
# TODO-76 - Inside account_settings() function, create form object from AccountForm() class and pass name and email of
#  current user. Pass form and redirect to 'account_settings.html' page.
# TODO-77 - Check if submit button is pressed, if true then get name and email from form and store them to
#  current_user.name and current_user.email respectively.
# TODO-78 - Now check if either of the password field have data in them.
# TODO-79 - Check if new_password and confirm_new_password match, if they don't flash message that passwords don't match
#  and redirect to account_settings page.
# TODO-80 - If condition is met, then generate hash password. Save the changes in db and flash account data updated
#  successfully. Redirect to account_settings page.
# TODO-81 - Create another route '/forgot_password' to enable user to change password. Add function forgot_password()
#  in it. Add GET and POST methods.
# TODO-82 - Inside forgot_password() function, create form object from ForgotPasswordForm() class and pass form and
#  redirect to 'forgot_password.html' page.
# TODO-83 - Check if submit button is pressed, if true then get email from form and store it in email variable.
# TODO-84 - Now useing this email check if user exists, if true then call generate_reset_token() function and pass email
#  to it. Store the token generated from this function to a variable named token.
# TODO-85 - Store full URL of 'reset_password' by passing _external=True. Also pass token it it. Save the URL to
#  'Change_my_password' variable.
# TODO-86 - Now call send_email() function and pass to_email, subject and message to it. Make sure to add
#  'Change_my_password' link in the message.
# TODO-87 - Once mail is sent flash success message for email sent and redirect to home page.
# TODO-88 - Create another route '/reset-password/<token>' to enable user to reset password. Add function
#  reset_password() in it. Add GET and POST methods.
# TODO-89 - Inside reset_password() function, pass token. Create form object from ResetPasswordForm() class, pass form
#  and redirect to 'reset_password.html' page.
# TODO-90 - Call verify_reset_token() function and pass token to it. Store its result in email variable since email is
#  retrieved from it. If email is not retrieved then flash message for invalid link or link expired. Redirect to
#  forgot_password page.
# TODO-91 - Find the user from User db whose email matches the extracted email. If user is not found then redirect to
#  forgot_password page.
# TODO-92 - If everything goes well and submit button is pressed, check if either of the password field have data in
#  them. Check if new_password and confirm_new_password match, if they don't flash message that passwords don't match
#  and redirect to account_settings page. If condition is met, then generate hash password and save the changes to db.
# TODO-93 - Flash success message for password updation and redirect to login page.
# TODO-94 - Create another route '/delete/<int:list_id>' to enable user delete tasks. Add function delete() in it. Add
#  POST method. Add @login_required to display the page only when a user is logged in. Redirect to my_saved_list_page.
# TODO-95 - Inside delete() function, pass list_id. Fetch a single TodoList record from the database using its list_id
#  and store it in task variable.
# TODO-96 - Check if task exists and task belongs to the logged-in user, if true then delete the task and save the
#  changes.
# TODO-97 - Create another route '/logout' to enable user to logout the session. Add function logout() in it. Add
#  @login_required to display the page only when a user is logged in.
# TODO-98 - Inside the function, add logout_user() to log user out of this Flask application using Flask-Login module.
#  Redirect to home page.

# base.html file
# TODO-99 - Create a folder named templates and add a html file. Name it base.html.
# TODO-100 - Set language as English, set charset="UTF-8", Title="Todo List". Use {% block title %} and {% endblock %}.
#  Add Bootstrap link for styling in head section and script link in body section.
# TODO-101 - Add links for font Handlee. Add external link for style.css.
# TODO-102 - Inside body section add {% include "header.html" %} to include header from header.html.
# TODO-103 - Add flash message loop for notfications. Use get_flashed_messages() function. Check if messages, add div
#  and set its id=flash-container.
# TODO-104 - Create this id in style.css and add position, top, right and z-index. z-index controls the vertical
#  stacking order of elements on a webpage—that is, which element appears in front of or behind another when they
#  overlap.
# TODO-105 - Run FOR loop for category and message in messages. Add another div and set its class as flash-msg. This
#  class contains padding, border, margin, color, animation and color change for success and danger messages. Add
#  category using Jinja.
# TODO-106 - Finally add message in the div using Jinja, end FOR loop and div. End if loop and with condition.
# TODO-107 - Add <main> opening and closing tags which encloses main content of the website. Add {% block content %} and
#  {% endblock %} to enclose body content inside it.
# TODO-108 - Add {% include "footer.html" %} to include footer from footer.html.
# TODO-109 - Add Bootstrap script link and close body and html tags.

# header.html file
# TODO-110 - Add another html file named header.html in templates folder.
# TODO-111 - Add a <div> and add class="header" to it. Inside style.css create class header and add width: 100%; in it.
# TODO-112 - Now create another div and add class="container header-inner" to it. Inside style.css create class
#  container and add max-width: 1100px; margin: 0 auto; padding: 0 24px; in it.
# TODO-113 - Create another class header-inner and add display type, padding, gap, font size, border-radius, box-shadow,
#  top margin and border.
# TODO-114 - Add <img> tag and add path for image file. Add class nav-logo to it. Create class nav-logo in style.css and
#  add width: clamp(120px, 18vw, 160px); height: auto; border-radius: 20%; in it.
# TODO-115 - Add another div and add class="nav-grid" to it. Create class nav-grid in style.css and add alignment,
#  display, justify content to end, align items in center and gap.
# TODO-116 - Now using jinja and if condition check if user is logged in, if yes, then display link for 'My Saved Lists'
#  using <a> tag. Add class nav-btn to it. Create this in style.css and add padding, border-radius, color and font-size.
#  Add background color while hovering.
# TODO-117 - Create another div just below it and add class nav-share-group to it. Create this in style.css and add
#  display type, grid-column, alignment and gap.
# TODO-118 - Inside this div add <a> tag for account settings. Add acc-set-link class to it. Create class and add
#  display, border-radius, color, font-size and more as per design requirements. Using Jinja display current user's
#  email as link in this tag.
# TODO-119 - Add <form> tag, add url of share_list and method as POST. Add class share-form-header to this. Create class
#  and add display type, alignement and gap.
# TODO-120 - Add input tag and define its styling in style.css. Define type, name, placeholder and field as required
#  inside this tag. Add button, define its type as submit and add classes icon-btn and share-btn to it. Define height,
#  width, opacity, display, alignment etc., in the class.
# TODO-121 - Add <img> tag to this button and define the url for the image. Add share-icon-btn class to it. Create this
#  class in style.css and add height, width, color and opacity.
# TODO-122 - Create a link for Logout using <a> tag which redirects to logout function.
# TODO-123 - Now inside else condition i.e., if user is not authenticated then display Home and Login links using <a>
#  tags by passing respective functions to them.
# TODO-124 - Add body in style.css and add font-family: 'Handlee', cursive; background: linear-gradient(120deg,#E0F2FE,
#  /* light sky blue */ #ECFEFF,   /* cyan tint */ #F0FDFA    /* mint tint */); inside it. This applies to body section.
# TODO-125 - Add html tag in style.css and add scroll-behavior: smooth; font-size: clamp(15px, 1.2vw, 17px);.

# footer.html
# TODO-126 - Add another html file named footer.html in templates folder.
# TODO-127 - Open <footer> tag and add class py-5 footer. Create this class in style.css and add text color,alignment,
#  resolution for screens, font-weight and padding. Add your footer in <p> tag.

# index.html
# TODO-128 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-129 - Use {% block title %} and add title 'Todo List' in it. End with {% endblock %}.
# TODO-130 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-131 - I have used readymade bootstrap 5 template from heros section named "Responsive left-aligned hero with
#  image". Copy its html code and paste it index.html inside {% block content %}.
# TODO-132 - Add image of your choice. Add 1 liner inside <h1> tag as heading.
# TODO-133 - Add description content inside <p> tag.
# TODO-134 - I have used 1 button and deleted the other. Centered it and increased it width. Add desired text on it.
#  Wrap it around <a> tag to create a link to login.
# TODO-135 - Similarly readymade bootstrap template is used for features section. I have used Custom Cards from features
#  section. I have edited the heading to "Features".
# TODO-136 - I have edited the url for my background image of each card as per need.
# TODO-137 - I have also edited the icons. Instead of image, I have inserted svg for icons and adjusted its height and
#  width.
# TODO-138 - I have edited <h3> tag to add features of my website.
# TODO-139 - All the changes are done for the other 2 cards as well. Make sure all the content is inside
#  {% block content %} and {% endblock %}.

# account_settings.html
# TODO-140 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-141 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-142 - Use {% block title %} and add title 'Account Settings' in it. End with {% endblock %}.
# TODO-143 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-144 - Add div with class container quick-add-form. Create quick-add-form class and add top margin in it.
# TODO-145 - Add <h1> tag with class='h3 mb-3 fw-normal mb-5'. Add text as Account Settings.
# TODO-146 - Add <p> tag. Inside it add <a> tag. Define href as '#password' with class change-password-link.
# TODO-147 - Hide both password fields by default by adding display: none; to them. Show them only when link is clicked,
#  therefore #password:target is used and display is changed to block display: block;.
# TODO-148 - Inside change-password-link add color, font-size and no text decoration. While hovering it should display
#  underline.
# TODO-149 - Now add another div with id=password. This is displayed when 'Change password' link is clicked. Render form
#  inside this using jinja.
# TODO-150 - Add extra_classes="account-form" to render form with class account-form. So initially password fields are
#  not displayed but when 'Change password' is clicked only then both fields are displayed. Close div.

# forgot_password.html
# TODO-151 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-152 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-153 - Use {% block title %} and add title 'Forgot Password' in it. End with {% endblock %}.
# TODO-154 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-155 - Add div with class container login. Create login class and add display, padding, font-weight and
#  justify-content to center.
# TODO-156 - Add <h1> tag with class="h3 mb-4". Edit text as 'Forgot your password?'.
# TODO-157 - Add <p> tag with class="text-muted". Add desired text to tell user to enter email for reset password link.
# TODO-158 - Using jinja render form.

# login.html
# TODO-159 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-160 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-161 - Use {% block title %} and add title 'Login' in it. End with {% endblock %}.
# TODO-162 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-163 - Add div with class container login.
# TODO-164 - Add <h1> tag with class="h3 mb-4 fw-normal mb-5". Edit text as 'Please sign in'.
# TODO-165 - Using jinja render form.
# TODO-166 - Add <p> tag with class="text-left text-muted mt-2". Inside it add <a> tag. Define href as link for
#  forgot_password with class text-decoration-none. Add text as 'Forgot your password?'.
# TODO-167 - Similarly Add <p> tag with class="text-muted text-center". Add text for <p> tag as 'New user?'.
# TODO-168 - Inside <p> tag add <a> tag. Define href as link for register with class fw-semibold. Add text as
#  'Click here to register'.

# my_saved_list.html
# TODO-169 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-170 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-171 - Use {% block title %} and add title 'My Saved Lists' in it. End with {% endblock %}.
# TODO-172 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-173 - Add div with class container saved_list. Create saved_list class in style.css and add display type, justify
#  content to center, padding, font-weight and font-size for all screens.
# TODO-174 - Add <form> tag. Define its method='POST', action='url_for('my_saved_list_page')' along with class
#  quick-add-form.
# TODO-175 - Inside this tag add <input> tag with type="text", name="task", placeholder="+ Add a task and press Enter",
#  class="create-input" and required. Create class create-input and add min-max width, padding, border, border-radius,
#  font-size, cursor and background. When focused change border-color, background and remove outline.
# TODO-176 - Add another <input> tag with type="hidden" and name="due_date".
# TODO-177 - Add FOR loop using jinja to display all tasks. Inside this loop using jinja create a set named priority_map
#  which had 4 options --> {3:'high', 2:'medium', 1:'low', 0:'default'}. They are color coded: high-red, medium-yellow,
#  low-green and default-blue shade(background color of website).
# TODO-178 - Below this add a div with class list-card priority-{{ list.priority }} where list.priority is obtained from
#  db and is of datatype int. Create list-card in style.css and add border-radius, padding, top-margin, width,
#  box-shadow, display type, gap, alignment and scroll-margin-top:100. For list-card.completed visibility is none.
# TODO-179 - Create priority class and add background colors for each priority. For priority-0: default-blue
#  shade(background color of website), priority-1:Green, priority-2:Yellow and priority-3:Red. Add hex code of these
#  and mark them as important so that the color applies no matter what.
# TODO-180 - If condition is also attached to check if a task is completed. Create a class .list-card.completed and add
#  text-decoration: line-through; and opacity: 0.5; in it. So when a task is completed it will be intersected from
#  center.
# TODO-181 - Add an id in the same div as list-{{ list.id }}, list.id is obtained from db. This gives each task a unique
#  identity in the HTML, so the browser (and JavaScript / links) can refer to that exact task.
# TODO-182 - Add if condition using jinja, and check if edit_card_id == list.id, i.e., if user is asking to edit the
#  task.
#  if true, then add <form> tag with method="POST" action="{{ url_for('edit_task', list_id=list.id) }}".
# TODO-183 - Add a div inside <form> tag with class form-group. Create this class and add display type, row-gap and
#  bottom margin. Add a <label> inside this div and name it Due Date. Add class .form-group label and add
#  font-size: 0.9rem; in it. Add <input> tag below label with type="date" name="due_date"
#  value="{{ list.due_date.strftime('%Y-%m-%d') }}. Here we are converting due_date to YYYY/MM/DD format provided if
#  due_date exists --> {{ if list.due_date }}.
# TODO-184 - Create class .form-group input in style.css and add padding, border-radius and border. Change border-color
#  and outline: none; when focused.
# TODO-185 - Create another div below this and add <button> in it with type="submit" class="form-save-btn". Name it
#  'Save'.
# TODO-186 - Create class form-save-btn and add display-type, padding, border-radius, background color, color, alignment
#  to center, font-size, cursor pointer and line-height. Change background when hovered.
# TODO-187 - Add <a> tag below <button>, Define href as link for my_saved_list_page with class cancel-btn. Add text as
#  'Cancel'.
# TODO-188 - Add class cancel-btn to form-save-btn so that both has same design parameters.
# TODO-189 - Now add elif condition {% elif edit_id == list.id %} to check if user wants to edit label color. Add <form>
#  tag inside it with method="POST" action="{{ url_for('set_priority', list_id=list.id) }}" class="color-tabs".
# TODO-200 - Create class color-tabs and add display-type, gap, top margin, alignment to right and justify content to
#  end.
# TODO-201 - Add for loop inside this form using jinja and loop through all 4 values of label colors 3:'high',
#  2:'medium', 1:'low', 0:'default'. Add a button inside this loop with name="priority" value="{{ value }}"
#  class="color-tab priority-{{ value }}". Value is integer obtained form FOR loop.
# TODO-202 - Create class color-tab and add height, width, border-radius, border, cursor and padding.
# TODO-203 - Create class color-tab.priority-0, the value will vary from 0 to 4. Add background colors depending on
#  value 0-Default blue color, 1-Green, 2-Yellow and 3-Red. When color-tab is hovered add transform: scale(1.2); which
#  scales an element to 120% of its original size.
# TODO-204 - Add <a> tag below, Define href as link for my_saved_list_page with class cancel-btn. Add text as 'Cancel'.
# TODO-205 - Now add else condition. Inside this add a div with class task-row. Create this class and add display-type,
#  alignment, gap and width.
# TODO-206 - Add a <form> tag inside this with action="{{ url_for('toggle_complete', list_id=list.id) }}" method="POST".
# TODO-207 - Add a <button> with type="submit" class="status-btn" and an if condition
#  {% if list.completed %}done{% else %}not-done{% endif %} which sets status done if list is completed else sets
#  not-done.
# TODO-208 - Create class status-btn and add height, width, border-radius, border-color, font-size, font-weight, cursor,
#  background and color. Create class for done --> .status-btn.done. Change background color and text color.
# TODO-209 - Add another if condition to add check mark. If completed add '✔'.
# TODO-210 - Add another div below to display task with class task-text. Create this class and add grid-column: 2;,
#  word-break: break-word;, line-height, min-width and font-size. Use Jinja to display task.
# TODO-211 - Add another div to display due date with class task-meta. Create this class and add grid-column: 3;,
#  display-type, align-items: center;, gap, white-space: nowrap;, and font-size.
# TODO-212 - Add <span> inside this div with class due-date. Create class and add color and font-size. Add if condition
#  for due date, if due_date exists then display it else display 'No due date'.
# TODO-213 - Now we will add a div for buttons. Add div with class action-buttons which consists of display-type,
#  alignment and gap. Inside this div add another div with class task-actions which consists of display-type, alignment
#  and gap.
# TODO-214 - Now we will add buttons. Add <form> tag for 'Star Button' with
#  action="{{ url_for('star_task_as_imp', list_id=list.id) }}" method="POST". Add button inside it with type="submit"
#  class="priority-icon-button". This class consists of no border - background - padding, display type, cursor and
#  alignment.
# TODO-215 - Add if condition using jinja and check {% if list.is_important %} i.e., if star is marked then display star
#  filled image else display star empty image. Both has same class priority-icon-btn. This class consists of height,
#  width, cursor and opacity. End if condition.
# TODO-216 - Add <a> tag for label edit button i.e., color for tasks with href for my_saved_list_page along with passing
#  list_id --> id:#list-{{ list.id }}. Add <img> tag to display label button with class icon-btn.
# TODO-217 - Similarly add <a> tag for edit button i.e., to edit task and date with href for my_saved_list_page along
#  with passing list_id --> id:#list-{{ list.id }}. Add <img> tag to display edit task button with class icon-btn.
# TODO-218 - Add <form> tag for 'Delete Button' with action="{{ url_for('delete', list_id=list.id) }}" method="POST".
#  Add button inside it with type="submit" class="delete-button". This class consists of no border - background -
#  padding only cursor.
# TODO-219 - Add <img> tag to display delete button with class icon-btn delete-icon. Class delete-icon consists of
#  height, width, cursor and opacity. Close <form> tag, if loop, FOR loop and final div.

# register.html
# TODO-220 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-221 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-222 - Use {% block title %} and add title 'Register' in it. End with {% endblock %}.
# TODO-223 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-224 - Add div with class container login.
# TODO-225 - Add <h1> tag with class="h3 mb-4 fw-normal mb-5". Edit text as 'Sign up to save lists'.
# TODO-226 - Using jinja render form.

# reset_password.html
# TODO-227 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-228 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-229 - Use {% block title %} and add title 'Reset Password' in it. End with {% endblock %}.
# TODO-230 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-231 - Add div with class container login.
# TODO-232 - Add <h1> tag with class="h3 mb-4 fw-normal mb-5". Edit text as 'Please sign in'.
# TODO-233 - Using jinja render form.



from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, SubmitField, PasswordField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from smtplib import SMTP
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from itsdangerous import URLSafeTimedSerializer



app = Flask(__name__)
app.secret_key = "any-string-you-want-to-keep-secret"
bootstrap = Bootstrap5(app)
serializer = URLSafeTimedSerializer(app.secret_key)


def generate_reset_token(email):
    return serializer.dumps(email, salt="password-reset")

def verify_reset_token(token, expiration=3600):
    try:
        return serializer.loads(
            token,
            salt="password-reset",
            max_age=expiration
        )
    except:
        return None


load_dotenv()


SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)



# Configure Tables
# Create a User table for all your registered userd
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(db.String(100), unique=True)
    password: Mapped[str] = mapped_column(db.Text, nullable=False) #changed
    name: Mapped[str] = mapped_column(db.String(100))

    lists = db.relationship('TodoList', back_populates='user')


class TodoList(db.Model):
    __tablename__ = 'todolists'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    task: Mapped[str] = mapped_column(db.String(200), nullable=False)
    due_date: Mapped[date | None] = mapped_column(db.Date, nullable=True)
    priority: Mapped[int] = mapped_column(db.Integer, nullable=False, default=0)
    is_important: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    completed: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="lists")


# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Register Form
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

# User Info and Password Change Form
class AccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Save Changes")

# Forgot Password Form
class ForgotPasswordForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(), Email()])
    submit = SubmitField("Send reset link")

# Reset Password Form
class ResetPasswordForm(FlaskForm):
    new_password = PasswordField("New Password", validators=[DataRequired(), Length(min=6)]) #changed
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Reset Password")


# Below lines deletes the contents of tables and creates new tables
# with app.app_context():
#     db.drop_all()
#     db.create_all()


def send_email(to_email, subject, message):
    msg = EmailMessage()

    msg['From'] = SMTP_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.set_content(message)

    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(SMTP_EMAIL, SMTP_PASSWORD)
        connection.send_message(msg)




@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('my_saved_list_page'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!", "danger")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=hash_and_salted_password
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('my_saved_list_page'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()

        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.", "danger")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, form.password.data):
            flash("Password incorrect, please try again.", "danger")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('my_saved_list_page'))


    return render_template('login.html', form=LoginForm())


@app.route('/my_saved_list_page', methods=['GET', 'POST'])
@login_required
def my_saved_list_page():
    if request.method == "POST":
        task = request.form.get("task")

        new_list = TodoList(
            task=task,
            due_date=date.today(),
            user_id=current_user.id
        )

        db.session.add(new_list)
        db.session.commit()

        return redirect(url_for("my_saved_list_page"))

    # Add line to filter list by priority
    lists = TodoList.query.filter_by(user_id=current_user.id).order_by(TodoList.is_important.desc(),
                                                                       TodoList.priority.desc(),
                                                                       TodoList.due_date.asc()).all()

    edit_id = request.args.get('edit', type=int)

    edit_card_id = request.args.get("edit_card", type=int)

    return render_template('my_saved_list.html', lists=lists, edit_id=edit_id,
                           edit_card_id=edit_card_id, date=date.today())


@app.route('/star_task_as_imp/<int:list_id>', methods=['POST'])
@login_required
def star_task_as_imp(list_id):
    task = TodoList.query.get(list_id)
    if task and task.user_id == current_user.id:
        task.is_important = not task.is_important
        db.session.commit()
    return redirect(url_for('my_saved_list_page'))


@app.route('/set_priority/<int:list_id>', methods=['POST'])
@login_required
def set_priority(list_id):
    task = TodoList.query.get(list_id)
    if task and task.user_id == current_user.id:
        task.priority = int(request.form.get("priority", 0))
        db.session.commit()
    return redirect(url_for("my_saved_list_page"))


@app.route('/edit_task/<int:list_id>', methods=['POST'])
@login_required
def edit_task(list_id):
    task = TodoList.query.get(list_id)
    if task and task.user_id == current_user.id:
        task.task = request.form.get("task", task.task)
        due_date_str = request.form.get("due_date")
        task.due_date = date.fromisoformat(due_date_str) if due_date_str else None
        db.session.commit()
    return redirect(url_for("my_saved_list_page"))


@app.route('/toggle-complete/<int:list_id>', methods=['POST'])
@login_required
def toggle_complete(list_id):
    task = TodoList.query.get(list_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("my_saved_list_page"))


@app.route('/share_list', methods=['POST'])
@login_required
def share_list():
    task = TodoList.query.filter_by(user_id=current_user.id).all()
    email = request.form.get("email")

    # makes full URL
    list_link = url_for("my_saved_list_page",_external=True)

    email_body = ""

    for t in task:
        email_body += f""" 
        Task: {t.task}
        Due Date: {t.due_date if t.due_date else 'No due date'}
        Completed: {'Yes' if t.completed else 'No'}\n"""

    email_body += f"\nView the full list here:\n{list_link}"

    send_email(
        to_email=email,
        subject=f"Task Shared With You.",
        message = email_body
    )

    flash("Task list and access link sent via email!", "success")
    return redirect(url_for("my_saved_list_page"))


@app.route('/account_settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    form = AccountForm(
        name=current_user.name,
        email=current_user.email
    )

    if form.validate_on_submit():

        current_user.name = form.name.data
        current_user.email = form.email.data

        # 🔐 Update password ONLY if user entered it
        if form.new_password.data or form.confirm_new_password.data:

            # Both fields must be filled  #changed
            # if not form.new_password.data or not form.confirm_new_password.data:
            #     flash("Please fill both password fields.", "danger")
            #     return redirect(url_for('account_settings'))

            # Passwords must match
            if form.new_password.data != form.confirm_new_password.data:
                flash("Passwords do not match.", "danger")
                return redirect(url_for('account_settings'))

            # Save hashed password
            current_user.password = generate_password_hash(
                form.new_password.data,
                method="pbkdf2:sha256",
                salt_length=8
            )

        db.session.commit()
        flash("Account settings updated successfully!", "success")
        return redirect(url_for('account_settings'))


    return render_template("account_settings.html", form=form)


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()

    if form.validate_on_submit():
        email = form.email.data

        # OPTIONAL: check if user exists
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if user:
            token = generate_reset_token(user.email)

            Change_my_password = url_for(
                'reset_password',
                token=token,
                _external=True  # creates full URL
            )
            # For now just send a simple email (or print/log it)
            send_email(
                to_email=email,
                subject="Password reset",
                message=f"Someone has requested a link to change your password. You can do this through the link "
                        f"below.\n"
                        f"{Change_my_password}\n"
                        f"If you didn't request this, please ignore this email.\n"
                        f"Your password won't change until you access the link above and create a new one.\n"
            )

        # Always show same message (security best practice)
        flash(
            "If an account with that email exists, a reset link has been sent.",
            "success"
        )
        return redirect(url_for('home'))

        # add actual link to the page

    return render_template('forgot_password.html',form=form)


@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    email = verify_reset_token(token)

    if not email:
        flash("The reset link is invalid or has expired.", "danger")
        return redirect(url_for('forgot_password'))

    user = db.session.execute(db.select(User).where(User.email == email)).scalar()

    if not user:
        return redirect(url_for('forgot_password'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        # 🔐 Update password ONLY if user entered it
        if form.new_password.data or form.confirm_new_password.data:
             #changed
            # Passwords must match
            if form.new_password.data != form.confirm_new_password.data:
                flash("Passwords do not match.", "danger")
                return render_template('reset_password.html', form=form)

            user.password = generate_password_hash(
                form.new_password.data,
                method="pbkdf2:sha256",
                salt_length=8
            )

        db.session.commit()
        flash("Your password has been updated.", "success")
        return redirect(url_for('login'))

    return render_template('reset_password.html', form=form)




@app.route('/delete/<int:list_id>', methods=['POST'])
@login_required
def delete(list_id):
    task = TodoList.query.get(list_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("my_saved_list_page"))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, port=5000)