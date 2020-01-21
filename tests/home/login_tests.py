from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox(executable_path="C:\\Users\\CurtA\\selenium\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test@email.com")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("abcabc")

        loginButton = driver.find_element(By.NAME, "commit")
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, "//div[@id='navbar']//img[@class='gravatar']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

ff = LoginTests()
ff.test_validLogin()