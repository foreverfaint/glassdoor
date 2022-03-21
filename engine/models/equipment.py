# -*- encoding: utf-8 -*-
from abc import abstractmethod
from enum import Enum
from typing import Dict, List

from .game_object import GameObject
from .module import ModuleContainer


class EquipableSlots(Enum):
    HEAD = 0
    BODY = 1
    LEFT_HAND = 2
    RIGHT_HAND = 3
    DUAL_HANDS = 4
    FOOT = 5


class Equipment(GameObject, ModuleContainer):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def requires(self, go: GameObject) -> bool:
        pass

    @abstractmethod
    def slot(self) -> EquipableSlots:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def desc_effects(self) -> str:
        pass

    @abstractmethod
    def desc_requirements(self) -> str:
        pass


class EquipableMixin(object):
    def __init__(self) -> None:
        super().__init__()
        self._eqpt: Dict[EquipableSlots, Equipment] = {}

    def equip(self, eq: Equipment) -> "EquipableMixin":
        if not eq.requires(self):
            raise ValueError(f"unmatch {eq.desc_requirements()}")

        # Unset the slot
        self.unequip(eq.slot())
        # Set eq to the slot
        self._eqpt[eq.slot()] = eq
        # Apply the effects of new eq
        for mod in eq.modules():
            self.add_module(mod)
        return self

    def unequip(self, slot: EquipableSlots) -> "EquipableMixin":
        # Clear the effects of old eq
        eq = self._eqpt.get(slot, None)
        if eq is not None:
            for mod in eq.modules():
                self.remove_module(mod)
        # Unset the slot
        self._eqpt[slot] = None
        return self   
