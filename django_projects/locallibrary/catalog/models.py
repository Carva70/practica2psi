from django.db import models


class Author(models.Model):

    # Fields
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name


class Books(models.Model):

    # Fields
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

