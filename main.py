from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time

from gformsbot.section import section_handler
import answer

driver_path = ChromeDriverManager().install()
service = ChromeService(driver_path)

options = webdriver.ChromeOptions()
options.add_argument("--lang=en")
# options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://forms.gle/MkX1C5WE4R3qSh6F6')

ans = [answer.section_1, answer.section_2, answer.section_3, answer.section_4]

for a in ans:
    time.sleep(0.3)
    section = section_handler(driver)
    print(section)
    section.answer_questions(a)
    section.proceed()
    time.sleep(0.3)