from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACCOUNT SID'
auth_token = 'AUTH TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test message.",
                     from_='+1336XXXXXXX',
                     to='+1336XXXXXXX'
                 )

print(message.sid)
