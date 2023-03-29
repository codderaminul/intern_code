from django.db import models
from config.g_model import TimeStampMixin


# Create your models here.
class variants(TimeStampMixin):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()



class products(TimeStampMixin):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField()


class product_images(TimeStampMixin):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    file_path = models.URLField()
    thumbnail = models.BooleanField()


class product_variants(TimeStampMixin):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(variants, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)


class product_variants_prices(TimeStampMixin):
    product_variant_one = models.ForeignKey(product_variants, on_delete=models.CASCADE, null=True,  related_name='product_variant_one')
    product_variant_two = models.ForeignKey(product_variants, on_delete=models.CASCADE, null=True, related_name='product_variant_two')
    product_variant_three = models.ForeignKey(product_variants, on_delete=models.CASCADE, null=True, related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(products, on_delete=models.CASCADE)
