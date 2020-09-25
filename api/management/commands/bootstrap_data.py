from django.core.management.base import BaseCommand, CommandError
from api.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Populates ShoeType and ShoeColor'

    def handle(self, *args, **kwargs):
        ShoeType.objects.bulk_create([
            ShoeType(style='Sneaker'),
            ShoeType(style='Boot'),
            ShoeType(style='Sandal'),
            ShoeType(style='Dress'),
            ShoeType(style='Other')
        ])

        ShoeColor.objects.bulk_create([
            ShoeColor(color_name='Red'),
            ShoeColor(color_name='Orange'),
            ShoeColor(color_name='Yellow'),
            ShoeColor(color_name='Green'),
            ShoeColor(color_name='Blue'),
            ShoeColor(color_name='Indigo'),
            ShoeColor(color_name='Violet'),
            ShoeColor(color_name='White'),
            ShoeColor(color_name='Black')
        ])