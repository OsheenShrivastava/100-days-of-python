
# main.py file
# TODO- - Import required Flask modules such as Flask, render_template, request, and session for handling routing,
#  templates, forms, and session storage.
# TODO- - Import Bootstrap5 from flask_bootstrap to enable Bootstrap styling inside Flask templates.
# TODO- - Import external libraries:
#  requests → for making API calls
#  os → for file and environment handling
#  dotenv → for loading environment variables
#  pandas → for CSV data processing
#  random.choice → for selecting random records
#  numpy → for handling missing values
# TODO- - Initialize the Flask application using Flask(__name__).
# TODO- - Set the secret key using app.secret_key. This is required for session management and flash messaging.
# TODO- - Initialize Bootstrap support for the application using Bootstrap5(app).
# TODO- - Load environment variables using load_dotenv() to securely access API keys. Create .env file and store API key
#  in it. Retrieve the LOTR API key from the .env file using os.getenv("API_KEY").
# TODO- - Define the base API URL for The One API. Create authorization headers containing the Bearer API key for
#  authenticated requests.
# TODO- - Define CSV file names for caching API data locally: books.csv, movies.csv, characters.csv and quotes.csv.
# TODO- - Create a predefined list "lotr_quotes" containing iconic LOTR quotes that will be displayed in the homepage
#  quote rotator.
# TODO- - Create a route for the homepage ('/'). Render the index.html and pass the lotr_quotes list so it can be
#  displayed dynamically in the rotating quote section.
# TODO- - Create a route for "/books" to display all LOTR books and their chapters. Check if the books CSV file already
#  exists to avoid unnecessary API calls. If the CSV file does not exist then fetch book data from the API. Retrieve
#  book IDs and names. Use request.get() method to do so.
# TODO- - If response for book is ok then fetch its chapters using the endpoint: /book/{book_id}/chapter.
# TODO- - Store chapters in a dictionary where the key is the book name
#  and the value is a list of chapter names.
# TODO- - If response is ok then convert the dictionary into a list of rows containing book and chapter pairs.
# TODO- - Convert the rows into a Pandas DataFrame and save it to books.csv.
# TODO- - If the CSV file exists, load the dataset using pandas.read_csv().
# TODO- - Group chapters by book name using pandas groupby() and convert the result into a dictionary.
# TODO- - Pass the grouped dictionary to the books.html template.
# TODO- - Create a route for "/movies" to display LOTR movie information. Check if movies.csv exists. If the file does
#  not exist then fetch movie data from the API. Extract attributes such as runtime, budget, box office revenue, academy
#  award nominations, academy award wins, and Rotten Tomatoes score.
# TODO- - Convert the movie dataset into a DataFrame and store it as movies.csv.
# TODO- - If the CSV file exists, load the movie data and convert it into a list of dictionaries using
#  to_dict(orient='records').
# TODO- - Pass the movies list to the movies.html template.
# TODO- - Create a route for "/characters" to display character information.
# TODO- - Retrieve search query and action parameters from the URL using request.args.
# TODO- - If characters.csv does not exist then Fetch character data from the API. Extract attributes such as name, wiki
#  URL, race, birth, death, gender, hair, height, realm, and spouse.
# TODO- - Convert the dataset into a DataFrame and save it as characters.csv. Load characters data from the CSV file.
# TODO- - Replace NaN values with None to avoid rendering issues in templates. Convert the dataset into a list of
#  dictionaries.
# TODO- - Filter out characters with empty names since the LOTR API includes many blank entries.
# TODO- - Sort the character list alphabetically for better display.
# TODO- - Implement search functionality: If the user clicks "Search", filter characters by name. If no search query is
#  provided, show a flash warning message.
# TODO- - If the search result is found, store the character in the session. If the search result is not found, display
#  a warning message.
# TODO- - Implement random character selection when the "Random Character" button is clicked.
# TODO- - Store the currently displayed character in the session so it persists across page reloads.
# TODO- - Pass both the selected character and the full character list to the characters.html template.
# TODO- - Create a route for "/quotes" to display random LOTR quotes. Check if quotes.csv exists to avoid repeated API
#  requests.
# TODO- - If the CSV file does not exist: Fetch quotes from the API. Fetch characters to map character IDs to character
#  names. Fetch movies to map movie IDs to movie titles.
# TODO- - Build dictionaries mapping character IDs and movie IDs to names.
# TODO- - Convert the quote dataset into rows containing: quote text, character name and movie name.
# TODO- - Convert the dataset into a DataFrame and save it as quotes.csv.
# TODO- - Load quotes data from CSV and convert it into a list of dictionaries. Select a random quote using
#  random.choice().
# TODO- - Pass the selected quote to the quotes.html template.
# TODO- - Create a file named style.css. Inside it add h1 element and set its font size for all screens. Similarly,
#  do the same for h2, h3 and p element.
# TODO- - Add body tag in style.css. This applies to everything included inside body. Iniside it add font family, text
#  color, background image as url along with background position to center, background no repeat and background
#  attachment as fixed. Keep margin and padding as 0.
# TODO- - Add body::before which will consist of position as fixed, inset: 0;, background, z-index: -1. z-index controls
#  the stacking order (vertical layering) of elements on a webpage — which element appears in front or behind others.
#  "-1" means the element is placed behind other elements. Basically darken the background yet keep text fully visible.
# TODO- - Start the Flask development server using app.run().
# TODO- - Enable debug mode for development and run the application on port 5001.

