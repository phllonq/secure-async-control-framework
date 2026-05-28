import json
from pathlib import Path


class PersistenceLayer:
    STATE_FILE = "runtime/client_state.json"

    @staticmethod
    def save(state: dict):
        Path("runtime").mkdir(exist_ok=True)

        with open(
            PersistenceLayer.STATE_FILE,
            "w"
        ) as file:
            json.dump(state, file)

    @staticmethod
    def load():
        path = Path(
            PersistenceLayer.STATE_FILE
        )

        if not path.exists():
            return {}

        with open(path, "r") as file:
            return json.load(file)


