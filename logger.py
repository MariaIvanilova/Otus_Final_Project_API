import logging
import os


def create_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Создаем директорию для логов если её нет
    os.makedirs("logs", exist_ok=True)

    # Создаем обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Создаем обработчик для записи логов в файл
    file_handler = logging.FileHandler("logs/log.log", mode="w")
    file_handler.setLevel(logging.DEBUG)

    # Форматирование логов
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger_api = create_logger()
