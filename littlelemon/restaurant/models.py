from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
###############################################################################

class Menu(models.Model):
  title    = models.CharField(max_length=255, db_index=True)
  price    = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
  #featured = models.BooleanField(db_index=True)
  #category = models.ForeignKey(Category, on_delete=models.PROTECT)
  inventory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)])

  def __str__(self)->str:
    return self.title + ' ... $' + str(self.price)

class Booking(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  no_of_guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)])
  bookingdate = models.DateTimeField()

  class Meta:
    unique_together = ('name', 'bookingdate')

  def __str__(self)->str:
    return str(self.bookingdate) + ' - ' + self.name + ', party of ' + str(self.no_of_guests)

