
# TODO-1 - Import required Selenium modules: webdriver for browser control, By for locating elements, WebDriverWait and
#  expected_conditions for dynamic waits.
# TODO-2 - Import os and time modules for file paths and delays.
# TODO-3 - Import exceptions like NoSuchElementException and TimeoutException to handle failures gracefully.
# TODO-4 - Define user credentials (email & password) and target website URL.
# TODO-5 - Create Chrome options object and configure browser behavior.
# TODO-6 - Enable "detach" option so browser stays open after script ends.
# TODO-7 - Create a persistent Chrome profile directory using os.getcwd() so login sessions and cookies can be reused.
# TODO-8 - Add user-data-dir argument to Chrome options for profile usage. Include double -- for command line argument
#  to Chrome. A directory named "chrome_profile" will be created.
# TODO-9 - Launch Chrome browser using webdriver with defined options.
# TODO-10 - Maximize browser window for better visibility.
# TODO-11 - Initialize WebDriverWait for handling dynamic elements. Wait for 2 seconds.
# TODO-12 - Navigate to the gym booking website using driver.get() function.
# TODO-13 - Create a retry() function to handle flaky network or element loading issues. Retry a function multiple times
#  before failing.
# TODO-14 - This function takes - func (function to execute), retries (max attempts), and description (for logging).
#  Start a loop that runs the function up to 'retries' times.
# TODO-15 - Print a message showing which function/action is being attempted along with the current attempt number.
# TODO-16 - Use a try block to execute the passed function (func). If the function executes successfully, return its
#  result immediately and stop further retries.
# TODO-17 - Catch TimeoutException to handle cases where Selenium elements are not found or page loading is slow.
# TODO-18 - Check if the current attempt is the last retry. If it's the final attempt and still failing, raise the
#  exception to stop execution and show the error.
# TODO-19 - If retries are still remaining, wait for a short delay (e.g., 1 second) before trying again to avoid rapid
#  repeated failures.
# TODO-20 - Continue retrying until success or all attempts are exhausted.
# TODO-21 - Create login() function: Click login button → enter email & password → submit form → wait for dashboard.
# TODO-22 - Wrap login() function inside retry() to ensure reliability.
# TODO-23 - Create book_class() function and pass booking_button in it. Click booking button and wait until its text
#  changes to "Booked".
# TODO-24 - Fetch all class cards using CSS selector.
# TODO-25 - Initialize counters for: booked classes, waitlisted classes, and already booked classes.
# TODO-26 - Loop through each class card and extract: day, time, class name, and booking button.
# TODO-27 - Filter classes: Only process Tuesday and Thursday classes at 6:00 PM.
# TODO-28 - Store class_name and day_title in class_info.
# TODO-29 - Check button text: If "Booked" → print 'already booked' with class_info and increment already_booked_count
#  by 1. Append class_info to processed_classes as Booked with class_info.
# TODO-30 - Check button text: If "Waitlisted" → print 'already on waitlist' with class_info and increment
#  already_booked_count by 1. Append class_info to processed_classes as Waitlisted with class_info.
# TODO-31 - Check button text: If "Book Class" → Call retry function by passing in book_class(button) function for
#  retry irterations. Print 'Successfully booked' with class_info and increment booked_count by 1. Append
#  class_info to processed_classes as New Booking with class_info. Add a delay of 0.5 secs.
# TODO-32 - Check button text: If "Join Waitlist" → Call retry function by passing in book_class(button) function for
#  retry irterations. Print 'Joined waitlist for' with class_info and increment waitlist_count by 1. Append class_info
#  to processed_classes as New Waitlist with class_info. Add a delay of 0.5 secs.
# TODO-33 - Maintain a list of processed classes for summary tracking.
# TODO-34 - Print booking summary counts (optional debug output).
# TODO-35 - Calculate total number of processed classes.
# TODO-36 - Create get_my_bookings() function: Navigate to "My Bookings" page and fetch all booking cards.
# TODO-37 - Wait until the "My Bookings" link is clickable using explicit wait. Click on the "My Bookings" link to
#  navigate to the bookings page.
# TODO-38 - Wait for the "My Bookings" page to fully load by checking for a unique element (e.g., page container with
#  specific ID).
# TODO-39 - Locate all booking cards using a CSS selector that matches elements with IDs containing 'card-'. Store all
#  found booking card elements in a list (all_cards).
# TODO-40 - Validate that booking cards were found: if the list is empty, assume the page did not load properly. Raise a
#  TimeoutException with a clear message if no cards are found, to fail gracefully.
# TODO-41 - Return the list of booking cards for further processing (verification).
# TODO-42 - Wrap get_my_bookings() inside retry() for reliability.
# TODO-43 - Loop through booking cards and extract: class name and timing details.
# TODO-44 - Verify only Tuesday/Thursday 6:00 PM classes. Count verified bookings. Add NoSuchElementException to handle
#  to handle exception for element does not exist.
# TODO-45 - Print Expected and Found results.
# TODO-46 - Compare expected vs actual bookings.
# TODO-47 - Print final result: SUCCESS if all bookings match, otherwise show mismatch count.



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

