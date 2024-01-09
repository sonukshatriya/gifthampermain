from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class admin_table(models.Model):
    a_name=models.CharField(max_length=20)
    a_email=models.EmailField()
    a_password=models.CharField(max_length=20)
    a_phone=models.BigIntegerField()
    a_status=models.IntegerField()

class user_table(models.Model):
    u_name=models.CharField(max_length=20)
    u_email=models.CharField(max_length=20)
    u_password=models.CharField(max_length=25)
    u_phone=models.BigIntegerField()
    u_status=models.IntegerField()

class user_detail_table(models.Model):
    user_id=models.ForeignKey(user_table, on_delete=models.CASCADE)
    dob=models.DateField()
    u_address=models.CharField(max_length=100)
    u_image=models.ImageField(upload_to='photos')
   def U_Image(self):
        return mark_safe('<img src={} width="100"/>'.format(self.u_image.url))

class giftstockist_table(models.Model):
       name=models.CharField(max_length=15)
       password=models.CharField(max_length=15)
       email=models.CharField(max_length=20)
       phone_no=models.IntegerField()
       address=models.TextField(max_length=40)
       stockist_image=models.ImageField(upload_to='photos')
    def Stockist_Image(self):
           return mark_safe('<img src={} width="100"/>'.format(self.stockist_image.url))

class category_table(models.Model):
        category_name=models.CharField(max_length=15)

class product_table(models.Model):
        catid = models.ForeignKey(category_table, on_delete=models.CASCADE)
        stockist_id = models.ForeignKey(giftstockist_table, on_delete=models.CASCADE)
        p_name=models.CharField(max_length=15)
        p_description=models.CharField(max_length=25)
        p_image=models.ImageField(upload_to='photos')
        p_quantity=models.IntegerField()
        p_price=models.BigIntegerField()
        p_status=models.IntegerField()
     def P_Image(self):
            return mark_safe('<img src={} width="100"/>'.format(self.p_image.url)

class cart_table(models.Model):
     user_id=models.ForiegnkeyField(usertable, on_delete=models.CASCADE)
     p_id=models.ForiegnkeyField(product_table, on_delete=models.CASCADE)
     p_quantity=
     total_amount=models.IntegerField()
     status=models.CharField(max_length=20)

class order_table(models.Model):
        userid=
        p_id=
        cart_id=
        order_status=models.CharField(max_length=20)

class card_table(models.Model):
        u_id=
        card_name=models.CharField(max_length=20)
        cvv=models.IntegerField()
        expiry_date=models.DateField()
        card_number=models.BigIntegerField()
        payment_id=models.CharField(max_length=20)
class payment_table(models.Model):
        u_id=
        order_id=
        payment_method=models.CharField(max_length=10)
        total_amount=models.()
        payment_status=models.CharField(max_length=10)

class return_product_table(models.Model):
        u_id=
        payment_id=
        order_id=
        date_of_return=models.DateField()
        return_status=models.CharField(max_length=15)

class feedback_table(models.Model):
        u_id=
        p_id=
        comment=models.TextField()
        rating=models.IntegerField()

class complain_table(models.Model):
        u_id=
        comment=models.TextField()
        complain_status=models.CharField(max_length=10)
        complain_date=models.DateField()











