
# main.py file
# TODO-1 - Import required modules from Flask such as Flask, render_template, request, redirect, url_for, flash, and
#  session.
# TODO-2 - Import Bootstrap5 from flask_bootstrap to use Bootstrap styling in templates.
# TODO-3 - Import requests to fetch product data from external APIs.
# TODO-4 - Import os to check file existence and access environment variables.
# TODO-5 - Import pandas as pd to store and read API data from CSV files.
# TODO-6 - Import randint and uniform from random.
# TODO-7 - Import FlaskForm from flask_wtf to create forms.
# TODO-8 - Import StringField, PasswordField, and SubmitField from wtforms for form fields.
# TODO-9 - Import DataRequired, Email, and Length validators from wtforms.validators for form validation.
# TODO-10 - Import SQLAlchemy and required ORM classes to create database models.
# TODO-11 - Import UserMixin, login_user, logout_user, current_user, and login_required from flask_login for
#  authentication.
# TODO-12 - Import generate_password_hash and check_password_hash from werkzeug.security for secure password handling.
# TODO-13 - Import EmailMessage and SMTP to send password reset emails.
# TODO-14 - Import load_dotenv to load environment variables from .env file.
# TODO-15 - Import LoginManager from flask_login to configure login system.
# TODO-16 - Import URLSafeTimedSerializer from itsdangerous to generate time-based reset tokens.
# TODO-17 - Import re for regex validation of card number, CVV, and expiry.
# TODO-18 - Import datetime to check whether entered card expiry date is valid.
# TODO-19 - Create Flask app using app = Flask(__name__). Set app.secret_key to enable sessions, flash messages, and
#  token generation.
# TODO-20 - Initialize Bootstrap using Bootstrap5(app).
# TODO-21 - Create serializer using URLSafeTimedSerializer(app.secret_key) for password reset links.
# TODO-22 - Load environment variables using load_dotenv().
# TODO-23 - Configure Flask-Login using LoginManager().
# TODO-24 - Attach login manager to app using login_manager.init_app(app).
# TODO-25 - Set login_manager.login_view = "login" so protected routes redirect to login page.
# TODO-26 - Set login_manager.login_message = None to disable default login-required flash message.
# TODO-27 - Define CSV file names for books, electronics, clothes, shoes, and furniture.
# TODO-28 - Create a file with extension ".env". Add Rainforest API link, SMTP Email and SMTP Password in it.
# TODO-29 - Read Rainforest API key from environment variable using os.getenv("RAINFOREST_API_KEY").
# TODO-30 - Read SMTP email and SMTP password from environment variables.
# TODO-31 - Define API URLs for Google Books API, DummyJSON product categories API, and Rainforest search API.
# TODO-32 - Add @login_manager.user_loader function to load a user from database using user_id.
# TODO-33 - Return db.session.get(User, int(user_id)) inside user loader.
# TODO-34 - Create Base class by inheriting from DeclarativeBase.
# TODO-35 - Configure SQLite database URI using app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'.
# TODO-36 - Initialize SQLAlchemy using db = SQLAlchemy(model_class=Base). Attach database to app using
#  db.init_app(app).
# TODO-37 - Create User model class inheriting from UserMixin and db.Model. Set __tablename__ = 'users' for User model.
# TODO-38 - Add id as primary key in User model. Add email column with unique=True. Add password column as non-nullable
#  text. Add name column for storing user's name. Add relationship cart_items to link User model with Cart model.
# TODO-39 - Create Cart model class inheriting from db.Model. Set __tablename__ = 'cart' for Cart model.
# TODO-40 - Add id as primary key in Cart model. Add user_id column as foreign key referencing users.id. Add title
#  column to store product title. Add price column to store product price. Add image column to store product image URL.
#  Add quantity column to store cart quantity. Add relationship user to connect Cart model back to User model.
# TODO-41 - Create RegisterForm class using FlaskForm. Add name field with DataRequired validator. Add email field with
#  DataRequired and Email validators. Add password field with DataRequired validator. Add submit button labeled
#  'Register'.
# TODO-42 - Create LoginForm class using FlaskForm. Add email field with DataRequired and Email validators. Add password
#  field with DataRequired validator. Add submit button labeled 'Login'.
# TODO-43 - Create AccountForm class for updating user details. Add name and email fields with proper validators. Add
#  new_password field with DataRequired and Length(min=6). Add confirm_new_password field with DataRequired and
#  Length(min=6). Add submit button labeled 'Save Changes'.
# TODO-44 - Create ForgotPasswordForm class. Add email field with DataRequired and Email validators. Add submit button
#  labeled 'Send reset link'.
# TODO-45 - Create ResetPasswordForm class. Add new_password field with DataRequired and Length(min=6). Add
#  confirm_new_password field with DataRequired and Length(min=6). Add submit button labeled 'Reset Password'.
# TODO-46 - Create a folder named "instance". Then create database using db.create_all() function. Keep optional code
#  block for db.drop_all() and db.create_all() commented for database reset when needed.
# TODO-47 - Create send_email() helper function. Initialize EmailMessage object inside send_email(). Set sender,
#  receiver, and subject fields in email. Set email body content using msg.set_content(message).
# TODO-48 - Connect to Gmail SMTP server using SMTP("smtp.gmail.com", 587). Start TLS for secure connection. Login using
#  SMTP email and password. Send email message using connection.send_message(msg).
# TODO-49 - Create generate_reset_token(email) function to generate signed reset token.
# TODO-50 - Create verify_reset_token(token, expiration=3600) function to verify token and return email if valid.
# TODO-51 - Return None if token is invalid or expired.
# TODO-52 - Create generate_meta(category) helper function to generate random price, rating, and reviews for category
#  products. Add ranges dictionary for books, clothes, electronics, shoes, home and furniture categories. Add sub
#  categories below the main categories. Give price range, rating range and review range for individual sub category.
# TODO-53 - Use ranges.get(category, default_values) to support unknown categories.
# TODO-54 - Generate random price using randint(). Generate random rating using uniform() and round(). Generate random
#  reviews using randint().
# TODO-55 - Return price, rating, and reviews from the function.
# TODO-56 - Create detect_category(title) helper function to detect product category from title text.
# TODO-57 - Convert title to lowercase for easier keyword matching.
# TODO-58 - Return "books" if title contains book-related words. Return "electronics" if title contains
#  phone/laptop/watch-related words. Return "clothes" if title contains clothing-related words. Return "shoes" if title
#  contains shoe-related words. Return "furniture" if title contains furniture-related words. Return "general" if no
#  known category is matched.
# TODO-59 - Create generate_meta_search(category) helper function for search result pricing and rating generation.
# TODO-60 - Define ranges for books, clothes, shoes, electronics, furniture, and general categories.
# TODO-61 - Generate random price, rating, and reviews from category range. Return generated values.
# TODO-62 - Add home route using @app.route('/'). Create home() function and render index.html.
# TODO-63 - Add books route using @app.route('/books').
# TODO-64 - Read selected_category from query parameter using request.args.get("category", "all"). Define list of book
#  categories.
# TODO-65 - Check if books.csv exists using os.path.exists(). If file exists, read data using pd.read_csv(). If file
#  does not exist, create empty DataFrame.
# TODO-66 - If data is empty, fetch books from Google Books API for each category. Build params dictionary with subject
#  query and maxResults. Send request to books API using requests.get().
# TODO-67 - If response is successful, get items from response JSON. Extract volumeInfo, title, authors, and thumbnail
#  image from each item.
# TODO-68 - Generate fake price, rating, and review count using generate_meta().
# TODO-69 - Append all product details into rows list. Convert rows list into DataFrame and save to books.csv.
# TODO-70 - Group data by category using data.groupby("category"). Convert grouped data into dictionary format for
#  template.
# TODO-71 - If selected_category is not "all", filter products_data for that category only.
# TODO-72 - Render products.html with products, selected_category, categories, and title="Books".
# TODO-73 - Add clothes route using @app.route('/clothes'). Read selected_category from query parameters.
# TODO-74 - Define clothes categories list.
# TODO-75 - Load existing clothes.csv if available, otherwise create empty DataFrame.
# TODO-76 - If data is empty, fetch product data from DummyJSON API for each clothes category. Extract title and
#  thumbnail image from API response.
# TODO-77 - Generate fake price, rating, and reviews using generate_meta().
# TODO-78 - Append all product details into rows list. Convert rows list into DataFrame and save to clothes.csv.
# TODO-79 - Group data by category. Convert grouped data into dictionary format for template.
# TODO-80 - If selected_category is not "all", filter products_data for that category only.
# TODO-81 - Render products.html with products, selected_category, categories, and title="Clothes".
# TODO-82 - Add electronics route using @app.route('/electronics').
# TODO-83 - Define electronics category list.
# TODO-84 - Load electronics.csv if it exists. If empty, fetch data from DummyJSON API for all electronics categories.
# TODO-85 - Generate fake price, rating, and reviews.
# TODO-86 - Append all product details into rows list. Convert rows list into DataFrame and save to electronics.csv.
# TODO-87 - Group data by category. Convert grouped data into dictionary format for template.
# TODO-88 - If selected_category is not "all", filter products_data for that category only.
# TODO-89 - Render products.html with products, selected_category, categories, and title="Electronics".
# TODO-90 - Add shoes route using @app.route('/shoes').
# TODO-91 - Define shoes category list.
# TODO-92 - Load shoes.csv if available. If empty, fetch shoes data from DummyJSON API.
# TODO-93 - Generate fake price, rating, and reviews using generate_meta().
# TODO-94 - Append all product details into rows list. Convert rows list into DataFrame and save to shoes.csv.
# TODO-95 - Group data by category. Convert grouped data into dictionary format for template.
# TODO-96 - If selected_category is not "all", filter products_data for that category only.
# TODO-97 - Render products.html with products, selected_category, categories, and title="Shoes".
# TODO-98 - Add furniture route using @app.route('/furniture').
# TODO-99 - Define furniture-related category list.
# TODO-100 - Load furniture.csv if available. If empty, fetch furniture data from DummyJSON API.
# TODO-101 - Generate fake price, rating, and reviews using generate_meta().
# TODO-102 - Append all product details into rows list. Convert rows list into DataFrame and save to furniture.csv.
# TODO-103 - Group data by category. Convert grouped data into dictionary format for template.
# TODO-104 - If selected_category is not "all", filter products_data for that category only.
# TODO-105 - Render products.html with products, selected_category, categories, and title="Furniture".
# TODO-106 - Add search route using @app.route("/search").
# TODO-107 - Read search query from request.args.get("q", "").strip().
# TODO-108 - Initialize empty results list.
# TODO-109 - Build params dictionary for Rainforest API including API key, search type, amazon domain, and search term.
# TODO-110 - Send request to Rainforest API using requests.get() with timeout.
# TODO-111 - Parse JSON response.
# TODO-112 - Loop through data.get("search_results", []). Get title from each search item and detect category using
#  detect_category().
# TODO-113 - Generate fake price, rating, and reviews using generate_meta_search().
# TODO-114 - Append title, image, price, rating, and reviews into results list.
# TODO-115 - Wrap request logic in try-except block to prevent app crash on API error. Print Rainforest search error in
#  console if exception occurs.
# TODO-116 - Render search.html with results and query.
# TODO-117 - Add login route using @app.route('/login', methods=['GET', 'POST']). Create LoginForm instance inside login
#  route.
# TODO-118 - Check if form.validate_on_submit() returns True. If yes then, query user from database by matching
#  submitted email.
# TODO-119 - If user does not exist, flash danger message and redirect back to login page.
# TODO-120 - If password does not match hashed password, flash danger message and redirect back.
# TODO-121 - If credentials are correct, call login_user(user). Flash success message after login.
# TODO-122 - Check for pending_cart in session and add it into database cart after successful login. If same item
#  already exists in cart, increase quantity. Otherwise create new Cart row and add it to database with user_id, title,
#  price and image. Commit cart changes to database. Flash item-added message if pending cart was saved.
# TODO-123 - Read next page from request.args.get("next"). Redirect user to next page if present, otherwise home page.
# TODO-124 - Render login.html with form on GET request.
# TODO-125 - Add register route using @app.route('/register', methods=['GET', 'POST']).
# TODO-126 - Create RegisterForm instance.
# TODO-127 - On valid submit, check if submitted email already exists in database. If user already exists, flash message
#  and redirect to login page.
# TODO-128 - Hash password using generate_password_hash() with pbkdf2:sha256 and salt_length=8.
# TODO-129 - Create new User object with form name, email, and hashed password. Add new user to database and commit.
# TODO-130 - Automatically log in the new user using login_user(new_user). Flash account-created success message.
# TODO-131 - Redirect to next page if present, otherwise home page.
# TODO-132 - Render register.html with form if request method is GET.
# TODO-133 - Add forgot_password route using @app.route('/forgot_password', methods=['GET', 'POST']).
# TODO-134 - Create ForgotPasswordForm instance.
# TODO-135 - On valid submit, read submitted email.
# TODO-136 - Query database to check if account exists for that email. If user exists, generate reset token using
#  generate_reset_token().
# TODO-137 - Build full reset password link by passing in token using url_for(..., _external=True).
# TODO-138 - Send password reset email using send_email(). Add to_email, subject and message in it.
# TODO-139 - Flash same generic success message whether account exists or not for security. Redirect to home page after
#  submission.
# TODO-140 - Render forgot_password.html with form on GET request.
# TODO-141 - Add reset_password route using @app.route('/reset-password/<token>', methods=['GET', 'POST']).
# TODO-142 - Verify token using verify_reset_token(token). If token is invalid or expired, flash danger message and
#  redirect to forgot_password page.
# TODO-143 - Query user using returned email. If no user found, redirect to forgot_password page.
# TODO-144 - Create ResetPasswordForm instance. On valid submit, check if new_password and confirm_new_password are
#  entered. If passwords do not match, flash danger message and render reset_password.html again.
# TODO-145 - If passwords match then, hash new password and save it to user.password. Commit updated password to
#  database.
#  Flash success message and redirect to login page.
# TODO-146 - Render reset_password.html with form on GET request.
# TODO-147 - Add account_settings route using @app.route('/account_settings', methods=['GET', 'POST']).
# TODO-148 - Protect account settings route using @login_required.
# TODO-149 - Pre-fill AccountForm with current_user.name and current_user.email. On valid submit, update
#  current_user.name and current_user.email.
# TODO-150 - If password fields are filled, check whether both passwords match. If passwords do not match, flash danger
#  message and redirect back.
# TODO-151 - If passwords match, hash new password and update current_user.password. Commit changes to database. Flash
#  success message and redirect back to account settings page.
# TODO-152 - Render account_settings.html with form.
# TODO-153 - Add logout route using @app.route('/logout').
# TODO-154 - Protect logout route using @login_required.
# TODO-155 - Call logout_user() to clear logged-in session. Flash info message after logout.
# TODO-156 - Redirect user to home page.
# TODO-157 - Add context processor function inject_cart_count().
# TODO-158 - Check whether current_user.is_authenticated. If logged in, calculate total cart quantity using
#  db.func.sum(Cart.quantity).
# TODO-159 - Return cart_count inside dictionary so it is available in all templates.
# TODO-160 - Return cart_count=0 for non-logged-in users.
# TODO-161 - Add add_to_cart route using @app.route("/add-to-cart", methods=["POST"]).
# TODO-162 - Read title, price, and image from request.form.
# TODO-163 - If user is not logged in, save item details in session["pending_cart"]. Redirect unauthenticated user to
#  login page and pass next=request.referrer.
# TODO-164 - If user is logged in, check whether item already exists in current user's cart. If item exists, increase
#  quantity by 1. Otherwise create a new Cart object with quantity=1.
# TODO-165 - Add new item to database if needed and commit. Flash success message after adding to cart.
# TODO-166 - Redirect back to referring page or home page.
# TODO-167 - Add cart_page route using @app.route("/cart_page"). Protect cart page using @login_required.
# TODO-168 - Query all cart items for current user.
# TODO-169 - Calculate total amount using sum(item.price * item.quantity for item in items).
# TODO-170 - Render cart.html with items and total.
# TODO-171 - Add update_cart route using @app.route("/update-cart/<int:item_id>", methods=["POST"]). Protect update_cart
#  route using @login_required.
# TODO-172 - Read action from submitted form. Query cart item by item_id.
# TODO-173 - Confirm that item exists and belongs to current user. If action is "increase", increase quantity by 1. If
#  action is "decrease", reduce quantity by 1.
# TODO-174 - If quantity becomes 0 or less, delete item from database. Commit changes to database.
# TODO-175 - Redirect back to cart page after update.
# TODO-176 - Add remove_from_cart route using @app.route("/remove-from-cart/<int:item_id>", methods=["POST"]).
# TODO-177 - Protect remove_from_cart route using @login_required.
# TODO-178 - Query cart item by item_id. Check that item belongs to current user.
# TODO-179 - Delete item from database and commit.
# TODO-180 - Redirect back to cart page.
# TODO-181 - Add fake_payment route using @app.route("/fake-payment", methods=["POST"]).
# TODO-182 - Protect fake_payment route using @login_required.
# TODO-183 - Query current user's cart items.
# TODO-184 - If cart is empty, flash warning message and redirect back to cart page.
# TODO-185 - Read card_number, expiry, and cvv from request.form.
# TODO-186 - Remove spaces from card_number before validation. Validate card number using regex to ensure exactly 16
#  digits. If not then flash error message.
# TODO-187 - Validate CVV using regex to ensure exactly 3 digits. If not then flash error message.
# TODO-188 - Validate expiry using regex to ensure MM/YY format. If not then flash error message.
# TODO-189 - Split expiry into month and year. Convert year into full year format using int("20" + year).
# TODO-190 - Get current date using datetime.now(). Check whether entered card has expired.
# TODO-191 - If expired, flash danger message and redirect back.
# TODO-192 - If all validation passes, delete all current user's cart items. Commit database changes.
# TODO-193 - Set session["payment_done"] = True to track successful payment state. Flash payment success message.
# TODO-194 - Redirect to success page.
# TODO-195 - Add success route using @app.route("/success").
# TODO-196 - Protect success route using @login_required.
# TODO-197 - Check session.pop("payment_done", None) to ensure page is visited only after successful payment.
# TODO-198 - If payment flag is not found, redirect to home page.
# TODO-199 - Render success.html if payment is valid.
# TODO-200 - Create a folder static and add file style.css in it. Add body tag, inside it add font-family as 'Inter' of
#  type sans-serif along with margin: 0;. Add html tag, insid eit add scroll-behavior: smooth;.
# TODO-201 - Add if __name__ == '__main__': block at the end of file.
# TODO-202 - Run app in debug mode using app.run(debug=True, port=5001).

