
# main.py file
# TODO-1 - Import Flask, render_template, flash, request, redirect and url_for from flask to build the web app and show
#  messages.
# TODO-2 - Import Bootstrap to style the app using Flask-Bootstrap.
# TODO-3 - Import requests, time and threading.
# TODO-4 - Import BeautifulSoup from bs4 for web scraping.
# TODO-5 - Import os to work with file paths.
# TODO-6 - Import pandas.
# TODO-7 - Import plotly.express as px. Import plotly.io as pio.
# TODO-8 - Create Flask app instance.
# TODO-9 - Initialize Bootstrap with the Flask app for styling.
# TODO-10 - Set SECRET_KEY required by Flask-WTF to protect forms from CSRF attacks.
# TODO-11 - Get current year using time.strftime("%Y") and convert it to an integer. Store this in variable year.
# TODO-12 - Create csv file name "top100_year_end_hot.csv" and store it in DATASET_FILE constant variable. Add
#  building_dataset and dataset_ready. Set them to False.
# TODO-13 - Create home route ("/") and under it create home() function. Add global variables building_dataset and
#  dataset_ready. Check If dataset_ready flag is True, if yes then flash success message and reset dataset_ready to
#  False.
# TODO-14 - Check if dataset file exists using os.path.exists(), if not then check whether dataset is ready. If not then
#  flash warning message for dataset being prepared and set building_dataset to True.
# TODO-15 - Add thread to build the data in background while displaying the home page. Use threading.Thread() function
#  and add target=build_dataset_background. build_dataset_background this will be a function which is called here. Call
#  thread.start() function to start. Add else and flash message for dataset being prepared in case user refreshes the
#  page. Render index.html template and pass building=True when the dataset is ready.
# TODO-16 - Create another function named build_dataset_background and add global variables building_dataset and
#  dataset_ready. Use try and except condition. Inside try, call another function named build_dataset() which will
#  scrape data, process it and save the result to a CSV file. Set dataset_ready to True below it.
# TODO-17 - Add Exception as e in except loop to display errors. Last but not the least add finally to run no matter
#  what and set building_dataset to False.
# TODO-18 - Now lets create named build_dataset(), this will scrape Billboard Year-End Hot 100 data from Wikipedia and
#  generate a CSV dataset. Inside this define Wikipedia URL for scraping year-wise data. Define request headers to avoid
#  bot blocking. Add User-Agent and Accept-Language.
# TODO-19 - Initialize empty lists to store the scraped data such as years, ranks, titles and artists. Add a FOR loop to
#  loop through year range dynamically. Example: from 2000 to current year.
# TODO-20 - Add try and except condition. Inside try send GET request to Wikipedia page for each year using requests.get
#  function. Pass base url + year, headers and timeout. Print the response status code.
# TODO-21 - If response code is not equal to 200 then skip that year. Now use BeautifulSoup to parse HTML by passing
#  response text in it and using "html.parser" as parser. Once parsed, find "table" element with class "wikitable" and
#  store  them to variable table. If there is no table then continue to find more.
# TODO-22 - Extract all table rows except header using find_all() function - table.find_all("tr")[1:]. Store the data to
#  a variable named rows. Set old_artist = None.
# TODO-23 - Add a FOR loop to loop through rows. Use find_all function and find "td" in row and save this to variable
#  cols. If no columns are found then continue.
# TODO-24 - Extract rank, title, and artist from cols using text.strip() function. Also remove quotes by replacing '"'
#  by ''. Append all the extracted data to their respective lists i.e., years, ranks, titles, artists. Update old_artist
#  for merged row handling.
# TODO-25 - Add polite delay between requests (avoid rate limiting) using time.sleep(). Finally check if there is any
#  exception if yes then print it.
# TODO-26 - Once all data is collected to lists then create a panda dataframe from collected lists and store them to
#  dataframe data. Using to_csv() convert this data to csv by passing the csv filename with index=False. Now our csv
#  file is created.
# TODO-27 - Coming back to our home route, if everything goes fine then our csv file will be created. Once created read
#  data from csv file using pandas.read_csv(DATASET_FILE) and store the data to dataframe data. Sort the data by
#  "artist" and drop all na and extract unique names. Store the data to list artists.
# TODO-28 - Finally render index.html template and pass artists and building=False.
# TODO-29 - Now in order to create chart on the basis if artist name entered by user, lets create another route
#  "/get-artist" with method as "POST". Define a function named get_artist() below this.
# TODO-30 - Inside this function check if dataset file exists before processing using os.path.exists(DATASET_FILE). If
#  not then flash message for dataset still being prepared and redirect to home.
# TODO-31 - If dataset is prepared then get artist name from form using request and get function -
#  request.form.get("artist") and store it in variable named artist.
# TODO-32 - Validate artist input, if empty then flash error message and redirect to home. If artist name is correct
#  then add try and except condition. Inside try laod dataset from CSV using pandas and store them to dataframe data.
# TODO-33 - Filter dataset using case-insensitive match i.e., case doesn't matter only the name. Use str.contains() to
#  allow partial matches. Find "artist" in data with no case sensitive and na. Store the extracted data to "filtered"
#  dataframe.
# TODO-34 - Check if filtered.empty" i.e., no matching records. If true then flash message for no records found for the
#  artist and redirect to home. If records exist, then filter them "year", count them and reset index to name="count".
# TODO-35 - Create a bar chart using Plotly Express where X-axis -> "year" named as Year and Y-axis -> "count" named as
#  Number of Songs. Add title and labels in px.bar() function alongwith count_per_year, x and y. Apply dark theme layout
#  to the chart using fig.update_layout() function setting theme as "plotly dark".
# TODO-36 - Convert Plotly figure to HTML string using pio.to_html() function by passing the fig in it. Use
#  full_html=False to display just the chart part in html not the whole HTML page.
# TODO-37 - Finally flash message for showing final results and render "index.html" template by passing chart to it.
# TODO-38 - In case of exception flash error message and redirect to home.
# TODO-39 - Finally run the file in Flask development server in debug mode.

