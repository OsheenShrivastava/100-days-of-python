
# TODO-1 - Import all files from Tkinter.
# TODO-2 - Create a Window and name it.
# TODO-3 - Run GUI and check. Import filedialog, messagebox, colorchooser from tkinter. Import Image, ImageTk,
#  ImageDraw, ImageFont from PIL. Import os.
# TODO-4 - Import customtkinter as ctk. Create a label to display background image. Create Welcome_Label,
#  Watermarking_Button and Click_Here label using customtkinter.
# TODO-5 - Click on Watermarking_Button to start watermarking image. Add the command to open another window upon
#  clicking the button.
# TODO-6 - Use place method to place the button on window and place it in center.
# TODO-7 - Use Canvas to apply a background image for the app. Use create_image() function to display image on canvas.
# TODO-8 - Create a Welcome label and place it on the screen using place method.
# TODO-9 - Create a Click Here! label just below watermarking button. Use place method to place it.
# TODO-10 - Once watermarking button is clicked it should redirect to Watermarking_Window() function.
# TODO-11 - Add global Add_File_Button, Welcome_Label, Click_Here_Label, Watermarking_Button, background_label,
#  background_label_2, tk_img, canvas, bg_img, filename, Text_Box in Watermarking_Window() function.
# TODO-12 - Destroy Welcome_Label, Click_Here_Label, Watermarking_Button, background_label, make sure background image
#  is same and add Add_File_Button.
# TODO-13 - Resize the window to 900x600. Show background image using label.
# TODO-14 - Create a Canvas window of 1000x600 and place it at (50,50).
# TODO-15 - Call default_image() function which will draw a blank image using Image draw. Add global variables canvas,
#  image_on_canvas, tk_img, img. Create an image using PhotoImage and create this image on canvas. Check if no image is
#  on the canvas then create one and if image is present then configure it.
# TODO-16 - Create a Button named "Select_File_Button" to allow user to select image file.
# TODO-17 - Add a Text_Label named "Text" and add a Text Window to obtain user input text for watermark.
# TODO-18 - Add a Font_Label named "Font" and add a Font Window to show options for different fonts to select from.
# TODO-19 - Add a Color_Label named "Color" and add a Color Window to show options for different colours.
# TODO-20 - Add a Size_Label named "Size" and add a Size Window to show options for different sizes.
# TODO-21 - Add a Rotation_Label named "Rotation" and add a Rotation Scale Window to show options for rotation options.
# TODO-22 - Call function open_image() when Select_File_Button is clicked. This function uses filedialog to open a file.
#  Add global img_canvas, image_on_canvas,tk_img. Add all the file types in it.
# TODO-23 - If no file is selected then it should return to the same page.
# TODO-24 - Inside open_image() function call show_uploaded_image() function and pass filename (path) to this function.
# TODO-25 - Add global variables canvas, image_on_canvas, tk_img,img in this function. Open the image and resize it.
# TODO-26 - Create a PhotoImage and display it on Canvas.
# TODO-27 - To show text on image when typed in text box add Text_Box.bind("<KeyRelease>", apply_watermark). It calls
#  apply_watermark() function which is responsible to apply the text input as watermark on the image. "<KeyRelease>"
#  is whenever the user releases a key after typing.
# TODO-28 - Add .ttf files for desired font in your project under the folder "fonts".
# TODO-29 - Create a list of font types using FOR loop and os. Create font_combobox and assign it a string variable
#  A StringVar is a special Tkinter variable that holds a string. Whenever the user selects a value from the dropdown,
#  this variable is updated.
# TODO-30 - Sets the default value for the dropdown. If font_files is not empty → pick the first font. If it’s empty →
#  set it to an empty string ("").
# TODO-31 - Creates a dropdown (OptionMenu) in the window. Options are populated from font_files (list of available
#  font names or paths), command=lambda x: apply_watermark() → whenever the user changes font, it calls your
#  apply_watermark() function to update the watermark with the new font. Place it on tthe canvas.
# TODO-32 - Create a button to choose colour. Add text as hex code of the colour choosen. Add bg and fg. Apply command
#  and call function pick_color.
# TODO-33 - Inside pick_color function add global variables font_color and Color_Box. Use colorchooser to ask colour
#  from user. Check hex code of colour when choosen and assign it to font_color variable.
# TODO-34 - Add is_dark function to show hex code as "white" for dark shaded and "black" for light shades. Inside
#  is_dark function check brightness using luminance formula. It checks if the colour choosen is light or dark and
#  returns the same status.
# TODO-35 - In pick_color function it checks if the choosen colour is light, then it sets the fg_color of text as
#  "black" else if choosen colour is dark, then it sets it "white".
# TODO-36 - Configure the Color_Box with bg as font_color, text as font_color and fg as fg_color. Then call
#  apply_watermark() function.
# TODO-37 - Create font_size_var = StringVar(value="40") under after window creation to have a default watermark.
# TODO-38 - Create a vcmd (Validate Command Window) named only_numbers which only allows numbers by checking if number
#  entered is digit. So it does not allow characters or special symbols.
# TODO-39 - Inside Font_Size_Box Add font_size_var in text, add validate="key" which Tells Tkinter when validation
#  should happen. "key" → validation triggers on each keystroke (every time the user types or deletes a character).
# TODO-40 - Add validatecommand as vcmd. Add Font_Size_Box.bind function and call apply_watermark().
# TODO-41 - Create rotation_var = IntVar() and rotation_var.set(0) after window creation to set default rotation 0
#  degrees.
# TODO-42 - Add rotation_var, degrees from -180 to 360 with orientation as horizontal. Call apply_watermark() command
#  to apply rotation to watermark.
# TODO-43 - Add Save_Image_Button. Call save_image command when clicked.
# TODO-44 - Add global variables img, tk_img, temp_img. Add warning messagebox if user tries to save image without
#  uploading image or applying a watermark.
# TODO-45 - Add dialogbox to save file with the desired extension. Show message when image is saved.
# TODO-46 - Add canvas.bind("<Button-1>", start_drag). Inside start_drag function store the difference between the
#  center of the watermark and the mouse position. Assign dragging = True.
# TODO-47 - Add canvas.bind("<B1-Motion>", drag_watermark) for dragging watermark on the image. Check if dragging is
#  True calculate new_x and new_y for the watermark so it stays under the cursor. Update the watermark's position as
#  the mouse is moved. Call apply_watermark().
# TODO-48 - Add canvas.bind("<ButtonRelease-1>", stop_drag) to stop dragging. Assign dragging = False. These type of
#  functions tells tkinter that when this event happens on the canvas, call this function.”
# TODO-49 - Create apply_watermark() function to apply watermark on image with the final changes. Add global variables
#  global tk_img, image_on_canvas, img, Text_Box, font_combobox, image_loaded, font_color, font_size_var, watermark_x,
#  watermark_y, temp_img inside this function.
# TODO-50 - Display a warning message if user inserts text without uploading an image.
# TODO-51 - Convert the image to RGBA to allow transparency.
# TODO-52 - Get the data from text box. If text is present then get all files for font using font_combobox.
# TODO-53 - Get font size entered by user from font_size_var. If no value is found then keep default font size as 40.
# TODO-54 - Using ImageFont add font_path and font size selected by user and store it in font variable.
# TODO-55 - Create dummy_img with image_mode=RGB, size=1px x 1px and color (0,0,0,0) for
#  (R,G,B,Transparency).
# TODO-56 - Draw a textbox at (0,0) position with given text and font. Measure text size, text_width and text_height.
#  left, top → where the text starts. right, bottom → where the text ends.
# TODO-57 - Create a transparent tight layer for text using same mode as dummy_img except add image size as
#  (text_w, text_h).
# TODO-58 - Draw text on the image with draw.text(). Add fill=font_color + "FF". "FF" is the alpha in hex
#  (255 in decimal → fully opaque). So fill=font_color + "FF" becomes "#FF0000FF" → fully opaque red in RGBA.
# TODO-59 - Apply rotation only to text. Obtain rotation from user. Check if angle is greater then 0, add text layer
#  with rotate function by adding angle,expand=True (so rotated text fits without cropping) and resample=Image.BICUBIC
#  for smooth rotation.
# TODO-60 - Calculate x and y co-ordinates which are watermark's center. Dividing width & height by 2 gives half the
#  size of the text image. This is used to adjust the placement so the text is centered at (watermark_x, watermark_y).
# TODO-61 - x = int(watermark_x - text_layer.width // 2). Moves the text’s top-left corner leftwards by half the text’s
#  width. That way, the center of the text will align with watermark_x.
# TODO-62 - Pastes the watermark (text_layer) onto temp_img at position (x, y) (the corrected top-left corner).
#  The third argument text_layer is used as a mask, which preserves transparency in the text image (so only the letters
#  show up, not the background).
# TODO-63 - temp_img is still in RGBA mode (has an alpha channel). Tkinter’s PhotoImage or most image formats require
#  RGB (no alpha channel). convert("RGB") → removes the alpha channel so the image is compatible for display or saving.
# TODO-64 - Create tk_img and display it on canvas.




