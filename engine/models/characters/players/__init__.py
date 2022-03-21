# -*- encoding: utf-8 -*-
from engine.models import character


class Assassin(character.Character):
    K = {
        character.CharacterAttrs.STRENGTH: 2,
        character.CharacterAttrs.WISDOM: 2,
        character.CharacterAttrs.DEXTERITY: 4,
        character.CharacterAttrs.MAX_HP: 20,
        character.CharacterAttrs.MAX_MP: 10,
        character.CharacterAttrs.HIT_RATE: 50,
        character.CharacterAttrs.MELEE_ATTACK: 2,
        character.CharacterAttrs.MELEE_DEFENSE: 2,
        character.CharacterAttrs.FIRE_ATTACK: 0,
        character.CharacterAttrs.FIRE_DEFENSE: 0,
        character.CharacterAttrs.ICE_ATTACK: 0,
        character.CharacterAttrs.ICE_DEFENSE: 0,
        character.CharacterAttrs.THUNDER_ATTACK: 0,
        character.CharacterAttrs.THUNDER_DEFENSE: 0,
    }

    def __init__(self):
        super().__init__()


class Warrior(character.Character):
    K = {
        character.CharacterAttrs.STRENGTH: 4,
        character.CharacterAttrs.WISDOM: 2,
        character.CharacterAttrs.DEXTERITY: 2,
        character.CharacterAttrs.MAX_HP: 30,
        character.CharacterAttrs.MAX_MP: 10,
        character.CharacterAttrs.HIT_RATE: 50,
        character.CharacterAttrs.MELEE_ATTACK: 2,
        character.CharacterAttrs.MELEE_DEFENSE: 2,
        character.CharacterAttrs.FIRE_ATTACK: 0,
        character.CharacterAttrs.FIRE_DEFENSE: 0,
        character.CharacterAttrs.ICE_ATTACK: 0,
        character.CharacterAttrs.ICE_DEFENSE: 0,
        character.CharacterAttrs.THUNDER_ATTACK: 0,
        character.CharacterAttrs.THUNDER_DEFENSE: 0,
    }

    def __init__(self):
        super().__init__()


class Mage(character.Character):
    K = {
        character.CharacterAttrs.STRENGTH: 2,
        character.CharacterAttrs.WISDOM: 4,
        character.CharacterAttrs.DEXTERITY: 2,
        character.CharacterAttrs.MAX_HP: 30,
        character.CharacterAttrs.MAX_MP: 10,
        character.CharacterAttrs.HIT_RATE: 50,
        character.CharacterAttrs.MELEE_ATTACK: 2,
        character.CharacterAttrs.MELEE_DEFENSE: 2,
        character.CharacterAttrs.FIRE_ATTACK: 0,
        character.CharacterAttrs.FIRE_DEFENSE: 0,
        character.CharacterAttrs.ICE_ATTACK: 0,
        character.CharacterAttrs.ICE_DEFENSE: 0,
        character.CharacterAttrs.THUNDER_ATTACK: 0,
        character.CharacterAttrs.THUNDER_DEFENSE: 0,
    }

    def __init__(self):
        super().__init__()


class Monk(character.Character):
    K = {
        character.CharacterAttrs.STRENGTH: 2,
        character.CharacterAttrs.WISDOM: 3,
        character.CharacterAttrs.DEXTERITY: 3,
        character.CharacterAttrs.MAX_HP: 20,
        character.CharacterAttrs.MAX_MP: 20,
        character.CharacterAttrs.HIT_RATE: 50,
        character.CharacterAttrs.MELEE_ATTACK: 2,
        character.CharacterAttrs.MELEE_DEFENSE: 2,
        character.CharacterAttrs.FIRE_ATTACK: 0,
        character.CharacterAttrs.FIRE_DEFENSE: 0,
        character.CharacterAttrs.ICE_ATTACK: 0,
        character.CharacterAttrs.ICE_DEFENSE: 0,
        character.CharacterAttrs.THUNDER_ATTACK: 0,
        character.CharacterAttrs.THUNDER_DEFENSE: 0,
    }
    