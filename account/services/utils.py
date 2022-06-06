from email import message
from django.core.mail import send_mail


def send_activate_code(activate_code: str, email: str):
    
    title = "hello i activate link to your account in site SnakeShop"
    message = f'please click link to activate account http://127.0.0.1:8000/api/v1/account/activate/{activate_code}/'
    from_email = 'test@test.com'
    
    send_mail(
        title,
        message,
        from_email,
        [email],
        fail_silently=False,
    )
    
def send_new_password(email, new_password):
    title = "Reset link:"
    message = f'Your new password: {new_password} from email: {email}'
    from_email = 'SnakeShop@python.kg'
        
    send_mail(
        title,
        message,
        from_email,
        [email],
        fail_silently=False,
    )