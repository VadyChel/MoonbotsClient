from moonlistclient.models.webhooks import *
from moonlistclient import MoonlistClient, Webhook
from discord.ext import commands


class MLCExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mclient = MoonlistClient(
            bot=self.bot,
            api_key="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            webhook=True,
            host="localhost"
        )
        self.mclient.webhook_manager.add(
            Webhook(
                token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                endpoint="/new_bot",
                trigger="new_bot"
            )
        )
        self.mclient.webhook_manager.add(
            Webhook(
                token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                endpoint="/new_comment",
                trigger="new_comment"
            )
        )
        self.mclient.webhook_manager.add(
            Webhook(
                token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                endpoint="/new_bump",
                trigger="new_bump"
            )
        )
        self.mclient.webhook_manager.add(
            Webhook(
                token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                endpoint="/bot_delete",
                trigger="bot_delete"
            )
        )
        self.mclient.webhook_manager.add(
            Webhook(
                token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                endpoint="/bot_edit",
                trigger="bot_edit"
            )
        )
        self.mclient.webhook_manager.add(
            Webhook(
                token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                endpoint="/bot_edit_currently",
                trigger="bot_edit_currently"
            )
        )

    @commands.Cog.listener()
    async def on_connect(self):
        await self.mclient.webhook_manager.run()

    @commands.Cog.listener()
    async def on_new_bot(self, data: NewBotWebhook):
        print("New bot was added. It data:\n", data)

    @commands.Cog.listener()
    async def on_new_bump(self, data: NewBumpWebhook):
        print("New bump was added. It data:\n", data)

    @commands.Cog.listener()
    async def on_new_comment(self, data: NewCommentWebhook):
        print("New comment was added. It data:\n", data)

    @commands.Cog.listener()
    async def on_bot_delete(self, data: BotDeleteWebhook):
        print("Bot was deleted. It data:\n", data)

    @commands.Cog.listener()
    async def on_bot_edit(self, data: BotEditWebhook):
        print("Bot was edited. It data:\n", data)

    @commands.Cog.listener()
    async def on_bot_edit_currently(self, data: BotEditCurrentlyWebhook):
        print("Bot currently was edited. It data:\n", data)


def setup(client):
    client.add_cog(MLCExample(client))