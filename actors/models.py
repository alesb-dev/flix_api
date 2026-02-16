from django.db import models


NATIONALITY_CHOICES = (
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('JP', 'Japan'),
    ('IN', 'India'),
    ('CN', 'China'),
    ('BR', 'Brazil'),
    ('CA', 'Canada'),
)

class Actor(models.Model):    
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=2, null=True, blank=True, 
                                   choices=NATIONALITY_CHOICES)



    def __str__(self):
        return self.name
    