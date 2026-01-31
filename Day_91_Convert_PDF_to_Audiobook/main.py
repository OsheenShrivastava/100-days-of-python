
# main.py file
# TODO-1 - Import requests to send HTTP requests to the VoiceRSS Text-to-Speech API.
# TODO-2 - Import os to work with file paths and environment variables.
# TODO-3 - Import load_dotenv from dotenv to load API keys from a .env file.
# TODO-4 - Import Flask, render_template, and flash from flask to build the web app and show messages.
# TODO-5 - Import FlaskForm from flask_wtf to create secure web forms.
# TODO-6 - Import DataRequired and Optional validators to validate form inputs.
# TODO-7 - Import SelectField, SubmitField, and FileField to build dropdowns, buttons, and file upload fields.
# TODO-8 - Import Bootstrap to style the app using Flask-Bootstrap.
# TODO-9 - Import time to generate timestamps (used later for cache busting).
# TODO-10 - Import PyPDF2 to read and extract text from uploaded PDF files.
# TODO-11 - Create Flask app instance.
# TODO-12 - Initialize Bootstrap with the Flask app for styling.
# TODO-13 - Set SECRET_KEY required by Flask-WTF to protect forms from CSRF attacks.
# TODO-14 - Load environment variables from .env file.
# TODO-15 - Create .env file and store API_KEY in it. Read VoiceRSS API key from environment variables.
# TODO-16 - Define VoiceRSS API endpoint URL.
# TODO-17 - Define gender dropdown options (Male/Female).
# TODO-18 - Define language dropdown options (US English, UK English, Hindi).
# TODO-19 - Define available male voices for US English, female voices for US English, male voices for UK English,
#  female voices for UK English, male voices for Hindi and female voices for Hindi.
# TODO-20 - Create UploadForm class inheriting from FlaskForm.
# TODO-21 - Add file upload field for PDF with validation, gender dropdown field and language dropdown field. Make sure
#  validators=[DataRequired() is added in all 3 fields.
# TODO-22 - Add male US voice and female US voice dropdown (optional, shown dynamically in UI). Similarly add dropdowns
#  for male UK voice, female UK voice, male Hindi voice and female Hindi voice.
# TODO-23 - Add submit button labeled “Convert to Speech”.
# TODO-24 - Add render_kw() function in all fields to apply bootstrap type styling to a normal form tag. Add
#  "class": "form-control" to pdf field. Add "class": "form-select" to all other fields except submit.
# TODO-25 - Create is_pdf_file(file_storage) function to check if uploaded file is a real PDF. Pass file_storage to it.
#  Move file pointer to start before reading header. Read first 1KB of file to check for %PDF signature. Reset file
#  pointer after reading. Return True if file header contains %PDF.
# TODO-26 - Create home route (/) supporting GET and POST methods.
# TODO-27 - Initialize form instance.
# TODO-28 - Create a folder named static and store all audio file into it. Check if audio file already exists to show
#  player in UI.
# TODO-29 - Check if form is submitted. Get uploaded PDF file from form and store it in variable file.
# TODO-30 - Validate file extension by converting it to lower_case and checking the extension.
# TODO-31 - Also check if file is pdf by calling is_pdf_file and passing file to it. Confirm it is a real PDF.
# TODO-32 - Show error message if invalid PDF and reload page. Pass audio_ready to form.
# TODO-33 - Initialize variable selected_voice to none to store selected voice.
# TODO-34 - Create list of all possible voice dropdown fields and store them to a list named voice_fields.
# TODO-35 - Loop through voice fields to find which dropdown has a selected value. Assign the first non-empty voice
#  value to selected_voice.
# TODO-36 - Show warning if no voice is selected. Print selected voice for debugging.
# TODO-37 - Use try and except logic. In try, reset file pointer before reading PDF. Create PdfReader object.
# TODO-38 - Initialize text_parts list to store text from each page. Loop through all PDF pages. Extract text from each
#  page. Append non-empty page text to list.
# TODO-39 - Join all page text into one string. Print extracted text length for debugging.
# TODO-40 - If there is an exception then  flash error message and reload the page.
# TODO-41 - Limit extracted text to first 1000 characters to avoid large API requests.
# TODO-42 - Create dictionary of parameters required by VoiceRSS API. This includes key, hl(language), v(voice),
#  src(text) and audio codec.
# TODO-43 - Send GET request to API with API_ENDPOINT and parameters. Raise error if HTTP request fails.
# TODO-44 - Print response status and content type for debugging. Preview first 200 characters of response for
#  debugging.
# TODO-45 - Read Content-Type header from API response. Check if response code is 200 and contains audio data.
# TODO-46 - If true, then open static/audio.mp3 in write-binary mode. Write API response content into audio file. Show
#  success message and set  audio_ready as true. Show error message if API did not return valid audio.
# TODO-47 - Generate timestamp-based version number to force browser to reload new audio file.
# TODO-48 - Render index.html with form, audio status, and version number.
# TODO-49 - Run Flask app in debug mode when script is executed directly.

