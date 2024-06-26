from aiogram import Router, F
from aiogram.types import Message
from dishka import FromDishka

from app.src.services.db.reposirories import GeneralRepository

default_router = Router()


@default_router.message(F.text.in_({'гапирня', 'гапирочка', 'гапирка'}))
async def gapirka_echo(message: Message):
	await message.answer('Да мой сладкий?')


@default_router.message(F.text)
async def message_handler(message: Message, repo: FromDishka[GeneralRepository]):
	await repo.messages.add_message(text=message.text)
	await repo.user.inscribe_message_count(user_id=message.from_user.id)


@default_router.message(F.photo)
async def photo_handler(message: Message, repo: FromDishka[GeneralRepository]):
	await repo.photos.add_photo(photo=message.photo[-1].file_id)
