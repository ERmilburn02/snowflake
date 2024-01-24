
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .collections import SoundCollection
from ..engine import Instance
from .asset import Asset
from .sound import Sound

if TYPE_CHECKING:
    from ..engine.game import Game

@dataclass
class GameObject:
    id: int
    name: str
    asset: Asset
    x: int
    y: int
    game: "Game"
    sounds: SoundCollection = SoundCollection()

    def place(self) -> None:
        self.game.send_tag(
            'O_HERE',
            self.id,
            '0:1',  # TODO: Why do 0:1 here?
            self.x,
            self.y,
            0,      # TODO
            1,      # TODO
            0,      # TODO
            0,      # TODO
            0,      # TODO
            '',     # TODO
            '0:1',  # TODO
            0,      # TODO
            1,      # TODO
            0       # TODO
        )

    def move(self) -> None:
        ...

    def animate(self) -> None:
        ...

    def add_sound(
        self,
        name: str,
        looping: bool = False,
        volume: int = 100,
        radius: int = 0
    ) -> None:
        self.sounds.add(
            Sound.from_name(
                name,
                looping,
                volume,
                radius,
                self.id,
                self.id # TODO: Different id for response object?
            )
        )

    def play_sound(self, sound_name: str) -> None:
        sound = self.sounds.by_name(sound_name)
        sound.play(self.game)