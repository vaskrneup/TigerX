import json
from pathlib import Path


class EnvManager:
    DEFAULT_ENV_FILE: Path = Path("PRIVATE_env.json")

    def __init__(self, env_file: (Path | str) = None):
        env_file: Path = Path(env_file) if type(env_file) is not Path else env_file

        if not str(env_file).endswith(".json"):
            raise ValueError(f"Environment File must be of type JSON, Given: `{env_file}`")

        self.env_file: Path = env_file or self.DEFAULT_ENV_FILE
        self.env_file_data: dict[str, any] = {}

        if not env_file.exists():
            self.write_env_file()

    def read_env_file(self) -> None:
        with open(self.env_file, "r") as env_file:
            self.env_file_data = json.load(env_file)

    def write_env_file(self) -> None:
        with open(self.env_file, "w") as env_file:
            json.dump(self.env_file_data, env_file)

    @property
    def data(self) -> dict[str, any]:
        return self.env_file_data
