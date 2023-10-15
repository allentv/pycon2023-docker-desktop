from functools import lru_cache

import docker


class DockerManager:
    def __init__(self) -> None:
        self.client = get_client()

    def get_containers(self) -> list:
        pass

    def get_images(self) -> list:
        pass

    def get_volumes(self) -> list:
        pass


@lru_cache
def get_client():
    return docker.from_env()
