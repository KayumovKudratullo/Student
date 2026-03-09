from django.db import models

class Banner(models.Model):
    title = models.CharField()
    text = models.TextField()
    background_img = models.ImageField()
    corusel_img = models.ImageField()

class Service(models.Model):
    icon_text = models.CharField()
    title = models.CharField()
    text = models.TextField()

class About(models.Model):
    text = models.TextField()
    year_experience = models.IntegerField()
    chefs = models.IntegerField()

class AboutImage(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="about/")


class FoodTypes(models.Model):
    title = models.CharField()

class Food(models.Model):
    title = models.CharField()
    price = models.PositiveIntegerField()
    text = models.TextField()
    foodtypes = models.ManyToManyField(FoodTypes)