import email
import smtplib
from email.message import EmailMessage


def emailAlert(subject, body, to, phoneCarrier=False):
    msgToSend = EmailMessage()
    msgToSend.set_content(body)
    msgToSend['subject'] = subject

    carrier = ""
    if(phoneCarrier):
        if(phoneCarrier == "AT&T"):
            carrier = "@txt.att.net"
        elif(phoneCarrier == "Boost Mobile"):
            carrier = "@sms.myboostmobile.com"
        elif(phoneCarrier == "Cricket Wireless"):
            carrier = "@mms.cricketwireless.net"
        elif(phoneCarrier == "Google Project Fi"):
            carrier = "@msg.fi.google.com"
        elif(phoneCarrier == "Republic Wireless"):
            carrier = "@text.republicwireless.com"
        elif(phoneCarrier == "Sprint"):
            carrier = "@messaging.sprintpcs.com"
        elif(phoneCarrier == "Straight Talk"):
            carrier = "@vtext.com"
        elif(phoneCarrier == "T-Mobile"):
            carrier = "@tmomail.net"
        elif(phoneCarrier == "Ting"):
            carrier = "@message.ting.com"
        elif(phoneCarrier == "Tracfone"):
            carrier = "@mmst5.tracfone.com"
        elif(phoneCarrier == "U.S. Cellular"):
            carrier = "@email.uscc.net"
        elif(phoneCarrier == "Verizon"):
            carrier = "@vtext.com"
        elif(phoneCarrier == "Virgin Mobile"):
            carrier = "@vmobl.com"
        else:
            carrier = False

    if(phoneCarrier != False):
        msgToSend['to'] = to + carrier
    else:
        msgToSend['to'] = to

    botAddress = "testandemailalerts@gmail.com"
    msgToSend['from'] = botAddress
    pswrd = "truhdxqpnonbupda"

    gmailServer = smtplib.SMTP("smtp.gmail.com", 587)
    gmailServer.starttls()
    gmailServer.login(botAddress, pswrd)
    gmailServer.send_message(msgToSend)

    gmailServer.quit()


# Testing code below ----------------------------------
if __name__ == '__main__':
    # Calls to emailAlert function take this form
    ##  emailAlert("subject", "body of message", "email@address.com", phoneCarrier)
    emailAlert("Test Auto-Message",
               "This is a test of the automated email system.", "9704880472", "AT&T")