# base.html file
# TODO-203 - Create a folder named templates and add a html file. Name it base.html.
# TODO-204 - Set language as English, set charset="UTF-8", Title="LoTR". Use {% block title %} and {% endblock %}. Add
#  Bootstrap link for styling in head section and script link in body section.
# TODO-205 - Add links for font Inter. Add external link for style.css.
# TODO-206 - Add {% include "header.html" %} to include header from header.html.
# TODO-207 - Add flash message loop for notfications. Use get_flashed_messages() function. Check if messages, add div
#  and set its id=flash-container.
# TODO-208 - Create this id in style.css and add position, top, right and z-index. z-index controls the vertical
#  stacking order of elements on a webpage—that is, which element appears in front of or behind another when they
#  overlap.
# TODO-209 - Run FOR loop for category and message in messages. Add another div and set its class as "flash-msg". This
#  class contains padding, border, margin, color, animation and color change for success, danger, info and warning
#  messages. Add category using Jinja.
# TODO-210 - Finally add message in the div using Jinja, end FOR loop and div. End if loop and with condition. Add
#  .flash-msg.warning, .flash-msg.danger, .flash-msg.info and .flash-msg.success classes in style.css and add background
#  color to it. Add animation for message fadeout.
# TODO-211 - Add main opening and closing tags. Inside them add {% block content %} and {% endblock %} to enclose body
#  content.
# TODO- - Close body and html tags.

