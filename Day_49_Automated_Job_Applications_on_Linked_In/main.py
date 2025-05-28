# TODO-1 - Import webdriver,By and Keys from selenium class

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

USERNAME = "Your Mail Id"
PASSWORD = "Your Password"
MOBILE_NUMBER = "Your Mobile Number"

# TODO-12 - Create a function to abort the process


def abort_application():
    try:
        time.sleep(2)
        close_button = driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Dismiss']")
        close_button.click()
        time.sleep(2)
        discard_button = driver.find_element(By.XPATH, "//button[@data-control-name='discard_application_confirm_btn']")
        discard_button.click()
        print("Application aborted.")
    except Exception as e:
        print("Error during abort:", e)


# TODO-2 - Keep chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# TODO-3 - Open the website

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4228121914&distance=25&f_AL=true&geoId=102713980&"
           "keywords=preschool%20teacher&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

time.sleep(2)

# TODO-4 - Click on Sign In Button

# Close login popup if appears
try:
    X_Button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]//button')
    X_Button.click()
except:
    pass

# Sign in
Sign_In_Button = driver.find_element(By.LINK_TEXT, value="Sign in")
Sign_In_Button.click()

time.sleep(2)

# TODO-5 - Store Username and Password as Global Variables at the top of the code and enter them

Username = driver.find_element(By.NAME, value="session_key")
Username.send_keys(USERNAME)
Password = driver.find_element(By.NAME, value="session_password")
Password.send_keys(PASSWORD)

# TODO-6 - Click on Final Sign In Button

Final_Sign_Button = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
Final_Sign_Button.click()

# CAPTCHA
input("Solve CAPTCHA and press Enter...")

time.sleep(5)

# TODO-14 - List all the jobs which are clickable and exceptions are added to move onto next application

all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    try:
        print("\n Opening job listing...")
        listing.click()
        time.sleep(3)

        # TODO-7 - Check applications which have "Easy Apply" written on them. Click only those.

        apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        if "Easy Apply" in apply_button.text:
            apply_button.click()
            print("Easy Apply clicked")
            time.sleep(2)

            # TODO-8 - Enter Mobile Number with exception

            try:
                Enter_Mobile_Number = driver.find_element(By.CSS_SELECTOR, value="input[id*='phoneNumber-national"
                                                                                 "Number']")
                if Enter_Mobile_Number.get_attribute("value") == "":
                    Enter_Mobile_Number.send_keys(MOBILE_NUMBER)
            except NoSuchElementException:
                print("Mobile number not required or field not found")

            # TODO-9 - Click on Next Button with exception.

            try:
                Next_Button = driver.find_element(By.CSS_SELECTOR, value=".display-flex.justify-flex-end.ph5.pv4 button")
                if "Next" in Next_Button.text:
                    Next_Button.click()
                    time.sleep(2)
            except NoSuchElementException:
                print("No Next button found")

            # TODO-10 - Click on Review Button, identify the * fields. Since we don't have to fill in complex
            #  application so we will abort the application. If no * fields are found then we will submit the
            #  application. Add exceptions to switch to next applications.

            try:
                Review_Buttons = driver.find_elements(By.CSS_SELECTOR, value=".display-flex.justify-flex-end.ph5.pv4 "
                                                                             "button")
                if len(Review_Buttons) > 1:
                    try:
                        label = driver.find_element(By.XPATH, "//label[contains(text(), 'ASP.NET MVC')]")
                        input_id = label.get_attribute("for")
                        input_field = driver.find_element(By.ID, input_id)

                        is_required_attr = input_field.get_attribute("required") is not None
                        is_aria_required = input_field.get_attribute("aria-required") == "true"

                        if is_required_attr or is_aria_required:
                            print("Field is required, skipping...")
                            abort_application()
                            continue
                        else:
                            print("Clicking Review button...")
                            Review_Buttons[1].click()
                            time.sleep(2)
                    except NoSuchElementException:
                        print("No specific required field found. Proceeding...")
                        Review_Buttons[1].click()
                else:
                    # TODO-11 - Click on Submit Button

                    Submit_Button = driver.find_element(By.CSS_SELECTOR, value="footer .display-flex.justify-flex-end."
                                                                               "ph5.pv4 button")
                    if Submit_Button.get_attribute("data-control-name") == "continue_unify":
                        print("Complex multi-step form, skipping...")
                        abort_application()
                        continue
                    else:
                        print("Submitting application...")
                        Submit_Button.click()
                        time.sleep(2)

            except Exception as e:
                print("Error on review/submit:", e)
                abort_application()
        else:
            print("Not Easy Apply. Skipping...")
            continue
    # TODO-13 - Add Final exception and abort application when nothing works out
    except (NoSuchElementException, ElementClickInterceptedException) as e:
        print("Error:", e)
        abort_application()
        continue

print("\n All listings processed.")

driver.quit()