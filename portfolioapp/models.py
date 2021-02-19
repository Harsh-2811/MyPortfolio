from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class Certificates(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='certificates')

    def __str__(self):
        return self.title

technologies = (
    ('Python','Python'),
    ('Django','Django'),
    ('Flask','Flask'),
    ('JavaScript','JavaScript/Jquery'),
    ('HTML,CSS','HTML,CSS'),
    ('MySQL','MYSQL'),
    ('MongoDB','MongoDB'),
    ('PostgreSQL','PostgreSQL'),
    ('Java','Java Swing'),
    ('React','React'),
)
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    main_image = models.ImageField(upload_to='projects')
    image1 = models.ImageField(upload_to='projects')
    image2 = models.ImageField(upload_to='projects')
    image3 = models.ImageField(upload_to='projects')
    image4 = models.ImageField(upload_to='projects')
    technologies = MultiSelectField(choices=technologies)
    slug = models.CharField(max_length=20,default="",null=True,blank=True)
    link = models.URLField(default="",null=True,blank=True)

    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=20)
    image=models.ImageField(upload_to='technology')
    expertise_level= models.IntegerField()

    def __str__(self):
        return self.name

