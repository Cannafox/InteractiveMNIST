import pygame
import logging
from typing import Union

logger = logging.getLogger('root')


class DrawingWindow:
    _instance = None

    def __new__(cls, *args, **kwargs):
        logger.info(f"Initializing {cls.__name__}")
        if cls._instance is None:
            cls._instance = super(DrawingWindow, cls).__new__(cls)
            cls._instance.__initialize(*args, **kwargs)

        return cls._instance

    def __initialize(self,
                     width: int = 28,
                     height: int = 28,
                     title: str = "Drawing Window"):
        self._running = True
        self._display_surf = Union[None, pygame.surface.Surface]

        self.size = (width, height)
        self.title = title

        logger.info(f"Initialized {title} ({width}x{height})")

    def init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill((255, 255, 255))
        logger.error(type(self._display_surf))
        self._running = True

    def run(self):
        for event in pygame.event.get():
            self.on_event(event)
        self.on_loop()
        self.on_render()

        return self._running

    def close(self):
        pygame.quit()

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            # logger.debug(f"Pressed {chr(event.key)}")
            if event.key == pygame.K_q:
                self._running = False
            if event.key == pygame.K_c:
                pass

        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(surface=self._display_surf,
                               color=(0, 0, 0),
                               center=pygame.mouse.get_pos(),
                               radius=10)
