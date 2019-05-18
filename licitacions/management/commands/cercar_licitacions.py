from django.core.management.base import BaseCommand
from licitacions.crawler import cercar_licitacions


class Command(BaseCommand):

    def handle(self, *args, **options):
        cercar_licitacions()
