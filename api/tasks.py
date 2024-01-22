from celery import shared_task
from django.core.mail import EmailMessage
from api.models import Booking

@shared_task(bind=True)
def send_mail_func(self):
    bookings=Booking.objects.all()
    for book in bookings:
        if book.end_date-book.start_date:
            print(f'No email to send yet for {book.client}')
        else:
            subject='Nck Car Rental Notice'
            message=f"Dear {book.client},Please be notified your rental is due and you're obliged to info management if there are any last minute changes"
            from_email='kumideveloper@gmail.com'
            to_email=['silaskumi4@gmail.com','kumideveloper@gmail.com',book.client.email]
            email=EmailMessage(
                subject,message,from_email,to_email
            )
            email.content_subtype='html'
            email.send()
            
    return 'Emails sent'