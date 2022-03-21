# -*- encoding: utf-8 -*-
from pathlib import Path


if __name__ == "__main__":
    from engine import serializer
    from engine.renderer import ConsoleRenderer
    from engine.models.characters import players
    
    renderer = ConsoleRenderer()

    player1 = players.Assassin()
    player1.set_full_health()
    player1.name = "褪色者"
    renderer.show(player1)

    player2 = players.Monk()
    player2.set_full_health()
    player2.name = "将军"
    renderer.show(player2)
    serializer.dumps(Path("./.cache/player2.pickle"), player2)

    from engine.models.equipments.weapons import Sword, Shield
    sword = Sword()
    shield = Shield()

    player1.equip(sword)
    player1.equip(shield)
    serializer.dumps(Path("./.cache/player1.pickle"), player1)

    player1.unequip(sword.slot())
    renderer.show(player1)

    player3 = serializer.loads(Path("./.cache/player1.pickle"))
    renderer.show(player3)
    
    