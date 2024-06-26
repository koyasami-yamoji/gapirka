from sqlalchemy.ext.asyncio import AsyncSession

from app.src.services.db.reposirories import BaseRepository, PhotoRepository, MessageRepository
from app.src.services.db.reposirories import UserRepository


class GeneralRepository(BaseRepository):
	def __init__(self, session: AsyncSession):
		super().__init__(session=session)
		self.user = UserRepository(session=session)
		self.photos = PhotoRepository(session=session)
		self.messages = MessageRepository(session=session)