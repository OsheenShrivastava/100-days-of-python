
# main.py file
# TODO-1 - Import Flask, render_template, flash, request and jsonify from flask to build the web app and show messages.
# TODO-2 - Import Bootstrap to style the app using Flask-Bootstrap.
# TODO-3 - Import Image from PIL.
# TODO-4 - Import numpy as np.
# TODO-5 - Import os to work with file paths.
# TODO-6 - Import secure_filename from werkzeug.utils to check the security of file.
# TODO-7 - Import time to generate timestamps (used later for cache busting).
# TODO-8 - Create Flask app instance.
# TODO-9 - Initialize Bootstrap with the Flask app for styling.
# TODO-10 - Set SECRET_KEY required by Flask-WTF to protect forms from CSRF attacks.
# TODO-11 - Using app.config define a folder named 'UPLOAD_FOLDER' and define its actual path --> static/uploads where
#  all the uploaded files will be stored.
# TODO-12 - Using os.makedirs() function check if the folder exists. Create that folder inside static by default.
# TODO-13 - Create home route (/) supporting GET and POST methods. Create a variable named image_filename and store the
#  preview/default image to it. Now create a file path using os.path.join() adding 'static' and image_filename for
#  preview image.
# TODO-14 - Create an empty list named colors. Check if request method is 'POST', if true then request image file using
#  request.files.get('image') --> specifically for uploaded file and store it to file.
# TODO-15 - Check if file exists and filename is not empty, if true then check whether file is secure using
#  secure_filename(file.filename) and store it in filename. It basically cleans the file name to the version required
#  before uploading.
# TODO-16 - Extract the file extension from the uploaded filename using filename.rsplit() where filename splits from the
#  right side, using . as separator. The 1 means: Split only once, starting from the end. [-1] - this picks the last
#  part of the split result. .lower()- converts the extension to lowercase. Store it in ext variable.
# TODO-17 - Check if ext is one of them ['png', 'jpg', 'jpeg', 'webp'] if false then flash inavalid file type message.
# TODO-18 - If true then add try and except loop. In try verigy image. Open image using PIL, verify it and reset file
#  pointer.
# TODO-19 - Add current time using time.time() to filename joining it with "_". Store this to variable new_filename.
#  This is done to make filename unique. Create final file path by joining the 'UPLOAD FOLDER' with new_filename, store
#  this to upload_path.
# TODO-20 - Finally store the file to the upload_path using file.save(upload_path).
# TODO-21 - Add image_filename = 'uploads/' + new_filename and file_path = os.path.join('static', image_filename) to
#  create path when a new image is uploaded. Flash message for new image.
# TODO-22 - Add except Exception: and flash message for invalid file type in case of exception. If no image is uploaded
#  then add else for if file and file.filename != '': condition saying that no image is selected using default image.
# TODO-23 - Now to show preview image when the website opens the first time add image conversion to pixels outside the
#  if request.method == 'POST': condition so that it runs for preview image. Print image_filename and file_path for
#  debug purpose.
# TODO-24 - Now to convert image to pixels add try and except loop. In try open image using PIL by passing file_path and
#  convert it to RGB.--> img = Image.open(file_path).convert('RGB').
# TODO-25 - In case of exception flash error message to upload valid file and change the image to preview image. Add
#  file_path for preview image and open it.
# TODO-26 - Finally resize image, convert image to Numpy array, reshape image to remove height,width and calculate
#  overall pixels. Use unique() function to count all unique colors as well as get their names.
# TODO-27 - Finally sort the colors in descending i.e., from more to less in terms of count. Now sort top 10 colors and
#  store it to variable top_colors.
# TODO-28 - Run FOR loop through top_colors and convert tuple RGB to hex code for all colors.
# TODO-29 - Finally render index.html and pass image_filename and colors to it.
# TODO-30 - Create another route named /flash-copy supporting POST method. Add function flash_copy inside it. This route
#  is our backend API endpoint that talks to your JavaScript when a color is copied.
# TODO-31 - request.json.get('hex') - get the value of hex sent from the frontend. Store this to hex_code. Send JSON
#  response back using jsonify by adding message as 'Copied {hex_code} to clipboard!' and category as 'success'.
#  JavaScript (backend) receives this and shows it as notification using flash.
# TODO-32 - Finally run the file in Flask development server in debug mode.

