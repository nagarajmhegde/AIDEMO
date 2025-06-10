from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://your-test-site.com/register")

    
    driver.find_element(By.NAME, "name").send_keys("Test User")
    
    driver.find_element(By.NAME, "email").send_keys("test@example.com")
    
    driver.find_element(By.NAME, "password").send_keys("Test@123")
    

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    assert "Welcome" in driver.page_source
    print("✅ Test Passed")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()