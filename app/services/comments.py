from app.services.base import BaseService
from app.repositories.comments import CommentsRepository

class CommentService(BaseService):
    async def get_all_comments(self):
        return await CommentsRepository.get_all()