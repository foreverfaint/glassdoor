# -*- encoding: utf-8 -*-
from abc import ABC, abstractmethod

from rich import console, table

from engine.models import game_object, character, equipment


class Renderer(ABC):
    @abstractmethod
    def show(self, go: game_object.GameObject):
        pass


class ConsoleRenderer(Renderer):
    def __init__(self):
        self._con = console.Console()

    def show(self, go: game_object.GameObject):
        if isinstance(go, character.Character):
            self._show_ch(go)
        elif isinstance(go, equipment.Equipment):
            self._show_eq(go)
        else:
            pass

    def _show_ch(self, ch: character.Character):
        tbl = table.Table(title=ch.name)

        tbl.add_column("Field", justify="right", style="cyan", no_wrap=True)
        tbl.add_column("Value", justify="right", style="green")

        tbl.add_row("lvl", str(ch.level))
        tbl.add_row("hp", str(ch.hp))
        tbl.add_row("mp", str(ch.mp))
        for attr in character.CharacterAttrs:
            tbl.add_row(attr.value, str(ch.get_lvl_attr(attr)))

        self._con.print(tbl)

    def _show_eq(self, eq: equipment.Equipment):
        tbl = table.Table(title=eq.name())

        tbl.add_column("Field", justify="right", style="cyan", no_wrap=True)
        tbl.add_column("Value", justify="right", style="green")

        tbl.add_row("slot", str(eq.slot()))
        tbl.add_row("effect", eq.desc_effects())
        tbl.add_row("requirements", eq.desc_requirements())
        
        self._con.print(tbl)

