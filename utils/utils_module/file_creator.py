class FileCreator:
    directory = ''
    file_names = []

    def __init__(self, directory: str, file_names: list[str]) -> None:
        self.directory = directory
        self.file_names = file_names
    
    def create_python_source(self):
        for file_name in self.file_names:
            f = open(f"{self.directory}\{file_name}.py", "w", encoding="UTF8")
            f.close()
    
    def create_input_text(self):
        for file_name in self.file_names:
            f = open(f"{self.directory}\{file_name}_input.txt", "w", encoding="UTF8")
            f.close()
    
    def create_output_text(self):
        for file_name in self.file_names:
            f = open(f"{self.directory}\{file_name}_output.txt", "w", encoding="UTF8")
            f.close()
