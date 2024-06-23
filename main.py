import logging
from utils import setup_custom_logger
from window import DrawingWindow

logger = setup_custom_logger("root", logging.DEBUG)


def main() -> None:
    app = DrawingWindow(height=28 * 10, width=28 * 10)

    app.init()
    while app.run():
        pass
    app.close()


if __name__ == "__main__":
    main()
