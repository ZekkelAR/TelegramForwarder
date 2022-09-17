from telethon import TelegramClient, events



app_id = "app_id"
api_hash = "hash"

client = TelegramClient('anon', app_id, api_hash)
channel = -93939393 #change with your channel want to forward
target = -929292 #change target channel
@client.on(events.NewMessage)
async def handler(event):
	#chat = await event.get_chat()
	#print(chat)
	chat_id = event.chat_id
	if chat_id == channel:
		msg = event.raw_text
		print("{}:{}" .format(chat_id,msg))
		if "gw ganteng" in msg:
			await client.send_message(target, "woiiii")
	if chat_id = channel:
		await client.send_message(target, "test forwarder")
client.start()
client.run_until_disconnected()