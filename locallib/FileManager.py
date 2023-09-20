import logger

FileLogger = logger.setup_logging("FileManager", False)

def clear_file(path: str) -> None:
    try:
        with open(path, 'w+', encoding='utf-8') as file:
            file.close()
    except FileNotFoundError as err:
        FileLogger.error(f"clear_file: {err}")