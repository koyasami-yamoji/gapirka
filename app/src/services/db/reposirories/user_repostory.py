from datetime import date
from typing import Optional

from sqlalchemy import select, update, func

from app.src.services.db.models import User
from app.src.services.db.reposirories.base import BaseRepository


class UserRepository(BaseRepository):

	async def create_user(self, user_id: int, username: Optional[str]):
		user = User(
			user_id=user_id,
			username=username
		)

		self.session.add(user)
		await self.session.commit()
		return User

	async def get_user(self, user_id: int, username: Optional[str]):
		result = await self.session.scalar(
			select(User.user_id).where(User.user_id == user_id)
		)
		if result:
			return result

		result = await self.create_user(user_id=user_id, username=username)
		return result

	async def inscribe_message_count(self, user_id: int):
		await self.session.execute(
			update(User).where(User.user_id == user_id).values(message_count=User.message_count + 1)
		)
		await self.session.commit()

	async def get_message_count(self, user_id: int):
		result = await self.session.execute(
			select(User.message_count).where(User.user_id == user_id)
		)
		return result.fetchone()
