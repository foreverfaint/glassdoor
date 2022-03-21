# -*- encoding: utf-8 -*-
from engine.models import character, module


class ChangeCharacterAttrsOnAttachDetach(module.AttachDetachModule):
    def __init__(self, attr: character.CharacterAttrs, change: int):
        super().__init__()
        self._attr = attr
        self._change = change

    def attach(self, target: character.Character):
        target.inc_lvl_attr(self._attr, self._change)

    def detach(self, target: character.Character):
        target.inc_lvl_attr(self._attr, -self._change)

    def desc(self) -> str:
        return f"{self._attr} {'+' if self._change > 0 else ''}{self._change}"