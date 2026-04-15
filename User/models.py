from django.db import models # type: ignore

class Banner(models.Model):
    title = models.CharField()
    text = models.TextField()
    background_img = models.ImageField(upload_to='banners/')
    corusel_img = models.ImageField(upload_to='banners/', null=True, blank=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    icon_text = models.CharField()
    title = models.CharField()
    text = models.TextField()

    def __str__(self):
        return self.title

class About(models.Model):
    text = models.TextField()
    year_experience = models.IntegerField()
    chefs = models.IntegerField()
    video = models.FileField(upload_to="about/videos/", null=True, blank=True)

    def __str__(self):
        return self.text

class AboutImage(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.about.text


class FoodTypes(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title

class Food(models.Model):
    title = models.CharField()
    price = models.PositiveIntegerField()
    text = models.TextField()
    foodtypes = models.ManyToManyField(FoodTypes, related_name="foods")

    def __str__(self):
        return self.title
    
class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField()
    pax = models.PositiveIntegerField()
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date}"