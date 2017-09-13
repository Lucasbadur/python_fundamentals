from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2989c28edfc36b172ec83469a0d17a99"
# Your Auth Token from twilio.com/console
auth_token  = "6eb34a7922b57ce80e2ee0d5ce239bd6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5519991449191", 
    from_="+18312288383 ",
    body="You spelled burgundy wrong")

print(message.sid)
