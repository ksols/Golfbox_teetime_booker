from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os


class Booker:
    def __init__(self, date):
        self.service = Service(
            executable_path="./chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=self.service)
        try:
            self.driver.get("https://golfbox.golf/#/")
            time.sleep(1.5)
            username_field = self.driver.find_element(By.ID, "gbLoginUsername")
            password_field = self.driver.find_element(By.ID, "gbLoginPassword")
            username_field.send_keys(os.getenv("GOLFBOX_USERNAME"))
            password_field.send_keys(os.getenv("GOLFBOX_PASSWORD"))
            signin_button = self.driver.find_element(
                By.CLASS_NAME, "text")
            signin_button.click()
            time.sleep(2)
        except Exception as e:
            print("Error in __init__: ", e)
            quit()
        # print(self.check_if_available(date))
        self.check_if_available(date)

    def book(self, date):
        try:
            self.driver.get(
                "https://www.golfbox.no/site/my_golfbox/ressources/booking/grid.asp?SelectedDate=" + date + "&Ressource_GUID={6F54A56D-A4BE-4C15-93FA-55D614D6AD4B}&Club_GUID={3E0C1D24-61FC-4528-AF75-55B35582049B}")
            time.sleep(3)
            # Change to desired time slot id value
            time_slot = self.driver.find_element(By.ID, "row1col12")
            print()
            print("Div element of interest:",
                  time_slot.get_attribute("onclick"))
            onclick_attribute_values = time_slot.get_attribute("onclick")
            date_time_string_to_use = onclick_attribute_values.split("'")[1]
            print("date_time_string_to_use", date_time_string_to_use)

            booking_url = "https://www.golfbox.no/site/my_golfbox/ressources/booking/window.asp?Ressource_GUID={6F54A56D-A4BE-4C15-93FA-55D614D6AD4B}&Booking_Start=" + \
                date_time_string_to_use + \
                "&club_GUID={3E0C1D24-61FC-4528-AF75-55B35582049B}"

            print("--------- Step 0 ---------")
            self.driver.get(booking_url)
            print("--------- Step 1 ---------")
            time.sleep(2)
            submit_button = self.driver.find_element(By.ID, "cmdSubmit")
            button_clickable = submit_button.find_element(By.TAG_NAME, "div")
            time.sleep(2)
            print("--------- Step 2 ---------")
            submit_button.click()
            print("--------- Step 3 ---------")
            print("Sleeper")
            time.sleep(20)
            print(f"Booket successfully: {date}")
        except Exception as e:
            print("Error in book method: ", e)
            quit()

    # Checks if date is available, returns True if it is

    def check_if_available(self, date):
        try:
            self.driver.get(
                "https://www.golfbox.no/site/my_golfbox/ressources/booking/grid.asp?SelectedDate=" + date + "&Ressource_GUID={6F54A56D-A4BE-4C15-93FA-55D614D6AD4B}&Club_GUID={3E0C1D24-61FC-4528-AF75-55B35582049B}")
            time.sleep(4)
            time_slot = self.driver.find_element(By.ID, "row1col12")
            # Find the child element with classname "item"
            item_element = time_slot.find_element(By.CLASS_NAME, "item")
            # Check if the item_element has children
            children = item_element.find_elements(By.XPATH, "./*")
            if children:
                print("Not available tee time...")
                # Someone has this tee time
                return False
            else:
                print("Selected tee time available.")
                # It is available
                self.book(date)
                return True
            time.sleep(5)
            self.driver.quit()
        except Exception as e:
            print("Error: ", e)
            quit()


if __name__ == "__main__":
    booker = Booker("20240623T000000")

# row1col12 18:15
# row2col12 18:24
