import pathlib

def input_path(question):
    input_dictionary_path = input(question).strip("& ").strip("'\"")
    dictionary_path = pathlib.Path(input_dictionary_path)

    if not(dictionary_path.is_file()) or len(input_dictionary_path)==0:
        return 1
    
    return dictionary_path

def read_file(path):
    file = open(path, 'r', encoding="utf-8")
    text = [line for line in file if line.split()]
    file.close()

    if len(text) == 0:
        return 1

    return text

def write_file(path, text):
    file = open(path, 'w', encoding="utf-8")

    file.writelines(text)

    file.close()


def main():
    file_path = input_path("Введите путь файла: ")

    if (file_path == 1):
        print("Неверный путь файла")
        return 1
    
    text = read_file(file_path)

    if text == 1:
        print("Файл пустой")
        return 1
    
    write_file(file_path, text)
main()