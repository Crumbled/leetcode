def import_dict(filename):
    dict_w = {}
    with open(filename, 'r',encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            k, v = line.strip('\n').split(':')
            dict_w.update({k: v})
    return dict_w