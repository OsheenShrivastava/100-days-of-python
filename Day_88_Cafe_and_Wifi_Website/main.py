# main.py file
# TODO-1 - Import Flask, render_template, redirect, url_for and flash from flask module.
# TODO-2 - Initialize Flask with app and create a home route.
# TODO-3 - Render template index.html.
# TODO-4 - Run the app. Check if the name of the file is "main" -->if __name__ == '__main__':. If true, then run the app
#  set debug=True which auto-reloads server when code changes,shows detailed error pages (stack traces) and enables
#  interactive debugger. Set the port to 5001.
# TODO-5 - Import FlaskForm from flask_wtf. Import Bootstrap5 from flask_bootstrap.
# TODO-6 - Import DataRequired from wtforms.validators. Import StringField, SubmitField, BooleanField from wtforms.
# TODO-7 - Import SQLAlchemy from flask_sqlalchemy. Import DeclarativeBase from sqlalchemy.orm.
# TODO-8 - Add secret key for Cross-Site Request Forgery (CSRF) attcks protection.
# TODO-9 - Initialise Bootstrap5.
# TODO-10 - Create a folder named "instance" and add cafes.db file in it which contains details of different cafes.
# TODO-11 - Create a folder named "static". Add another folder named "img" and add all the required images in it.
# TODO-12 - Create style.css file inside "static" folder.
# TODO-13 - Add requirements.txt file and install the given versions - WTForms==3.0.1, Flask_WTF==1.2.1, Flask==3.0.2,
#  Flask-SQLAlchemy==3.1.1, SQLAlchemy==2.0.28, Werkzeug==3.0.1 and Bootstrap-Flask==2.3.3.
# TODO-14 - Initialize db by creating class Base(DeclarativeBase): and add pass inside it. DeclarativeBase is a base
#  class provided by SQLAlchemy. It creates a base class for all ORM (Object-Relational Mapping) models.
# TODO-15 - Define path for cafes.db using app.config --> app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'.
# TODO-16 - Create an object db from SQLAlchemy(model_class=Base) like this --> db = SQLAlchemy(model_class=Base). This
#  is used to read and write data to db.
# TODO-17 - Now db exists, but it is NOT yet connected to any Flask app. So, add db.init_app(app) which is a
#  Flask-SQLAlchemy initialization step that connects your database object (db) with your Flask app (app).
# TODO-18 - Now we will create a db model which matches the existing cafe.db table. Create class Cafe(db.Model) where
#  db.Model is the base ORM class provided by Flask-SQLAlchemy. __tablename__ = 'cafe' sets the table name in the
#  database.
# TODO-19 - Define the database column, define its Column data type. Here we will define the data type as Integer for
#  id. Set primary_key=True as this column uniquely identifies each row. It means Values must be unique, Values cannot
#  be NULL,Database automatically indexes it and Usually auto-increments.
# TODO-20 - Define column datatype String for name,map_url,img_url,location,seats and coffee_price. Add nullable=False
#  means this column should not be empty.
# TODO-21 - Similarly, define column datatype Boolean for has_sockets,has_toilet,has_wifi and can_take_calls. Add
#  nullable=False.
# TODO-22 - Add method to_dict inside class Cafe to convert the table to dictionary for ease of access.
#  self.__table__.columns accesses the database table definition which contains all columns of the model.
#  for column in self.__table__.columns loops over each column object. column.name gets the column name as a string.
#  getattr(self, column.name) dynamically fetches the value from the object.
# TODO-23 - Create form CafeForm(FlaskForm) to create flask form to add new cafe. Use StringField function, add label
#  which will be seen by user and validators=[DataRequired()] to validate form input. Use StringField for cafe_name,
#  location_url, image_url, location_name, number_of_seats and average_coffee_price.
# TODO-24 - Use BooleanField for toilets, wifi, sockets and calls. No validators are required for Boolean.
# TODO-25 - Use SubmitField for submit button.
# TODO-26 - Create form ApiKeyForm(FlaskForm) to create flask form for API Key. Use StringField function for api_key
#  along with validators=[DataRequired()]. Use SubmitField for delete button.
# TODO-27 - In @app.route('/'), inside home() function sort through cafe db using cafe name and sort it in ascending
#  order. Store the output in result variable.
# TODO-28 - Result is a SQLAlchemy Result object, not a list yet. scalars() function is used to extract only the model
#  objects (Cafe) and removes tuple wrapping. all() converts the result into a list. Store this list in all_cafes.
# TODO-29 - Convert all_cafes list to dictionary using to_dict() function in a FOR loop. Store this dictionary in cafes.
# TODO-30 - Render template "index.html" and pass cafes to it.
# TODO-31 - Add another route '/add_new_cafe' to add new cafe. Add GET and POST methods to accept data from form and add
#  it to db. Create add_new_cafe function.
# TODO-32 - Inside add_new_cafe() function, create add_new_cafe_form object from CafeForm() class. Check if submit
#  button is pressed using if add_new_cafe_form.validate_on_submit():. If yes, then save the data from form to db like
#  this --> cafe_name = add_new_cafe_form.cafe_name.data. Take all the parameters from form and save them in different
#  variables.
# TODO-33 - Create another object "new_cafe" of class Cafe() and inside this add these variables to the respective db
#  variables to create new cafe.
# TODO-34 - Use this --> db.session.add(new_cafe) to add this new cafe to db. Use db.session.commit() to save this in
#  database.
# TODO-35 - Redirect to home using redirect(url_for('home')) after saving.
# TODO-36 - Render template add_new_cafe_edit_cafe.html to display the form page and pass add_new_cafe_form in it.
# TODO-37 - Add another route '/edit_cafe/<int:cafe_id>' to edit cafe. Add GET and POST methods to accept data from
#  form and add the changes to db. Create edit_cafe function and pass cafe_id.
# TODO-38 - Obtain current cafe record by passing cafe_id to query.get() function. Store this in cafe variable.
# TODO-39 - Create another object edit_cafe_form from class CafeForm() and store all the form details to different
#  variables.
# TODO-40 - Check if submit button is pressed, if yes then take the data from these variables and store them to their
#  respective db variables. Add db.session.commit() function to save them to db. Redirect to home using
#  redirect(url_for('home')) after saving.
# TODO-41 - Render template add_new_cafe_edit_cafe.html to display the form page, pass add_new_cafe_form in it along
#  with variable is_edit=True. "is_edit" variable is passed to differentiate between adding new cafe and editing
#  existing cafe.
# TODO-42 - Add another route '/delete_cafe/<int:cafe_id>' to edit cafe. Add GET and POST methods to accept data from
#  form and add the changes to db. Create delete_cafe function and pass cafe_id.
# TODO-43 - Create an object api_key_form from class ApiKeyForm(). Obtain current cafe record by passing cafe_id to
#  query.get() function. Store this in cafe variable.
# TODO-44 - Check if submit button is pressed, if yes then obtain api_key from api_key_form and check if api_key is
#  equal to the correct key. If yes then delete cafe using db.session.delete(cafe) and save the final db after deleting
#  using db.session.commit().
# TODO-45 - Use flash() function to display successful deletion of cafe. Redirect to home using
#  redirect(url_for('home')) after saving.
# TODO-46 - If api_key entered is incorrect, then flash "Invalid API Key" message to the user.
# TODO-47 - Render template delete_cafe.html to display the API key form page, pass api_key_form in it along
#  with the cafe record of the form to be deleted.