# account_settings.html
# TODO-212 - Add a file named "account_settings.html" in templates folder.
# TODO-213 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-214 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-215 - Use {% block title %} and add title 'Account Settings' in it. End with {% endblock %}.
# TODO-216 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-217 - Add div with class "container login". Create "container" class in style.css and add max-width, margin and
#  padding in it. Create class "login" in style.css and add display type as grid, justify content to center, padding and
#  font-weight.
# TODO-218 - Add <h1> tag with class='h3 mb-3 fw-normal mb-5'. Add text as Account Settings.
# TODO-219 - Add <p> tag. Inside it add <a> tag. Define href as '#password' with class change-password-link.
# TODO-220 - Hide both password fields by default by adding display: none; to them. Show them only when link is clicked,
#  therefore #password:target is used and display is changed to block display: block;.
# TODO-221 - Inside change-password-link add color, font-size and no text decoration. While hovering it should display
#  underline.
# TODO-222 - Now add another div with id=password. This is displayed when 'Change password' link is clicked. Render form
#  inside this using jinja.
# TODO-223 - Add extra_classes="account-form" to render form with class account-form. So initially password fields are
#  not displayed but when 'Change password' is clicked only then both fields are displayed. Close div.

# forgot_password.html
# TODO-224 - Add a file named "forgot_password.html" in templates folder.
# TODO-225 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-226 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-227 - Use {% block title %} and add title 'Forgot Password' in it. End with {% endblock %}.
# TODO-228 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-229 - Add div with class "container login". We have already used these classes in account settings form.
# TODO-230 - Add <h1> tag with class="h3 mb-4". Edit text as 'Forgot your password?'.
# TODO-231 - Add <p> tag with class="text-muted". Add desired text to tell user to enter email for reset password link.
# TODO-232 - Using jinja render form.

# login.html
# TODO-233 - Add a file named "login.html" in templates folder.
# TODO-234 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-235 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-236 - Use {% block title %} and add title 'Login' in it. End with {% endblock %}.
# TODO-237 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-238 - Add div with class "container login".
# TODO-239 - Add <h1> tag with class="h3 mb-4 fw-normal mb-5". Edit text as 'Sign in to continue'.
# TODO-240 - Using jinja render form.
# TODO-241 - Add <p> tag with class="text-left text-muted mt-2". Inside it add <a> tag. Define href as link for
#  forgot_password with class text-decoration-none. Add text as 'Forgot your password?'.
# TODO-242 - Similarly Add <p> tag with class="text-muted text-center". Add text for <p> tag as 'New user?'.
# TODO-243 - Inside <p> tag add <a> tag. Define href as link for register with class fw-semibold. Add text as
#  'Click here to register'.
# TODO-244 - Add next=request.args.get('next')). next=request.args.get('next') adds a query parameter called next to the
#  URL. request.args.get('next') means: get the value of next from the current page URL.
#  For Example :User tries to open /checkout. They are not logged in, so redirected to: /login?next=/checkout.
#  On login page, register link keeps that next value: /register?next=/checkout.
#  After registration, you redirect user to /checkout
#  In simple words this line makes a register link and preserves the page the user should return to after registering.

# register.html
# TODO-245 - Add a file named "register.html" in templates folder.
# TODO-246 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-247 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-248 - Use {% block title %} and add title 'Register' in it. End with {% endblock %}.
# TODO-249 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-250 - Add div with class "container login".
# TODO-251 - Add <h1> tag with class="h3 mb-4 fw-normal mb-5". Edit text as 'Create account'.
# TODO-252 - Using jinja render form. Add url for register along with next=request.args.get('next') to request the value
#  of next from the current page URL.

# reset_password.html
# TODO-253 - Add a file named "reset_password.html" in templates folder.
# TODO-254 - Include {% from 'bootstrap5/form.html' import render_form %} to render forms.
# TODO-255 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-256 - Use {% block title %} and add title 'Reset Password' in it. End with {% endblock %}.
# TODO-257 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-258 - Add div with class "container login".
# TODO-259 - Add <h1> tag with class="h3 mb-4 fw-normal mb-5". Edit text as 'Please sign in'.
# TODO-260 - Using jinja render form.

