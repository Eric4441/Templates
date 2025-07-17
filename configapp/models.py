from django.db import models
class Category(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Regions(models.Model):
    title=models.CharField(max_length=40)
    context=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class District(models.Model):
    title=models.CharField(max_length=250)
    context=models.TextField(blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    region=models.ForeignKey(Regions, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} ({self.context})"
class Neighbourhood(models.Model):
    title = models.CharField(max_length=250)
    context = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} ({self.context})"

