import os


def get_Start_with():
    print("Bulk Directory Deletion Tool")
    print("Type Exit to quit anytime")
    res = input("What does your file start with? ")
    if res.lower() == 'exit':
        print("Goodbye!")
    else:
        conf = input(f'Confirm:: {res} (Y|n) ')
        if conf.lower() == 'y':
            remove_folder(res)
        elif conf.lower() == 'exit' or conf.lower() == 'n':
            new_res = input('Would you like to continue? (y/n)')
            if new_res.lower() == 'y':
                return get_Start_with()
            else:
                print("Goodbye!")
        else:
            return get_Start_with()


def remove_folder(item_name):
    for item in os.listdir():
        if item.startswith(f'{item_name}'):
            os.rmdir(item)
            print(f"clean up {item}")
            


# used to create test folder to remove
def test_folder_maker():
    for i in range(10):
        os.mkdir(f'Mytest{i}')

#test_folder_maker()

           
get_Start_with()