# success.html
# TODO-261 - Add a file named "success.html" in templates folder.
# TODO-262 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-263 - Use {% block title %} and add title 'Payment Successful' in it. End with {% endblock %}.
# TODO-264 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-265 - Add div with class="container text-center mt-5".
# TODO-266 - Add <h2> tag with class="text-success" which is a built-in bootstrap class for success message. Edit text
#  as 'Payment Successful'.
# TODO-267 - Add <p> tag with text as "Your order has been placed successfully.".
# TODO-268 - Add <a> tag. Define href as link for 'home' with class="btn btn-primary mt-3". Edit its text as
#  'Continue Shopping'.
# TODO-269 - Close <a> tag and div.

# search.html
# TODO-270 - Add a file named "search.html" in templates folder.
# TODO-271 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-272 - Use {% block title %} and add title 'Search' in it. End with {% endblock %}.
# TODO-273 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-274 - Add div with class="books-container". Create this class in style.css and add display as flex, flex
#  direction as column, gap, max-width, margin and padding.
# TODO-275 - Add <h2> tag and edit text as 'Search results for "{{ query }}"' where is query is added using jinja.
# TODO-276 - Add if condition using jinja to check if results exists. If true then add for loop using jinja to iterate
#  over items.
# TODO-277 - For each item, create a parent <div> with class="book-card". Create this class in style.css and add display
#  type as grid, gap, padding and bottom border.
# TODO-278 - Inside book-card, add an <img> tag to display the book image using {{ item.image }}. Add class="book-img"
#  to it which consists of width, height and object-fit: cover;. Add loading="lazy": this tells the browser to not load
#  this image immediately. Load it only when it is about to come into the user’s view. decoding="async": this tells the
#  browser can continue showing the page, image processing happens in the background. This helps page feel smoother.
# TODO-279 - Add a child <div> with class="book-info" to store book details like title, rating, reviews, price, and
#  button. Create this class ".book-info h3" in style.css and add font-size and bottom margin to it.
# TODO-280 - Inside book-info, add <h3> tag to display the book title using {{ item.title }}.
# TODO-281 - Add a <div> with class="rating" to show star rating and review count. Create this class and add text color,
#  font-size, margin and letter spacing.
# TODO-282 - Use Jinja set statement: {% set stars = item.rating|int %} to convert rating into integer value.
# TODO-283 - Add Jinja for loop: {% for i in range(stars) %}★{% endfor %} to display filled stars based on rating.
# TODO-284 - Add another Jinja for loop: {% for i in range(5-stars) %}☆{% endfor %} to display remaining empty stars up
#  to 5.
# TODO-285 - Inside rating div, add <span> with class="review-count" to display review count using {{ item.reviews }}.
#  Create this class and add text color, font-size, font-weight and left margin.
# TODO-286 - Add <p> tag with class="price" to display book price using ₹{{ item.price }}. Create this class and add
#  text color, font-weight and margin.
# TODO-287 - Add a <form> with method="POST" and action="{{ url_for('add_to_cart') }}" to send selected item to cart.
# TODO-288 - Inside the form, add hidden input field for title using <input type="hidden" name="title"
#  value="{{ item.title }}">, for price using <input type="hidden" name="price" value="{{ item.price }}"> and for image
#  using <input type="hidden" name="image" value="{{ item.image }}">.
# TODO-289 - Add a submit <button> with class="add-cart" and text 'Add to Cart'. Create this class and add background,
#  padding, border-radius, cursor as pointer with no border.
# TODO-290 - Add classes ".add-cart:hover" and ".add-cart:active" to give a feeling of button press. Both will contain
#  box-shadow and transform function for Y. Add transform: translateY(-3px); on hover while transform: translateY(0px);
#  in active class.
# TODO-291 - Close the for loop using {% endfor %} after all result items are displayed.
# TODO-292 - Add Jinja else block: {% else %} to handle the case when no results are found.
# TODO-293 - Inside else block, add <p> tag with text: "No results found for "{{ query }}"". Use jinja to show the
#  search query.
# TODO-294 - Close the if condition using {% endif %}. Close the div.

# header.html
# TODO-295 - Add a file named "header.html" in templates folder.
# TODO-296 - Add <header> tag with class="navbar" to create the top navigation bar section. Create this class in
#  style.css and add display type as grid, alignment, padding resolution for all screens, background, text color, gap,
#  width and box-sizing as border-box.
# TODO-297 - Add @media (max-width:700px) to apply styles only when the screen width is 700px or smaller. Inside class
#  ".navbar" which includes template column ratio and row-gap. Add class "search-bar" which includes order: 3; - the
#  search bar should appear as 3rd item and max-width: 200px;. Add class ".nav-right a" which includes font-size and
#  padding.
# TODO-298 - Add class ".navbar > * " and insert min-width as 0. This select every direct child inside .navbar and allow
#  it to shrink properly.
# TODO-299 - Inside navbar, add a <div> with class="logo" to hold brand name and tagline. Create this class and add
#  font-size resolution for all screens, font-weight, display type as grid and line-height.
# TODO-300 - Inside logo div, add <span> with class="brand" and text 'Shopora' for website name. Create this class and
#  add font-size resolution for all screens and font-weight.
# TODO-301 - Add another <span> with class="tagline" and text 'Shop Anything' for subtitle or tagline. Create this class
#  and add font-size resolution for all screens, text-color and letter spacing.
# TODO-302 - Add a <form> for search with action="{{ url_for('search') }}" and method="GET".
# TODO-303 - Add class="search-bar" to the form and create this class in style.css for layout and styling. Create this
#  class and add display tpe as grid and min-width as 0.
# TODO-304 - Inside the form, add input field of type="text" with name="q" to send search query to backend. Add
#  placeholder text as 'Search products' inside the input field. Set value="{{ request.args.get('q','') }}" so
#  previously searched text stays visible in the search box.
# TODO-305 - Create class ".search-bar input" and add padding and font-size resolution for all screens. Set min-width as
#  0 alongwith no border and outline.
# TODO-306 - Add a <button> inside search form with text 'Search' to submit the form. Create class ".search-bar button"
#  and add background, cursor as pointer, padding and font-size resolution for all screens along with no border.
# TODO-307 - Add a <div> with class="nav-right" to store navigation links on the right side. Create this class display
#  type as grid, grid-auto-flow: column;, grid-auto-columns: max-content;, gap, justify content to end, align items to
#  center and min-width as 0.
# TODO-308 - Inside nav-right, add anchor tag <a href="/">Home</a> for homepage navigation. Create class ".nav-right a"
#  and add display type as grid, place items to center, text-decoration: none;, text color, transition, padding and
#  font-size resolution for all screens.
# TODO-309 - Add class ".nav-right a:hover" to change style on hover. Add background, text color and border-radius to
#  it.
# TODO-310 - Add Jinja if condition: {% if current_user.is_authenticated %} to check whether user is logged in. If user
#  is logged in, add logout link using <a href="/logout">Logout</a>.
# TODO-311 - Add anchor tag linking to account settings page using <a href="/account_settings">. Inside it, add <span>
#  with class="user-avatar" to display user profile initial. Create this class and add background, text color,
#  border-radius, padding, font-size, font-weight, alignment, justify content to center and display as inline-flex.
# TODO-312 - display: inline-flex behaves like an inline element that takes only needed width.
# TODO-313 - Use {{ current_user.name[0] | upper }} to show the first letter of logged-in user's name in uppercase.
# TODO-314 - Add Jinja else block: {% else %} for users who are not logged in.
# TODO-315 - Inside else block, add login link using <a href="/login">Login</a>.
# TODO-316 - Add register link using <a href="/register">Register</a>.
# TODO-317 - Close authentication condition using {% endif %}.
# TODO-318 - Add cart link using <a href="/cart_page" class="cart"> to open cart page. Inside cart link, add cart icon
#  and text 'Cart'. Create "cart" class in style.css and add position as relative and font-weight.
# TODO-319 - Add <span> with class="cart-count" to show number of cart items. Create this class and add position as
#  absolute, top, right, background, text color, border-radius, padding and font-size resolution for all screens.
# TODO-320 - Inside cart-count, add Jinja if condition: {% if cart_count %} to check whether cart has items. If
#  cart_count exists, display {{ cart_count }}. Add else block to display 0 when cart is empty. Close cart_count
#  condition using {% endif %}.
# TODO-321 - Close all tags.

