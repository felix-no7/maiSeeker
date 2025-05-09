from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import json

maimaiDX = "https://maimaidx-eng.com/maimai-mobile/home/ratingTargetMusic/"
sega = "https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=maimaidxex&redirect_url=https://maimaidx-eng.com/maimai-mobile/&back_url=https://maimai.sega.com/"
songData = ""

SEGA_ID = "felixno7"
PASSWORD = "2xdugajr"

driver = webdriver.Chrome()
driver.get(sega)

driver.find_element(By.CLASS_NAME,"c-button--openid--segaId").click()
time.sleep(1)

driver.find_element(By.ID,"sid").send_keys(SEGA_ID)
driver.find_element(By.ID,"password").send_keys(PASSWORD)
driver.find_element(By.ID,"btnSubmit").click()
time.sleep(1)

driver.get(maimaiDX)
time.sleep(0.5)

html = BeautifulSoup(driver.page_source)

level = html.select("div.music_lv_block.f_r.t_c.f_14")
name = html.select("div.music_name_block.t_l.f_13.break")
score = html.select("div.music_score_block.w_120.t_r.f_r.f_12")

r15 = []
b35 = []
for i in range(50):
    if i<=14:
        r15.append((level[i].text,name[i].text,score[i].text.replace("%","")))
    else:
        b35.append((level[i].text,name[i].text,score[i].text.replace("%","")))

print("\nr15:")
for info in r15:
    print(info)
print("\nb35:")
for info in b35:
    print(info)

with open("lv.json","rb") as f:
    lv = json.load(f)

print(lv["snooze"])
print(lv["snooze"]["13+"])

time.sleep(1)