# index.html
# TODO-40 - Create a folder named templates and add a html file. Name it index.html.
# TODO-41 - Set language as English, set charset="UTF-8", Title="Billboard Artist Analyzer".
# TODO-42 - Add a meta tag which provides information about the webpage, not content shown on the page. name="viewport"
#  - viewport is the visible area of your webpage on a device. content="width=device-width, initial-scale=1" - Set the
#  page width equal to the device’s actual screen width and initial-scale=1 - sets the default zoom level when the page
#  loads i.e.,100% zoom (normal size).
# TODO-43 - Add Bootstrap link for styling in head section and script link in body section.
# TODO-44 - Add external link for style.css.
# TODO-45 - Using Jinja add if condition checking if building == True, if yes then add meta tag that simulates an HTTP
#  header with content="5" telling the browser to auto-refresh the page every 5 secs.
# TODO-46 - Add body tag inside this add a div with class="container py-5". "container" is a bootstrap class creates a
#  centered content area with responsive width according tot he screen size. "py-5" adds vertical padding of size 5.
# TODO-47 - Inside this div add <h1> tag with class="text-center mb-4" which aligns the text in center along with a
#  bottom margin of size 4. Add text as "Billboard Year End Hot 100".
# TODO-48 - Add element h1 using CSS selector in style.css. Inside it add font-weight, letter-spacing, color, text-align
#  and bottom margin.
# TODO-49 - Below h1 tag add another div with class="card bg-secondary p-4 shadow-lg". Create card class in style.css
#  and add border-radius, box-shadow, padding, background-color marking it as important i.e., “Apply this style NO
#  MATTER WHAT". Make sure border is none.
# TODO-50 - bg-secondary - sets background color as Bootstrap’s secondary theme color (usually a gray tone), p-4 - adds
#  padding of size 4 and shadow-lg - add a deeper shadow to the box.
# TODO-51 - Add a form tag with method="POST" and action="{{ url_for('get_artist') }}". Inside this add a div with
#  class="row g-3 align-items-center" - adds a row with medium spacing between input and button and vertically center
#  all columns relative to each other.
# TODO-52 - Inside this add another div with class="col-md-9" - which controls how wide a column should be at different
#  screen sizes. Here, takes 9 out of 12 parts of the row → 75% width for medium screen and 100% on small screens.
# TODO-53 - Add input tag with type="text" name="artist" class="form-control form-control-lg" placeholder="Enter artist
#  name". Create class form-control in style.css and add border-radius, border, padding, font-size and background color.
# TODO-54 - form-control-lg is a Bootstrap CSS class used to make input fields larger than the default size. Close div.
#  Add form-control:focus in style.css and change border-color.
# TODO-55 - Add another div below it with class="col-md-3 d-grid" where it takes 25% width for medium and large screens
#  and 100% for small screens (3/12 = 0.25). d-grid - display type is grid.
# TODO-56 - Add a button tag with class="btn btn-warning btn-lg" where byn is a classic bootstrap styling. btn-warning
#  is also bootstrap class which gives button a yellow/orange color.
# TODO-57 - Create a class btn-warning and add background color, font-weight, border-radius, text color along with no
#  border. Also change background color on hover. Add button text as "Hit the Charts". Close all divs and form.
# TODO-58 - Add flash message loop for notfications. Add a div with id="flash-container". Create this id in style.css
#  and add position, top, right and z-index. z-index controls the vertical stacking order of elements on a webpage—that
#  is, which element appears in front of or behind another when they overlap.
# TODO-59 - Use get_flashed_messages() function. Check if messages and add div. Run FOR loop for category and message
#  in messages. Add another div and set its class as flash-msg. This class contains padding, border, margin, color,
#  animation and color change for success, danger, ingo and warning messages. Add category using Jinja.
# TODO-60 - Finally add message in the div using Jinja, end FOR loop and div. End if loop and with condition. Close all
#  divs.
# TODO-61 - Add if condition using jinja which checks if chart exists, if true then we will display the card. Add a div
#  with class="card bg-secondary mt-4 p-3 shadow-lg". Add class .card.mt-4 and add background color, border-radius and
#  box-shadow. Rest all bootstrap built in classes are used where shadow-lg is for large shadow effect. Close if
#  condition, div, body and html tags.
# TODO-62 - Add body tag in style.css and add min-height: 100vh;, font-family, color, background color and background
#  image. background image is created using radial-gradient function which spreads color outward from a center point
#  (like a circle).
# TODO-63 - radial-gradient(shape position, color start, color end) so shape=circle, position=20% 20%(left 20%, top 20%)
#  , color=#a18cd1, start=0%, color=transparent, end=40% here color start - color starts strong and color end - fades
#  out by 40%. 4 shades are created like this and arranged to give a multicolor background image.




