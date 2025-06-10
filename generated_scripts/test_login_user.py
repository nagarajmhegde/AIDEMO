from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://your-test-site.com/login")

    
    driver.find_element(By.NAME, "username").send_keys("testuser")
    
    driver.find_element(By.NAME, "password").send_keys("Test@123")
    

    driver.find_element(By.NAME, "login").click()
    time.sleep(2)

    assert "Dashboard" in driver.page_source
    print("✅ Test Passed")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()