# index.html file
# TODO- - Create a file named index.html inside the templates folder.
# TODO- - Extend the base template using {% extends "base.html" %}.
# TODO- - Define the page title using Jinja block syntax. Open the title block using {% block title %} and set the page
#  title to "Home". Close the title block using {% endblock %}.
# TODO- - Define the main page content using {% block content %} and {% endblock %}.
# TODO- - Create a main container div with class "hero-section". This section will act as the landing header of the
#  website.
# TODO- - Add a heading element <h2> with class "hero-title". Display the welcome text "WELCOME TO LoTR REALM!".
# TODO- - Wrap the text "LoTR REALM!" inside a <span> element so it can be styled separately.
# TODO- - Add a subtitle paragraph with class "hero-sub". Display the text: "BOOKS. CHARACTERS. QUOTES. MOVIES. ALL IN
#  ONE REALM."
# TODO- - Create a container div with class "quote-rotator". This will hold a rotating list of quotes from the LOTR
#  universe. Inside it create another div with class "quote-track". This container will hold all animated quote items.
# TODO- - Use a Jinja FOR loop to iterate through the list "lotr_quotes" passed from the Flask backend.
# TODO- - Inside the loop create a div with class "quote-item". Each div will represent a single quote in the rotating
#  animation. Add inline animation delay using: style="animation-delay: {{ loop.index0 * 4 }}s;". This staggers each
#  quote animation so they appear one after another.
# TODO- - Display the quote text using {{ q['quote'] }}. Add a line break <br> after the quote text.
# TODO- - Display the quote author using {{ q['author'] }} and prefix it with a dash (—).
# TODO- - Close the quote-item div and end the FOR loop using {% endfor %}. Close the quote-track and quote-rotator
#  containers.
# TODO- - Add styling in style.css. Create ".hero-section" class and add position, display as grid, alignment, center
#  items, padding, min height and text alignment.
# TODO- - Create ".hero-title". Add font family and text color. Create class ".hero-title span". Add text color in it.
# TODO- - Create ".hero-sub" and add font family, font size, letter spacing, text color, opacity and margin.
# TODO- - Create ".quote-rotator" and add inset: 0;, display type as grid, alignment, height, width, margin, text
#  alignment, position, width and overflow: hidden;.
# TODO- - Create ".quote-track" with position relative, flex layout for animation control along with height and width.
# TODO- - Create ".quote-item" and add font family, font size, font style, text color, text shadow, text alignment,
#  height, display as flex, opacity, position, width and animation. Add key frames to display animation in action. Add
#  animation delay for all the items being displayed.

# base.html file
# TODO- - Create a folder named templates and add a html file. Name it base.html. Add style.css in the folder static.
# TODO- - Set language as English, set charset="UTF-8", Title="LoTR". Use {% block title %} and {% endblock %}. Add
#  Bootstrap link for styling in head section and script link in body section.
# TODO- - Add links for font Uncial Antiqua and Cormorant Garamond. Add external link for style.css.
# TODO- - Add {% include "header.html" %} to include header from header.html.
# TODO- - Add flash message loop for notfications. Use get_flashed_messages() function. Check if messages, add div
#  and set its id=flash-container.
# TODO- - Create this id in style.css and add position, top, right and z-index. z-index controls the vertical
#  stacking order of elements on a webpage—that is, which element appears in front of or behind another when they
#  overlap.
# TODO- - Run FOR loop for category and message in messages. Add another div and set its class as flash-msg. This
#  class contains padding, border, margin, color, animation and color change for success and danger messages. Add
#  category using Jinja.
# TODO- - Finally add message in the div using Jinja, end FOR loop and div. End if loop and with condition. Add
#  .flash-msg.warning and .flash-msg.danger class in style.css and add background color to it. Add animation for message
#  fadeout.
# TODO- - Add main opening and closing tags. Inside them add {% block content %} and {% endblock %} to enclose body
#  content. Add {% include "footer.html" %} to include footer from footer.html.
# TODO- - Close body and html tags.

