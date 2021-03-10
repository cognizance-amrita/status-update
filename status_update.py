import requests, re, json, smtplib
from email.message import EmailMessage
import datetime as dt

def send_mail():
    EMAIL_ADDRESS = 'cognizance.amrita@gmail.com'
    EMAIL_PASSWORD = 'aunwvulwcegtncnt'

    headers = {
        'Content-Type': 'application/json',
    }
    data = '{ "query":"{ members { email } }" }'
    response = requests.post('https://cognizance-amrita.herokuapp.com/graphql/', headers=headers, data=data)
    content = response.json()
    emails = []
    for j in content['data']['members']:
        emails.append(j['email'])

    msg = EmailMessage()
    msg['Subject'] = 'Status Update'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = emails
    msg.set_content(
        '''
        <html>
        <p>
        <b>Greetings,</b><br>
        This is an automatically generated thread for  sending your daily status update for today. Please send your status update as a reply to this thread after 06:00 PM and <b>before 05:00 AM</b>.<br>
        Remember to mention the work you did today (including relevant non-technical work), the work/goals you plan for tomorrow, and any blockers you are facing. Also, include a proper signature for your update.<br>
        A good model for a status update would be-<br><br>
        <div style="margin-left: 30px;">
        <code>
            Greetings,<br><br>

            <b>Done:</b><br>
                Work done in paragraphs, or descriptive bullet points<br>
            <b>Planned:</b><br>
                Each plan/goal in Bullet points<br>
            <b>Blockers:</b> (optional)<br>
                Mention any blockers you are facing (if any), so others in the club can help  you out.<br>
            <b>Hours worked:</b> [Hours you worked]<br><br>
            [ Signature ]
        </code></div><br><br>
        Kindly note that an automated bot is tracking your status updates, and generating reports. Failing to send status updates repeatedly shall entail severe actions.<br><br>
        <b>Wishing you a productive day!</b>
        </p>
        </body>
        </html>
        '''
    , subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        smtp.send_message(msg)

while True:
    if datetime.now().strftime("%H:%M:%S") == '14:15:00':
        send_mail()