class Manager:
    def __init__(self) -> None:
        pass
    def clear_file(self, PATH: str):
        try:
            with open(PATH, 'w+') as file:
                file.close()
        except FileNotFoundError as e:
            print(e)