# index.html
# TODO-322 - Add a file named "index.html" in templates folder.
# TODO-323 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-324 - Use {% block title %} and add title 'Home' in it. End with {% endblock %}.
# TODO-325 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-326 - Add an input tag with type="checkbox", id="toggle-shop", and hidden attribute. Use this hidden checkbox to
#  control category section visibility or toggle behavior using CSS.
# TODO-327 - Make sure id="toggle-shop" matches the label's for attribute so clicking the label toggles the checkbox.
#  Create #toggle-shop:checked ~ .categories in style.css and add padding, text alignment and dispaly as block.
# TODO-328 - Add a <section> with class="hero" to create the main hero section of the homepage. Create this class and
#  add background, text color, padding and text alignment.
# TODO-329 - Inside hero section, add a <div> with class="hero-content" to store heading, description, and button.
#  Create this class and add max-width and margin.
# TODO-330 - Add <h1> tag with text 'Welcome to Shopora' as the main homepage heading. Create class ".hero h1" and add
#  font-size for all screens along with bottom margin.
# TODO-331 - Add <p> tag with text 'Discover Books, Electronics, Clothes, Furniture & More' as hero description. Create
#  class ".hero p" and add font-size for all screens along with bottom margin.
# TODO-332 - Add <label> tag with for="toggle-shop" and class="shop-btn" to act like a button. Add text
#  'Shop by Category' inside the label so user can click it to toggle category section.
# TODO-333 - Create class ".shop-btn" and add background, padding, font-size, cursor pointer, border-radius, text color,
#  display as inline-block, transition, box-shadow with no text decoration and border. display: inline-block - stays in
#  same line but width and height work.
# TODO-334 - Add classes ".shop-btn:hover" and ".shop-btn:active" to give a feeling of button press. Both will contain
#  box-shadow and transform function for Y. Add transform: translateY(-3px); on hover while transform: translateY(0px);
#  in active class. Additionally cjhange the background in hover function.
# TODO-335 - Add a <section> with id="categories" and class="categories" to display shopping categories. Create class
#  ".categories" and set this display as none to hide it by default. We have already seen toggling of categories above
#  using id toggle-shop.
# TODO-336 - Add <h2> tag with text 'Shop by Category' as section heading. Add a <div> with class="category-grid" to
#  hold all category cards in grid layout.
# TODO-337 - Create class ".category-grid" and add display type as grid, gap and top margin.
# TODO-338 - Inside category-grid, add anchor tag linking to books page using {{ url_for('books') }} and
#  class="category-card". Create this class in style.css and add background, padding, border-radius, box-shadow,
#  font-size, cursor pointer, display as inline-block, text color and no text-decoration.
# TODO-339 - Add classes ".category-card:hover" and ".category-card:active" to give a feeling of button press. Both will
#  contain box-shadow and transform function for Y. Add transform: translateY(-3px); on hover while
#  transform: translateY(0px); in active class. Add this class to all <a> tags.
# TODO-340 - Add text 'Books' inside the books category link.
# TODO-341 - Add anchor tag linking to clothes page using {{ url_for('clothes') }} and class="category-card". Add text
#  'Clothes' inside the clothes category link.
# TODO-342 - Add anchor tag linking to electronics page using {{ url_for('electronics') }} and class="category-card".
#  Add text 'Electronics' inside the electronics category link.
# TODO-343 - Add anchor tag linking to shoes page using {{ url_for('shoes') }} and class="category-card". Add text
#  'Shoes' inside the shoes category link.
# TODO-344 - Add anchor tag linking to furniture page using {{ url_for('furniture') }} and class="category-card". Add
#  text 'Furniture' inside the furniture category link.
# TODO-345 - Add another <section> with class="benefits" to display key features or advantages of the website. Create
#  this class and add padding, text alignment and background.
# TODO-346 - Add <h2> tag with text 'Why Shopora?' as benefits section heading.
# TODO-347 - Add a <div> with class="benefits-grid" to arrange all benefits in grid layout. Create this class and add
#  dispaly as grid, gap and top margin.
# TODO-348 - Inside benefits-grid, add <div> with class="benefit" and text 'Free Delivery'. Create this class and add
#  background, padding, border-radius, box-shadow and font-size. Change background, add box-shadow and transform
#  function on hover.
# TODO-349 - Add other benefit divs with text 'Secure Payments', 'Easy Returns' and 'Quality Products'.
# TODO-350 - Close all divs and section.

# products.html
# TODO-351 - Add a file named "products.html" in templates folder.
# TODO-352 - Extend base.html file using Jinja template {% extends "base.html" %} to include all everything accept main
#  body.
# TODO-353 - Use {% block title %} and add title using jinjs {{ title }} in it. End with {% endblock %}.
# TODO-354 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-355 - Add a parent <div> with class="books-layout" to hold both sidebar filters and product listing section.
# TODO-356 - Create class="books-layout" in style.css and style it by adding display type as grid, gap and padding.
# TODO-357 - Add <aside> tag with class="filters" to create the sidebar filter section. Create this class and add
#  padding, background, border-radius, height to fit content, top and position as sticky. Position is sticky so that it
#  stays at its place when page is scrolled.
# TODO-358 - Inside filters sidebar, add <h3> tag to display selected category name dynamically.
# TODO-359 - Use Jinja expression {{ selected_category|replace('-', ' ')|title if selected_category != 'all' else title
#  }} to show formatted selected category name.
# TODO-360 - If selected_category is not 'all', replace hyphens with spaces and convert text into title case. If
#  selected_category is 'all', display the page title instead.
# TODO-361 - Create class ".filters h3" and add bottom margin in it.
# TODO-362 - Add unordered list <ul> inside the filters sidebar to show all filter options. Create class ".filters ul".
#  Set list-style as none and padding as 0.
# TODO-363 - Add first list item <li> for 'All' category. Create class ".filters li" and add bottom margin to it.
# TODO-364 - Inside it, add anchor tag linking to current route using {{ url_for(request.endpoint) }}.
# TODO-365 - Add class="filter-link" to the anchor tag for common filter link styling. Create this class and add
#  padding, text color, border-radius, display type as block and text-decoration as none. Change background and text
#  color on hover.
# TODO-366 - Use Jinja if condition inside class attribute to add class="active-filter" when selected_category == 'all'.
#  Create class ".active-filter" and add background, text color, border-radius and font-weight.
# TODO-367 - Add Jinja for loop: {% for category in categories %} to iterate through all categories. Inside loop, add
#  list item <li> for each category.
# TODO-368 - Add anchor tag linking to same endpoint with category parameter using
#  {{ url_for(request.endpoint, category=category) }}. Add class="filter-link" to all category links.
# TODO-369 - Use Jinja if condition to add class="active-filter" when selected_category matches the current category.
# TODO-370 - Display formatted category name using {{ category|replace('-', ' ')|title }}.
# TODO-371 - Close the category loop using {% endfor %}.
# TODO-372 - Add <section> with class="books-container" to display all product cards.
# TODO-373 - Add Jinja outer loop: {% for category, items in products.items() %} to iterate through category-wise
#  product data.
# TODO-374 - Add inner loop: {% for item in items %} to iterate through each product item inside a category.
# TODO-375 - For each item, add parent <div> with class="book-card" to create a product card.
# TODO-376 - Inside book-card, add <img> tag with src="{{ item.image }}" and class="book-img" to show product image.
# TODO-377 - Add loading="lazy" and decoding="async" attributes to optimize image loading performance.
# TODO-378 - Add child <div> with class="book-info" to store all textual product details. Inside book-info, add <h3> tag
#  to display product title using {{ item.title }}.
# TODO-379 - Add Jinja if condition: {% if item.author %} to check if author exists.
# TODO-380 - If author is available, add <p> tag with class="author" and display text 'By: {{ item.author }}'. Create
#  class ".author" in style.css and add text color and font-size in it. Close author condition using {% endif %}.
# TODO-381 - This author line is mainly useful for books and can be skipped for other product categories.
# TODO-382 - Add <div> with class="rating" to display star rating and reviews.
# TODO-383 - Use Jinja set statement: {% set stars = item.rating|default(0)|int %} to safely convert rating to integer.
# TODO-384 - Use default(0) so code does not break if rating is missing.
# TODO-385 - Add Jinja loop: {% for i in range(stars) %}★{% endfor %} to display filled stars. Add second Jinja loop:
#  {% for i in range(5-stars) %}☆{% endfor %} to display remaining empty stars.
# TODO-386 - Add <span> with class="review-count" to display review count using {{ item.reviews }}.
# TODO-387 - Add <p> tag with class="price" to display product price using ₹{{ item.price }}.
# TODO-388 - Add <form> with method="POST" and action="{{ url_for('add_to_cart') }}" to submit selected product to cart.
# TODO-389 - Inside the form, add hidden input field for title using <input type="hidden" name="title"
#  value="{{ item.title }}">.
# TODO-390 - Add hidden input field for price using <input type="hidden" name="price" value="{{ item.price }}">.
# TODO-391 - Add hidden input field for image using <input type="hidden" name="image" value="{{ item.image }}">.
# TODO-392 - Add submit button with class="add-cart" and text 'Add to Cart'.
# TODO-393 - Close inner item loop using {% endfor %}. Close outer category loop using {% endfor %}. Close
#  books-container section and books-layout div properly.

