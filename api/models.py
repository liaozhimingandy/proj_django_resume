from django.db import models


# Create your models here.
class Hello:
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
