from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from warehouse.models import Invoice


@receiver(m2m_changed, sender=Invoice.products.through)
def update_invoice_total_amount(sender, instance, action, **kwargs):
    if action in ('post_add', 'post_remove', 'post_clear'):
        instance.update_total_amount()