# cart.html
# TODO-394 - Extend base.html using Jinja template: {% extends "base.html" %} so common layout like navbar and footer
#  are reused.
# TODO-395 - Add {% block title %} and set page title as 'Cart'. Close it using {% endblock %}.
# TODO-396 - Add {% block content %} and {% endblock %} to wrap the main cart page content.
# TODO-397 - Add a parent <div> with class="container mt-5" to create Bootstrap container with top margin.
# TODO-398 - Inside container, add <div> with class="row" to create Bootstrap row layout.
# TODO-399 - Add left-side column using <div class="col-md-8"> for cart items section. Inside left column, add <h2>
#  heading with class="mb-4" and text 'Your Cart'.
# TODO-400 - Add Jinja if condition: {% if items %} to check whether cart contains items. Add Jinja for loop:
#  {% for item in items %} to iterate through each cart item.
# TODO-401 - For each item, add parent <div> with classes="cart-item d-flex align-items-center mb-4 p-3 shadow-sm".
#  Create class ".cart-item" in style.css and add border-radius, background and box-shadow. Add class ".cart-item form"
#  for form and add margin:0; in it.
# TODO-402 - Create another class ".cart-item span" for span tag and add min-width, text alignment and font-weight. Add
#  transform function to move it up and transition function to smoothen the transformation.
# TODO-403 - Use d-flex and align-items-center to place image and content side by side and vertically aligned. Add
#  margin bottom, padding, and shadow using Bootstrap utility classes.
# TODO-404 - Inside cart-item, add <img> tag with src="{{ item.image }}" to display item image. Set width="100" and add
#  class="me-3" to create spacing between image and item details.
# TODO-405 - Add child <div> with class="flex-grow-1" so item details take remaining horizontal space.
# TODO-406 - Inside it, add <h5> tag to display product title using {{ item.title }}.
# TODO-407 - Add <p> with class="text-muted" to display product price using ₹{{ item.price }}.
# TODO-408 - Add a nested <div> with classes="d-flex align-items-center gap-3" to keep quantity controls and remove
#  button close together.
# TODO-409 - Add form for decrease action with action="{{ url_for('update_cart', item_id=item.id) }}" and method="POST".
# TODO-410 - Inside decrease form, add hidden input field with name="action" and value="decrease".
# TODO-411 - Add submit button with classes="btn btn-outline-secondary btn-sm" and text '−'. Create class
#  "btn-outline-secondary" in style.css and add height, width, font-size, line-height with 0 padding. Add display as
#  flex and align items to center.
# TODO-412 - Add <span> with class="px-2" to display current item quantity using {{ item.quantity }}.
# TODO-413 - Add form for increase action with action="{{ url_for('update_cart', item_id=item.id) }}" and method="POST".
# TODO-414 - Inside increase form, add hidden input field with name="action" and value="increase".
# TODO-415 - Add submit button with classes="btn btn-outline-secondary btn-sm" and text '+'.
# TODO-416 - Add remove form with action="{{ url_for('remove_from_cart', item_id=item.id) }}" and method="POST".
# TODO-417 - Add remove button with classes="btn btn-danger btn-sm" and text 'Remove'.
# TODO-418 - Close item loop using {% endfor %}.
# TODO-419 - Add Jinja else block: {% else %} to handle empty cart case. Inside else block, add <p> tag with text 'Your
#  cart is empty.'.
# TODO-420 - Close items condition using {% endif %}.
# TODO-421 - Add right-side column using <div class="col-md-4"> for payment section. Inside it, add <div> with
#  class="payment-box p-4 shadow-sm" to create payment panel.
# TODO-422 - Add <h4> heading with class="mb-3" and text 'Secure Payment'.
# TODO-423 - Add Jinja if condition: {% if items %} to show payment form only when cart has items.
# TODO-424 - Add form with action="{{ url_for('fake_payment') }}" and method="POST" for payment submission.
# TODO-425 - Add label with text 'Card Number'.
# TODO-426 - Add input field with type="text", name="card_number", class="form-control mb-2", placeholder="1234 5678
#  9012 3456", and required attribute.
# TODO-427 - Add wrapper <div> with classes="d-flex gap-2 mt-3" to place expiry and CVV side by side.
# TODO-428 - Add child <div> with class="w-50" for expiry field. Add label with text 'Expiry'.
# TODO-429 - Add input field with type="text", name="expiry", class="form-control mb-3", and placeholder="MM/YY".
# TODO-430 - Add pattern="(0[1-9]|1[0-2])\/\d{2}" to validate expiry in MM/YY format.
# TODO-431 - Add title="Enter in MM/YY format" to show hint on invalid input. Add maxlength="5" and required attribute.
# TODO-432 - Add second child <div> with class="w-50" for CVV field. Add label with text 'CVV'.
# TODO-433 - Add input field with type="password", name="cvv", class="form-control mb-3", placeholder="***",
#  maxlength="3", and required attribute. Create class ".form-control" and set its bottom margin.
# TODO-434 - Add element "input[name="expiry"], input[name="cvv"]" in style.css and add text alignment and letter
#  spacing for both of them.
# TODO-435 - Add submit button with type="submit" and classes="btn pay-btn w-100 mt-2". Create class ".pay-btn" in
#  style.css and add background, text color, border-radius, padding, font-weight, transition with no border. Change
#  background on hover and add transform and opacity when active.
# TODO-436 - Display total payment amount inside button using text 'Pay ₹{{ total }}'.
# TODO-437 - Add Jinja else block for empty cart payment UI.
# TODO-438 - Inside else block, add <div> with classes="text-center text-muted".
# TODO-439 - Add <p> tag with text 'Your cart is empty'.
# TODO-440 - Add disabled button with classes="btn btn-secondary w-100 mt-2" and text 'Add items to proceed'. In
#  style.css add "button:disabled" which consist of opacity and cursor: not-allowed; to prevent fake payment when cart
#  is empty.
# TODO-441 - Close payment condition using {% endif %}.
# TODO-442 - Close all Bootstrap row, column, and container divs properly.





from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap5
import requests
import os
import pandas as pd
from random import randint, uniform
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from email.message import EmailMessage
from smtplib import SMTP
from dotenv import load_dotenv
from flask_login import LoginManager
from itsdangerous import URLSafeTimedSerializer
import re
from datetime import datetime



app = Flask(__name__)
app.secret_key = "any-string-you-want-to-keep-secret"
bootstrap = Bootstrap5(app)
serializer = URLSafeTimedSerializer(app.secret_key)

load_dotenv()


# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = None


BOOKS_FILE = "books.csv"
ELECTRONICS_FILE = "electronics.csv"
CLOTHES_FILE = "clothes.csv"
SHOES_FILE = "shoes.csv"
FURNITURE_FILE = "furniture.csv"


Rainforest_API_Key = os.getenv("RAINFOREST_API_KEY")

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# Category	API
# Electronics	DummyJSON
# Clothes	FakeStoreAPI
# Books	Google Books API
# Shoes/Fashion	Platzi Fake Store
# Full store demo	JSONData API

books_url = 'https://www.googleapis.com/books/v1/volumes'
products_url = 'https://dummyjson.com/products/category/'
search_url = "https://api.rainforestapi.com/request"


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
# Create a User table for all your registered users
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(db.String(100), unique=True)
    password: Mapped[str] = mapped_column(db.Text, nullable=False)
    name: Mapped[str] = mapped_column(db.String(100))

    cart_items = db.relationship('Cart', back_populates='user')

