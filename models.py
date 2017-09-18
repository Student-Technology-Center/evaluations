from django.db import models

RATEING_CHOICES = (
    (1, "Not at all"),
    (2, "Slightly"),
    (3, "Somewhat"),
    (4, "Very"),
    (5, "Extremely"),
)

YES_NO = (
    ("Yes", "Yes"),
    ("No", "No"),
)

# Create your models here.
class Evaluation(models.Model):
    """
    Model representing a clients evaluation
    """
    instructor_name = models.CharField("Instructor", max_length = 64)
    workshop_name = models.CharField("Name of Workshop", max_length = 64)
    workshop_date = models.DateField("Date")

    clarity = models.IntegerField("Was the information presented clearly?", choices=RATEING_CHOICES, default='3')
    usefullness = models.IntegerField("Were the workshop materials useful?", choices=RATEING_CHOICES, default='3')
    instructor_knowledge = models.IntegerField("Was the instructor knowledgeable on the topic?", choices=RATEING_CHOICES, default='3')
    instructor_time = models.IntegerField("Did the instructor take he time to answer your questions?", choices=RATEING_CHOICES, default='3')

    ontime = models.CharField("Did the workshop start on time?", max_length = 8, choices=YES_NO, default='Yes')

    intrest = models.CharField("Was this personal intrest or class/project related?", max_length = 512, null=True, blank=True)
    difficulty = models.CharField("What part of the workshop was the most difficult for you?", max_length = 512, null=True, blank=True)
    favorite = models.CharField("What was your favorite part of the workshop?" ,max_length = 512, null=True, blank=True)
    offered = models.CharField("What other workshops would you like to see offered?", max_length = 512, null=True, blank=True)


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '{}-{}-{}'.format(instructor_name, workshop_name, workshop_date)