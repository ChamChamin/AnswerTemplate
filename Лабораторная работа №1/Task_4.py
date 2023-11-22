dict_ = {
    "global_count": 0,
    "unique_count": 0
}
global_list = ["Григорий", "Арсений", "Кирилл", "Павел", "Иван", "Евгений", "Марк", "Дмитрий", "Владислав", "Марк",
               "Иван", "Евгений"]

unique_list = list(set(global_list))

dict_["global_count"] = len(global_list)

dict_["unique_count"] = len(unique_list)

print(dict_)