from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
import os, requests, time, threading
from bs4 import BeautifulSoup
import pandas
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)
app.config['SECRET_KEY'] = "any-key-you-want-to-use"
Bootstrap(app)

year = int(time.strftime("%Y"))

DATASET_FILE = "top100_year_end_hot.csv"
building_dataset = False
dataset_ready = False


def build_dataset():
    base_url = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    years, ranks, titles, artists = [], [], [], []

    for i in range(2000, year):
        try:
            response = requests.get(base_url + str(i), headers=headers, timeout=10)
            print(f"Year {i} → {response.status_code}")

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", {"class": "wikitable"})
            if not table:
                continue

            rows = table.find_all("tr")[1:]
            old_artist = None

            for row in rows:
                cols = row.find_all("td")
                if not cols:
                    continue

                rank = cols[0].text.strip()
                title = cols[1].text.strip().replace('"', '')
                artist = cols[2].text.strip() if len(cols) > 2 else old_artist

                years.append(i)
                ranks.append(rank)
                titles.append(title)
                artists.append(artist)

                old_artist = artist

            time.sleep(0.3)

        except Exception as e:
            print(f"Error on year {i}: {e}")

    data = pandas.DataFrame({
        "year": years,
        "rank": ranks,
        "title": titles,
        "artist": artists
    })

    data.to_csv(DATASET_FILE, index=False)
    print("Dataset created!")


def build_dataset_background():
    global building_dataset, dataset_ready
    try:
        build_dataset()
        dataset_ready = True
        print("Background dataset build finished.")
    except Exception as e:
        print(f"Background build failed: {e}")
    finally:
        building_dataset = False


@app.route("/")
def home():
    global building_dataset, dataset_ready

    if dataset_ready:
        flash("Dataset is ready! You can now search artists 🎉", "success")
        dataset_ready = False  # Reset so message shows only once

    if not os.path.exists(DATASET_FILE):
        if not building_dataset:
            flash("Dataset is being prepared in the background. Please wait a few seconds ⏳",
                  "warning")

            building_dataset = True

            thread = threading.Thread(target=build_dataset_background)
            thread.start()
        else:
            flash("Dataset is still being prepared. Please wait…", "info")

        return render_template("index.html", building=True)

    data = pandas.read_csv(DATASET_FILE)
    artists = sorted(data["artist"].dropna().unique())

    return render_template("index.html", artists=artists, building=False)


@app.route("/get-artist", methods=["POST"])
def get_artist():
    if not os.path.exists(DATASET_FILE):
        flash("Dataset is still being prepared. Please try again shortly.", "warning")
        return redirect(url_for("home"))

    artist = request.form.get("artist")

    if not artist:
        flash("Please enter an artist name.", "danger")
        return redirect(url_for("home"))

    try:
        data = pandas.read_csv(DATASET_FILE)
        filtered = data[data["artist"].str.contains(artist, case=False, na=False)]

        if filtered.empty:
            flash("No songs found for this artist.", "warning")
            return redirect(url_for("home"))

        count_per_year = filtered.groupby("year").size().reset_index(name="count")

        fig = px.bar(
            count_per_year,
            x="year",
            y="count",
            title=f"{artist.title()} on Billboard Year-End Hot 100",
            labels={"count": "Number of Songs", "year": "Year"}
        )

        fig.update_layout(template="plotly_dark")
        chart_html = pio.to_html(fig, full_html=False)

        flash(f"Showing results for {artist.title()} 🎵", "success")
        return render_template("index.html", chart=chart_html)

    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True, port=5000)