# base.html file
# TODO-50 - Create a folder named templates and add a html file. Name it base.html. Add style.css in the folder static.
# TODO-51 - Set language as English, set charset="UTF-8", Title="Convert PDF to AudioBook". Use {% block title %} and
#  {% endblock %}. Add Bootstrap link for styling in head section and script link in body section.
# TODO-52 - Add links for font Space Grotesk. Add external link for style.css.
# TODO-53 - Add flash message loop for notfications. Use get_flashed_messages() function. Check if messages, add div
#  and set its id=flash-container.
# TODO-54 - Create this id in style.css and add position, top, right and z-index. z-index controls the vertical
#  stacking order of elements on a webpage—that is, which element appears in front of or behind another when they
#  overlap.
# TODO-55 - Run FOR loop for category and message in messages. Add another div and set its class as flash-msg. This
#  class contains padding, border, margin, color, animation and color change for success and danger messages. Add
#  category using Jinja.
# TODO-56 - Finally add message in the div using Jinja, end FOR loop and div. End if loop and with condition.
# TODO-57 - Add <main> opening and closing tags which encloses main content of the website. Add {% block content %} and
#  {% endblock %} to enclose body content inside it.
# TODO-58 - Add {% include "footer.html" %} to include footer from footer.html.
# TODO-59 - Close body and html tags.

# footer.html
# TODO-60 - Add another html file named footer.html in templates folder.
# TODO-61 - Open <footer> tag and add class footer. Create this class in style.css and add display type ad grid,
#  text color, alignment, font-size resolution for screens, font-weight and padding. Add your footer in <p> tag. Set
#  margin for <p> inside footer to 0 in style.css.
# TODO-62 - Add * in style.css and add box-sizing: border-box;
# TODO-63 -  Add html, body tags inside them add height, font-family and background. Add margin and padding as 0. Add
#  body tag, inside it add display as flex, flex-direction: column; and font-size for all screens.
# TODO-64 - Add main tag, inside it add flex: 1;(fills all free space), display as grid, align-items: center;,
#  overflow: hidden; and padding: 10px 0;.

