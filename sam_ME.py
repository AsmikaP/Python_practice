
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ME():
    def __init__(self):
        self.port = 465 
        # For SSL
        self.smtp_server = "host18.indiandns.com"
        self.sender_email = "test@veminence.com" # Enter your address        
        self.receiver_email = "receive@veminence.com" # Enter receiver address        
        self.password = "Veminence@2023"
        self.severity = input("Enter the severity : ")
        self.hostname = input("Enter the hostname : ")
        self.starttime = input("Enter the start time of outage : ")
        self.reportedtime = input("Enter the reported time of outgae : ")
        self.endtime = input("Enter the end of the outage : ")
        message = MIMEMultipart("alternative")
        message["Subject"] = input("Enter the subject line : ")
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        
text = """\
          Hi,
          
          How are you?
          Real Python has many great tutorials:www.realpython.com"""
html = """\
        <html>
        <body> <table> 
        <tr> 
        <th>Severity</th> 
        </tr> 

        <tr>
        <td>Alfreds Futterkiste</td> 
        <td>Maria Anders</td>
        <td>Germany</td>
        </tr> </table> 
        </body>
        </html>"""  
        
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1) 
message.attach(part2) 
     
context = ssl.create_default_context() 
with smtplib.SMTP_SSL("host18.indiandns.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())

class ME_1(ME):
     pass

class ME_2(ME):
     pass

class ME_3(ME): 
     pass
        


obj = ME()