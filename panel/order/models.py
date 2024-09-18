from django.db import models

class Order(models.Model):
    order_code = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    expiration = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) +" "+ str(self.order_code)