# index.html
# TODO-65 - Using bootstrap5/form.html import render_form. Extend base.html file using Jinja template
#  {% extends "base.html" %} to include all everything accept main body.
# TODO-66 - Use {% block title %} and add title 'Convert PDF to AudioBook' in it. End with {% endblock %}.
# TODO-67 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-68 - Create a <div> with class page-wrapper to center and style the full page layout. Add this class in style.css
#  and add min-height and display type as grid.
# TODO-69 - Create a Bootstrap container upload_form to hold the upload form and audio player. Add this class in
#  style.css. Select all direct child elements inside the upload form container for styling and set their bottom margin
#  to margin-bottom: 4px;
# TODO-70 - Add upload_form in style.css and add display type as grid, justify content to center, padding, font-weight,
#  border-radius, box-shadow, top margin, width and gap.
# TODO-71 - Add a heading <h3> to display the page title “Convert PDF to Audiobook”. Add class .upload_form h3 to
#  style.css and add font-weight, padding-bottom, margin-bottom and font-size for all screens.
# TODO-72 - Create a <form> element with POST method to send user data securely. Add enctype="multipart/form-data" to
#  allow PDF file uploads. Apply class voice-form for custom CSS styling.
# TODO-73 - Add this class to style.css. This class will use :has() to check condition inside the form. Find element
#  with id-"language", inside it finr the <option> with value "en-us". :checked() function states that "this is
#  currently selected". Similarly check if gender is male by adding this further -->
#  :has(#gender option[value="male"]:checked).
# TODO-74 - Finally when language(en-us) and gender(male) is selected then add class .male-en and display it using
#  display: block;.
# TODO-75 - Similarly add this for all other options --> female-en, male-uk, female-uk, male-hi and female-hi.
# TODO-76 - Include form.hidden_tag() to enable CSRF protection for Flask-WTF forms.
# TODO-77 - Add another div with class="mb-3", margin-bottom: 3(16px). Inside it display the PDF upload label using
#  form.pdf.label. Render the PDF file input field using form.pdf. Make sure everything is inside jinja template.
# TODO-78 - Similarly add div with same class for language and gender. display the language selection label using
#  form.language.label and gender selection label using form.gender.label. Render the language dropdown field using
#  form.language and gender dropdown field using form.gender.
# TODO-79 - Add another div with class="mb-3 voice-group male-en". Create class voice-group in style.css and add
#  display: none; in it.
# TODO-80 - Display label and dropdown for US Male voice --> (form.male_en.label) & (form.male_en).
# TODO-81 - Add another div with class="mb-3 voice-group male-en". Display label and dropdown for US Female voices -->
#  (form.female_en.label) & (form.female_en).
# TODO-82 - Add another div with class="mb-3 voice-group male-uk". Display label and dropdown for UK Male voices -->
#  (form.male_uk.label) & (form.male_uk).
# TODO-83 - Add another div with class="mb-3 voice-group female-uk". Display label and dropdown for UK Female voices -->
#  (form.female_uk.label) & (form.female_uk).
# TODO-84 - Add another div with class="mb-3 voice-group male-hi". Display label and dropdown for Hindi Male voices -->
#  (form.male_hi.label) & (form.male_hi).
# TODO-85 - Add another div with class="mb-3 voice-group female-hi". Display label and dropdown for Hindi Female voices
#  --> (form.female_hi.label) & (form.female_hi).
# TODO-86 - Add another div with class="mt-3". Add a submit button using form.submit styled with Bootstrap classes -->
#  class="btn btn-primary w-100". Make button full width using w-100. Close form tag.
# TODO-87 - Add class .upload_form label in style.css and add font-size clamp for all screens.
# TODO-88 - Add classes .upload_form input, .upload_form select and .upload_form textarea together separated by commas.
#  Add styling --> font-size for all screens and padding.
# TODO-89 - Create class .upload_form button for submit button and add font-size for all screens, font-weight and
#  padding.
# TODO-90 - Check if audio_ready is True before displaying audio player using jinja.
# TODO-91 - Create a div container with class="audio-player mt-2" for audio controls and title. Create this class in
#  style.css and add top margin and text alignment.
# TODO-92 - Display heading “Your Audiobook” using <h5> when audio is ready.
# TODO-93 - Add HTML5 <audio> player with controls enabled to embed sound directly into a webpage. Add class
#  .audio-player audio and add height, width and max-width in it.
# TODO-94 - The controls attribute tells the browser: “Show the built-in audio player interface.” such as Play / Pause,
#  Volume control, Progress bar (seek forward/back) and Current time / duration.
# TODO-95 - Add <source> tag. Inside it add file from Flask static folder using url_for. Append cache-busting version
#  query string using audio_version --> v={{ audio_version }}. State the type="audio/mpeg". This loads generated MP3
#  file.
# TODO-96 - Add fallback message if browser does not support audio playback. Close if condition.
# TODO-97 - Add <a> tag to create download button linking to generated MP3 file in static folder using
#  href="{{ url_for('static', filename='audio.mp3') }}".
# TODO-98 - Use download attribute so file downloads instead of opening in browser.
# TODO-99 - Style download button with Bootstrap success class --> class="btn btn-success mt-1". Add margin top spacing
#  using mt-1. Close <a> tag.
# TODO-100 - Close container and wrapper divs properly.





import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Optional
from wtforms import SelectField, SubmitField, FileField
from flask_bootstrap import Bootstrap
import time
import PyPDF2



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'any-string-you-want-to-keep-secret'


load_dotenv()

API_KEY = os.getenv("API_KEY")

API_ENDPOINT = "https://api.voicerss.org/"


