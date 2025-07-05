from typing import SupportsIndex
from pygame.mixer import Sound
from ImageManager import resource_path

_audio_channels: list[Sound] = list[Sound]([None] * 52)

def set_sound(path: str, channel: SupportsIndex):
    full_path = resource_path(path)
    sound = Sound(full_path)
    _audio_channels[channel] = sound

def get_sound(channel: int):
    return _audio_channels[channel]