# header.html file
# TODO-48 - Create a folder named templates and add a html file. Name it header.html.
# TODO-49 - Set language as English, set charset="UTF-8", Title="Cafe & WiFi. Add Bootstrap link for styling in head
#  section and script link in body section.
# TODO-50 - Use {% block styles %} and load bootstrap style using {% block styles %} as bootstrap.load_css(). Add
#  Bootstrap links for fonts Amatic SC and Handlee. Add external link for style.css.
# TODO-51 - Inside body section, add bootstrap template for header section. Choose your own. Add logo using <img> tag
#  and add image to it. This template consists of content enclosed in <p> tag. 2 buttons one to "Add New Cafe" and
#  second "Home" button.
# TODO-52 - In style.css, Grid type of display is used for header section along with background image. Add color, font
#  and spacing for <p> tag. Add border-radius, width and alignment for logo. Add position as absolute for home button
#  along with top and right positions. Relative position is used so that button is placed relative to card section
#  not body. Center the content in header.
# TODO-53 - Add a divider with width:20px.

# footer.html file
# TODO-54 - Add another html file named footer.html in templates folder.
# TODO-55 - Open <footer> tag and add style to footer such as font,text color,alignment and resolution for screens.
#  Add your footer in <p> tag.

# index.html file
# TODO-56 - Include header.html file using Jinja template.
# TODO-57 - Use Jinga to to display flash messages. Receive message using get_flashed_messages, with_categories=true
#  means: each message is returned as a tuple. So messages becomes a list. {% if messages %} Checks if any messages
#  exist. <div id="flash-container"> Wrapper container for all flash messages. FOR loop loops through each flash
#  message. <div class="flash-msg {{ category }}"> Creates dynamic CSS classes: like success and error. {{ message }}
#  Outputs the actual flash message text. Close all loops and conditions.
# TODO-58 - Inside style.css id flash-container has position fixed, top and right position as 20px and z-index: 9999;
#  is used to force an element to appear on top of almost everything else on the page. 9999 is just a very large value,
#  commonly used to say this must be on top no matter what.
# TODO-59 - Add class flash-msg which has some padding, margin, color, animation and border-radius. Add class for
#  flash-msg.success which defines background color for success and class flash-msg.danger for background color of
#  danger.
# TODO-60 - Add @keyframes which is an at-rule used to define an animation. 0% { opacity: 1; } - At the start of the
#  animation element is fully visible. 80% { opacity: 1; } - For 80% of the animation time element stays fully visible,
#  this creates a pause effect. 100% { opacity: 0; } - At the end element becomes fully transparent (fades out).
# TODO-61 - Now we will display cards section, we will use div with class cards-grid where display type is grid,auto
#  fit columns and gap of 2 rem.
# TODO-62 - Now we will create 1 card and the rest will be created using FOR loop. So add another div with class card
#  and card-section. Add class card-section in style.css and define its background color, border-radius, width, height
#  and overflow: hidden; which tells the browser if content goes outside this box, don’t show it.
# TODO-63 - Create another div in index.html for image of the card. Add class card-img-wrapper to this div and create
#  this class in style.css. Define width, aspect-ratio and overflow: hidden; - Hide anything that goes outside the
#  element’s box.
# TODO-64 - Add <img> tag along with the image. Add card-img-wrapper class for image with some modifications. Create
#  this class in style.css  and img in front of it for image. This defines width, height, border-radius and
#  object-fit:cover - fills the container completely while keeping aspect ratio.
# TODO-65 - Now create another div for body of the card. Add class card-body to this div, add the class to style.css
#  which consists of font-size for all types of screens.
# TODO-66 - Add <h1> for cafe name with class card-title. Add this class in style.css which defines font-family, color
#  and font size for different screens. Add a horizontal line using <hr/> tag.
# TODO-67 - Now we will add other details. First add class .card-body p in style.css to style all <p> tags. This
#  consists of text-align, font-family, font-weight and text color. Now add <p> tag for Location, add svg for icon, <a>
#  tag for google map location. Add {{ cafe.map_url }} in href and {{ cafe.location }} between opening and closing tags.
# TODO-68 - Add <p> tag for Number of seats and add {{ cafe.seats }} to display actual data from db.
# TODO-69 - Add <p> tag for Toilet and add svg for icon. Now add if condition using jinja and check
#  {% if cafe.has_toilet: %} if true then add label Yes else No.
# TODO-70 - Similarly add <p> tag for WiFi, svg for icon and if condition {% if cafe.has_wifi: %} if true then add label
#  Yes else No.
# TODO-71 - Add <p> tag for Sockets, svg for icon and if condition {% if cafe.has_sockets: %} if true then add label
#  Yes else No.
# TODO-72 - Add <p> tag for Calls, svg for icon and if condition {% if cafe.can_take_calls: %} if true then add label
#  Yes else No.
# TODO-73 - Add <p> tag for Avg. Coffee Price. Add actual coffee price using Jinja {{ cafe.coffee_price }}.
# TODO-74 - Now add <p> tag with class card-actions. Create this class in style.css which consists of display: flex;,
#  margin-top sizeable for screen, gap, bottom and justify-content to center.
# TODO-75 - Inside this <p> tag add <a> tag for Edit. Add inline style tag for text-color. For href use url_for()
#  function and point it to edit_cafe page along with passing cafe_id.
# TODO-76 - Similarly create tag for Delete. Add inline style tag for text-color. For href use url_for() function and
#  point it to delete_cafe page along with passing cafe_id.
# TODO-77 - End all <div> and for loop. Finally include footer.html file using Jinja template.