# footer.html file
# TODO- - Add another html file named footer.html in templates folder.
# TODO- - Open <footer> tag and add class footer. Create this class in style.css and add text color, alignment,
#  font-size resolution for screens, font-weight, font-family and background as transparent. Add your footer in <p> tag.

# header.html file
# TODO- - Create a file named header.html inside the templates folder.
# TODO- - Add a <nav> element and assign it a class "navbar" to create the website navigation bar.
# TODO- - Inside the navbar, create a <div> with class "logo". Add a heading element <h3> inside the logo div and set
#  the text to "LoTR".
# TODO- - Add navigation links using <a> anchor tags for different pages of the website. Use Flask's url_for() function
#  to dynamically generate URLs for routes.
# TODO- - Add a link for the Home page using {{ url_for('home') }}, Books page using {{ url_for('books') }}, Movies page
#  using {{ url_for('movies') }}, Characters page using {{ url_for('characters') }} and Quotes page using
#  {{ url_for('quotes') }}.
# TODO- - Style the navbar in style.css by creating a ".navbar" class and defining properties such as display,
#  background color, padding, alignment, and spacing.
# TODO- - Add styling for navbar links using ".navbar a" selector and define font, color, hover effects, margin,
#  font-size for all screens and spacing between links.
# TODO- - Style the logo section separately using ".logo" to apply custom font, LOTR-themed colors, spacing, margin and
#  hover animations.

# books.html file
# TODO- - Create a file named books.html inside the templates folder.
# TODO- - Extend the base layout by adding {% extends "base.html" %}. This allows the page to inherit common layout
#  elements such as header, footer, styles, and scripts.
# TODO- - Define the page title using Jinja block syntax. Open the title block using {% block title %} and set the title
#  text to "Books". Close the title block using {% endblock %}.
# TODO- - Define the content section of the page using {% block content %}. All page-specific HTML should be placed
#  inside this block.
# TODO- - Use a Jinja FOR loop to iterate through the chapters dictionary passed from the Flask backend. The dictionary
#  contains book names as keys and lists of chapters as values.
# TODO- - Inside the loop, create a container div with class "book-card". This div will visually represent each book
#  section.
# TODO- - Add a heading <h2> inside the card to display the book name using {{ book }}.
# TODO- - Create another div with class "chapter-scroll". This container will hold all chapters for the current book and
#  allow scrolling if the list is long.
# TODO- - Inside this container, create another Jinja FOR loop to iterate through the list of chapters.
# TODO- - Display each chapter using a paragraph tag <p> and insert the chapter name using {{ chapter }}. Close the
#  inner FOR loop using {% endfor %}.
# TODO- - Close the chapter-scroll div and the book-card div. Close the outer FOR loop using {% endfor %}.
# TODO- - Style the layout in style.css. Create ".book-card" class and add background, padding, margin, border-radius,
#  border, width and backdrop filter to blur the text.
# TODO- - Create another class named .book-card h2 to style book name. Add font family, text color and bottom margin.
# TODO- - Create ".chapter-scroll" class and add max-height and overflow-y: auto to allow scrolling.
# TODO- - Add .chapter-scroll p class which consists of margin and text color. Chnage the text color on hover with some
#  transition.

