from django.db import models

class News(models.Model):
    image = models.ImageField(upload_to='news')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

class Sitate(models.Model):
    image = models.ImageField(upload_to='sitate')
    author = models.CharField(max_length=200)
    text = models.TextField()

class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    description = models.TextField()

class About(models.Model):
    text = models.TextField()

class Professor(models.Model):
    fullname = models.CharField(max_length=200)
    job_position = models.CharField(max_length=200)
    description = models.TextField()
    fakultet = models.CharField(max_length=200)
    kafedra = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    email = models.EmailField()
    google_h_index = models.IntegerField()
    scopus_h_index = models.IntegerField()
    wos_h_index = models.IntegerField()
    facebook = models.URLField()
    instagram = models.URLField()
    telegram = models.URLField()
    youtube = models.URLField()

class Maqola(models.Model):
    files = models.FileField(upload_to='maqolalar')

class Kitob(models.Model):
    files = models.FileField(upload_to='kitoblar')

class Presentation(models.Model):
    files = models.FileField(upload_to='presentations')

class Project(models.Model):
    images = models.ImageField(upload_to='projects')
    videos = models.FileField(upload_to='projects')

class Event(models.Model):
    images = models.ImageField(upload_to='events')
    videos = models.FileField(upload_to='events')
    files = models.FileField(upload_to='events')

class KafedraPhoto(models.Model):
    image = models.ImageField(upload_to='kafedra_photos')

class KafedraVideo(models.Model):
    video = models.FileField(upload_to='kafedra_videos')

class BakalavrLesson(models.Model):
    text = models.TextField()

class MagistLesson(models.Model):
    text = models.TextField()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()

class IndependentWork(models.Model):
    file = models.FileField(upload_to='independent_works')

class ControlWork(models.Model):
    file = models.FileField(upload_to='control_works')

class GraduateStudy(models.Model):
    file = models.FileField(upload_to='graduate_studies')
