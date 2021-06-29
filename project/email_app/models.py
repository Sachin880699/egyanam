from django.db import models

class EmailLoginAttempt(models.Model):

    email = models.CharField(max_length  = 1000 , null = True , blank  = True)
    ip_address = models.CharField(max_length  = 1000 , null = True , blank  = True)
    created_at = models.DateField(auto_now_add = True)