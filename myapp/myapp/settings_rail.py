from myapp.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')