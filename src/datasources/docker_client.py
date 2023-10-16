from functools import lru_cache

import docker


class DockerManager:
    def __init__(self) -> None:
        # Comment out the below line to avoid connecting to Docker service
        # self.client = get_client()
        self.client = None

    def get_containers(self) -> list:
        # TODO: Add implementation
        return []

    def get_images(self) -> list:
        # TODO: Add implementation
        return []

    def get_volumes(self) -> list:
        # TODO: Add implementation
        return []


@lru_cache
def get_client() -> docker.DockerClient:
    return docker.from_env()
