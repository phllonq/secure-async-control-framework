import aiosqlite


class DatabaseManager:
    def __init__(
        self,
        db_path: str = "c2.db"
    ):
        self.db_path = db_path

    async def initialize(self):
        async with aiosqlite.connect(
            self.db_path
        ) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS sessions (
                    client_id TEXT PRIMARY KEY,
                    connected_at REAL
                )
                """
            )

            await db.commit()


