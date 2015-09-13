from django.core.management.base import BaseCommand, CommandError

from patient.models import Patient

import logging

class Command(BaseCommand):
    def handle(self, *args, **options):
        log = logging.getLogger(__name__)
        log.info("Deleting existing data...")
        Patient.objects.all().delete()
