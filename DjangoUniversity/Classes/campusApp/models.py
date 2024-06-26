from django.db import models


# Model of UniversityCampus
class UniversityCampus(models.Model):
    # Attributes:
    campus_name = models.CharField(max_length=60, default='', blank=True, null=False)
    state = models.CharField(max_length=12, default='', blank=True, null=False)
    campus_id = models.IntegerField(default='', blank=True, null=False)

    # Object manager to later interact with this
    # Model's database through operations
    object = models.Manager()

    # Returns a specifies format to display this object as a String
    def __str__(self):
        # retrieves the 'campus_name' of the instance via 'self'
        # and concatenates it to the string that is being returned
        return "{0.campus_name}".format(self)

    # Sets the reference name of this Model
    # Django adds an 's' to each Model object by default
    # so this overrides that behavior
    class Meta:
        verbose_name_plural = 'University Campus'
