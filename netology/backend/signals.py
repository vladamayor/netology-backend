from typing import Type

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import Signal, receiver
from django_rest_passwordreset.signals import reset_password_token_created

from netology.backend.tasks import send_email
from netology.models import ConfirmEmailToken, User

new_user_registered = Signal()

new_order = Signal()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """
    Отправляем письмо с токеном для сброса пароля
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param kwargs:
    :return:
    """
    # send an e-mail to the user

    send_email.delay(
        subject=f"Password Reset Token for {reset_password_token.user}",
        body=reset_password_token.key,
        from_email=settings.EMAIL_HOST_USER,
        to=[reset_password_token.user.email],
    )


@receiver(post_save, sender=User)
def new_user_registered_signal(
    sender: Type[User], instance: User, created: bool, **kwargs
):
    """
    отправляем письмо с подтрердждением почты
    """
    if created and not instance.is_active:
        # send an e-mail to the user
        token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)

        send_email.delay(
            subject=f"Hello {instance.email} !!",
            body=f'Your validation token is: "{token.key}"',
            from_email=settings.EMAIL_HOST_USER,
            to=[instance.email],
        )


@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    send_email.delay(
        subject="Обновление статуса заказа",
        body="Заказ сформирован",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
