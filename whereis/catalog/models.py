from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30, help_text='name of person', primary_key=True)
    location = models.CharField(max_length=30, help_text='name of location')
    email = models.EmailField()
    lastUpdate = models.DateTimeField()


    # Metadata
    class Meta:
        ordering = ['name', 'lastUpdate']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name + self.location
