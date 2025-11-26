from django.apps import AppConfig

class MarketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'market'
    def ready(self):
        import market.signals
        from market.signals import create_default_categories
        from django.db import connection
        # Só criar categorias se as tabelas já existem (após migrate)
        if 'market_category' in connection.introspection.table_names():
            create_default_categories()