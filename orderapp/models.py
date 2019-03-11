from django.db import models
from django.utils import timezone
import datetime
from datetime import date

class Menu(models.Model):
    item = models.CharField(max_length=50)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.item
"""
    def vote_count(self):
        if self.request.user:
            menu = Menu.objects.all()
            userobj = UserObjects.object.all()
            for obj in userobj:
                if (userobj.like_status == True and userobj.date_liked == date.today):
                    menu.votes += 1
        return self.votes
"""

class UserObjects(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    like_status = models.BooleanField(default=False)
    date_liked = models.DateField(default= date.today)


"""
    def was_voted_recently(self):
        if self.last_voted <=  timezone.now() - datetime.timedelta(hours=5, minutes=59, seconds=59):
            self.votes =0

        #return self.votes
"""
