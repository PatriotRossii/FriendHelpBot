from kutana import Plugin, t
from utils.database import Database

plugin = Plugin(name=t("UserDialog"))
cursor = Database.cursor()


@plugin.on_commands(["start"])
async def __(msg, ctx):
	cursor.execute("SELECT user FROM query WHERE user = ?", [msg.sender_id])
	user = cursor.fetchone()
	
	if not user:
		cursor.execute("INSERT INTO query VALUES(?,NULL)", [msg.sender_id])
		Database.commit()

		await ctx.reply("Вы скоро будете подключены к собеседнику")
	else:
		await ctx.reply("Вы уже стоите в очереди")
