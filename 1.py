import pathlib

def read_file(question):

    input_dictionary_path = input(question).strip("& ").strip("'\"")
    dictionary_path = pathlib.Path(input_dictionary_path)

    if not(dictionary_path.is_file()) or len(input_dictionary_path)==0:
        return 1
    
    file = open(dictionary_path, 'r', encoding="utf-8")
    text = file.read().split()
    file.close()

    if len(text) == 0:
        return 2

    return text

def main():
    dict_list = read_file("Введите путь к файлу словаря: ")

    if dict_list == 1:
        print ("Неверный путь файла")
        return 1
    elif dict_list == 2:
        print ("Файл пуст")
        return 1
    
    file_list = read_file("Введите путь к файлу со словами: ")

    if file_list == 1:
        print ("Неверный путь файла")
        return 1
    elif file_list == 2:
        print ("Файл пуст")
        return 1
    
    for word in file_list:
        check = False
        for d_word in dict_list:
            if word == d_word:
                check = True
        if not(check):
            print (f"{word} нет в словаре")

    return 0

main()