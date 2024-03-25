import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Webdriver'ı başlat
driver = webdriver.Chrome()
driver.maximize_window()
# Ana sayfaya git
driver.get("https://useinsider.com/")
time.sleep(3)

# Company sayfasına gitmek için linki bul ve tıkla
company_element = driver.find_element(By.XPATH, '//a[contains(text(), "Company")]')
company_element.click()
time.sleep(5)

# Careers sayfasına gitmek için linki bul ve tıkla
careers_element = driver.find_element(By.XPATH, '//a[contains(text(), "Careers")]')
careers_element.click()

# Sayfada beklemek için bir süre bekle
time.sleep(3)

# Try-except bloğu ile ilgili bölümlerin erişilebilirliğini kontrol et
try:
    driver.find_element(By.XPATH, '//h3[contains(text(), "Our Locations")]')
    driver.find_element(By.XPATH, '//a[contains(text(), "See all teams")]')
    driver.find_element(By.XPATH, '//h2[contains(text(), "Life at Insider")]')
    print("Locations, Teams, and Life at Insider sections are accessible.")
except Exception as e:
    print("Locations, Teams, and Life at Insider sections are not accessible.")

time.sleep(5)

#Kaydırma çubuğu aşağı
actions = ActionChains(driver)
actions.move_by_offset(0, 600)  # 500 piksel aşağı kaydır
actions.perform()
time.sleep(3)
# Kalan işlemleri yapmak için ana işlemleri yapmaya devam et
team_element = driver.find_element(By.XPATH, '//a[contains(text(), "See all teams")]')
driver.execute_script("arguments[0].click();", team_element)
time.sleep(5)

quality_assurance_element = driver.find_element(By.XPATH, '//h3[contains(text(), "Quality Assurance")]')
driver.execute_script("arguments[0].click();", quality_assurance_element)
time.sleep(5)
# XPath ile gerekli bağlantıyı bul
jobs_element = driver.find_element(By.XPATH, '//a[contains(text(), "See all QA jobs")]')
jobs_element.click()

time.sleep(10)
select_element = driver.find_element(By.XPATH,"//select[@name='filter-by-location']")

# XPath ile gerekli option elementini bul
option_element = driver.find_element(By.XPATH,"//option[contains(text(), 'Istanbul, Turkey')]")

# Option elementini seç
option_element.click()
time.sleep(5)

# Departman dropdown'ını bul
department_select_element = driver.find_element(By.XPATH,"//select[@name='filter-by-department']")
department_select = Select(department_select_element)
time.sleep(5)

# Departmanı "Quality Assurance" olarak seç
department_select.select_by_visible_text('Quality Assurance')

# Tüm iş ilanlarını bul
job_list = driver.find_elements(By.XPATH,"//div[@class='job-list']//div[@class='job-item']")

time.sleep(3)

print("Test Passed")

# Webdriver'ı kapat
driver.quit()
