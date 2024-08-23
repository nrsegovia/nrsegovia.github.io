AUTHOR = 'Nicolas Rodriguez-Segovia'
SITENAME = 'Nicolas Rodriguez-Segovia'
SITEURL = ""
THEME = "themes/cool-theme"
INDEX_SAVE_AS = 'index.html'

PATH = "content"

TIMEZONE = 'Australia/Canberra'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False
PAGE_ORDER_BY = 'date'
PAGE_EXCLUDES = []
STATIC_PATHS = ['images']
ARTICLE_PATHS = ['news']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TEMPLATE_PAGES = {'publications.html': 'publications.html',
                  'cv.html': 'cv.html',
                  'projects.html': 'projects.html'}