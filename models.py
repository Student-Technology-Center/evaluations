from django.db import models

# Create your models here.
class Evaluation(models.Model):
    """
    Model representing a clients evaluation
    """
    instructor_name = models.CharField(max_length = 64)
    workshop_name = models.CharField(max_length = 64)
    workshop_date = models.DateField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.instructor_name + "_" + self.workshop_name