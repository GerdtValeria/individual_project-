from app.services.base import BaseService
from app.repositories.comments import CommentsRepository

class CommentService(BaseService):
    async def get_all_comments(self):
        return await CommentsRepository.get_all()
    
    async def add_comment(self):
        return await CommentsRepository.add_comment()
    
    async def edit_comment(self):
        return await CommentsRepository.add_comment()
    
    async def delete_comment(self):
        return await CommentsRepository.delete_comment()
    