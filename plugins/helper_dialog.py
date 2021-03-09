from kutana import Plugin, t
from utils.database import Database


plugin = Plugin(name=t("HelperDialog"))
cursor = Database.cursor()


@plugin.on_commands(["start_helper"])
async def __(msg, ctx):
	cursor.execute("SELECT user FROM query WHERE helper is NULL LIMIT 1")
	user = cursor.fetchone()

	if user:
		user_id = user[0]
		cursor.execute("UPDATE query SET helper = ? WHERE user = ?", [msg.sender_id, user_id])
		Database.commit()

		await ctx.reply("Собеседник найден. Общайтесь!")
		await ctx.send_message(user_id, "Собеседник найден. Общайтесь!")
	else:
		await ctx.reply("Собеседник не найден. Попробуйте повторить поиск через некоторое время")