# importing twilio
from twilio.rest import Client


account_sid = 'AC04700f58fbc12c696249b1cee21b77c9'
auth_token = '3abc58720ba65f274e5f8ee63ab05cdb'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
message = client.messages.create(
    from_=' +16592014009',
    body='body',
    to='+917984767866'
)

print(message.sid)