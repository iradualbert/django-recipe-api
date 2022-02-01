from operator import mod
from unicodedata import category
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
    def __str__(self):
        return self.name
    
    
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(Category, related_name="ingredients", on_delete=models.CASCADE)
    
    
    def to_json(self):
        return {
            "name": self.name,
            "notes": self.notes,
            "category": self.category.to_json()
        } 
     
    def __str__(self):
        return self.name
    
    