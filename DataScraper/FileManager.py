class Manager:
    def __init__(self, PATH: str) -> None:
        self.PATH: str = PATH
    def clear_file(self):
        try:
            with open(self.PATH, 'w+', encoding='utf-8') as file:
                file.close()
        except FileNotFoundError as e:
            print(e)