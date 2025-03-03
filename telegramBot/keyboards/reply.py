from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
     keyboard=[
         [
             KeyboardButton(text='расскажи о создателе'),
             KeyboardButton(text='стих'),
         ],
         {
             KeyboardButton(text='поддержать создателя')
         }
     ],
    resize_keyboard=True,
    input_field_placeholder='yes,excellent so much funny enges'

)


