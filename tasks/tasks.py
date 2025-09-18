from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone
import datetime

@shared_task
def send_daily_summary_email():
    today = timezone.now().date()
    users = User.objects.all()

    for user in users:
        pending_tasks = Task.objects.filter(
            user=user, 
            status='pending',
            due_date__date=today
        )

        if pending_tasks.exists() and user.email:
            subject = f"Your Daily Task Summary for {today.strftime('%B %d')}"
            
            message = f"Hi {user.username},\n\nYou have {pending_tasks.count()} task(s) due today that are still pending:\n\n"
            for task in pending_tasks:
                message += f"- {task.title}\n"
            
            message += "\nDon't forget to complete them!\n\nBest,\nSmart To-Do Team"
            
            send_mail(
                subject,
                message,
                'noreply@smarttodo.com',
                [user.email],
                fail_silently=False,
            )
            print(f"Sent summary email to {user.email}")