class StringEditor:

    @staticmethod
    def replace_space_to_underscore(string: str):
        return string.replace(' ', '_')

    @staticmethod
    def replace_special_character(string: str):
        for special, no_special in (('?', '？'), ('!', '！')):
            if special in string:
                string = string.replace(special, no_special)
        return string

    @staticmethod
    def remove_tab(string: str):
        return string.replace('    ', '')

    @staticmethod
    def extract_string_after_bracket(line: str):
        if ']' in line:
            name = line.split(']')[1]
            return name.strip()
        else:
            return line.strip()

# 테스트
if __name__ == '__main__':
    TEMPLATE_FOR_LOADING_INPUT_TEXT = '''
    from pathlib import Path
    directory = Path(__file__).parent
    file_name = Path(__file__).stem
    input_text = f"{directory}\{file_name}_input.txt"

    import sys
    sys.stdin = open(input_text)
    input = sys.stdin.readline
    '''

    print(TEMPLATE_FOR_LOADING_INPUT_TEXT)
    print(StringEditor.remove_tab(TEMPLATE_FOR_LOADING_INPUT_TEXT))