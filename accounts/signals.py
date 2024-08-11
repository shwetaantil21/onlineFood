from .models import User, UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


# Receiver
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance,created, **kwargs):
    if created:
        print("Create the user profile")
        UserProfile.objects.create(user=instance)
        print("user profile created")
    else:
        # del the userprofile get error
        try:
            print("user is updated")
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the user profile if not exist
            UserProfile.objects.create(user=instance)
            print("Profile was not exist but created")



# post_save.connect(post_save_create_profile_receiver, sender=User)