# movies.html file
# TODO- - Create a file named movies.html inside the templates folder.
# TODO- - Extend the base template by adding {% extends "base.html" %}. This allows the page to reuse the common layout
#  structure such as navbar, footer, styles, and scripts.
# TODO- - Define the page title section using Jinja block syntax. Open the title block with {% block title %} and set
#  the page title to "Movies". Close the title block using {% endblock %}.
# TODO- - Define the main content section using {% block content %}. All movie-related content will be placed inside
#  this block.
# TODO- - Create a container div with class "movie-grid". This container will hold all movie cards in a grid layout.
# TODO- - Use a Jinja FOR loop to iterate through the list of movies passed from the Flask backend. Inside the loop,
#  create a div with class "movie-box". This div represents an individual movie card.
# TODO- - Add a heading <h3> to display the movie title using {{ movie.movie }}.
# TODO- - Display movie runtime, movie budget, box office revenue, Academy Award nominations, Academy Award wins and
#  Rotten Tomatoes using jinja and a paragraph tag with their respective emojies.
# TODO- - Close the movie-box div. Close the Jinja FOR loop using {% endfor %}. Close the movie-grid container div.
# TODO- - Style the layout in style.css. Create ".movie-grid" class and use CSS Grid to display movie cards in columns.
#  Add gap, width and margin.
# TODO- - Create ".movie-box" class and add background color, padding, border-radius, text alignment and hover animation
#  for better UI appearance. Add class .movie-box h3, inside it add text color.

# characters.html file
# TODO- - Create a file named characters.html inside the templates folder.
# TODO- - Extend the base layout using {% extends "base.html" %}. This allows the page to inherit common elements like
#  navbar, footer, styles, and scripts.
# TODO- - Define the page title using Jinja block syntax. Open the title block using {% block title %} and set the title
#  text to "Characters". Close the title block using {% endblock %}.
# TODO- - Define the main page content using {% block content %}. All character-related UI elements will be placed
#  inside this block.
# TODO- - Add a hidden checkbox input with id="toggle-characters". This checkbox will be used for toggling visibility of
#  the full character list using CSS.
# TODO- - Check if a character object is available using the Jinja conditional: {% if character %}
# TODO- - Create a section element with class "character-dossier". This section will display detailed information about
#  the selected character.
# TODO- - Create a search form using <form method="GET"> so that search queries appear in the URL. Set the form action
#  to {{ url_for('characters') }} so that it submits to the characters route.
# TODO- - Add an input field with name="search" for searching characters. Set placeholder text to "Search character...".
#  Preserve the search value using: {{ request.args.get('search', '') }} so the search text remains visible after
#  submission.
# TODO- - Add a "Search" button with type="submit". Set name="action" and value="search" so the backend knows this is a
#  search request.
# TODO- - Add another button labeled "Random Character". Set name="action" and value="random" so the backend can return
#  a random character.
# TODO- - Display the character name using <h1>{{ character.character }}</h1>.
# TODO- - Create a container div with class "dossier-grid". This will organize character attributes in a grid layout.
# TODO- - Display character attributes inside individual div elements. Use a <span> element to show attribute labels
#  such as Race, Height, Gender, etc. Use Jinja conditional fallback values with "or 'Unknown'" for attributes that may
#  be missing.
# TODO- - Display all the character attributes using jinja - Race, Height, Gender, Birth, Spouse, Death, Realm and Hair.
# TODO- - Add a link to the character's wiki profile using {{ character.wiki }}.
# TODO- - Use target="_blank" and rel="noopener noreferrer" to safely open the wiki link in a new browser tab.
# TODO- - Add a label element with class "toggle-btn" linked to the hidden checkbox. This will allow users to toggle
#  visibility of the full character list. Close the conditional block {% endif %}.
# TODO- - Create a new section with class "characters-section". This section will display a complete list of all
#  characters.
# TODO- - Add a heading with class "section-title" labeled "All Characters". Create a container div with class
#  "characters-grid". This grid will display characters in a responsive layout.
# TODO- - Use a Jinja FOR loop to iterate through the list "all_characters". Display each character name inside a div
#  with class "character-item". Close the FOR loop and container div.
# TODO- - Add styling in style.css. Create ".character-dossier" class for the character profile section. Add width,
#  margin, padding, border, background, text alignment and backdrop filter.
# TODO- - Create ".character-dossier h1" class which consists of font-famliy, font-size for all screens, text-color,
#  letter spacing and bottom margin.
# TODO- - Create class ".search-form" for search box which has text alignment and bottom margin.
# TODO- - Create class ".search-input" for input field which will have padding, width, border, background, text-color,
#  font-size with no outline.
# TODO- - Create class ".search-btn" for search button which has padding, border, text-color, cursor pointer, smooth
#  transition with background as transparent. Change background color and text color on hover.
# TODO- - Create ".dossier-grid" class using CSS Grid for attribute layout. This class consists of display type as grid,
#  text alignment, margin and gap.
# TODO- - Create another class ".dossier-grid div" for div. This class consists of font-size, text color, padding and
#  border. Create another class ".dossier-grid span" for span. This class consists of display type as block, font-size,
#  letter spacing, text color, margin and transform text to uppercase.
# TODO- - Create another class ".toggle-btn" for toggle button to view all characters. Set display as inline-block, add
#  margin, padding, border, text color, letter spacing, cursor pointer, transparent background and a smooth transition.
#  Change background color, text color and add shadow on hover.
# TODO- - Create another class ".characters-section" for all characters section. Add width, margin, transition,
#  opacity as 0, display none and overflow: hidden;
# TODO- - Add #toggle-characters:checked ~ .characters-section to display character when button is toggled. Add opacity
#  as 1, margin and display as block.
# TODO- - Create another class ".section-title" for all characters title. Add text alignment, font, text color,
#  font-size and margin.
# TODO- - Create ".characters-grid" class to display characters in a responsive grid. Add display type as grid and gap.
# TODO- - Create ".character-item" to display individual characters. Add padding, text color, border, text alignment,
#  font family, font-size, cursor pointer and transition. Change text color and add transform scale on hover.

