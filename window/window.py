import pygame
import logging
import numpy as np

logger = logging.getLogger('root')


class DrawingWindow:

    def __init__(
        self,
        width: int = 28,
        height: int = 28,
        title: str = "Drawing Window",
        bg_color: pygame.Color = pygame.Color('white')
    ) -> None:
        logger.info(f"Initializing {self.__class__.__name__}")
        pygame.init()

        self._running = True
        self._updated = False

        self.size = (width, height)
        self.title = title
        self.bg_color = bg_color

        self._display_surf = pygame.display.set_mode(
            (width, height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(bg_color)

        logger.info(f"Initialized {title} ({width}x{height})")

    def get_screen_array(self) -> np.ndarray:
        return pygame.surfarray.array3d(self._display_surf)

    def is_running(self) -> bool:
        return self._running

    def process_events(self) -> None:
        self._updated = False
        for event in pygame.event.get():
            self.on_event(event)

    def close(self) -> None:
        pygame.quit()

    def render(self) -> None:
        pygame.display.flip()

    def updated(self) -> bool:
        return self._updated

    def on_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            try:
                logger.debug(f"Pressed {chr(event.key)}")
            except Exception:
                logger.warning(f"{event.key} not convertable to char")
            if event.key == pygame.K_q:
                self._running = False
            if event.key == pygame.K_c:
                pass

        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(surface=self._display_surf,
                               color=(0, 0, 0),
                               center=pygame.mouse.get_pos(),
                               radius=10)

        if event.type == pygame.MOUSEBUTTONUP:
            self._updated = True
