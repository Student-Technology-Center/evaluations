from django.db import models

RATEING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)

# Create your models here.
class Evaluation(models.Model):
    """
    Model representing a clients evaluation
    """
    instructor_name = models.CharField(max_length = 64)
    workshop_name = models.CharField(max_length = 64)
    workshop_date = models.DateField()
    instructor_knowledge = models.IntegerField(choices=RATEING_CHOICES, default='1')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.instructor_name + "_" + self.workshop_name