
# main.py file
# TODO-1 - Import Flask utilities (Flask, render_template, request, redirect, url_for) for web app routing and form
#  handling.
# TODO-2 - Import Selenium modules: webdriver (browser control), By (locators), Service (driver setup), WebDriverWait
#  and expected_conditions (dynamic waits).
# TODO-3 - Import ChromeDriverManager to auto-install and manage ChromeDriver.
# TODO-4 - Import smtplib for sending email alerts. Import os and dotenv.
# TODO-5 - Create Flask app instance.
# TODO-6 - Create a file with extension ".env" and add EMAIL, APP_PASSWORD and CHROMEDRIVER_PATH in it. Load dotenv.
#  Using os obtain all three environment variables and store them to their respective variables.
# TODO-7 - Set DEBUG variable using app.debug to control browser closing. app.debug → returns True or False. DEBUG →
#  stores that value. If app is NOT in debug mode → close browser. If app is in debug mode → keep browser open. To
#  enable debug: app.run(debug=True).
# TODO-8 - Create send_email() function to notify when price drops.
# TODO-9 - Define email subject and body including product title, price, and URL.
# TODO-10 - Connect to Gmail SMTP server using TLS (smtp.gmail.com, port 587).
# TODO-11 - Login using email credentials and app password.
# TODO-12 - Send email to the recipient.
# TODO-13 - Return True if email is sent successfully.
# TODO-14 - Handle exceptions and return False if sending fails.
# TODO-15 - Create check_price() function with url and target_price parameters.
# TODO-16 - Configure Chrome options: detach mode, disable automation detection, set user-agent. With detach=True -
#  Script runs, Browser opens, Script ends and Browser stays open. User-agent is Your ID card i.e., I am a normal
#  browser (Chrome/Windows/etc.). disable automation detection is like removing the “BOT” sticker from your forehead.
# TODO-17 - Launch Chrome browser using webdriver and ChromeDriverManager.
# TODO-18 - Initialize WebDriverWait for handling dynamic elements. Wait for 10 secs.
# TODO-19 - Open the product URL.
# TODO-20 - Extract product title using ID "productTitle". Use wait function combined with presence_of_element_located()
#  function by identifying using "ID". Finally strip it.
# TODO-21 - Similarly Extract price parts using CLASS_NAME: whole (a-price-whole). Find fraction (a-price-fraction)
#  using driver.find_element() function.
# TODO-22 - Combine both prices and convert final price into float.
# TODO-23 - Compare current price with target_price.
# TODO-24 - If price is lower: call send_email() and return success message.
# TODO-25 - If price is higher: return "still high" message.
# TODO-26 - Handle exceptions and return error message.
# TODO-27 - Close browser using driver.quit() if not in DEBUG mode.
# TODO-28 - Create run_bot() function for automation. Pass product_url and target_price to it.
# TODO-29 - Configure Chrome options (maximize, anti-detection, user-agent).
# TODO-30 - Launch browser using webdriver. Install ChromeDriverManager and add options too. Wait for 10 secs and open
#  product url.
# TODO-31 - Use try, except and finally condition to extract product title and price. Use
#  EC.presence_of_element_located() function by CLASS_NAME for both.
# TODO-32 - Print debug logs for title and price.
# TODO-33 - Compare price with target_price.
# TODO-34 - If price drops: send email and return success message. If price is higher: return "still high" message.
# TODO-35 - Handle exceptions and return error message.
# TODO-36 - Close browser if not in DEBUG mode.
# TODO-37 - Create home route "/" with GET and POST methods.
# TODO-38 - Check if "prefill=1" in query parameters.
# TODO-39 - Extract url and price from request args.
# TODO-40 - Redirect to same route with "auto=1" to trigger bot execution. Pass url and price too.
# TODO-41 - Check if "auto=1" in query parameters.
# TODO-42 - Extract url and price.
# TODO-43 - Call run_bot() function and pass url and price to it.
# TODO-44 - Render index.html template with result, url, target_price, clear=False.
# TODO-45 - Handle POST request from form.
# TODO-46 - Get url and price from request.form.
# TODO-47 - Call run_bot() function and pass url and target_price to it.
# TODO-48 - Redirect to home with result.
# TODO-49 - Get result from query parameters.
# TODO-50 - Render index.html with result and clear=True.
# TODO-51 - Create "/auto" route.
# TODO-52 - Define default product URL and target price.
# TODO-53 - Redirect to home with prefill=1 to trigger automation flow. Also pass product_url, target_price and
#  clear=False.
# TODO-54 - Run Flask app in debug mode.
# TODO-55 - Disable reloader to prevent duplicate Selenium execution.