# quotes.html file
# TODO- - Create a file named quotes.html inside the templates folder.
# TODO- - Extend the base layout using {% extends "base.html" %}. This allows the page to inherit common components like
#  navbar, footer, styles, and scripts.
# TODO- - Define the page title using Jinja block syntax. Open the title block using {% block title %} and set the title
#  text to "Quotes". Close the title block using {% endblock %}.
# TODO- - Define the main content section using {% block content %}. All quote-related UI elements will be placed inside
#  this block.
# TODO- - Create a container div with class "quote-container".This will act as the main wrapper for the quote section
#  and help center the content.
# TODO- - Add a form element to request a new random quote from the backend. Set the form method to GET so parameters
#  appear in the URL. Set the form action to {{ url_for('quotes') }} so the request is sent to the quotes route.
# TODO- - Add a button with class "random-btn". Set type="submit", name="action", and value="random" so the backend
#  knows the user requested a random quote.
# TODO- - Create a div with class "quote-flip-card". This container will hold the 3D flip animation card. Inside it,
#  create another div with class "quote-flip-inner". This inner container will rotate to create the card flip effect.
# TODO- - Create the front side of the card using a div with class "quote-front". Inside the front section, add a
#  heading element <h1> with class "quote-text". Display the quote text using Jinja syntax {{ quote.quote }}. Wrap the
#  quote in quotation marks for styling.
# TODO- - Create the back side of the card using a div with class "quote-back". Display the quote author using a
#  paragraph with class "quote-author". Use {{ quote.character }} to show the character who said the quote.
# TODO- - Display the movie source using a paragraph with class "quote-movie". Use {{ quote.movie }} to show which movie
#  the quote came from. Close the flip card containers.
# TODO- - Create ".quote-container" class to center content and control layout. Add display tupe as grid.
# TODO- - Create ".quote-flip-card" class and add perspective property to enable the 3D flip animation. Add width,
#  height, margin and  perspective: 1000px;. "perspective" in CSS is used to create a 3D effect for elements that use
#  3D transforms like rotateX, rotateY, or translateZ. It defines how far the viewer is from the object, which controls
#  how strong the 3D depth effect looks.
# TODO- - Create ".quote-flip-inner" class and add transform-style: preserve-3d and transition properties for smooth
#  flipping. Add width, height and position. Add rotation of 180 deg for class ".quote-flip-card:hover" and
#  ".quote-flip-inner".
# TODO- - Create ".quote-front" and ".quote-back" classes. Set position: absolute, backface-visibility: hidden (This
#  prevents mirrored text, ghost text and both sides overlapping), height, width, display as flex, alignment, padding,
#  border, border radius and background.
# TODO- - Add ".quote-front" additionally which will consist of background image, background position and background
#  repeat. Also add ".quote-front::before" which appears before the content inside ".quote-front". It will consist of
#  content: "";, position: absolute;, inset: 0; (inset is shorthand for: top: 0; right: 0; bottom: 0; left: 0;) and
#  background: rgba(0,0,0,0.2);
# TODO- - Add class ".quote-back" which will have transformation to rotate 180 deg.
# TODO- - Create class ".quote-text" to style quote which has font family, font-size for all screens, font-weight,
#  font-style, line-height, text-alignment, margin, text color, max width, overflow wrap and word break.
# TODO- - Create class ".quote-author" which will have font-family, font-size, text color and margin.
# TODO- - Create class ".quote-movie" which will have font-size, opacity and margin.
# TODO- - Create class ".random-form" for form consisting of only margin.
# TODO- - Create class ".random-btn" for form button consisting of padding, border, text color, font family, margin,
#  cursor pointer and transparent background. Change background and text color on hover.