from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont
import customtkinter as ctk
import os


canvas = None
image_on_canvas = None
tk_img = None
filename = None
img = None
font_combobox = None
Text_Box = None
image_loaded = False  # global flag
temp_img = None
font_color = "#000000"
watermark_x = 250
watermark_y = 250

# Dragging globals
dragging = False
offset_x = 0
offset_y = 0


def default_image():
    global canvas, image_on_canvas, tk_img, img, image_loaded

    img = Image.new("RGB", (500, 500), color=(200, 200, 200))
    draw = ImageDraw.Draw(img)
    draw.text((img.width//2, img.height//2), "No Image Loaded", fill=(50, 50, 50))

    tk_img = ImageTk.PhotoImage(img)

    image_loaded = False  # still no real image uploaded

    if image_on_canvas is None:
        image_on_canvas = canvas.create_image(50, 50, anchor="nw", image=tk_img)
    else:
        canvas.itemconfig(image_on_canvas, image=tk_img)


def show_uploaded_image(image_input):
    global canvas, image_on_canvas, tk_img, img, image_loaded

    # --- Show uploaded image only ---
    img = Image.open(image_input)
    img = img.resize((500, 500))
    tk_img = ImageTk.PhotoImage(img)

    image_loaded = True

    # Draw uploaded image on top
    if image_on_canvas is None:
        image_on_canvas = canvas.create_image(50, 50, anchor="nw", image=tk_img)
    else:
        canvas.itemconfig(image_on_canvas, image=tk_img)


def open_image():

    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("All files", "*.*"),
                   ("JPG files", "*.jpg;*.jpeg"),
                   ("PNG Files", "*.png"))
    )

    if not filename:
        print("No file selected!")
        return

    print("Opening file:", filename)

    show_uploaded_image(filename)


