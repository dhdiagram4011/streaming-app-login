from django.contrib import admin
from .models import StreamingUser

# class StreamingUser(AbstractUser):
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=100)
#     created_date = models.DateTimeField(auto_now_add=True)
#     published_date = models.DateTimeField(null=True, blank=True)


class StreamingUserAdmin(admin.ModelAdmin):
    list_display = ['username','mails','passwords','phone_numbers','created_date']


admin.site.register(StreamingUser,StreamingUserAdmin)