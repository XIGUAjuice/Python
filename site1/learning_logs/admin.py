from django.contrib import admin
# Register your models here.
from learning_logs.models import Topic
from learning_logs.models import Content

admin.site.register(Topic)
admin.site.register(Content)
