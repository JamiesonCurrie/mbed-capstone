from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=255, db_index=True)

  def __str__(self)->str:
    return self.title

###############################################################################

class MenuItem(models.Model):
  title     = models.CharField(max_length=255, db_index=True)
  slug      = models.SlugField()
  category  = models.ForeignKey(Category, on_delete=models.PROTECT)
  price     = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
  featured  = models.BooleanField(db_index=True)
  inventory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)])

  def __str__(self)->str:
    return '(' + str(self.category) + ') ' + self.title + ' : $' + str(self.price) + ' [' + self.featured + '] (' + self.inventory + ')'

###############################################################################

class Booking(models.Model):
    name             = models.CharField(max_length=200)
    no_of_guests     = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)])
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
      unique_together = ('name', 'reservation_date')

    def __str__(self):
        return str(self.reservation_date) + ' @ ' + self.reservation_slot + ' for ' + self.name + ', party of ' + str(self.no_of_guests)