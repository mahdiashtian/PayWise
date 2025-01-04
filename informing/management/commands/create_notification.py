from django.core.management.base import BaseCommand

from informing.models import Notification
from users.models import User


class Command(BaseCommand):
    help = 'Creates a new notification for a user'

    def add_arguments(self, parser):
        parser.add_argument('--user_id', type=int, required=True)
        parser.add_argument('--title', type=str, required=True)
        parser.add_argument('--content', type=str, required=True)
        parser.add_argument('--type', type=str, choices=['info', 'warning', 'error'], default='info')
        parser.add_argument('--is_read', type=bool, default=False)

    def handle(self, *args, **options):
        try:
            user = User.objects.get(id=options['user_id'])

            notification = Notification.objects.create(
                user=user,
                title=options['title'],
                content=options['content'],
                type=options['type'],
                is_read=options['is_read']
            )

            self.stdout.write(
                self.style.SUCCESS(f'Successfully created notification "{notification.title}" for user {user.id}'))

        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with id {options["user_id"]} does not exist'))
