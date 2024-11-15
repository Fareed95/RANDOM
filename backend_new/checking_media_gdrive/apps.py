from django.apps import AppConfig


class CheckingMediaGdriveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checking_media_gdrive'
    def ready(self):
        import backend_new.signals 