# add_new_cafe_edit_cafe.html file
# TODO-78 - Import render_form from bootstrap5/form.html using Jinja template.
# TODO-79 - Include header.html file to display header on edit and new cafe form page.
# TODO-80 - Create a div with class container and new_cafe. Add this class to style.css. Inside new_cafe class add
#  display type, padding, font-family, background and padding.
# TODO-81 - Inside this div check if is_edit is true, if yes then set h1 tag to "Edit The Cafe" else set it to
#  "Add new cafe" since we are using same form for both.
# TODO-82 - Use jinja template render form --> render_form(form).
# TODO-83 - Finally include footer.html to display footer.

# delete_cafe.html file
# TODO-84 - Import render_form from bootstrap5/form.html using Jinja template.
# TODO-85 - Include header.html file to display header.
# TODO-86 - Add same code for Flash messages similat to index.html.
# TODO-87 - Create a div with class container and delete_cafe. Add this class to style.css. Inside new_cafe class
#  add display type, padding, font-family, background color, padding, grid-template column space which define fractional
#  units for 1 column and finally align content to center.
# TODO-88 - Inside this div add <h2> tag to display "Delete Cafe" and add the cafe name using Jinga --> {{ cafe.name }}.
# TODO-89 - Use jinja template render form --> render_form(form).
# TODO-90 - Finally include footer.html to display footer.