gender_menu = [("male", "Male Voice"), ("female", "Female Voice")]
language_menu = [("en-us", "English (US)"), ("en-gb", "English (UK)"), ("hi-in", "Hindi (India)")]
male_voice_en = [("john", "John"), ("mike", "Mike")]
female_voice_en  = [("linda", "Linda"), ("amy", "Amy"), ("mary", "Mary"), ("finnish", "Finnish")]
male_voice_uk = [("harry", "Harry")]
female_voice_uk = [("alice", "Alice"), ("nancy", "Nancy"), ("lily", "Lily")]
male_voice_hi  = [("kabir", "Kabir")]
female_voice_hi  = [("puja", "Puja")]



class UploadForm(FlaskForm):
    pdf = FileField('Upload PDF',validators=[DataRequired()], render_kw={"class": "form-control"})
    gender = SelectField('Choose Gender', choices=gender_menu, validators=[DataRequired()],
                         render_kw={"class": "form-select"})
    language = SelectField('Choose Language', choices=language_menu, validators=[DataRequired()],
                           render_kw={"class": "form-select"})

    male_en = SelectField("Male Voice (US)", choices=male_voice_en, validators=[Optional()],
                          render_kw={"class": "form-select"})
    female_en = SelectField("Female Voice (US)", choices=female_voice_en, validators=[Optional()],
                            render_kw={"class": "form-select"})

    male_uk = SelectField("Male Voice (UK)", choices=male_voice_uk, validators=[Optional()],
                          render_kw={"class": "form-select"})
    female_uk = SelectField("Female Voice (UK)", choices=female_voice_uk, validators=[Optional()],
                            render_kw={"class": "form-select"})

    male_hi = SelectField("Male Voice (Hindi)", choices=male_voice_hi, validators=[Optional()],
                          render_kw={"class": "form-select"})
    female_hi = SelectField("Female Voice (Hindi)", choices=female_voice_hi, validators=[Optional()],
                            render_kw={"class": "form-select"})

    submit = SubmitField('Convert to Speech')


def is_pdf_file(file_storage):
    file_storage.seek(0)
    header = file_storage.read(1024)  # read first 1KB
    file_storage.seek(0)  # reset pointer
    return b"%PDF" in header


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadForm()

    audio_ready = os.path.exists("static/audio.mp3")

    if form.validate_on_submit():

        # ✅ Step 1 — Validate PDF file type
        file = form.pdf.data

        if not file.filename.lower().endswith(".pdf") or not is_pdf_file(file):
            flash("Please upload a valid PDF file.", "danger")
            return render_template('index.html', form=form, audio_ready=audio_ready)

        # 🎤 Step 2 — Determine which visible voice dropdown was used
        selected_voice = None

        voice_fields = [form.male_en, form.female_en, form.male_uk, form.female_uk, form.male_hi, form.female_hi]

        for field in voice_fields:
            if field.data:  # Only the visible dropdown will have value
                selected_voice = field.data
                break

        if not selected_voice:
            flash("⚠️ Please select a voice option.", "warning")
            return render_template('index.html', form=form, audio_ready=audio_ready)

        print("Selected voice:", selected_voice)

        try:
            file.seek(0)  # reset pointer
            reader = PyPDF2.PdfReader(file)

            text_parts = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

            text = "\n".join(text_parts).strip()
            print("✅ Extracted text length:", len(text))

        except Exception as e:
            print("❌ PDF READ ERROR:", e)
            flash("Error reading PDF file.", "danger")
            return render_template('index.html', form=form, audio_ready=audio_ready)

        text = text[:1000]  # reduce limit

        parameters = {
            "key": API_KEY,
            "hl": form.language.data,
            "v": selected_voice,
            "src": text,
            "c": "MP3"
        }

        response = requests.get(API_ENDPOINT, params=parameters)
        response.raise_for_status()

        print("Status Code:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))
        print("Response Preview:", response.text[:200])

        content_type = response.headers.get("Content-Type", "")

        if response.status_code == 200 and "audio" in content_type:
            with open('static/audio.mp3', 'wb') as audio_file:
                audio_file.write(response.content)
                flash("🎧 Your audiobook is ready! Click download below.", "success")
                audio_ready = True
        else:
            flash("❌ Failed to convert PDF to audio. Please try again.", "danger")
            print("Error:", response.text)

    # 🔥 Cache-busting version number
    audio_version = int(time.time()) if audio_ready else None

    return render_template('index.html', form=form, audio_ready=audio_ready,
                           audio_version=audio_version)




if __name__ == '__main__':
    app.run(debug=True)