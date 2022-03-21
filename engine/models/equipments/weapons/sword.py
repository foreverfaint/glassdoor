# -*- encoding: utf-8 -*-
from typing import Generator

from engine.models import module, equipment, character
from engine.models.modules import ChangeCharacterAttrsOnAttachDetach


class Sword(equipment.Equipment):
    # The modules are removed from ModuleMixin by object ID.
    # Therefore multiple `modules` calls generate the same instances.
    MODS = [
        ChangeCharacterAttrsOnAttachDetach(character.CharacterAttrs.MELEE_ATTACK, 5)
    ]

    def __init__(self):
        super().__init__()

    def modules(self) -> Generator[module.Module, None, None]:
        yield from self.MODS

    def requires(self, ch: character.Character) -> bool:
        return ch.level >= 1

    def desc_requirements(self) -> str:
        return f"等级1+"

    def name(self) -> str:
        return "单手剑"

    def slot(self) -> equipment.EquipableSlots:
        return equipment.EquipableSlots.RIGHT_HAND

    def desc_effects(self) -> str:
        return ';'.join([mod.desc() for mod in self.MODS])
