from django.db import models

# Create your models here.
class categoryData(models.Model):
    category_id = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=50,default="null")
    def __str__(self):
        return self.Category
    
class ProductData(models.Model):
    productName = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=250)
    price = models.IntegerField()
    productQuantity = models.IntegerField()
    category = models.ForeignKey(categoryData,default="0", on_delete=models.CASCADE)
    
    # productImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.productName



class cartData(models.Model):
    product = models.ForeignKey(ProductData, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return ("cart for" + self.product)