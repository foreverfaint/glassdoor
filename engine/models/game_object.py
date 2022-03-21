# -*- encoding: utf-8 -*-
import uuid
from abc import ABC


class GameObject(ABC):
    def __init__(self):
        super().__init__()
        self._id = uuid.uuid4()

    def __eq__(self, __o: object) -> bool:
        return self._id == (GameObject)(__o)._id if isinstance(__o, GameObject) else False

    def __hash__(self) -> int:
        return hash(self._id)