def apply_watermark(event=None):

    global tk_img, image_on_canvas, img, Text_Box, font_combobox, image_loaded, font_color, font_size_var, watermark_x, \
        watermark_y, temp_img

    if not image_loaded:
        messagebox.showwarning("No Image", "Please upload an image first!")
        return

    # Use RGBA to allow transparency
    temp_img = img.copy().convert("RGBA")


    text = Text_Box.get("1.0", END).strip()
    if text:
        font_file = font_combobox.get()
        font_path = os.path.join("fonts", font_file)

        # Get font size
        try:
            font_size = int(font_size_var.get())
        except ValueError:
            font_size = 40

        try:
            font = ImageFont.truetype(font_path, font_size)
        except:
            font = ImageFont.load_default()

        # Step - 1: Measure Text size
        dummy_img = Image.new("RGB", (1, 1), color=(0, 0, 0, 0))
        dummy_draw = ImageDraw.Draw(dummy_img)

        left, top, right, bottom = dummy_draw.textbbox((0, 0), text, font=font)

        text_w = right - left
        text_h = bottom - top


        # Step - 2: Create a transparent tight layer for the text
        text_layer = Image.new("RGBA", (text_w, text_h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer)
        # font_color is likely a hex string, e.g., "#FF0000" for red
        # "FF" is the alpha in hex (255 in decimal → fully opaque)
        # So fill=font_color + "FF" becomes "#FF0000FF" → fully opaque red in RGBA

        draw.text((-left, -top), text, font=font, fill=font_color + "FF")


        # Step - 3: Apply Rotation only to text
        # Rotates only the text layer by the user-selected angle.
        # expand=True ensures the rotated text fits completely without cropping.
        # BICUBIC gives smooth rotation.
        angle = rotation_var.get()
        if angle != 0:
            text_layer = text_layer.rotate(angle, expand=True, resample=Image.BICUBIC)


        # --- Step - 4: Paste at correct position ---
        x = int(watermark_x - text_layer.width // 2)
        y = int(watermark_y - text_layer.height // 2)

        temp_img.paste(text_layer, (x, y), text_layer)

        # temp_img = temp_img.convert("RGB")
        # temp_img is still in RGBA mode (has an alpha channel)
        # Tkinter’s PhotoImage or most image formats require RGB (no alpha channel)
        # convert("RGB") → removes the alpha channel so the image is compatible for display or saving

        # Effect:
        # Image can now be shown on the Tkinter canvas
        # Original background is preserved
        # Watermark text stays visible

        # Summary
        # convert("RGB") → make the image compatible with Tkinter display

        temp_img = temp_img.convert("RGB")  # back to RGB


    tk_img = ImageTk.PhotoImage(temp_img)
    if image_on_canvas is None:
        image_on_canvas = canvas.create_image(0, 0, anchor="nw", image=tk_img)
    else:
        canvas.itemconfig(image_on_canvas, image=tk_img)


def is_dark(rgb):
    """Check brightness of color"""
    r, g, b = rgb
    brightness = (r*299 + g*587 + b*114) / 1000  # luminance formula
    return brightness < 128


def pick_color():
    global font_color, Color_Box
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:
        font_color = color[1]

        fg_color = "white" if is_dark(color[0]) else "black"

        Color_Box.config(bg=font_color, text=font_color, fg=fg_color)

        apply_watermark()


def only_numbers(P):
    """Allow only digits in Entry"""
    return P.isdigit() or P == ""


def start_drag(event):

    # Purpose: Initializes the drag when you press the mouse button on the canvas.
    # dragging = True → marks that the watermark is now being dragged.
    # event.x and event.y → the position of the mouse click on the canvas.
    # offset_x and offset_y → store the difference between the center of the watermark and the mouse position, so the
    # watermark doesn’t jump when you start dragging.

    global dragging, offset_x, offset_y
    dragging = True
    offset_x = watermark_x - event.x
    offset_y = watermark_y - event.y


def drag_watermark(event):

    # Purpose: Updates the watermark’s position as you move the mouse.
    # event.x + offset_x → calculates new x for the watermark so it stays under the cursor.
    # apply_watermark() → redraws the image with the watermark at the new position.
    # Only works while dragging (if dragging:).

    global watermark_x, watermark_y
    if dragging:
        watermark_x = event.x + offset_x
        watermark_y = event.y + offset_y
        apply_watermark()


def stop_drag(event):

    # Purpose: Stops dragging when you release the mouse button.
    # dragging = False → prevents further movement until you click again.

    global dragging
    dragging = False


def save_image():
    global img, tk_img, temp_img
    if temp_img is None:
        messagebox.showwarning("No Image", "Please apply a watermark first!")
        return

    # Ask user where to save
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")]
    )

    if file_path:
        # Save the currently displayed image
        temp_img.save(file_path)
        messagebox.showinfo("Saved", f"Image saved to {file_path}")



def Watermarking_Window():

    global Add_File_Button, Welcome_Label, Click_Here_Label, Watermarking_Button, background_label, background_label_2,\
        tk_img, canvas, bg_img, filename, Text_Box, font_combobox, font_color, Color_Box, font_size_var

    # Destroy welcome screen items
    if Welcome_Label:
        Welcome_Label.destroy()
    if Click_Here_Label:
        Click_Here_Label.destroy()
    if Watermarking_Button:
        Watermarking_Button.destroy()
    if background_label:
        background_label.destroy()

    # Resize window for image view
    window.geometry("900x600")

    # Show Add Files page background
    background_label_2 = Label(window, image=bg_img)
    background_label_2.place(relwidth=1, relheight=1)

    # Create canvas if not exists
    if not canvas:
        canvas = Canvas(window, width=1000, height=600, highlightthickness=0, bd=0)
        canvas.place(x=50, y=50)

        default_image()

        Select_File_Button = Button(window, width=30, text="Select File", font=("Arial", 14), command=open_image)
        canvas.create_window(800, 100, anchor="center", window=Select_File_Button)

        Text_Label = Label(window, width=10, text="Text", font=("Arial", 14), pady=5)
        canvas.create_window(630, 200, anchor="center", window=Text_Label)

        Text_Box = Text(window, width=15, height=2, font=("Arial", 10))
        canvas.create_window(850, 200, anchor="center", window=Text_Box)
        # To show text on image when typed in text box.
        Text_Box.bind("<KeyRelease>", apply_watermark)

        Font_Label = Label(window, width=10, text="Font", font=("Arial", 14), pady=5)
        canvas.create_window(630, 250, anchor="center", window=Font_Label)

        font_files = [f for f in os.listdir("fonts") if f.endswith(".ttf")]
        font_combobox = StringVar()
        font_combobox.set(font_files[0] if font_files else "")
        font_menu = OptionMenu(window, font_combobox, *font_files, command=lambda x: apply_watermark())
        font_menu.place(x=843, y=285)

        Color_Label = Label(window, width=10, text="Color", font=("Arial", 14), pady=5)
        canvas.create_window(630, 300, anchor="center", window=Color_Label)

        Color_Box = Button(window, text=font_color, width=12, height=1, font=("Arial", 10), command=pick_color,
                           bg="black", fg="white", relief="raised")
        canvas.create_window(850, 300, anchor="center", window=Color_Box)

        Font_Size_Label = Label(window, width=10, text="Font Size", font=("Arial", 14), pady=5)
        canvas.create_window(630, 350, anchor="center", window=Font_Size_Label)

        vcmd = (window.register(only_numbers), "%P")
        Font_Size_Box = Entry(window, textvariable=font_size_var, width=15, font=("Arial", 10), validate="key",
                              validatecommand=vcmd)
        canvas.create_window(850, 350, anchor="center", window=Font_Size_Box)
        # To show change in font size on image when typed in entry box.
        Font_Size_Box.bind("<KeyRelease>", apply_watermark)

        Rotation_Label = Label(window, width=10, text="Rotation", font=("Arial", 14), pady=5)
        canvas.create_window(630, 425, anchor="center", window=Rotation_Label)

        # lambda x: apply_watermark() → This creates an anonymous function that calls apply_watermark() only when the
        # slider value changes.
        Rotation_Slider = Scale(window, variable=rotation_var, from_=-180, to=360, orient="horizontal", length=200,
                                font=("Arial", 10), label="Rotation (°)", command=lambda x: apply_watermark())
        canvas.create_window(850, 410, anchor="center", window=Rotation_Slider)

        Save_Image_Button = Button(window, width=30, text="Save Image", font=("Arial", 14), command=save_image)
        canvas.create_window(800, 500, anchor="center", window=Save_Image_Button)


        # --- Drag-and-drop ---
        canvas.bind("<Button-1>", start_drag)
        canvas.bind("<B1-Motion>", drag_watermark)
        canvas.bind("<ButtonRelease-1>", stop_drag)



# ---------------- MAIN WINDOW ----------------

window = ctk.CTk()
window.title("Watermarking App")
window.geometry("400x400")

font_size_var = StringVar(value="40")

rotation_var = IntVar()
rotation_var.set(0)  # default rotation 0 degrees

# Background for welcome page
bg_img = PhotoImage(file="background.png")

background_label = Label(window, image=bg_img)
background_label.place(relwidth=1, relheight=1)

# Welcome Label
Welcome_Label = ctk.CTkLabel(
    master=window,
    text="Welcome to Watermarking App",
    fg_color="#213448",   # background color
    text_color="white",
    corner_radius=20,     # makes it rounded
    font=("Arial", 15)
)
Welcome_Label.place(relx=0.5, rely=0.1, anchor="center")

# Watermarking button
Watermarking_Button = ctk.CTkButton(
    master=window,
    text="Watermark Photos",
    fg_color="#547792",   # background color
    text_color="white",
    corner_radius=20,     # makes it rounded
    width=200,
    height=50,
    command=Watermarking_Window
)
Watermarking_Button.pack(pady=(200, 5))

# Click here label
Click_Here_Label = ctk.CTkLabel(
    master=window,
    text="Click Above",
    fg_color="#94B4C1",   # background color
    text_color="white",
    corner_radius=20,     # makes it rounded
    font=("Arial", 10)
)
Click_Here_Label.pack(pady=(0, 20))



window.mainloop()