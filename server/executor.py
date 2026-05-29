import asyncio
import logging

logger = logging.getLogger(__name__)


class TaskExecutor:
    async def execute(
        self,
        task_name: str
    ) -> dict:
        logger.info(
            f"Executing task: {task_name}"
        )

        await asyncio.sleep(1)

        return {
            "status": "completed",
            "task": task_name
        }


