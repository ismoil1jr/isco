from django.apps import AppConfig


class MeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'me'

    def ready(self):
        import me.signals

