from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Subscribe

def send_campaign(campaign):
    # Here, i used filter method to only send emails to subscribed user. 
    recipients = Subscribe.objects.filter(is_active=True).values_list('email', flat=True)
    #used to render template
    email_subject = campaign.subject
    email_preview_text = campaign.preview_text
    email_article_url = campaign.article_url
    email_html_content = campaign.html_content
    email_text_content = campaign.text_content
    email_date = campaign.date

    # used to render the email template with campaign data
    email_body = render_to_string('send-campaign.html', {
        'subject': email_subject,
        'preview_text': email_preview_text,
        'article_url': email_article_url,
        'published_date': email_date,
        'html_content': email_html_content,
    })

    send_mail(
        subject=email_subject,
        message=email_text_content,
        html_message=email_body,
        from_email='admin@test.com',
        recipient_list=recipients,
    )

#Subscribe.objects.filter(is_active=True).values_list('email', flat=True)