from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap5
import requests
import os
from dotenv import load_dotenv
import pandas as pd
from random import choice
import numpy as np
from flask import session



app = Flask(__name__)
app.secret_key = "any-string-you-want-to-keep-secret"
bootstrap = Bootstrap5(app)

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://the-one-api.dev/v2"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

BOOKS_FILE = "books.csv"
MOVIES_FILE = "movies.csv"
CHARACTERS_FILE = "characters.csv"
QUOTES_FILE = "quotes.csv"

lotr_quotes = [
    {
        "quote": "All we have to decide is what to do with the time that is given us.",
        "author": "Gandalf"
    },
    {
        "quote": "Even the smallest person can change the course of the future.",
        "author": "Galadriel"
    },
    {
        "quote": "You shall not pass!",
        "author": "Gandalf"
    },
    {
        "quote": "A wizard is never late, nor is he early. He arrives precisely when he means to.",
        "author": "Gandalf"
    },
    {
        "quote": "There is some good in this world, and it’s worth fighting for.",
        "author": "Samwise Gamgee"
    },
    {
        "quote": "I would rather share one lifetime with you than face all the ages of this world alone.",
        "author": "Arwen"
    },
    {
        "quote": "For Frodo.",
        "author": "Aragorn"
    },
    {
        "quote": "One does not simply walk into Mordor.",
        "author": "Boromir"
    },
    {
        "quote": "I can’t carry it for you… but I can carry you!",
        "author": "Samwise Gamgee"
    },
    {
        "quote": "My precious.",
        "author": "Gollum"
    }
]

@app.route('/')
def home():
    return render_template('index.html', lotr_quotes=lotr_quotes)


@app.route('/books')
def books():
    if not os.path.exists(BOOKS_FILE):

        chp_dict = {}
        rows = []
        data = None

        books_response = requests.get(f"{BASE_URL}/book", headers=headers)

        if books_response.status_code == 200:
            books_data = books_response.json()['docs']

            # STEP 1 — Collect chapters
            for book in books_data:
                book_id = book['_id']
                name = book['name']

                chp_response = requests.get(
                    f"{BASE_URL}/book/{book_id}/chapter",
                    headers=headers
                )

                if chp_response.status_code == 200:
                    chp_data = chp_response.json()['docs']

                    chp_dict[name] = [
                        chapter['chapterName']
                        for chapter in chp_data
                    ]
                else:
                    print("Error:", chp_response.status_code)

            # STEP 2 — Build rows AFTER loop
            for book_name, chapters in chp_dict.items():
                for chapter in chapters:
                    rows.append({
                        "book": book_name,
                        "chapter": chapter
                    })

            # STEP 3 — Create CSV once
            data = pd.DataFrame(rows)
            data.to_csv(BOOKS_FILE, index=False)

        else:
            print("Error:", books_response.status_code)
            data = pd.DataFrame()

    else:
        data = pd.read_csv(BOOKS_FILE)

    if data is None or data.empty:
        grouped = {}
    else:
        grouped = data.groupby("book")["chapter"].apply(list).to_dict()

    return render_template('books.html', chapters=grouped)


@app.route('/movies')
def movies():
    if not os.path.exists(MOVIES_FILE):

        rows = []
        movies_data = None

        movies_response = requests.get(f"{BASE_URL}/movie", headers=headers)

        if movies_response.status_code == 200:
            movies_data = movies_response.json()['docs']

            for movie in movies_data:
                rows.append({
                    "movie": movie['name'],
                    "runtimeInMinutes": movie['runtimeInMinutes'],
                    "budgetInMillions": movie['budgetInMillions'],
                    "boxOfficeRevenueInMillions": movie['boxOfficeRevenueInMillions'],
                    "academyAwardNominations": movie['academyAwardNominations'],
                    "academyAwardWins": movie['academyAwardWins'],
                    "rottenTomatoesScore": movie['rottenTomatoesScore'],
                })

            data = pd.DataFrame(rows)
            data.to_csv(MOVIES_FILE, index=False)
            movies_data = data.to_dict(orient='records')

        else:
            print("Error:", movies_response.status_code)
            data = pd.DataFrame()

    else:
        data = pd.read_csv(MOVIES_FILE)
        movies_data = data.to_dict(orient='records')
    return render_template('movies.html', movies=movies_data)


