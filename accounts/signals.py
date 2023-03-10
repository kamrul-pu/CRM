from django.contrib.auth.models import User,Group
from accounts.models import Customer
from django.db.models.signals import post_save

def customer_profile(sender,instance,created,**kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
                user = instance,
                name = instance.username,
                email = instance.email
            )

post_save.connect(customer_profile,sender=User)
