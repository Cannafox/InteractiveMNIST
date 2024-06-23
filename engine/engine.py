import logging
import numpy as np

logger = logging.getLogger('root')


class Engine:

    def __init__(self) -> None:
        logger.info(f"Initializing {self.__class__.__name__}")
        self.data = None

    def get_image_info(self) -> str:
        return f"{type(self.data)} {self.data.dtype} {self.data.shape} [{self.data.min()}; {self.data.max()}]"

    def load_image(self, image_array: np.ndarray) -> None:
        assert isinstance(image_array, np.ndarray)
        logger.info(
            f"Loading image array {image_array.shape} {image_array.dtype}")

        image_array = self._normalize_image(image_array)

        self.data = image_array

    def _normalize_image(self, image_array: np.ndarray) -> np.ndarray:
        logger.info(f"Normalizing image data {image_array.max()}->1.0")

        return image_array / 255.