# base.html file
# TODO-33 - Create a folder named templates and add a html file. Name it base.html. Add style.css in the folder static.
# TODO-34 - Set language as English, set charset="UTF-8", Title="Image Colour Palette Generator". Use {% block title %}
#  and {% endblock %}. Add Bootstrap link for styling in head section and script link in body section.
# TODO-35 - Add links for font Pacifico. Add external link for style.css.
# TODO-36 - Add flash message loop for notfications. Use get_flashed_messages() function. Check if messages, add div
#  and set its id=flash-container.
# TODO-37 - Create this id in style.css and add position, top, right and z-index. z-index controls the vertical
#  stacking order of elements on a webpage—that is, which element appears in front of or behind another when they
#  overlap.
# TODO-38 - Run FOR loop for category and message in messages. Add another div and set its class as flash-msg. This
#  class contains padding, border, margin, color, animation and color change for success and danger messages. Add
#  category using Jinja.
# TODO-39 - Finally add message in the div using Jinja, end FOR loop and div. End if loop and with condition.
# TODO-40 - Add <main> opening and closing tags which encloses main content of the website. Add {% block content %} and
#  {% endblock %} to enclose body content inside it.
# TODO-41 - Add {% include "footer.html" %} to include footer from footer.html.
# TODO-42 - Add <script> opening and closing tags to start a javascript block inside html file.
# TODO-43 - Inside it add document.addEventListener("DOMContentLoaded", function () - Waits until the entire HTML page
#  is loaded before running the script. This prevents errors like “element not found”.
# TODO-44 - const flashContainer = document.getElementById("flash-container"); - Finds the element where flash messages
#  (like “Copied!”) will appear and stores it in a variable.
# TODO-45 - document.querySelectorAll(".color").forEach(btn => Selects all elements with class color
#  (the color boxes/buttons). Runs the following code for each one. btn.addEventListener("click", function () - Adds a
#  click event to each color button. Everything inside runs when a user clicks a color.
# TODO-46 - const hex = this.dataset.hex; - Gets the HEX color value stored in the button’s data-hex attribute.
#  const label = this.querySelector(".copy-text"); - Finds the small text inside the button (like “Copy”) so we can
#  change it to “Copied ✓”.
# TODO-47 - navigator.clipboard.writeText(hex).then(() => Copies the HEX value to the user’s clipboard. .then() runs
#  only after copy is successful. label.textContent = "Copied ✓"; - Changes the button text from Copy → Copied ✓.
# TODO-48 - fetch("/flash-copy", { method: "POST", headers: { "Content-Type": "application/json" },
#  body: JSON.stringify({ hex: hex }) }) - Sends a POST request to your Flask backend at /flash-copy. method: "POST" →
#  sending data. Content-Type: application/json → tells server it's JSON. body → sends {"hex": "#FF5733"}.
# TODO-49 - .then(res => res.json()) - Waits for server response and converts it into JSON format. .then(data => - Runs
#  after server sends back data like: { "message": "Copied #FF5733!", "category": "success" }.
# TODO-50 - const msg = document.createElement("div"); msg.className = "flash-msg " + data.category; - Creates a new
#  <div> for the flash message. Adds classes like: flash-msg success and flash-msg error.
# TODO-51 - msg.textContent = data.message; - Sets the message text coming from backend.
# TODO-52 - flashContainer.appendChild(msg); - Adds the flash message inside your flash container on the page.
# TODO-53 - setTimeout(() => { msg.remove(); label.textContent = "Copy";}, 2000); - After 2 seconds (2000 ms): Removes
#  the flash message. Changes button text back from Copied ✓ → Copy.
# TODO-54 - Close all blocks - then(data => { ... }) block, clipboard success block, button click event, loop for all
#  .color buttons and DOMContentLoaded event.
# TODO-55 - Close body and html tags.

# footer.html
# TODO-56 - Add another html file named footer.html in templates folder.
# TODO-57 - Open <footer> tag and add class footer. Create this class in style.css and add display type ad grid,
#  text color, alignment, font-size resolution for screens, font-weight and padding. Add your footer in <p> tag. Set
#  margin for <p> inside footer to 0 in style.css.
# TODO-58 - Add * in style.css and add box-sizing: border-box;
# TODO-59 - Add html, body tags inside them add min-height, font-family and background as 'bg.jpg' stored in 'static'
#  folder. Add margin and padding as 0. Add background-size: cover; -  Make the background image large enough to
#  completely cover the element. Add background-position: center; - Keep the center of the image visible when cropping
#  happens. Without this, browser may crop from a corner. With this, cropping happens equally from all sides.
# TODO-60 - Add body tag, inside it add display as flex, flex-direction: column; and font-size for all screens.
#  Add background-attachment: fixed; - The background image does NOT move when you scroll. Add overflow-y: auto; -
#  Controls vertical scrolling behavior of an element. What auto does: Adds a vertical scrollbar ONLY IF content is
#  taller than the container. If content fits → no scrollbar.
# TODO-61 - Add main tag, inside it add flex: 1;(fills all free space), display as flex with flex-direction: column;,
#  align-items: center;, gap: 6px; and padding: 0;.

