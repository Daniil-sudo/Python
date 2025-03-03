from datetime import datetime
import json
import aiofiles
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply

upr = Router()  #user privat router
DATA_FILE = "user_responses.json"  # Change to JSON file




@upr.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, давай знакомиться.Я кибер шаман, на службе своего создателя." +
                         "Расскажи о себе...", reply_markup=reply.start_kb)


@upr.message(F.text == 'расскажи о создателе')
async def menu_cmd(message: types.Message):
    await message.answer("Я бы назвал его кибер-самураем или солдатом пустоты, это человек необычайной живучести, способный создавать умения из ничего. "
                         "Поразительно, что он и куёт, и пишет код, наверное, он будет одним из выживших в робо-апокалипсисе ")

@upr.message(F.text == 'поддержать создателя')
async def menu_cmd(message: types.Message):
    await message.answer("поддержи создателя")

@upr.message(F.text == 'стих')
async def menu_cmd(message: types.Message):
    await message.answer("Пуля - висок"
                         "Мысли как птицы"
                         "Ярость - бросок"
                         "Как не разбиться?"
                         "В городе снов,вороны - крысы"
                         "Стук каблуков - запах мелисы"
                         "Маленькая девочка - просит монетку"
                         "Бог даст на тарелочке - будет конфетка"
                         "Боже прости дурака, ты ведь все видишь, помог бы слегка")


@upr.message(F.text)
async def menu_cmd(message: types.Message, DATA_FILE=None, new_message=None):
    text_lower = message.text.lower()
    if "прив" in text_lower or "зда" in text_lower or text_lower == "привет":
        await message.answer('это было очень познавательно, если хочешь, расскажи больше')
    elif "салам" in text_lower or "здрав" in text_lower: # Removed duplicate "привет"
        await message.answer('это было очень познавательно, если хочешь, расскажи больше')

        # Save the user's response to a file
    try:
        user_id = message.from_user.id
        username = message.from_user.username or "No Username"
        timestamp = datetime.now().isoformat()
        text = message.text or "No Text"
        chat_id = message.chat.id
        message_id = message.message_id
        first_name = message.from_user.first_name or "No First Name"
        last_name = message.from_user.last_name or "No Last Name"

        new_message = {
            "timestamp": timestamp,
            "user_id": user_id,
            "username": username,
            "text": text,
            "chat_id": chat_id,
            "message_id": message_id,
            "first_name": first_name,
            "last_name": last_name
        }

        # Load existing data (if any), append, and write back
        try:
            async with aiofiles.open(DATA_FILE, mode='r', encoding='utf-8') as f:
                content = await f.read()
                if content:
                    all_messages = json.loads(content)  # Load JSON
                else:
                    all_messages = []  # Start a new array
        except FileNotFoundError:
            all_messages = []  # If the file doesn't exist, create a new array
        except json.JSONDecodeError:  # If the file exists but is invalid JSON
            print("Error: Invalid JSON in file.  Overwriting with new array.")
            all_messages = []  # Overwrite if the file exists but is invalid JSON
        all_messages.append(new_message)  # Add to the array

        # Write the entire JSON array back to the file.
        async with aiofiles.open(DATA_FILE, mode='w', encoding='utf-8') as f:
            await f.write(json.dumps(all_messages, indent=4, ensure_ascii=False))  # Overwrites the whole file

    except Exception as e:
        print(f"Error saving response: {e}")
'''
использование фильтров , по первым словам буквам выдается ответ
'''