# index.html file
# TODO-56 - Create a folder named templates and add a html file. Name it index.html.
# TODO-57 - Set language as English, set charset="UTF-8", Title="Amazon Price Tracker". Add meta details in meta tag:
#  name="viewport" - It tells the browser how to control the page’s size and scaling on different devices (phones,
#  tablets, laptops) and content="width=device-width, initial-scale=1.0 - Sets the width of the webpage to match the
#  device’s screen width. Example: Mobile → ~360px, Tablet → ~768px, Desktop → wider. Sets the initial zoom level when
#  the page loads 1.0 = no zoom (normal size). Create a folder named static and add file named style.css. Add external
#  link for style.css.
# TODO-58 - Inside the body section add a div with class container. Add this class in style.css and add background,
#  padding, border-radius, width, box-shadow and text alignment.
# TODO-59 - Add <h1> tag inside the div with text "🛒 Price Tracker". Create class hi in style.css and add bottom margin
#  and text color.
# TODO-60 - Create a form below using <form> tag with method="POST". Inside this form add a <label> tag with text
#  "Product URL". Add an <input> tag with type="text", name="url", placeholder="Paste Amazon link..." and
#  value="{{ '' if clear else (request.form.url or url or '') }}". The if condition states that url stays empty if clear
#  flag is true else url will be requested from form or passed by variable/default url or if nothing satisfies then it
#  stays empty.
# TODO-61 - Similarly add another <label> tag with text "Target Price (₹)". Add an <input> tag with type="number",
#  name="price", placeholder="Enter target price" and value="{{ '' if clear else (request.form.price or target_price or
#  '') }}".
# TODO-62 - Create a class named input in style.css and add width, padding, top margin, bottom margin, border, font-size
#  and border-radius. Add input:focus and add border-color, outline: none; to change border color when focused.
# TODO-63 - Add a <button> tag with id="track-btn" and type="submit". Set its text as "Track Price". Add button in
#  style.css and add width, padding, background, text color, border, border-radius, font-size, cursor as pointer and
#  transition. Change background on hover.
# TODO-64 - Add if condition using jinja and check if result exists, if yes then add a div with class result. Add if
#  condition "{% if '🔥' in result %}success {% elif '❌' in result %}error {% else %}normal {% endif %}".
# TODO-65 - Create class result in style.css and add top margin, padding, border-radius and font-weight. Create class
#  success and add background color and text color. Create class normal and add background color and text color. Create
#  class error and add background color and text color.
# TODO-66 - End if loop, close div, close body and finally close html tag.
# TODO-67 - Add body in style.css and add margin:0, font-family, background, height, display as flex, justify content to
#  center and align items to center.



from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
import dotenv
import os

dotenv.load_dotenv()


app = Flask(__name__)

# -------- CONFIG --------
EMAIL = os.environ.get("EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")
DEBUG = app.debug

# -------- EMAIL --------
def send_email(title, price, url):
    try:
        subject = "Amazon Price Drop Alert!"
        body = f"{title}\n\nPrice: ₹{price}\n{url}"
        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(EMAIL, APP_PASSWORD)
            connection.sendmail(EMAIL, EMAIL, message.encode("utf-8"))
            return True

    except Exception as e:
        print("Email Error:", e)
        return False



# -------- AMAZON PRICE CHECK --------
def check_price(url, target_price):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    wait = WebDriverWait(driver, 10)

    driver.get(url)

    try:
        title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text.strip()

        price_whole = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))).text

        price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

        price = float(price_whole.replace(",", "") + "." + price_fraction)

        if price < target_price:
            email_status = send_email(title, price, url)

            if email_status:
                return f"🔥 Price dropped! ₹{price} | 📧 Email sent successfully!"
            else:
                return f"🔥 Price dropped! ₹{price} | ❌ Email failed!"
        else:
            return f"Price is ₹{price} (still high)"

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        if not DEBUG:
            driver.quit()



# -------- SELENIUM BOT (AUTO CLICK) --------
def run_bot(product_url, target_price):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    wait = WebDriverWait(driver, 10)

    driver.get(product_url)

    try:
        # 🔹 Get title
        title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text.strip()

        # 🔹 Get price
        price_whole = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))).text

        price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

        price = float(price_whole.replace(",", "") + "." + price_fraction)

        print("BOT TITLE:", title)
        print("BOT PRICE:", price)

        # 🔹 Compare
        if price < target_price:
            email_status = send_email(title, price, product_url)

            if email_status:
                return f"🔥 Price dropped! ₹{price} | 📧 Email sent successfully!"
            else:
                return f"🔥 Price dropped! ₹{price} | ❌ Email failed!"
        else:
            return f"Price is ₹{price} (still high)"

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        if not DEBUG:
            driver.quit()



# -------- ROUTES --------
@app.route("/", methods=["GET", "POST"])
def home():

    # 🔹 Step 1: Just fill form (no processing)
    if request.args.get("prefill") == "1":
        url = request.args.get("url")
        price = request.args.get("price", type=int)

        # 🔥 immediately redirect to processing
        return redirect(url_for(
            "home",
            url=url,
            price=price,
            auto="1"
        ))

    # 🔹 Step 2: Now run bot
    if request.args.get("auto") == "1":
        url = request.args.get("url")
        price = request.args.get("price", type=int)

        result = run_bot(url, price)

        return render_template(
            "index.html",
            result=result,
            url=url,
            target_price=price,
            clear=False
        )

    # Normal method
    if request.method == "POST":
        url = request.form["url"]
        target_price = int(request.form["price"])

        result = run_bot(url, target_price)
        return redirect(url_for("home", result=result))

    result = request.args.get("result")

    return render_template("index.html", result=result, clear=True)



# 🔥 AUTO ROUTE
@app.route("/auto")
def auto_run():
    product_url = "https://www.amazon.in/Reebok-Stride-Runner-Running-Shoes/dp/B09SHVCTZF"
    target_price = 50000

    return redirect(url_for("home", url=product_url, price=target_price, clear=False, prefill="1"))



# -------- RUN --------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)