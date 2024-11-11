from django.db import models

# Create your models here.

difficulty = (
('easy', 'Easy'), 
('intermediate', 'Intermediate'), 
('hard', 'Hard'), 
)

class Recipe(models.Model):
  name = models.CharField(max_length=225)
  ingredients = models.CharField(max_length=225)
  cooking_time = models.IntegerField(default=10)
  difficulty = models.CharField(max_length=30, choices=difficulty)
  pic = models.ImageField(upload_to='recipes', default='no_image.png')

  def __str__(self): 
    return str(self.name)