# index.html
# TODO-62 - Using bootstrap5/form.html import render_form. Extend base.html file using Jinja template
#  {% extends "base.html" %} to include all everything accept main body.
# TODO-63 - Use {% block title %} and add title 'Image Colour Palette Generator' in it. End with {% endblock %}.
# TODO-64 - Add {% block content %} and {% endblock %} to enclose main content inside it.
# TODO-65 - Create a <div> with class page-wrapper to center and style the full page layout. Add this class in style.css
#  and add min-height, display type as grid and grid-template-rows: auto 1fr auto;.
# TODO-66 - grid-template-rows: auto 1fr auto; - It means your grid has 3 rows, and each row behaves differently.
#  auto (Row 1) - Height is based on content size only. Row grows just enough to fit what’s inside. 1fr (Row 2) -
#  fr = fraction of available space. 1fr means: Take up all remaining vertical space. This row stretches to fill
#  leftover space after the auto rows take what they need. auto (Row 3) - Again adjusts height based on content.
# TODO-67 - Create a <div> with class container. Inside it add tag <h5> with text as "Image Colour Palette Generator".
# TODO-68 - Create class .container > h5 in style.css and add font-size for all screens, font-weight, padding, display
#  type as grid, alignment to center, text color and letter-spacing: 1px;.
# TODO-69 - Add another div with class="card upload-card". Create class card and add width. max-width, margin, padding,
#  background, border-radius, box-shadow, alignment to center, display type as grid, gap and backdrop-filter: blur(6px);
#  - to blur a small section outside the border of card. Create another class upload-card and add max-width and margin.
# TODO-70 - Add tag <h2> inside above div with class="card-title". Set the text as "Upload an Image". Create class
#  card-title and add font-family, text color and font-size for all screens.
# TODO-71 - Create a <form> element with POST method to send user data securely. Add enctype="multipart/form-data" to
#  allow image file uploads. Add action as link for 'home'.
# TODO-72 - Inside this form add a div with class="mb-3" i.e., margin-bottom = size 3 (16px). Inside this add <input>
#  tag which will be a "file upload field".
# TODO-73 - Add class="form-control" - Makes the input full width, adds padding and gives consistent styling
#  (border, font, spacing). type="file" - Changes the input into a file picker. When clicked: Opens file explorer
#  (Windows/Mac), lets user choose a file and selected file gets attached to the form. id="imageUpload" - Unique
#  identifier for JavaScript or label linking. name="image" - to access the image using Flask-Form. accept="image/*" -
#  Restricts file chooser to image files only. Allowed examples: .jpg, .png, .jpeg, .gif and .webp.
# TODO-74 - Add a <button> tag with class="btn". Add its text as "Generate Palette". Create class btn in style.css and
#  add padding, border-radius, background, text color, font-weight, cursor: pointer;, transition: 0.3s ease; (for
#  animation) and no border. Add background: #c48b97; and transform: translateY(-2px); when hovered.
# TODO-75 - Add <img> tag with source as  url_for('static', filename=image_filename) since we are passing image name as
#  "image_filename" to index.html. Add class="preview-img". Create this class and add width, border-radius, top-margin,
#  box-shadow and object-fit: cover;.
# TODO-76 - object-fit: cover - makes an <img> or <video> fill its container completely while keeping its aspect ratio.
#  When you set a fixed size on an image container:  width: 100%; height: 200px; object-fit: cover;. Without object-fit,
#  the image would stretch and look distorted. With cover, it zooms and crops instead — much cleaner.
# TODO-77 - Add <h2> tag below this with class="card-title" and set its text as "Your Color Palette".
# TODO-78 - Add if condition using jinja to display top 10 colour colors. Inside if condition add a div with
#  class="palette". Create this class and add display type as grid, grid-template-columns: repeat(5, 1fr); - 5 columns
#  per row., border-radius, alignment to center, gap and top-margin.
# TODO-79 - Add @media (max-width: 600px) {.palette { grid-template-columns: repeat(3, 1fr);}} for mobile layout.
# TODO-80 - Add FOR loop using jinja and loop through 'colors' passed from main.py. Add <button> tag inside this loop
#  with type="button", class="color", data-hex="{{ color }}" and style="background: {{ color }}".
# TODO-81 - type="button" - Tells the browser this button is just a clickable button, NOT a form submit button. HTML
#  allows storing extra info using attributes that start with "data-". So when user clicks the color, JS knows which hex
#  value to copy. {{ color }} - Insert the value of color from Python here. Set background color of button of the
#  respective hex code.
# TODO-82 - Create class color in style.css and add flex: 0 0 auto; - short for flex-grow: 0; flex-shrink: 0;
#  flex-basis: auto; Stay your natural size. Don’t grow. Don’t shrink. Add text color, font-weight, border-radius,
#  min-width, text alignment, padding, font-size, cursor: pointer;, transition: transform 0.15s ease, filter 0.2s ease;,
#  border: none; and position: relative;.
# TODO-83 - On hover add  transform: translateY(-2px); - to slow the animation of lifting the button.
#  filter: brightness(85%); - to change the brightness of the respective color to a bit dark when hovered.
# TODO-84 - Add {{ color }} to display the hex code at the center. Add <span> with class="copy-text" and text as "Copy".
#  We have two pieces of text: The color value (like #FF5733) and the word Copy. The <span> wraps just the "Copy" text
#  so JavaScript can change it without affecting the hex code text.
# TODO-85 - Create class copy-text in style.css and add position: absolute; since the color tab's position was relative.
#  The element is removed from normal flow and positioned relative to its nearest positioned ancestor. inset: 0; - This
#  covers entire button so wherever it is clicked it will show "copy". Add display type as flex, align-items: center;,
#  justify-content: center;, background, text color, font-size, font-weight,  opacity: 0;(to hide by default) and
#  transition: 0.2s ease; (animation). On hover set opacity: 1;.
# TODO-86 - End FOR loop, if condition and close all divs.



