from django.apps import AppConfig


class InformingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'informing'

    def ready(self):
        import informing.signals