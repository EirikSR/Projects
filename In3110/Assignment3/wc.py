import sys
import os


def split(word):  # Splits words into characters
    return [c for c in word]


def get_file_info(
    name, type_
):  # Function for counting words, characters and lines from file

    with open(name + "." + type_, "r") as f:
        line = f.readline()
        line_cnt = 1
        word_cnt = 0
        char_cnt = 0
        while line:
            # print("--" + line + "--")
            line = f.readline()
            line_strip = line.strip()
            string_length = len(line_strip.split())
            # print(string_length)
            char_length = len(split(line))
            line_cnt += 1
            word_cnt += string_length
            char_cnt += char_length

    print([line_cnt, word_cnt, char_cnt, name + "." + type_])


file_name = sys.argv[1]
wd = os.getcwd()
file_lst = os.listdir(wd)

if split(file_name)[0] == "*":  # checks if multiple files are to be counted
    # print(file_lst)

    specific_file = False

    try:
        c = split(file_name)[1]
        specific_file = True
    except:
        specific_file = False

    if specific_file == True:  # For counting all files of specific type
        c = split(file_name)[1]
        type_target = file_name.split(".")[1]

        for file_ in file_lst:

            if (
                split(file_)[0] != "." and split(file_)[0] != "_"
            ):  # Avoids files such as .gitignore
                name, type_ = file_.split(".")
                if type_ == type_target:
                    get_file_info(name, type_)

    elif specific_file == False:  # Counting all files
        for file_ in file_lst:
            if (
                split(file_)[0] != "." and split(file_)[0] != "_"
            ):  # Avoids files such as .gitignore
                name, type_ = file_.split(".")
                get_file_info(name, type_)

    else:
        print("Error, no file format found after *")

else:  # Counts for one specific file
    try:
        name, type_ = file_name.split(".")
        get_file_info(name, type_)
    except:
        print("Error, filename not in directory")