@app.route('/characters')
def characters():
    characters_data = None
    random_character = None
    valid_characters = []

    search_query = request.args.get('search')

    action = request.args.get('action')


    if not os.path.exists(CHARACTERS_FILE):

        rows = []

        characters_response = requests.get(f"{BASE_URL}/character", headers=headers)

        if characters_response.status_code == 200:
            characters_data = characters_response.json()['docs']

            for character in characters_data:
                rows.append({
                    "character": character.get('name'),
                    "wiki": character.get('wikiUrl'),
                    "race": character.get('race'),
                    "date_of_birth": character.get('birth'),
                    "gender": character.get('gender'),
                    "date_of_death": character.get('death'),
                    "hair": character.get('hair'),
                    "height": character.get('height'),
                    "realm": character.get('realm'),
                    "spouse": character.get('spouse')
                })

            data = pd.DataFrame(rows)
            data.to_csv(CHARACTERS_FILE, index=False)

        else:
            return render_template('characters.html', character=None, all_characters=[])


    data = pd.read_csv(CHARACTERS_FILE, keep_default_na=False, na_values=[])

    data = data.replace({np.nan: None})

    characters_data = data.to_dict(orient='records')

    # Remove empty names (important for LOTR API)
    valid_characters = [c for c in characters_data if c.get('character')]

    if not valid_characters:
        return render_template('characters.html', character=None, all_characters=[])

    valid_characters = sorted(valid_characters,key=lambda x: x['character'].lower())

    # SEARCH LOGIC
    # CASE 1: User clicked Search
    if action == "search":
        if not search_query:
            flash("Please enter a character name to search.", "danger")

            random_character = session.get("current_character")
        else:
            filtered = [
                c for c in valid_characters
                if search_query.lower() in c['character'].lower()
            ]

            if filtered:
                random_character = filtered[0]
                session["current_character"] = random_character
            else:
                flash("No character found.", "warning")
                random_character = session.get("current_character")

    # CASE 2: User clicked Random
    elif action == "random":
        random_character = choice(valid_characters)
        session["current_character"] = random_character

    # CASE 3: Page opened normally
    else:
        if "current_character" in session:
            random_character = session["current_character"]
        else:
            random_character = choice(valid_characters)
            session["current_character"] = random_character

    return render_template('characters.html', character=random_character,
                           all_characters=valid_characters)


@app.route('/quotes')
def quotes():
    if not os.path.exists(QUOTES_FILE):

        rows = []

        # Fetch quotes
        quotes_response = requests.get(f"{BASE_URL}/quote", headers=headers)

        if quotes_response.status_code == 200:
            quotes_json = quotes_response.json()['docs']
        else:
            print("Error:", quotes_response.status_code)
            quotes_json = []

        # Fetch characters
        characters_response = requests.get(f"{BASE_URL}/character", headers=headers)

        character_map = {}

        if characters_response.status_code == 200:
            characters_json = characters_response.json()['docs']

            for char in characters_json:
                character_map[char['_id']] = char['name']
        else:
            print("Error:", characters_response.status_code)

        # Fetch movies
        movies_response = requests.get(f"{BASE_URL}/movie", headers=headers)

        movies_map = {}

        if movies_response.status_code == 200:
            movies_json = movies_response.json()['docs']

            for movie in movies_json:
                movies_map[movie['_id']] = movie['name']

        # Build dataset
        for quote in quotes_json:
            rows.append({
                "quote": quote.get("dialog"),
                "character": character_map.get(quote.get('character'), "Unknown"),
                "movie": movies_map.get(quote.get('movie'), "Unknown")
            })

        data = pd.DataFrame(rows)
        data.to_csv(QUOTES_FILE, index=False)

    data = pd.read_csv(QUOTES_FILE)
    quotes_data = data.to_dict(orient='records')
    random_quote = choice(quotes_data)

    return render_template('quotes.html', quote=random_quote)


if __name__ == '__main__':
    app.run(debug=True, port=5001)