# Cart table
class Cart(db.Model):
    __tablename__ = 'cart'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(db.Text)
    price: Mapped[int] = mapped_column(db.Integer)
    image: Mapped[str] = mapped_column(db.Text)
    quantity: Mapped[int] = mapped_column(db.Integer)

    user = db.relationship('User', back_populates='cart_items')


# Register Form
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

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
    # db.drop_all()
    # db.create_all()


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


def generate_meta(category):

    ranges = {

        # BOOKS
        "fiction": (199, 499, 3.9, 4.7, 200, 6000),
        "fantasy": (299, 699, 4.0, 4.8, 500, 8000),
        "mystery": (199, 499, 3.8, 4.6, 150, 5000),
        "science fiction": (299, 699, 4.0, 4.8, 300, 7000),
        "romance": (149, 399, 3.7, 4.5, 100, 4000),
        "history": (399, 899, 4.0, 4.7, 200, 5000),
        "biography": (399, 899, 4.1, 4.8, 300, 6000),
        "business": (499, 1199, 4.1, 4.8, 500, 9000),
        "self-help": (299, 799, 4.0, 4.7, 500, 10000),
        "technology": (599, 1999, 4.2, 4.8, 200, 5000),

        # CLOTHES
        "mens-shirts": (499, 1999, 3.8, 4.6, 50, 3500),
        "womens-dresses": (799, 3999, 3.9, 4.7, 80, 4000),
        "tops": (399, 1499, 3.7, 4.5, 40, 3000),

        # ELECTRONICS
        "smartphones": (8000, 120000, 4.0, 4.8, 500, 25000),
        "laptops": (30000, 200000, 4.0, 4.7, 200, 15000),
        "tablets": (10000, 90000, 4.0, 4.7, 150, 10000),
        "mobile-accessories": (199, 3999, 3.7, 4.6, 50, 20000),
        "mens-watches": (999, 15000, 3.8, 4.6, 40, 5000),
        "womens-watches": (899, 12000, 3.8, 4.6, 40, 4500),

        # SHOES
        "mens-shoes": (1199, 8999, 3.8, 4.7, 50, 6000),
        "womens-shoes": (999, 7999, 3.8, 4.7, 40, 5500),

        # HOME
        "furniture": (3000, 80000, 3.9, 4.6, 20, 2500),
        "home-decoration": (399, 6999, 3.8, 4.6, 30, 4000),
        "kitchen-accessories": (199, 2999, 3.7, 4.5, 50, 8000),
    }

    p_min, p_max, r_min, r_max, rev_min, rev_max = ranges.get(
        category,
        (299, 4999, 3.8, 4.6, 20, 4000)
    )

    price = randint(p_min, p_max)
    rating = round(uniform(r_min, r_max), 1)
    reviews = randint(rev_min, rev_max)

    return price, rating, reviews


def detect_category(title):

    t = title.lower()

    # books
    if any(x in t for x in ["book", "novel", "author", "guide"]):
        return "books"

    # electronics
    if any(x in t for x in ["iphone","phone","smartphone","laptop","tablet","watch","headphone","earbuds"]):
        return "electronics"

    # clothes
    if any(x in t for x in ["shirt","t-shirt","dress","hoodie","jacket","top","jeans"]):
        return "clothes"

    # shoes
    if any(x in t for x in ["shoe","sneaker","boot","running shoe","trainer"]):
        return "shoes"

    # furniture
    if any(x in t for x in ["chair","table","sofa","desk","bed","cabinet"]):
        return "furniture"

    return "general"


def generate_meta_search(category):

    ranges = {

        "books": (199, 999, 3.8, 4.8, 50, 8000),

        "clothes": (399, 2999, 3.6, 4.7, 20, 5000),

        "shoes": (999, 8999, 3.8, 4.7, 40, 6000),

        "electronics": (2999, 120000, 4.0, 4.8, 100, 20000),

        "furniture": (3000, 80000, 3.9, 4.6, 20, 2500),

        "general": (299, 4999, 3.7, 4.6, 20, 4000)
    }

    p_min, p_max, r_min, r_max, rev_min, rev_max = ranges[category]

    price = randint(p_min, p_max)
    rating = round(uniform(r_min, r_max), 1)
    reviews = randint(rev_min, rev_max)

    return price, rating, reviews


# ------------------------------
# HOME
# ------------------------------

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/books')
def books():

    selected_category = request.args.get("category", "all")

    categories = [
        "fiction",
        "fantasy",
        "mystery",
        "science fiction",
        "romance",
        "history",
        "biography",
        "business",
        "self-help",
        "technology"
    ]

    if os.path.exists(BOOKS_FILE):
        data = pd.read_csv(BOOKS_FILE)
    else:
        data = pd.DataFrame()

    if data.empty:

        rows = []

        for category in categories:

            params = {
                "q": f"subject:{category}",
                "maxResults": 20
            }

            response = requests.get(books_url, params=params)

            if response.status_code == 200:

                products = response.json().get("items", [])

                for item in products:

                    volume = item.get("volumeInfo", {})

                    image = volume.get("imageLinks", {}).get("thumbnail", "https://via.placeholder.com/150")

                    price, rating, reviews = generate_meta(category)

                    rows.append({
                        "category": category,
                        "title": volume.get("title", "Unknown Book"),
                        "author": ", ".join(volume.get("authors", ["Unknown Author"])),
                        "image": image,
                        "price": price,   # Google API has no price
                        "rating": rating,
                        "reviews": reviews
                    })

        data = pd.DataFrame(rows)
        data.to_csv(BOOKS_FILE, index=False)

    products_data = (
        data.groupby("category")
        .apply(lambda x: x.to_dict("records"))
        .to_dict()
    )

    if selected_category != "all":
        products_data = {
            selected_category: products_data.get(selected_category, [])
        }

    return render_template(
        "products.html",
        products=products_data,
        selected_category=selected_category,
        categories=categories,
        title="Books"
    )



@app.route('/clothes')
def clothes():

    selected_category = request.args.get("category", "all")

    categories = ["mens-shirts", "womens-dresses", "tops"]

    if os.path.exists(CLOTHES_FILE):
        data = pd.read_csv(CLOTHES_FILE)
    else:
        data = pd.DataFrame()

    if data.empty:

        rows = []

        for category in categories:

            response = requests.get(f'{products_url}{category}')

            if response.status_code == 200:

                products = response.json()["products"]

                for item in products:

                    price, rating, reviews = generate_meta(category)

                    rows.append({
                        "category": category,
                        "title": item["title"],
                        "image": item["thumbnail"],
                        "price": price,
                        "rating": rating,
                        "reviews": reviews
                    })

        data = pd.DataFrame(rows)
        data.to_csv(CLOTHES_FILE, index=False)

    products_data = (
        data.groupby("category")
        .apply(lambda x: x.to_dict("records"))
        .to_dict()
    )

    if selected_category != "all":
        products_data = {
            selected_category: products_data.get(selected_category, [])
        }

    return render_template(
        "products.html",
        products=products_data,
        selected_category=selected_category,
        categories=categories,
        title="Clothes"
    )



@app.route('/electronics')
def electronics():

    selected_category = request.args.get("category", "all")

    categories = ["smartphones", "laptops", "tablets", "mobile-accessories", "mens-watches", "womens-watches"]

    if os.path.exists(ELECTRONICS_FILE):
        data = pd.read_csv(ELECTRONICS_FILE)
    else:
        data = pd.DataFrame()

    if data.empty:

        rows = []

        for category in categories:

            response = requests.get(f'{products_url}{category}')

            if response.status_code == 200:

                products = response.json()["products"]

                for item in products:
                    price, rating, reviews = generate_meta(category)

                    rows.append({
                        "category": category,
                        "title": item["title"],
                        "image": item["thumbnail"],
                        "price": price,
                        "rating": rating,
                        "reviews": reviews
                    })

        data = pd.DataFrame(rows)
        data.to_csv(ELECTRONICS_FILE, index=False)

    products_data = (
        data.groupby("category")
        .apply(lambda x: x.to_dict("records"))
        .to_dict()
    )

    if selected_category != "all":
        products_data = {
            selected_category: products_data.get(selected_category, [])
        }

    return render_template(
        "products.html",
        products=products_data,
        selected_category=selected_category,
        categories=categories,
        title="Electronics"
    )



