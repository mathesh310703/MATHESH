
from email.message import EmailMessage
import ssl
import smtplib
import datetime 
import time
import psycopg2
import functools


connection = psycopg2.connect(user = "postgres", password = 'root', host = 'localhost',port = '5432',database='localhost')
cursor = connection.cursor()
print("database is connected successfully")
cursor.execute("select mail_id from register_form where cgpa>8;")
result = cursor.fetchall()
cursor.execute("select interview_date from register_form where cgpa>8;")
interview_date = cursor.fetchall()


for i in interview_date:
    print(i)
    new_interview = i
    

#converting tuple to int  
    test_tuple1 = new_interview
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, test_tuple1)
    print("Tuple to integer conversion : " + str(res))

    #date time to timestamp function  
    string = res
    element = datetime.datetime.strptime(string,"%Y-%m-%d %H:%M:%S")
    tuple = element.timetuple()
    interview_time = time.mktime(tuple)
    
    print("interview_time:",interview_time)

def email():

    email_sender = 'stardustmass73@gmail.com'
    email_password = 'ylnuitzaktxgqqfi'
    email_reciever = new_email

    subject = 'Remainder for your Interview'
    body = """
    Dear user,
    Hey, user it's time to show off your technical skills, U have a technical interview scheduled tomorrow.
    we would be testing you on various aspects such as 
    1) Data science tools
    2) Machine learning
    3) IOT
    4) Artificial Intelliegnce 
    5) python 
    so we expect you to be well prepared on the above mentioned topics. Good luck buddy,

    with regards
    Ram
    (HR Manager)
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)
    em.add_alternative(
        """
    <html>
        <body bgcolor = "lightblue">
            <p><strong>hey buddy,</p>
            <p>it's time to show off your technical skills, U have a technical interview scheduled on 
            we would be testing you on various aspects such as </p>
            <p><strong>1) Data science tools</strong></p>
            <p><strong>2) Machine learning</strong></p>
            <p><strong>3) IOT</strong></p>
            <p><strong>4) Artificial Intelliegnce</strong></p>
            <p><strong>5) python </strong></p>
            <p>so we expect you to be well prepared on the above mentioned topics. Good luck buddy,</p>
            <p>with regards;</p>
            <p>ram</p>
        </body>
    </html>
    """,
    subtype = "html"
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp:
        smtp.login(email_sender ,email_password )
        current_time = time.time()
        print("current time is :",current_time)
        send_time = interview_time- 86400
        print("send time is:",send_time)
        send_time=time.sleep(send_time - current_time)
        smtp.sendmail(email_sender,email_reciever,em.as_string())

        print("email sent successfully")

for i in result:
    print(i)
    new_email = i
    email()
 
cursor.close()
print("database connection is closed")