from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, BooleanField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


app = Flask(__name__)
app.secret_key = "any-string-you-want-to-keep-secret"
bootstrap = Bootstrap5(app)

# Initialize DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'

db = SQLAlchemy(model_class=Base)

# Initialize the app with extension
db.init_app(app)


# Create model that matches existing table
class Cafe(db.Model):
    __tablename__ = 'cafe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250))
    coffee_price = db.Column(db.String(250))

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# Create form for Add New Cafe form
class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired()])
    image_url = StringField('Image URL', validators=[DataRequired()])
    location_name = StringField('Location Name', validators=[DataRequired()])
    number_of_seats = StringField('Number of Seats, e.g. 20-30,50+', validators=[DataRequired()])
    toilets = BooleanField('Does it have toilets?')
    wifi = BooleanField('Does it have WiFi?')
    sockets = BooleanField('Are there Sockets?')
    calls = BooleanField('Can take Calls?')
    average_coffee_price = StringField('Average Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Create form for inserting api key
class ApiKeyForm(FlaskForm):
    api_key = StringField("Enter API Key", validators=[DataRequired()])
    submit = SubmitField("Confirm & Delete")



@app.route('/')
def home():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name.asc()))
    all_cafes = result.scalars().all()
    cafes = [cafe.to_dict() for cafe in all_cafes]

    return render_template('index.html', cafes=cafes)


@app.route('/add_new_cafe', methods=['GET', 'POST'])
def add_new_cafe():
    add_new_cafe_form = CafeForm()
    if add_new_cafe_form.validate_on_submit():
        cafe_name = add_new_cafe_form.cafe_name.data
        location_url = add_new_cafe_form.location_url.data
        image_url = add_new_cafe_form.image_url.data
        location_name = add_new_cafe_form.location_name.data
        number_of_seats = add_new_cafe_form.number_of_seats.data
        toilets = add_new_cafe_form.toilets.data
        wifi = add_new_cafe_form.wifi.data
        sockets = add_new_cafe_form.sockets.data
        calls = add_new_cafe_form.calls.data
        average_coffee_price = add_new_cafe_form.average_coffee_price.data

        print(cafe_name)
        print(location_url)
        print(image_url)
        print(location_name)
        print(number_of_seats)
        print(toilets)
        print(wifi)
        print(sockets)
        print(calls)
        print(average_coffee_price)

        new_cafe = Cafe(name=cafe_name, map_url=location_url, img_url=image_url,
                        location=location_name, seats=number_of_seats, has_toilet=toilets,
                        has_wifi=wifi, has_sockets=sockets, can_take_calls=calls, coffee_price=average_coffee_price)

        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add_new_cafe_edit_cafe.html', form=add_new_cafe_form)


@app.route('/edit_cafe/<int:cafe_id>', methods=['GET', 'POST'])
def edit_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    edit_cafe_form = CafeForm(
        cafe_name=cafe.name,
        location_url=cafe.map_url,
        image_url=cafe.img_url,
        location_name=cafe.location,
        number_of_seats=cafe.seats,
        toilets=cafe.has_toilet,
        wifi=cafe.has_wifi,
        sockets=cafe.has_sockets,
        calls=cafe.can_take_calls,
        average_coffee_price=cafe.coffee_price
    )

    if edit_cafe_form.validate_on_submit():
        cafe.name = edit_cafe_form.cafe_name.data
        cafe.map_url = edit_cafe_form.location_url.data
        cafe.img_url = edit_cafe_form.image_url.data
        cafe.location = edit_cafe_form.location_name.data
        cafe.seats = edit_cafe_form.number_of_seats.data
        cafe.has_toilet = edit_cafe_form.toilets.data
        cafe.has_wifi = edit_cafe_form.wifi.data
        cafe.has_sockets = edit_cafe_form.sockets.data
        cafe.can_take_calls = edit_cafe_form.calls.data
        cafe.coffee_price = edit_cafe_form.average_coffee_price.data

        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add_new_cafe_edit_cafe.html', form=edit_cafe_form, is_edit=True)


@app.route('/delete_cafe/<int:cafe_id>', methods=['GET', 'POST'])
def delete_cafe(cafe_id):
    api_key_form = ApiKeyForm()
    cafe = Cafe.query.get(cafe_id)

    if api_key_form.validate_on_submit():
        if api_key_form.api_key.data == "delete that cafe":
            db.session.delete(cafe)
            db.session.commit()
            flash(f"Successfully deleted {cafe.name}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid API Key!", "danger")
    return render_template("delete_cafe.html", form=api_key_form, cafe=cafe)



if __name__ == '__main__':
    app.run(debug=True, port=5001)