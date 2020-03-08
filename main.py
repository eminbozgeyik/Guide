import pickle
import os


def display_menu():
    print("1. Kayıtları listele")
    print("2. Kayıtları Ara")
    print("3. Kayıt Ekle")
    print("4. Kayıt Sil")
    print("5. Çıkış")
    print()


def menu_loop():
    while True:
        display_menu()
        option = input("Seçenek (1-5): ")
        print("\n")
        if option.isdigit() and 1 <= int(option) <= 5:
            break
    return option


def main_loop():
    while True:
        option = menu_loop()
        if option == "1":
            list_records()
        elif option == "2":
            search_record()
        elif option == "3":
            add_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            break


def list_records():
    records_list = read_file()
    print(f"Kayıt Sayısı: {len(records_list)}\n")
    print(f"{'İsim':^10} {'Soyisim':^10} {'Telefon':^11}")
    for record in records_list:
        print(
            f"{record.get('name',' '):10.10} {record.get('second_name',' '):10.10}{record.get('tel_number',' '):11.11}")


print()


def search_record():
    print("Kayıt Arama")
    name = input("İsim: ")
    second_name = input("Soyisim: ")
    records_list = search_record_from_file(name, second_name)
    print("Telefon Numarası: ", end='')
    for record in records_list:
        print(f"{record.get('tel_number'):11.11}", end='')
    print("\n")


def add_record():
    print("Yeni Kayıt Ekle")
    name = input("İsim: ")
    second_name = input("Soyisim: ")
    tel_number = input("Telefon Numarası: ")
    print(f"Yeni kayıt: {name} {second_name} - {tel_number}")
    if are_you_sure():
        add_record_to_file(name, second_name, tel_number)
        print("Kayıt Eklendi\n")


def delete_record():
    print("Kayıt Silmek")
    name = input("İsim: ")
    second_name = input("Soyisim: ")
    records_list = search_record_from_file(name, second_name)
    print("Telefon Numarsı: ", end='')
    for record in records_list:
        print(f"{record.get('tel_number'):11.11}", end='')
    print("\n")
    if are_you_sure():
        delete_records_from_file(records_list)
        print("Kayıt Silindi!\n")


def are_you_sure():
    while True:
        answer = input(" Emin misiniz? (E)vet/(H)ayır: ")
        print()
        if answer.upper() == "E":
            return True
        elif answer.upper == "H":
            return False


def read_file():
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as fileObject:
            records_list = pickle.load(fileObject)
    else:
        records_list = list()
    return records_list


def write_file(records_list_param: list):
    with open("data.bin", "wb") as fileObject:
        pickle.dump(records_list_param, fileObject)


def search_record_from_file(name_param: str, second_name_param: str):
    records_list = read_file()
    response_list = list()
    for record in records_list:
        if record.get("name").upper() == name_param.upper() and \
                record.get("surname").upper() == second_name_param.upper():
            response_list.append(record)
    return response_list


def delete_records_from_file(records_list_param: list):
    records_list = read_file()
    for record in records_list:
        for record_for_delete in records_list_param:
            if record.get("name") == record_for_delete.get("name") and \
                    record.get("second_name") == record_for_delete.get("second_name"):
                records_list.remove(record_for_delete)
                continue
    write_file(records_list)


def add_record_to_file(name_param: str, second_name_param: str, tel_number_param: str):
    records_list = read_file()
    record_dict = dict(name=name_param, second_name=second_name_param, tel_number=tel_number_param)
    records_list.append(record_dict)
    write_file(records_list)


main_loop()
