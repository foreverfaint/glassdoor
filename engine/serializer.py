# -*- encoding: utf-8 -*-
import pickle
from pathlib import Path

from engine.models import character


def dumps(file: Path, ch: character.Character):
    file.parent.mkdir(parents=True, exist_ok=True)
    with file.open("wb") as f:
        pickle.dump(ch, f)


def loads(file: Path) -> character.Character:
    with file.open("rb") as f:
        return pickle.load(f)
