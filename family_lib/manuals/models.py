from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    product_tag = models.CharField( max_length=500, blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField( max_length=50)  # Field name made lowercase.
    product_description = models.CharField( max_length=256, blank=True, null=True)  # Field name made lowercase.
    product_model = models.CharField( max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.product_name

class Manual(models.Model):
    manual_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    manual_title = models.CharField( max_length=100)  # Field name made lowercase.
    manual_description = models.CharField( max_length=500, blank=True, null=True)  # Field name made lowercase.
    manual_url = models.CharField( max_length=200, blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product_id')
    manual_file=models.FileField(upload_to='files/',null=True)

