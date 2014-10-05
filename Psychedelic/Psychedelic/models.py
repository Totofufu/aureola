from django.db import models

class Suportee(models.Model):
  name = models.CharField(max_length = 100, blank = True, default = '')
  age = models.IntegerField(default = 0)
  birthday = models.IntegerField(default = 0)
  location = models.CharField(max_length = 100, blank = True, default = '')
  autobiography = models.TextField(blank = True, default = '')
  contactAt = models.TextField(blank = True, default = '')
  findMeAt = models.TextField(blank = True, default = '')
  supporters = models.ManyToManyField('Supporter', related_name = 'supportees')

class Supporter(models.Model):
  name = models.CharField(max_length = 100, blank = True, default = '')
  age = models.IntegerField(default = 0)

class Goals(models.Model):
  suportee = models.ForeignKey(Suportee, related_name = 'goals')
  completed = models.BooleanField(default = True)
  dateOfCompletion = models.IntegerField(default = 0)
  meansToAchieve = models.TextField(blank = True, default = '')

class Pledge(models.Model):
  suportee = models.ForeignKey(Suportee, related_name = 'pledges')
  suporter = models.ForeignKey(Supporter, related_name = 'pledges')
  value = models.CharField(max_length = 100, blank = True, default = '')

# class Hobo(models.Model):
#   name = models.CharField(max_length = 100, blank = True, default = 'I am a bum')
#   age = models.IntegratedField(default = -5)
#   job = models.CharField(max_length = 100, blank = True, default = 'I am a bum')