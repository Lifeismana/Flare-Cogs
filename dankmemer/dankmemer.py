# -*- coding: utf-8 -*-

from io import BytesIO
import os
import typing

import aiohttp
import discord
from redbot.core import commands

from . import gif, images, movie, text as textmeme
from .converters import ImageFinder


class DankMemer(commands.Cog):
    """Dank Memer Commands."""

    __version__ = "0.0.18"

    def format_help_for_context(self, ctx):
        """Thanks Sinbad."""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\nCog Version: {self.__version__}"

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    async def red_get_data_for_user(self, *, user_id: int):
        # this cog does not story any data
        return {}

    async def red_delete_data_for_user(self, *, requester, user_id: int) -> None:
        # this cog does not story any data
        pass

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    async def send_error(self, ctx, data):
        await ctx.send(f"Oops, an error occured. `{data['error']}`")

    async def get_img(self, url):
        async with self.session.get(url) as resp:
            if resp.status == 200:
                file = await resp.read()
                file = BytesIO(file)
                file.seek(0)
                return file
            if resp.status == 404:
                return {
                    "error": "Server not found, ensure the correct URL is setup and is reachable. "
                }
            try:
                return await resp.json()
            except aiohttp.ContentTypeError:
                return {"error": "Server may be down, please try again later."}

    async def send_img(self, ctx, image):
        if not ctx.channel.permissions_for(ctx.me).send_messages:
            return
        if not ctx.channel.permissions_for(ctx.me).attach_files:
            await ctx.send("I don't have permission to attach files.")
            return
        try:
            await ctx.send(file=image)
        except aiohttp.ClientOSError:
            await ctx.send("An error occured sending the picture.")

    @commands.command()
    async def abandon(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Abandoning your son?"""
        data = images.abandon(self, text)
        data.name = "abandon.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command(aliases=["aborted"])
    async def abort(self, ctx, image: ImageFinder = None):
        """All the reasons why X was aborted."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.aborted(self, image)
        data.name = "abort.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def affect(self, ctx, image: ImageFinder = None):
        """It won't affect my baby."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.affect(self, image)
        data.name = "affect.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def airpods(self, ctx, image: ImageFinder = None):
        """Flex with airpods."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = gif.airpods(self, image)
        data.name = "airpods.gif"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def america(self, ctx, image: ImageFinder = None):
        """Americafy a picture."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = gif.america(self, image)
        data.name = "america.gif"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def armor(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Nothing gets through this armour."""
        data = images.armor(self, text)
        data.name = "armor.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def balloon(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Pop a balloon.

        Texts must be comma seperated.
        """
        data = images.ballon(self, text)
        data.name = "balloon.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def bed(self, ctx, user: discord.Member, user2: discord.Member = None):
        """There's a monster under my bed."""
        user2 = user2 or ctx.author
        user, user2 = user2, user
        # could it be done better ?
        avatars = [
            BytesIO(await user.avatar_url_as(static_format="png").read()),
            BytesIO(await user2.avatar_url_as(static_format="png").read()),
        ]
        data = images.bed(self, avatars)
        data.name = "bed.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def bongocat(self, ctx, image: ImageFinder = None):
        """Bongocat-ify your image."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.bongocat(self, image)
        data.name = "bongocat.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def boo(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Scary.

        Texts must be comma seperated.
        """
        data = images.boo(self, text)
        data.name = "boo.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def brain(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Big brain meme.

        Texts must be 4 comma seperated items.
        """
        data = images.brain(self, text)
        data.name = "brain.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def brazzers(self, ctx, image: ImageFinder = None):
        """Brazzerfy your image."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.brazzers(self, image)
        data.name = "brazzers.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def byemom(
        self,
        ctx,
        user: typing.Optional[discord.Member] = None,
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """Bye mom.

        User is a discord user ID, name or mention.
        """
        user = user or ctx.author
        data = images.byemom(
            self=self,
            avatar=BytesIO(await user.avatar_url_as(static_format="png").read()),
            username=user.name,
            text=text,
        )
        data.name = "byemom.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()  # TODO: Maybe remove?
    async def cancer(self, ctx, image: ImageFinder = None):
        """Squidward sign."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.cancer(self, image)
        data.name = "cancer.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def changemymind(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Change my mind?"""
        data = images.changemymind(self, text)
        data.name = "changemymind.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def cheating(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Cheating?.

        Text must be comma seperated.
        """
        data = images.cheating(self, text)
        data.name = "cheating.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def paperplease(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Papers Please Citation.

        Text must be 3 comma seperated values.
        """
        data = images.citation(self, text)
        data.name = "citation.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def communism(self, ctx, image: ImageFinder = None):
        """Communism-ify your picture."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = gif.communism(self, image)
        data.name = "communism.gif"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def confusedcat(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Confused cat meme.

        Text must be 2 comma seperated values.
        """
        data = images.confusedcat(self, text)
        data.name = "confusedcat.png"
        await self.send_img(ctx, discord.File(data))

    # TODO we should be able to send 2 images
    @commands.command()
    async def corporate(self, ctx, image: ImageFinder = None):
        """Corporate meme."""
        if image is None:
            image = [BytesIO(await ctx.author.avatar_url_as(static_format="png").read())]
        else:
            image = [await self.get_img(url=image)]
        data = images.corporate(self, image)
        data.name = "corporate.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def cry(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Drink my tears meme.

        Text must be 2 comma seperated values.
        """
        data = images.cry(self, text)
        data.name = "cry.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def dab(self, ctx, image: ImageFinder = None):
        """Hit a dab."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.dab(self, image)
        data.name = "dab.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def dank(self, ctx, image: ImageFinder = None):
        """Dank, noscope 420."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = gif.dank(self, image)
        data.name = "dank.gif"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def deepfried(self, ctx, image: ImageFinder = None):
        """Deepfry an image."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.deepfry(self, image)
        data.name = "deepfry.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def delete(self, ctx, image: ImageFinder = None):
        """Delete Meme."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.delete(self, image)
        data.name = "delete.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def disability(self, ctx, image: ImageFinder = None):
        """Disability Meme."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.disability(self, image)
        data.name = "disability.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def doglemon(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Dog and Lemon Meme.

        Text must be 2 comma seperated values.
        """
        data = images.doglemon(self, text)
        data.name = "doglemon.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def door(self, ctx, image: ImageFinder = None):
        """Kick down the door meme."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.door(self, image)
        data.name = "door.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def egg(self, ctx, image: ImageFinder = None):
        """Turn your picture into an egg."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.egg(self, image)
        data.name = "egg.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command(aliases=["em"])
    async def emergencymeeting(
        self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)
    ):
        """Call an emergency meeting."""
        data = images.emergencymeeting(self, text)
        data.name = "emergencymeeting.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def excuseme(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Excuse me, what the...

        Text must be 2 comma seperated values.
        """
        data = images.excuseme(self, text)
        data.name = "excuseme.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def expanddong(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Expanding?

        Text must be 2 comma seperated values.
        """
        data = images.expanddong(self, text)
        data.name = "expanddong.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def facts(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Facts book.

        Text must be 2 comma seperated values.
        """
        data = images.facts(self, text)
        data.name = "facts.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def failure(self, ctx, image: ImageFinder = None):
        """You're a failure meme."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.failure(self, image)
        data.name = "failure.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def fakenews(self, ctx, image: ImageFinder = None):
        """Fake News."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.fakenews(self, image)
        data.name = "fakenews.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def farmer(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Farmer.

        Text must be 2 sentences comma seperated.
        """
        data = images.farmer(self, text)
        data.name = "farmer.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def fedora(self, ctx, image: ImageFinder = None):
        """*Tips Fedora*."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.fedora(self, image)
        data.name = "fedora.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def floor(
        self,
        ctx,
        user: typing.Optional[discord.Member] = None,
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """The floor is ....

        User is a discord user ID, name or mention.
        """
        user = user or ctx.author
        data = images.floor(self=self, avatar=BytesIO(await user.avatar_url_as(static_format="png").read()), text=text)
        data.name = "floor.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def fuck(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Feck.

        Text must be 2 comma seperated values.
        """
        data = images.fuck(self, text)
        data.name = "fuck.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def garfield(
        self,
        ctx,
        user: typing.Optional[discord.Member] = None,
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """I wonder who that's for - Garfield meme.

        User is a discord user ID, name or mention."""
        user = user or ctx.author
        data = images.garfield(self, BytesIO(await user.avatar_url_as(static_format="png").read()), text)
        data.name = "garfield.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command(aliases=["rainbow", "lgbtq"])
    async def lgbt(self, ctx, image: ImageFinder = None):
        """Rainbow-fy your picture."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.gay(self, image)
        data.name = "gay.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def godwhy(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """God why."""
        data = images.godwhy(self, text)
        data.name = "godwhy.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def goggles(self, ctx, image: ImageFinder = None):
        """Remember, safety goggles on."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.goggles(self, image)
        data.name = "goggles.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def hitler(self, ctx, image: ImageFinder = None):
        """Worse than hitler?."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.hitler(self, image)
        data.name = "hitler.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def humansgood(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Humans are wonderful things."""
        data = images.humansgood(self, text)
        data.name = "humansgood.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def inator(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Xinator."""
        data = images.inator(self, text)
        data.name = "inator.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command(aliases=["invertcolor", "invertcolors", "invercolours"])
    async def invertcolour(self, ctx, image: ImageFinder = None):
        """Invert the colour of an image."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.invert(image)
        data.name = "invert.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def ipad(self, ctx, image: ImageFinder = None):
        """Put your picture on an ipad."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.ipad(self, image)
        data.name = "ipad.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def jail(self, ctx, image: ImageFinder = None):
        """Send yourself to jail."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.jail(self, image)
        data.name = "jail.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def justpretending(
        self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)
    ):
        """Playing dead.

        Text must be 2 comma seperated values.
        """
        data = images.justpretending(self, text)
        data.name = "justpretending.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def keepyourdistance(
        self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)
    ):
        """Keep your distance."""
        data = images.keepurdistance(self, text)
        data.name = "keepurdistance.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def kimborder(self, ctx, image: ImageFinder = None):
        """Place yourself under mighty kim."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.kimborder(self, image)
        data.name = "kimborder.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def knowyourlocation(
        self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)
    ):
        """Google wants to know your location.

        Text must be 2 comma seperated values.
        """
        data = images.knowyourlocation(self, text)
        data.name = "knowyourlocation.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()  # TODO: MP4s
    async def kowalski(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Kowlalski tapping.

        Text must be 2 comma seperated values.
        """
        data = movie.kowalski(self, text)
        oldname = data.name
        data.name = "kowalski.gif"
        await self.send_img(ctx, discord.File(data))

        try:
            os.remove(oldname)
        except (FileNotFoundError, OSError, PermissionError):
            pass

    @commands.command()
    async def laid(self, ctx, image: ImageFinder = None):
        """Do you get laid?"""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.laid(self, image)
        data.name = "laid.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()  # TODO: MP4s
    async def letmein(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """LET ME IN."""
        data = movie.letmein(self, text)
        data.name = "letmein.mp4"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def lick(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Lick lick.

        Text must be 2 comma seperated values.
        """
        data = images.lick(self, text)
        data.name = "lick.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def madethis(self, ctx, user: discord.Member, user2: discord.Member = None):
        """I made this!"""
        user2 = user2 or ctx.author
        users = [BytesIO(await user2.avatar_url_as(static_format="png").read()), BytesIO(await user.avatar_url_as(static_format="png").read())]
        data = images.madethis(self, users)
        data.name = "madethis.png"
        await self.send_img(ctx, discord.File(data))

    # MAYBE WE SHOULD REMOVE IT
    @commands.command()  # Support other urls soon
    async def magickify(self, ctx, image: ImageFinder = None):
        """Peform magik."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        # we don't give it text
        data = images.magik(self, image)
        data.name = "magik.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def master(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Yes master!

        Text must be 3 comma seperated values.
        """
        data = images.master(self, text)
        data.name = "master.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def meme(
        self,
        ctx,
        image: typing.Optional[ImageFinder],
        top_text: commands.clean_content(fix_channel_mentions=True),
        bottom_text: commands.clean_content(fix_channel_mentions=True),
        color: typing.Optional[str],
        font: typing.Optional[str] = None,
    ):
        """Make your own meme.

        For text longer then one word for each variable, enclose them in "" This endpoint works a
        bit differently from the other endpoints. This endpoint takes in top_text and bottom_text
        parameters instead of text. It also supports color and font parameters. Fonts supported
        are: arial, arimobold, impact, robotomedium, robotoregular, sans, segoeuireg, tahoma and
        verdana. Colors can be defined with HEX codes or web colors, e.g. black, white, orange etc.
        Try your luck ;) The default is Impact in white.
        """
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        # hmmm i should rewrite that
        if font:
            fnt = font
        else:
            fnt = ""
        if color:
            clr = color
        else:
            clr = ""
        data = images.meme(self, image, top_text, bottom_text, clr, fnt)
        data.name = "meme.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def note(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Pass a note back."""
        data = images.note(self, text)
        data.name = "note.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def nothing(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Woah!

        nothing.
        """
        data = images.nothing(self, text)
        data.name = "nothing.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def obama(self, ctx, user: typing.Optional[discord.Member]):
        """Obama.

        user: discord User, takes their avatar and display name.
        """
        user = user or ctx.author
        data = images.obama(
            self, BytesIO(await user.avatar_url_as(static_format="png").read()), user.display_name
        )
        data.name = "obama.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def ohno(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Oh no, it's stupid!"""
        data = images.ohno(self, text)
        data.name = "ohno.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def piccolo(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Piccolo."""
        data = images.piccolo(self, text)
        data.name = "piccolo.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def plan(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Gru makes a plan.

        Text must be 3 comma seperated values.
        """
        data = images.plan(self, text)
        data.name = "plan.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def presentation(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Lisa makes a presentation."""
        data = images.presentation(self, text)
        data.name = "presentation.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def quote(
        self,
        ctx,
        user: typing.Optional[discord.Member] = None,
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """Quote a discord user."""
        user = user or ctx.author
        data = images.quote(
            self, BytesIO(await user.avatar_url_as(static_format="png").read()), user.name, text
        )
        data.name = "quote.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def radialblur(self, ctx, image: ImageFinder = None):
        """Radiarblur-ify your picture.."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.radialblur(self, image)
        data.name = "radialblur.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command(aliases=["restinpeace"])
    async def tombstone(self, ctx, image: ImageFinder = None):
        """Give a lucky person a tombstone."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.rip(self, image)
        data.name = "rip.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def roblox(self, ctx, image: ImageFinder = None):
        """Turn yourself into a roblox character."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.roblox(self, image)
        data.name = "roblox.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def salty(self, ctx, image: ImageFinder = None):
        """Add some salt."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.salty(self, image)
        data.name = "salty.gif"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def satan(self, ctx, image: ImageFinder = None):
        """Place your picture over Satan."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.satan(self, image)
        data.name = "satan.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def savehumanity(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """The secret to saving humanity."""
        data = images.savehumanity(self, text)
        data.name = "savehumanity.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def screams(self, ctx, user: discord.Member, user2: discord.Member = None):
        """Why can't you just be normal?

        **Screams**
        """
        user2 = user2 or ctx.author
        avatars = [
            BytesIO(await user2.avatar_url_as(static_format="png").read()),
            BytesIO(await user.avatar_url_as(static_format="png").read()),
        ]
        data = images.screams(self, avatars)
        data.name = "screams.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def shit(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """I stepped in crap."""
        data = images.shit(self, text)
        data.name = "shit.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def sickban(self, ctx, image: ImageFinder = None):
        """Ban this sick filth!"""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.sickban(self, image)
        data.name = "sickban.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def slap(self, ctx, user: discord.Member, user2: discord.Member = None):
        """*SLAPS*"""
        user2 = user2 or ctx.author
        avatars = [
            BytesIO(await user2.avatar_url_as(static_format="png").read()),
            BytesIO(await user.avatar_url_as(static_format="png").read()),
        ]
        data = images.slap(self, avatars)
        data.name = "slap.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def slapsroof(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """This bad boy can fit so much in it."""
        data = images.slapsroof(self, text)
        data.name = "slapsroof.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def sneakyfox(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """That sneaky fox.

        Text must be 2 comma seperated values.
        """
        data = images.sneakyfox(self, text)
        data.name = "sneakyfox.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def spank(self, ctx, user: discord.Member, user2: discord.Member = None):
        """*spanks*"""
        user2 = user2 or ctx.author
        avatars = [
            BytesIO(await user2.avatar_url_as(static_format="png").read()),
            BytesIO(await user.avatar_url_as(static_format="png").read()),
        ]
        data = images.spank(self, avatars)
        data.name = "spank.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def stroke(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """How to recognize a stroke?"""
        data = images.stroke(self, text)
        data.name = "stroke.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def surprised(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Pikasuprised.

        Text must be 2 comma seperated values.
        """
        data = images.surprised(self, text)
        data.name = "surprised.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def sword(
        self,
        ctx,
        user: typing.Optional[discord.Member] = None,
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """Swordknife.

        Text must be split on commas.
        """
        user = user or ctx.author

        data = images.sword(self, user.name, text)
        data.name = "sword.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def theoffice(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """The office.

        Text must be 2 sentences comma seperated.
        """
        data = images.theoffice(self, text)
        data.name = "theoffice.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def thesearch(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """The search for intelligent life continues.."""
        data = images.thesearch(self, text)
        data.name = "thesearch.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def trash(self, ctx, image: ImageFinder = None):
        """Peter Parker trash."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image =  await self.get_img(url=image)
        data = images.trash(self, image)
        data.name = "trash.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def trigger(self, ctx, image: ImageFinder = None):
        """Triggerfied."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = gif.trigger(self, image)
        data.name = "trigger.gif"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def tweet(
        self,
        ctx,
        user: typing.Optional[discord.Member],
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """Create a fake tweet.

        user: discord User, takes their avatar, display name and name.
        text: commands.clean_content(fix_channel_mentions=True)ing. Text to show on the generated image.
        """
        user = user or ctx.author
        data = images.tweet(
            self, BytesIO(await user.avatar_url_as(static_format="png").read()), user.display_name, user.name, text
        )
        data.name = "tweet.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def ugly(self, ctx, image: ImageFinder = None):
        """Make a user ugly."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.ugly(self, image)
        data.name = "ugly.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def unpopular(
        self,
        ctx,
        user: typing.Optional[discord.Member] = None,
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """Get rid of that pesky teacher."""
        user = user or ctx.author
        data = images.unpopular(self, BytesIO(await user.avatar_url_as(static_format="png").read()), text)
        data.name = "unpopular.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def violence(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Violence is never the answer."""
        data = images.violence(self, text)
        data.name = "violence.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def violentsparks(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Some violent sparks.

        Text must be 2 comma seperated values.
        """
        data = images.violentsparks(self, text)
        data.name = "violentsparks.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def vr(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Woah, VR is so realistic."""
        data = images.vr(self, text)
        data.name = "vr.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def walking(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """Walking Meme."""
        data = images.walking(self, text)
        data.name = "walking.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def wanted(self, ctx, image: ImageFinder = None):
        """Heard you're a wanted fugitive?"""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.wanted(self, image)
        data.name = "wanted.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def warp(self, ctx, image: ImageFinder = None):
        """Warp?."""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image =  await self.get_img(url=image)
        data = images.warp(self, image)
        data.name = "warp.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def whodidthis(self, ctx, image: ImageFinder = None):
        """Who did this?"""
        if image is None:
            image = await ctx.author.avatar_url_as(static_format="png").read()
            image = BytesIO(image)
        else:
            image = await self.get_img(url=image)
        data = images.whodidthis(self, image)
        data.name = "whodidthis.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def whothisis(
        self,
        ctx,
        user: typing.Optional[discord.Member],
        username: commands.clean_content(fix_channel_mentions=True),
    ):
        """who this is."""
        user = user or ctx.author
        data = images.whothisis(self,  BytesIO(await user.avatar_url_as(static_format="png").read()), username)
        data.name = "whothisis.png"
        await self.send_img(ctx, discord.File(data))

    @commands.command()
    async def yomomma(self, ctx):
        """Yo momma!."""
        await ctx.send(textmeme.yomomma())

    @commands.command()
    async def youtube(
        self,
        ctx,
        user: typing.Optional[discord.Member] = None,
        *,
        text: commands.clean_content(fix_channel_mentions=True),
    ):
        """Create a youtube comment."""
        user = user or ctx.author
        data = images.youtube(
            self, BytesIO(await user.avatar_url_as(static_format="png").read()), user.name, text
        )
        data.name = "youtube.png"
        await self.send_img(ctx, discord.File(data))

    # New Endpoints

    @commands.command()
    async def wwe(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        """WWE Meme.

        Text must be 5 comma seperated values.
        """
        data = images.expandingwwe(self, text)
        data.name = "expandingwwe.png"
        await self.send_img(ctx, discord.File(data))


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]
