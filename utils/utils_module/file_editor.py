from .string_editor import StringEditor


class FileEditor:
    directory = ''
    file_names = []

    def __init__(self, directory, file_names: list[str]) -> None:
        self.directory = directory
        self.file_names = file_names

    def insert_template_for_python(self):
        TEMPLATE_FOR_LOADING_INPUT_TEXT = '''\
        from pathlib import Path
        directory = Path(__file__).parent
        file_name = Path(__file__).stem
        input_text = f"{directory}\{file_name}_input.txt"

        import sys
        sys.stdin = open(input_text)
        input = sys.stdin.readline
        '''

        for file_name in self.file_names:
            f = open(f"{self.directory}\{file_name}.py", "a", encoding="UTF8")
            f.write(StringEditor.remove_tab(TEMPLATE_FOR_LOADING_INPUT_TEXT))
            f.close()
