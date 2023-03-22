from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sql",
#         "NAME": "Test",
#         "HOST": "localhost",
#         "USER": "root",
#         "PASSWORD": "root",
#     }
# }
