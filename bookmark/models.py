from django.db import models

class userInfo(models.Model) :
    user_name = models.CharField(max_length= 12)

    def __str__(self):
        return self.user_name