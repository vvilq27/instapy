from instapyModules.instapyy import InstaPy
from selenium import webdriver
# # from sys import platform
# from .settings import Settings



session = InstaPy(username=insta_username,
                  password=insta_password)

session.set_dont_include(["dziecko", "hotel", "hotelspa", "spa", "zabiegi", "butik", "fashionblogger", "mama", "nails", "studio", "kosmetyki", "krem", "fryzjer", "wellhair", "moda", "paznokcie", "salon", "sklep"])
session.set_relationship_bounds(enabled = True, min_posts=10, min_followers = 100, max_followers = 1500, min_following=300)
session.set_do_follow(enabled=True, percentage=40)

session.login()
session.like_by_tags([ "gory", "podroze", "warsawgirl", "polskadziewczyna"], amount=25, skip_top_posts=True)

# session.follow_by_tags(['warsawgirl'], amount= 30)
# session.follow_by_tags(['kolarstwo'], amount=5)
# session.follow_by_tags(['wspinaczka'], amount=5)

# session.like_by_tags(["warsawgirl", "polskadziewczyna", "tatry", "motocykl"], amount=10)
# ses = webdriver.Chrome(executable_path=r'C:/PYTHON37/Lib/site-packages/chromedriver78/chromedriver.exe')

# ses.get("http:instagram.com")