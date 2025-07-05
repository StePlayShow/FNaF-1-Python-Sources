from pygame.image import load, save
from pygame.transform import scale
from os import path, sep
import sys

_image_library = {}
def get_image(img_path: str, alpha: int, size: tuple[int, int] = None):
    image = _image_library.get(img_path)
    if image is None:
        full_path = resource_path(img_path)
        #try:
        image = load(full_path).convert_alpha()
        #except FileNotFoundError:
            #image = pygame.image.load("data/sprites/NoImage.png").convert_alpha()
        _image_library[img_path] = image
    if size is not None:
        image = scale(image, size)
    image.set_alpha(alpha)
    return image

def remove_image(img_path: str):
    _image_library[img_path] = None

def screenshot(display1, num):
    save(display1, resource_path(f'data/sprites/Screen/screenshot_{num}.png'))

def resource_path(relative_path: str) -> str:
    if sys.platform == "darwin":  # macOS
        base_path = path.abspath(
            path.join(path.dirname(sys.executable), "..", "..", "..")
            # здесь можно добавить или убрать ".." в зависимости от глубины вложенности
        )
    else:  # Windows или Linux
        if getattr(sys, 'frozen', False):
            base_path = path.dirname(sys.executable)
        else:
            base_path = path.dirname(path.abspath(__file__))

    canonical_path = relative_path.replace('/', sep)
    return path.join(base_path, canonical_path)