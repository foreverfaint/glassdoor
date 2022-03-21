# -*- encoding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Generator

from .game_object import GameObject


class Module(ABC):
    @abstractmethod
    def desc(self) -> str:
        pass


class OneTimeModule(Module):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def apply(self, target: GameObject):
        pass


class AttachDetachModule(Module):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def attach(self, target: GameObject):
        pass

    @abstractmethod
    def detach(self, target: GameObject):
        pass


class OverTimeModule(Module):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._interval: int = 1
        self._i: int = 0
        self._n: int = 1
        self._last_tick = None

    @abstractmethod
    def on_tick(self, target: GameObject):
        pass

    def tick(self, target: GameObject, tick: int) -> bool:
        if self._last_tick is None:
            self._last_tick = tick

        if (tick - self._last_tick) % self._interval == 0:
            self.on_tick(target, self._i, self._n)
            self._i += 1

        self._last_tick = tick
        return self._i >= self._n

    def serialize(self) -> Dict[str, Any]:
        return {"_interval": self._interval, "_i": self._i, "_n": self._n}

    def deserialize(self, data: Dict[str, Any]):
        super().deserialize(data)
        self._interval: int = data.get("interval", 1)
        self._i: int = data.get("i", 1)
        self._n: int = data.get("n", 1)


class ModuleContainer(ABC):
    @abstractmethod
    def modules(self) -> Generator[Module, None, None]:
        pass


class ModuleMixin(object):
    def __init__(self) -> None:
        super().__init__()
        self._detachable_mods: List[AttachDetachModule] = []
        self._overtime_mods: List[OverTimeModule] = []

    def add_module(self, mod: Module) -> "ModuleMixin":
        if isinstance(mod, OneTimeModule):
            mod.apply(self)
        elif isinstance(mod, OverTimeModule):
            self._overtime_mods.append(mod)
        elif isinstance(mod, AttachDetachModule):
            mod.attach(self)
            self._detachable_mods.append(mod)
        return self

    def remove_module(self, mod: Module) -> "ModuleMixin":
        if isinstance(mod, AttachDetachModule):
            self._detachable_mods.remove(mod)
            mod.detach(self)
        return self

    def update_module(self, tick: int) -> "ModuleMixin":
        for mod in list(self._overtime_mods):
            if mod.tick(self, tick):
                self._overtime_mods.remove(mod)
        return self