# Add your credentials at the top of your script
ACCOUNT_EMAIL = "Your Email"  # The email you registered with
ACCOUNT_PASSWORD = "Your Password"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"


chrome_options = webdriver.ChromeOptions()

# Keep the browser open if the script finishes or crashes.
# If True, you need to "manually quit" chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)

# Create chrome_profile directory which Selenuim will use every time.
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# Set Chrome Options. Include double -- for command line argument to Chrome.
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Launch the browser with profile.
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 2)

# Navigate to site
driver.get(GYM_URL)

# ----------------  Step 9: Network Resilience ----------------
# Simple retry wrapper
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)


# Function to perform entire login process with retry
def login():
    # ----------------  Step 2 - Automated Login ----------------
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    time.sleep(2)
    login_button.click()

    # Enter email and password
    email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-input")))
    email_input.clear()

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()

    email_input.send_keys(ACCOUNT_EMAIL)
    time.sleep(1)
    password_input.send_keys(ACCOUNT_PASSWORD)
    time.sleep(1)

    # Click Login submit button
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
    submit_button.click()
    time.sleep(1)

    # Wait for schedule page to load
    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
    time.sleep(1)


# Function to book a class process that checks if the button text changed with retry
def book_class(booking_button):
    booking_button.click()

    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")


# Put the entire login flow into the retry-wrapper
retry(login, description="login")


# ----------------  Step 3 - Class Booking: Book Upcoming Tuesday Class  ----------------

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

# Counters for booked classes for the booking summary
booked_count = 0
waitlist_count = 0
already_booked_count = 0

# ----------------  Step 6: Book EVERY Tuesday AND Thursday 6pm class ----------------
# ----------------         and print a detailed class summary         ----------------
processed_classes = []


for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday OR Thursday
    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            # Track the class details
            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"✓ Already booked: {class_info}")
                already_booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                # Use retry for entire booking action
                retry(lambda: book_class(button), description="Booking")

                print(f"✓ Successfully booked: {class_info}")
                booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[New Booking] {class_info}")
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                # Use retry for entire waitlist action
                retry(lambda: book_class(button), description="Waitlisting")

                print(f"✓ Joined waitlist for: {class_info}")
                waitlist_count += 1
                # Add detailed class info
                processed_classes.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5)

# print("\n--- BOOKING SUMMARY ---")
# print(f"New bookings: {booked_count}")
# print(f"New waitlist entries: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
# print(f"Total Tuesday & Thursday 6pm classes: {booked_count + waitlist_count + already_booked_count}")
#
# # Print detailed class list
# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f"  • {class_detail}")

# ----------------  Step 7: Verify Class Bookings on My Bookings Page ----------------
total_booked = booked_count + already_booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Function to navigate to my bookings with retry
def get_my_bookings():
    # Navigate to My Bookings Page
    my_bookings_link = wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings_link.click()

    # Wait for My Bookings Page to load
    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    # Ensure we actually found cards - if empty, the page might not have loaded
    if not all_cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return all_cards

# Put navigation to the Bookings page and get cards in the retry wrapper
all_cards = retry(get_my_bookings, description="Get my bookings")

verified_count = 0

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")