import telegram
import asyncio

async def send_telegram_bot(message):
    bot = telegram.Bot(token='7261855742:AAHkBu8Y9fNpasMt8aMN2cHn7sDWSHTziJY')

    # chat_id может быть как ID чата, так и username группы
    chat_ids = [
        '1271362249',
        '-1002193449783',
        '5380811884',
        '1899271190', 
        '6284877530',
        # '@refPrint',  
    ]
    
    for chat_id in chat_ids:
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"Message sent to {chat_id}")
        except telegram.error.TelegramError as e:
            print(f"Failed to send message to {chat_id}: {e}")

def send_telegram_notification(mes):
    asyncio.run(send_telegram_bot(mes))



def get_chat_id():
    bot = telegram.Bot(token='7261855742:AAHkBu8Y9fNpasMt8aMN2cHn7sDWSHTziJY')
    updates = bot.get_updates()
    
    for update in updates:
        print(update.message.chat.id)