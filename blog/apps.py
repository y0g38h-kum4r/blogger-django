from django.apps import AppConfig


class BlogConfig(AppConfig): #inherits from appconfig class
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