@app.route('/shoes')
def shoes():

    selected_category = request.args.get("category", "all")

    categories = ["mens-shoes", "womens-shoes"]

    if os.path.exists(SHOES_FILE):
        data = pd.read_csv(SHOES_FILE)
    else:
        data = pd.DataFrame()

    if data.empty:

        rows = []

        for category in categories:

            response = requests.get(f'{products_url}{category}')

            if response.status_code == 200:

                products = response.json()["products"]

                for item in products:
                    price, rating, reviews = generate_meta(category)

                    rows.append({
                        "category": category,
                        "title": item["title"],
                        "image": item["thumbnail"],
                        "price": price,   # Google API has no price
                        "rating": rating,
                        "reviews": reviews
                    })

        data = pd.DataFrame(rows)
        data.to_csv(SHOES_FILE, index=False)

    products_data = (
        data.groupby("category")
        .apply(lambda x: x.to_dict("records"))
        .to_dict()
    )

    if selected_category != "all":
        products_data = {
            selected_category: products_data.get(selected_category, [])
        }

    return render_template(
        "products.html",
        products=products_data,
        selected_category=selected_category,
        categories=categories,
        title="Shoes"
    )



@app.route('/furniture')
def furniture():

    selected_category = request.args.get("category", "all")

    categories = ["furniture", "home-decoration", "kitchen-accessories"]

    if os.path.exists(FURNITURE_FILE):
        data = pd.read_csv(FURNITURE_FILE)
    else:
        data = pd.DataFrame()

    if data.empty:

        rows = []

        for category in categories:

            response = requests.get(f'{products_url}{category}')

            if response.status_code == 200:

                products = response.json()["products"]

                for item in products:
                    price, rating, reviews = generate_meta(category)

                    rows.append({
                        "category": category,
                        "title": item["title"],
                        "image": item["thumbnail"],
                        "price": price,   # Google API has no price
                        "rating": rating,
                        "reviews": reviews
                    })

        data = pd.DataFrame(rows)
        data.to_csv(FURNITURE_FILE, index=False)

    products_data = (
        data.groupby("category")
        .apply(lambda x: x.to_dict("records"))
        .to_dict()
    )

    if selected_category != "all":
        products_data = {
            selected_category: products_data.get(selected_category, [])
        }

    return render_template(
        "products.html",
        products=products_data,
        selected_category=selected_category,
        categories=categories,
        title="Furniture"
    )



@app.route("/search")
def search():

    # total 100 requests are allowed.
    # used = 7
    # remaiining = 93

    query = request.args.get("q", "").strip()

    results = []

    try:
        params = {
            "api_key": Rainforest_API_Key,
            "type": "search",
            "amazon_domain": "amazon.com",
            "search_term": query
        }

        response = requests.get(search_url, params=params, timeout=10)

        data = response.json()

        for item in data.get("search_results", []):

            title = item.get("title", "")

            category = detect_category(title)

            price, rating, reviews = generate_meta_search(category)

            results.append({
                "title": item.get("title"),
                "image": item.get("image"),
                "price": price,   # Google API has no price
                "rating": rating,
                "reviews": reviews
            })

    except Exception as e:
        print("Rainforest search error:", e)

    return render_template(
        "search.html",
        results=results,
        query=query
    )



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()

        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.", "danger")
            return redirect(url_for('login', next=request.args.get("next")))
        # Password incorrect
        elif not check_password_hash(user.password, form.password.data):
            flash("Password incorrect, please try again.", "danger")
            return redirect(url_for('login', next=request.args.get("next")))
        else:
            login_user(user)
            flash("Login successful.", "success")

            # Add pending item to cart
            pending = session.pop("pending_cart", None)

            if pending:
                item = Cart.query.filter_by(user_id=current_user.id, title=pending["title"]).first()

                if item:
                    item.quantity += 1
                else:
                    new_item = Cart(
                        user_id=current_user.id,
                        title=pending["title"],
                        price=pending["price"],
                        image=pending["image"],
                        quantity=1
                    )

                    db.session.add(new_item)

                db.session.commit()

                flash("Item added to cart successfully!", "success")

            next_page = request.args.get("next")
            return redirect(next_page or url_for('home'))

    return render_template('login.html', form=form)



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
            return redirect(url_for('login', next=request.args.get("next")))

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

        flash("Account created successfully!", "success")

        next_page = request.args.get("next")
        return redirect(next_page or url_for("home"))

    return render_template('register.html', form=form)



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



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for('home'))



# To update cart count
@app.context_processor
def inject_cart_count():

    if current_user.is_authenticated:

        count = db.session.query(db.func.sum(Cart.quantity)).filter_by(user_id=current_user.id).scalar()

        return dict(cart_count=count)

    return dict(cart_count=0)



@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():

    title = request.form.get("title")
    price = request.form.get("price")
    image = request.form.get("image")

    # If User not logged in
    if not current_user.is_authenticated:

        session["pending_cart"] = {
            "title": title,
            "price": price,
            "image": image
        }

        return redirect(url_for("login", next=request.referrer))

    # If User logged in
    item = Cart.query.filter_by(user_id=current_user.id, title=title).first()

    if item:
        item.quantity += 1
    else:
        new_item = Cart(
            user_id=current_user.id,
            title=title,
            price=price,
            image=image,
            quantity=1
        )

        db.session.add(new_item)

    db.session.commit()

    flash("Item added to cart successfully!", "success")

    return redirect(request.referrer or url_for("home")) #check if this works or not



@app.route("/cart_page")
@login_required
def cart_page():

    items = Cart.query.filter_by(user_id=current_user.id).all()

    total = sum(item.price * item.quantity for item in items)

    return render_template(
        "cart.html",
        items=items,
        total=total
    )



@app.route("/update-cart/<int:item_id>", methods=["POST"])
@login_required
def update_cart(item_id):

    action = request.form.get("action")

    item = Cart.query.get(item_id)

    if item and item.user_id == current_user.id:

        if action == "increase":
            item.quantity += 1

        elif action == "decrease":
            item.quantity -= 1

            # Remove item if quantity becomes 0
            if item.quantity <= 0:
                db.session.delete(item)
                db.session.commit()
                return redirect(url_for("cart_page"))
        db.session.commit()

    return redirect(url_for("cart_page"))



@app.route("/remove-from-cart/<int:item_id>", methods=["POST"])
@login_required
def remove_from_cart(item_id):

    item = Cart.query.get(item_id)

    if item and item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()

    return redirect(url_for("cart_page"))



@app.route("/fake-payment", methods=["POST"])
@login_required
def fake_payment():

    items = Cart.query.filter_by(user_id=current_user.id).all()

    # 🚫 If cart is empty → block payment
    if not items:
        flash("Your cart is empty. Add items before making a payment.", "warning")
        return redirect(url_for("cart_page"))

    card_number = request.form.get("card_number", "").replace(" ", "")
    expiry = request.form.get("expiry", "")
    cvv = request.form.get("cvv", "")

    # Card Number Validation
    if not re.fullmatch(r"\d{16}", card_number):
        flash("Invalid card number. Must be 16 digits.", "danger")
        return redirect(url_for("cart_page"))

    # CVV Validation
    if not re.fullmatch(r"\d{3}", cvv):
        flash("Invalid cvv. Must be 3 digits.", "danger")
        return redirect(url_for("cart_page"))

    #  Expiry Validation
    if not re.fullmatch(r"(0[1-9]|1[0-2])\/\d{2}", expiry):
        flash("Invalid expiry format. Use MM/YY.", "danger")
        return redirect(url_for("cart_page"))

    # Check if expired
    month, year = expiry.split("/")
    month = int(month)
    year = int("20" + year)

    now = datetime.now()

    if year < now.year or (year == now.year and month < now.month):
        flash("Card has expired.", "danger")
        return redirect(url_for("cart_page"))

    # Clear cart after payment
    Cart.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()

    session["payment_done"] = True

    flash("Payment successful!", "success")

    return redirect(url_for("success"))



@app.route("/success")
@login_required
def success():
    if not session.pop("payment_done", None):
        return redirect(url_for("home"))
    return render_template("success.html")



if __name__ == '__main__':
    app.run(debug=True, port=5001)