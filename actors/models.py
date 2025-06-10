from django.db import models

NATIONALITIES = [
    ('American', 'USA'),
    ('Brazilian', 'Brazilian'),
    ('British', 'British'),    
    ('Canadian', 'Canadian'),
    ('Australian', 'Australian'),
    ('French', 'French'),
    ('German', 'German'),
    ('Spanish', 'Spanish'),
    ('Italian', 'Italian'),
    ('Japanese', 'Japanese'),
    ('Chinese', 'Chinese'),
    ('Indian', 'Indian'),
    ('Other', 'Other')
]

class Actor(models.Model):
    name = models.CharField(max_length=200)    
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(
            max_length=100,
            choices=NATIONALITIES, 
            default='Brazilian'
        )

    def __str__(self):
        return self.name