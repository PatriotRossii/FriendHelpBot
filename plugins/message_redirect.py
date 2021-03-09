from kutana import Plugin, t
from utils.database import Database

plugin = Plugin(name=t("MessageRedirect"))
cursor = Database.cursor()


@plugin.on_unprocessed_messages()
async def __(msg, ctx):
	cursor.execute("SELECT user, helper FROM query WHERE user = ? OR helper = ?", [msg.sender_id, msg.sender_id])
	result = cursor.fetchone()

	if not result:
		await ctx.reply("Начните диалог, отправив команду /start")
		return

	opponent = [e for e in result if e != msg.sender_id]
	opponent_id = opponent[0]
	await ctx.send_message(opponent_id, "Собеседник: " + msg.text, attachments=msg.attachments)
