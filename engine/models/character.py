# -*- encoding: utf-8 -*-
from typing import Dict, Any
from enum import Enum

from engine.models import game_object, module, equipment


class CharacterAttrs(Enum):
    STRENGTH = "str"
    WISDOM = "wis"
    DEXTERITY = "dex"
    MAX_HP = "max_hp"
    MAX_MP = "max_mp"
    HIT_RATE = "hit_rate"
    MELEE_ATTACK = "melee_att"
    MELEE_DEFENSE = "melee_def"
    FIRE_ATTACK = "fire_att"
    FIRE_DEFENSE = "fire_def"
    ICE_ATTACK = "ice_att"
    ICE_DEFENSE = "ice_def"
    THUNDER_ATTACK = "thdr_att"
    THUNDER_DEFENSE = "thdr_def"


class Character(game_object.GameObject, module.ModuleMixin, equipment.EquipableMixin):
    K = {
        CharacterAttrs.STRENGTH: 1,
        CharacterAttrs.WISDOM: 1,
        CharacterAttrs.DEXTERITY: 1,
        CharacterAttrs.MAX_HP: 1,
        CharacterAttrs.MAX_MP: 1,
        CharacterAttrs.HIT_RATE: 1,
        CharacterAttrs.MELEE_ATTACK: 1,
        CharacterAttrs.MELEE_DEFENSE: 1,
        CharacterAttrs.FIRE_ATTACK: 0,
        CharacterAttrs.FIRE_DEFENSE: 0,
        CharacterAttrs.ICE_ATTACK: 0,
        CharacterAttrs.ICE_DEFENSE: 0,
        CharacterAttrs.THUNDER_ATTACK: 0,
        CharacterAttrs.THUNDER_DEFENSE: 0,
    }

    def __init__(self):
        super().__init__()
        self._name = ""
        self._hp = 0
        self._mp = 0
        self._lvl = 1
        self._extra = {attr: 0 for attr in CharacterAttrs}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def mp(self) -> int:
        return self._mp
       
    @property
    def level(self) -> int:
        return self._lvl

    @property
    def is_dead(self) -> bool:
        return self.hp <= 0

    def add_hp(self, change: int) -> "Character":
        self._hp = max(0, min(self.get_lvl_attr(CharacterAttrs.MAX_HP), self._hp + change))
        return self

    def add_mp(self, change: int) -> "Character":
        self._mp = max(0, min(self.get_lvl_attr(CharacterAttrs.MAX_MP), self._mp + change))
        return self

    def get_lvl_attr(self, attr: CharacterAttrs) -> int:
        def _c1(x: int) -> int:
            return int(x * self.K[attr] + self._extra[attr])

        def _c2(x: int) -> int:
            return int(self.K[attr] + self._extra[attr])

        if attr in {CharacterAttrs.HIT_RATE}:
            return _c2(self.get_lvl_attr(CharacterAttrs.DEXTERITY))
        elif attr in {CharacterAttrs.MAX_HP}:
            return _c1(self.get_lvl_attr(CharacterAttrs.STRENGTH))
        elif attr in {CharacterAttrs.MAX_MP}:
            return _c1(self.get_lvl_attr(CharacterAttrs.WISDOM))
        return _c1(self._lvl)

    def inc_lvl_attr(self, attr: CharacterAttrs, change: int) -> "Character":
        self._extra[attr] = self._extra[attr] + change
        return self

    def set_full_health(self) -> "Character":
        self.add_hp(self.get_lvl_attr(CharacterAttrs.MAX_HP))
        self.add_mp(self.get_lvl_attr(CharacterAttrs.MAX_MP))
        return self

    def upgrade(self) -> "Character":
        self._lvl += 1
        return self

    def __getstate__(self) -> Dict:
        return {
            "_id": self._id,
            "_name": self._name,
            "_lvl": self._lvl,
            "_hp": self._hp,
            "_mp": self._mp,
            "_eq": self._eqpt
        }

    def __setstate__(self, state: Dict):
        self._id = state["_id"]
        self._name = state["_name"]
        self._hp = state.get("_hp", 0)
        self._mp = state.get("_mp", 0)
        self._lvl = state.get("_lvl", 1)
        self._extra = {attr: 0 for attr in CharacterAttrs}
        # clean all the modules 
        module.ModuleMixin.__init__(self)
        # relearn the skills
        # reequip the equipments
        equipment.EquipableMixin.__init__(self)
        for eq in state.get("_eq", {}).values():
            self.equip(eq)
        # full health
        self.set_full_health()
