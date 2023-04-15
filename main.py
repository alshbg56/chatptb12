import os, requests
from pyrogram import Client, filters, enums

api_id = 24726477
api_hash = "ba993a0f5b0bccfbf2a25d061826eeed"
bot_token = os.environ['bot_token']

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
@app.on_message(filters.command(['start']))
def hi(app, msg):
  app.send_message(msg.chat.id, "مرحبا بك في بوت ذكاء الاصطناعي")
  return

@app.on_message(filters.text)
def replytomsg(app, msg):
  if "/start" not msg.text:
    app.send_chat_action(msg.chat.id, enums.ChatAction.TYPING)
    msgchat = requests.get("https://alsh-bg.ml/openai/x.php?key="+os.environ['api_key']+"&text=" + msg.text).json()['msg']
    app.send_message(msg.chat.id, msgchat)
    return
  
app.run()
