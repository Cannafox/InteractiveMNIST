import logging
from utils import setup_custom_logger
from window import DrawingWindow
from engine import Engine

logger = setup_custom_logger("root", logging.DEBUG)


def main() -> None:
    app = DrawingWindow(height=28 * 10, width=28 * 10)
    engine = Engine()

    while app.is_running():
        app.process_events()
        app.render()

        if app.updated():
            engine.load_image(app.get_screen_array())

            logger.debug(engine.get_image_info())

    app.close()


if __name__ == "__main__":
    main()
