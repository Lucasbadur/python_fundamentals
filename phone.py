from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "account"
# Your Auth Token from twilio.com/console
auth_token  = "yourtokenhere"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="destinationnumber", 
    from_="numberorigin",
    body="You spelled burgundy wrong")

print(message.sid)
