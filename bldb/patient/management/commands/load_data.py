from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from patient.models import Patient

import logging
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        log = logging.getLogger(__name__)
        log.info("Deleting existing data...")
        Patient.objects.all().delete()
        log.info("Loading data...")
        
        log.info(settings.BASE_DIR)
