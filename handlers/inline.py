# handlers/inline.py
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto

def register_handlers(app):

    @app.on_inline_query()
    async def inline_cards(_, query):
        # Example cards (replace with hosted images later)
        results = [
            InlineQueryResultArticle(
                title="🔴 Red 5",
                input_message_content=InputTextMessageContent("I played 🔴 5"),
                description="Play Red 5"
            ),
            InlineQueryResultArticle(
                title="🔵 Blue Skip",
                input_message_content=InputTextMessageContent("I played 🔵 Skip"),
                description="Play Blue Skip"
            ),
            InlineQueryResultArticle(
                title="🟢 Green Reverse",
                input_message_content=InputTextMessageContent("I played 🟢 Reverse"),
                description="Play Green Reverse"
            ),
            InlineQueryResultArticle(
                title="🟡 Yellow +2",
                input_message_content=InputTextMessageContent("I played 🟡 +2"),
                description="Play Yellow +2"
            ),
            InlineQueryResultArticle(
                title="❌ Wild",
                input_message_content=InputTextMessageContent("I played ❌ Wild"),
                description="Play Wild card"
            ),
        ]

        await query.answer(results, cache_time=1)