from flask import Flask, render_template, flash, request, jsonify
from flask_bootstrap import Bootstrap
from PIL import Image
import numpy as np
import os
from werkzeug.utils import secure_filename
import time


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'any-string-you-want-to-keep-secret'


app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'] , exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def home():

     image_filename = 'preview.jpg'

     # This image path is for preview image
     file_path = os.path.join('static', image_filename)

     colors = []

     if request.method == 'POST':
         file = request.files.get('image')

         if file and file.filename != '':
             filename = secure_filename(file.filename)
             ext = filename.rsplit('.', 1)[-1].lower()

             # ✅ Allow only real image extensions
             if ext not in ['png', 'jpg', 'jpeg', 'webp']:
                 flash('Invalid file type. Please upload an image file.', 'danger')

             else:
                 try:
                     # Verify image before saving
                     img_test = Image.open(file)
                     img_test.verify()  # check integrity
                     file.seek(0)  # reset file pointer

                     new_filename = str(int(time.time())) + "_" + filename
                     upload_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                     file.save(upload_path)

                     image_filename = 'uploads/' + new_filename
                     file_path = os.path.join('static', image_filename)

                     flash('New image uploaded successfully!', 'success')

                 except Exception:
                     flash('Uploaded file is not a valid image.', 'danger')

         else:
             flash('No image selected. Using default preview.', 'success')

     print("IMAGE FILENAME FOR HTML:", image_filename)
     print("FILEPATH USED FOR NUMPY:", file_path)

     # Generate palette
     try:
         # Open Image using PIL
         img = Image.open(file_path).convert('RGB')
     except Exception:
         flash('Error loading image. Please upload a valid image file.', 'danger')
         image_filename = 'preview.jpg'
         file_path = os.path.join('static', image_filename)
         img = Image.open(file_path).convert('RGB')

     # Resize
     img = img.resize((150, 150))
     # Convert image to Numpy Array
     img_array = np.array(img)
     # Reshape to remove height and width and calculate overall pixels
     pixels = img_array.reshape(-1, 3)

     # Get most frequent colors
     unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
     # Sort by frequency
     sorted_indices = np.argsort(-counts)
     top_colors = unique_colors[sorted_indices[:10]]

     # Convert to HEX
     for color in top_colors:
        colors.append('#%02x%02x%02x' % tuple(color))

     print(colors)

     return render_template('index.html', image_filename=image_filename, colors=colors)


@app.route('/flash-copy', methods=['POST'])
def flash_copy():
    hex_code = request.json.get('hex')
    return jsonify({
        'message': f'Copied {hex_code} to clipboard!',
        'category': 'success'
    })




if __name__ == '__main__':
    app.run(debug=True)