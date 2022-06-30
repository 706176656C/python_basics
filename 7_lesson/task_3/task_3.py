import os

FILES = ['1.txt', '2.txt', '3.txt']


def merging():
    result_file = 'result.txt'
    files_dict = {}

    for file in FILES:
        with open(os.path.join(os.getcwd(), file)) as reading_file:
            len_in_dict = len(reading_file.readlines())
            if len_in_dict not in files_dict.keys():
                files_dict[len_in_dict] = list(file.split())
            else:
                files_dict.get(len_in_dict).append(file)

    sort_key = sorted(files_dict.keys())
    files_sort_dict = {num: files_dict[num] for num in sort_key}

    with open(os.path.join(os.getcwd(), result_file), 'w') as result:
        for quantity_str, name_file in files_sort_dict.items():
            for item in range(len(name_file)):
                result.write(str(name_file[item]) + '\n')
                result.write(str(quantity_str) + '\n')
                with open(os.path.join(os.getcwd(), name_file[item])) as reading_file:
                    for rw_string in reading_file:
                        result.write(rw_string + reading_file.readline())
                result.write('\n')
    return


merging()
