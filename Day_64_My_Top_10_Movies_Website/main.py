from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'
Bootstrap5(app)

URL_to_search_movie = "https://api.themoviedb.org/3/search/movie"
URL_for_movie_details = "https://api.themoviedb.org/3/movie"

TMDB_API_Key = "Your TMDB API Key"


class Base(DeclarativeBase):
    pass

# configure the SQLite database, relative to the app intance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

# CREATE DB
db = SQLAlchemy(model_class=Base)

# Initialize the app with extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()

class Review_Rating_form(FlaskForm):
    Your_Rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    Your_Review = StringField('Your Review', validators=[DataRequired()])
    Done = SubmitField('Done')

class Add_Movie(FlaskForm):
    Movie_Title = StringField('Movie Title', validators=[DataRequired()])
    Add_Movie = SubmitField('Add Movie')


@app.route("/")
def home():

    # READ ALL RECORDS
    # .all() is used to return a list else it will gives you a generator of Book objects (not tuples).
    #  all_movies is a list in descending order i.e., lowest rating first
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    #  Since all_movies list is a descending list, therefore it is easier to assign ranking in descending order using
    #  len(all_movies) - i
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = Review_Rating_form()

    id = request.args.get('id')

    if form.validate_on_submit():

        # UPDATE A PARTICULAR RECORD BY PRIMARY KEY
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie_to_update.rating = float(form.Your_Rating.data)
        movie_to_update.review = form.Your_Review.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", form=form)


@app.route("/delete", methods=['GET'])
def delete():
    id = request.args.get('id')

    # DELETE A PARTICULAR RECORD BY PRIMARY KEY
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = Add_Movie()

    if form.validate_on_submit():
        movie_title = form.Movie_Title.data

        parameters = {
            "api_key": f"{TMDB_API_Key}",
            "query": f"{movie_title}"
        }

        response = requests.get(url=URL_to_search_movie, params=parameters)

        data = response.json()["results"]

        return render_template("select.html", data=data)

    return render_template("add.html", form=form)


@app.route("/select", methods=['GET', 'POST'])
def select_movie():
    movie_api_id  = request.args.get('id')

    if movie_api_id:
        final_url = f"{URL_for_movie_details}/{movie_api_id}"

        parameters = {
            "api_key": f"{TMDB_API_Key}",
            "language": "en-US"
        }

        response = requests.get(url=final_url, params=parameters)

        data = response.json()

        # CREATE RECORD
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
        )

        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('edit', id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)




# TODO-1 - Add Base Class and inherit properties of DeclarativeBase class.
# TODO-2 - Congifure SQLite Database relative to the app instance folder.
# TODO-3 - Create db.
# TODO-4 - Initialize the app with extension.
# TODO-5 - Create Table consisting of id,title,year,description,rating,ranking,review,img_url fields. Use this
#  db.create_all() to create the table.
# TODO-6 - Add a new record  given below
#  new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# and commit it. Check it using DB Browser SQLite.
# TODO-7 - Read all records in home route.
# TODO-8 - Add second movie
#  second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# TODO-9 - Pass all movies in index.html. Add a FOR loop and change the fields everywhere using Jinja.
# TODO-10 - Add {{ url_for('edit', id=movie.id) }} in href of "Update" button in index.html file. Pass id as well.
# TODO-11 - Create a class Review_Rating_form by inheriting FlaskForm class. Create 3 fields for Rating,Review and Done
#  button.
# TODO-11 - Add route for edit page,add methods and render edit.html file. Create an object "form" of
#  Review_Rating_form class and pass it in edit.html file.
# TODO-12 - Check if request.method is "POST" and also validate the form on submit. Request id from edit.html.
# TODO-13 - Update a rating and review record in the database using Primary Key 'id' and redirect to home page.
# TODO-14 - If you write a Flask view function it’s often useful to return a 404 Not Found error for missing entries.
#  Flask-SQLAlchemy provides some extra query methods. So you can use movie = db.get_or_404(Movie, id) in edit function.
# TODO-15 - Add {{ url_for('delete', id=movie.id) }} in href of "Delete" button in index.html file. Pass id as well.
# TODO-16 - Add route for delete page,add methods. Delete the movie in the database using Primary Key 'id' and render
#  redirect to home page.
# TODO-17 - Add {{ url_for('add') }} in href of "Add Movie" button in index.html file.
# TODO-18 - Add route for add page, add methods and render add.html file.
# TODO-19 - Add {% from 'bootstrap5/form.html' import render_form %} in add.html and render form using
#  {{ render_form(form, novalidate=True) }}
# TODO-20 - Create a class Add_Movie by inheriting FlaskForm class. Create 2 fields Movie_Title and Add_Movie button.
# TODO-21 - Create an object "form" of Add_Movie class and pass it in add.html file.
# TODO-22 - Sign in to "The Movie Database". Go to Settings -> API and get an API Key. Fill out their form, get the
#  API key, and then copy that API key into your project.
# TODO-23 - Import requests module and copy the URL from the link below:
#  https://developer.themoviedb.org/reference/search-movie.
# TODO-24 - Include parameters:
# parameters = {
#             "api_key": f"{TMDB_API_Key}",
#             "query": f"{movie_title}"
#         }
# TODO-25 - Request the movies with reference to the title entered by the user to the URL and passing the parameters.
#  Convert the data to json and extract "results" form it.
# TODO-26 - Render select.html and pass the "results" data in it.
# TODO-27 - In select.html add FOR loop {% for movie in data: %} and edit the movie title and release date like
#  {{ movie["title"] }} - {{ movie["release_date"] }}.
# TODO-28 - Add href=" {{ url_for('select_movie', , id=movie.id) }} " in select.html, pass movie id to redirect it to
#  select_movie function.
# TODO-29 - Create a route for select_movie function and request the movie id from select.html file.
# TODO-30 - Use this URL to search for movie details "https://api.themoviedb.org/3/movie/{movie_id}", add the id
#  received from select.html to the URL then and make a request to this URL using request module by passing below
#  parameters.
# parameters = {
#             "api_key": f"{TMDB_API_Key}",
#             "language": "en-US"
#         }
# TODO-31 - Using below create a new record for new movie.
# CREATE RECORD
# new_movie = Movie(
#     title=data["title"],
#     year=data["release_date"].split("-")[0],
#     description=data["overview"],
#     img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
# )
# TODO-32 - Since we are not passing rating,ranking and review so make sure to turn nullable=True else it will give
#  error.
# rating: Mapped[float] = mapped_column(Float, nullable=True)
# ranking: Mapped[int] = mapped_column(Integer, nullable=True)
# review: Mapped[str] = mapped_column(String(250), nullable=True)
# TODO-33 - Create new movie and redirect route to edit.html by passing new_movie id.
# TODO-34 - Now we need to add ranking on the basis of rating edited by us. More the rating higher the ranking. So,
# sort movies in home route by ranking instead of title.
# Change this: result = db.session.execute(db.select(Movie).order_by(Movie.title))
# To: result = db.session.execute(db.select(Movie).order_by(Movie.rating))
# TODO-35 - Add FOR Loop to assign movie rank based on rating.