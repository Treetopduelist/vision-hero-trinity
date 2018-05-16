import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "TRI")

@client.event
async def on_ready():
    print("Bot is Ready!")
        
@client.event
async def on_message(message):
    if message.content.lower() == "rule help":
        await client.send_message(message.channel, "Here is a list of all available commands: \n Rule flip summon \n Rule effect monster \n Rule normal monster \n Rule gemini monster \n Rule simultaneous summon \n Rule chronograph sorcerer \n Rule negate \n Rule card limit \n Rule legal \n Rule noble knight borz \n Rule noble knight medraut \n Rule noble knight gwalchavad \n Rule dragon spirit of white \n Rule simorgh, bird of ancestry \n Rule major riot \n Rule the shallow grave")
    elif message.content.lower() == "rule flip":
        await client.send_message(message.channel, "Neither player can Normal/Special Summon effect monster(s) more than three times each turn. \n Flip summons do NOT count towards the Summon Limit.")
    elif message.content.lower() == "rule flip summon ":
        await client.send_message(message.channel, "Neither player can Normal/Special Summon effect monster(s) more than three times each turn. \n Flip summons do NOT count towards the Summon Limit.")
    elif message.content.lower() == "rule set monster":
        await client.send_message(message.channel, "Neither player can Normal/Special Summon effect monster(s) more than three times each turn. \n Setting a monster as your normal set does NOT count towards the Summon Limit.")
    elif message.content.lower() == "rule set":
        await client.send_message(message.channel, "Neither player can Normal/Special Summon effect monster(s) more than three times each turn. \n Setting a monster as your normal set does NOT count towards the Summon Limit.")
    elif message.content.lower() == "rule effect":
        await client.send_message(message.channel, "Neither player can Normal/Special Summon effect monster(s) more than three times each turn. \n This rule does NOT affect non-effect monsters. \n Players may summon any number of non-effect monsters each turn.")
    elif message.content.lower() == "rule effect monster":
        await client.send_message(message.channel, "*Neither player can Normal/Special Summon effect monster(s) more than three times each turn.* \n This rule does NOT affect non-effect monsters.\n Players may summon any number of non-effect monsters each turn.\n A “Non-Effect monster” is any monster without an effect.\n For example, {Gaia Saber, the Lightning Shadow} is not an effect monster, and summoning this monster will not count towards the Summon Limit.")
    elif message.content.lower() == "rule normal monster":
        await client.send_message(message.channel, "*Neither player can Normal/Special Summon effect monster(s) more than three times each turn.* \n This rule does NOT affect non-effect monsters.\n Players may summon any number of non-effect monsters each turn.\n A “Non-Effect monster” is any monster without an effect.\n For example, {Gaia Saber, the Lightning Shadow} is not an effect monster, and summoning this monster will not count towards the Summon Limit.")
    elif message.content.lower() == "rule non-effect":
        await client.send_message(message.channel, "*Neither player can Normal/Special Summon effect monster(s) more than three times each turn.* \n This rule does NOT affect non-effect monsters.\n Players may summon any number of non-effect monsters each turn.\n A “Non-Effect monster” is any monster without an effect.\n For example, {Gaia Saber, the Lightning Shadow} is not an effect monster, and summoning this monster will not count towards the Summon Limit.")
    elif message.content.lower() == "rule normal":
        await client.send_message(message.channel, "*Neither player can Normal/Special Summon effect monster(s) more than three times each turn.* \n This rule does NOT affect non-effect monsters.\n Players may summon any number of non-effect monsters each turn.\n A “Non-Effect monster” is any monster without an effect.\n For example, {Gaia Saber, the Lightning Shadow} is not an effect monster, and summoning this monster will not count towards the Summon Limit.")
    elif message.content.lower() == "rule gemini":
        await client.send_message(message.channel, "Gemini Monsters NEVER count towards the Summon Limit. \n Summoning a Gemini monster from *anywhere* does not count towards the Summon Limit. \n Gemini-Summoning a Gemini monster which is already face-up on the field does not count towards the summon limit.")
    elif message.content.lower() == "rule gemini monster":
        await client.send_message(message.channel, "Gemini Monsters NEVER count towards the Summon Limit. \n Summoning a Gemini monster from *anywhere* does not count towards the Summon Limit. \n Gemini-Summoning a Gemini monster which is already face-up on the field does not count towards the summon limit.")
    elif message.content.lower() == "rule simultaneous summon":
        await client.send_message(message.channel, "Multiple monsters summoned at the same time only count as one summon towards the Summon Limit.\n For example, Pendulum Summoning multiple effect monsters at once counts as one summon.\n Summoning an effect monster(s) and a non-effect monster(s) at the same time still counts as one Summon. \n Summoning multiple non-effect monsters at the same time counts as 0 summons towards the Summon Limit.")
    elif message.content.lower() == "rule simultaneous":
        await client.send_message(message.channel, "Multiple monsters summoned at the same time only count as one summon towards the Summon Limit.\n For example, Pendulum Summoning multiple effect monsters at once counts as one summon.\n Summoning an effect monster(s) and a non-effect monster(s) at the same time still counts as one Summon. \n Summoning multiple non-effect monsters at the same time counts as 0 summons towards the Summon Limit.")
    elif message.content.lower() == "rule chronograph sorcerer":
        await client.send_message(message.channel, "Summoning Chronograph Sorcerer and 1 Effect Monster from your hand with the effect of Chronograph Sorcerer counts as 2 summons. \n This is because the effect of Chronograph Sorcerer creates a consecutive Summon, rather than a Simultaneous Summon.")
    elif message.content.lower() == "rule negate":
        await client.send_message(message.channel, "A player who has already summoned effect monster(s) at least 3 times in a turn can NOT attempt to summon another in that turn. \n For example, a player who has already summoned an effect monster(s) three times in a turn can not attempt to activate Shaddoll Fusion. \n If a mandatory effect to summon a monster is activated, (For example, Wulf, Lightsworn Beast) and the player attempting to summon that monster has already achieved three summons in a turn, that mandatory effect *fizzles*; It will activate, and resolve without effect.")
    elif message.content.lower() == "rule negated":
        await client.send_message(message.channel, "A player who has already summoned effect monster(s) at least 3 times in a turn can NOT attempt to summon another in that turn. \n For example, a player who has already summoned an effect monster(s) three times in a turn can not attempt to activate Shaddoll Fusion. \n If a mandatory effect to summon a monster is activated, (For example, Wulf, Lightsworn Beast) and the player attempting to summon that monster has already achieved three summons in a turn, that mandatory effect *fizzles*; It will activate, and resolve without effect.")
    elif message.content.lower() == "rule card limit":
        await client.send_message(message.channel, "*The minimum maindeck size is reduced from 40 to 30.* \n *Normally, Decks cannot include more than 1 of each Unlimited card.* \n *Normally, Decks cannot include any Semi-Forbidden or Co-Forbidden cards.* \n *Decks may never include more than 1 of each Semi/Co-Forbidden card*. \n *For every 5 cards above the minimum maindeck size (30),  \n that deck may include either: \n 1 extra copy of an Unlimited card  \n or 1 Semi-Forbidden card. \n or up to 2 different Co-Forbidden cards.")
    elif message.content.lower() == "card limit":
        await client.send_message(message.channel, "These rules from affect the combined Main, Extra, and Side decks. \n If your Main Deck already contains the maximum allowed quantity of Trinities, both your Side and Extra deck may not contain any Trinities. \n All other usual Side-Deck rules apply. \n for more information on the Card Limit, type *Rule Card Limit.*")
    elif message.content.lower() == "rule legal":
        await client.send_message(message.channel, "Cards which are not legal in the TCG are not legal in Trinity.\n OCG exclusive cards are not legal in Trinity unless also legal in the TCG.\n All cards which are legal in any TCG territory are legal in all of Trinity.\n All JUMP-Promotional cards are legal in Trinity, regardless of Territory.\n All TCG text updates and errata also apply to Trinity.\n This does not include OCG-exclusive text updates and errata.")
    elif message.content.lower() == "rule noble knight borz":
        await client.send_message(message.channel, "This card is treated as a Normal Monster while on the field.\n The only cards which are capable of *cheating the Summon Limit* are Non-effect monsters and Gemini monsters.\n A Summon of *Noble Knight Borz* will count towards the Summon Limit. \n This is because Borz is neither a non-effect nor a Gemini Monster.")
    elif message.content.lower() == "rule noble knight medraut":
        await client.send_message(message.channel, "This card is treated as a Normal Monster while on the field.\n The only cards which are capable of *cheating the Summon Limit* are Non-effect monsters and Gemini monsters.\n A Summon of *Noble Knight Medraut* will count towards the Summon Limit. \n This is because Medraut is neither a non-effect nor a Gemini Monster.")
    elif message.content.lower() == "rule noble knight gwalchavad":
        await client.send_message(message.channel, "This card is treated as a Normal Monster while on the field.\n The only cards which are capable of *cheating the Summon Limit* are Non-effect monsters and Gemini monsters.\n A Summon of *Noble Knight Gwalchavad*.. Gwolchavud... uh... okay, bots can't type. You know what card it anyway. Yeah, a summon of that card will count towards the Summon Limit. \n This is because the card is neither a non-effect nor a Gemini Monster.")
    elif message.content.lower() == "rule dragon spirit of white":
        await client.send_message(message.channel, " This card is treated as a Normal Monster while in the hand/Graveyard. \n A *Dragon Spirit of White* summoned from *anywhere* will count towards the Summon Limit. \n This is because Spirit is neither a non-effect nor a Gemini Monster.")
    elif message.content.lower() == "rule simorgh, bird of ancestry":
        await client.send_message(message.channel, "This card is treated as a Normal Monster while in the hand. \n A *Simorgh, Bird of Ancestry* summoned from *anywhere* will count towards the Summon Limit. \n This is because Simorgh is neither a non-effect nor a Gemini Monster.")
    elif message.content.lower() == "rule simorgh":
        await client.send_message(message.channel, "Simorgh, Bird of Ancestry is treated as a Normal Monster while in the hand. \n A *Simorgh, Bird of Ancestry* summoned from *anywhere* will count towards the Summon Limit. \n This is because Simorgh is neither a non-effect nor a Gemini Monster.")
    elif message.content.lower() == "rule major riot":
        await client.send_message(message.channel, "**Major Riot** \n *Both you and your opponent then Special Summon the same number of Monster Cards from your hand in face-down Defense Position.*\n All monsters Summoned by *Major Riot* will count towards the Summon Limit, regardless of them being effect or non-effect monsters. \n This is because the cards Summoned from the Hand are not public knowledge.\n Monsters your opponent summons with this card will count towards your opponent’s Summon Limit.\n This is because your opponent is summoning the Monsters.\n This card cannot be activated if either player has already achieved 3 Summons of Effect monsters.\n If either player has already achieved their 3 summons of the turn when Major Riot attempts to resolve, it will activate but not resolve; it *Fizzles*.")
    elif message.content.lower() == "the shallow grave":
        await client.send_message(message.channel, "Each player selects 1 monster in their Graveyard and Special Summons it in face-down Defense Position.\n Monsters your opponent summons with this card will count towards your opponent’s Summon Limit. \n This is because your opponent is summoning the Monsters. \n This card cannot be activated if either player has already achieved 3 Summons of Effect monsters. \n If either player has already achieved their 3 summons of the turn when The Shallow Grave attempts to resolve, it will activate but resolve without effect; it *Fizzles*.")
    elif message.content.lower() == "Bot, who is the best admin?":
        await client.send_message(message.channel, "The correct answer is Boddity77.")
    elif message.content.lower() == "What is the best card in the game?":
        await client.send_message(message.channel, "I think it's Vision HERO Trinity!")



client.run("NDIzMjU5MzQ2NzQ3NTIzMDc0.DdyNgQ.4x2dJBCvPFa7_m3K-Tw8survpD8")
