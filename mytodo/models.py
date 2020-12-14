from django.db import models

#ToDoのクラス
class Do(models.Model):
    do = models.CharField(max_length=300)

    def __str__(self):
        return self.do

#Didのクラス
class Did(models.Model):
    did = models.CharField(max_length=300)

    def __str__(self):
        return self.did
        
