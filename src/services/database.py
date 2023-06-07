import logging

from gino import Gino, exceptions

logger = logging.getLogger(__name__)
db = Gino()


class GinoConnection:
    def __init__(self, url):
        self.url = url
        self.db = None

    async def __aenter__(self):
        self.db = db
        await self.db.set_bind(self.url)
        return self.db

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.db.pop_bind().close()

        if exc_type is exceptions:
            logger.critical(f"Database error: {exc_type}")
            return False

        return True