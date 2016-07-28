from twilio.rest import TwilioRestClient

account_sid = "ACa96671d4945919838d207119a37c5d9f" # Your Account SID from www.twilio.com/console
auth_token  = "2432d9954a90d7897fa1016f269f0e4a"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Venkat",
    to="+17036249888",
    from_="+12403033454")
print(message.sid)
