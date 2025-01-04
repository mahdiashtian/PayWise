from django.core.management.base import BaseCommand

from users.fixtures.users import create_sample_users


class Command(BaseCommand):
    help = "Create sample users for development purposes."

    def add_arguments(self, parser):
        parser.add_argument(
            '--quantity',
            type=int,
            default=10,
            help='Number of sample users to create (default is 10).'
        )

    def handle(self, *args, **options):
        quantity = options['quantity']
        create_sample_users(quantity)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {quantity} sample users.'))
