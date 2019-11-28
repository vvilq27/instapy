from instapyModules.instapyy import InstaPy
from selenium import webdriver
# # from sys import platform
# from .settings import Settings


insta_username = 'arasssu'
insta_password = 'p0p3k12345'

session = InstaPy(username=insta_username,
                  password=insta_password)

session.login()
session.like_by_tags(["warsawgirl"], amount=3, skip_top_posts=True)
# session.like_by_tags(["warsawgirl", "polskadziewczyna", "tatry", "motocykl"], amount=10)
# ses = webdriver.Chrome(executable_path=r'C:/PYTHON37/Lib/site-packages/chromedriver78/chromedriver.exe')

# ses.get("http:instagram.com")