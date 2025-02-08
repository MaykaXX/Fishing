
fish_list = ['karasik']
fish = input("Enter: ")
fish1 = input("Enter: ")
fish_list.extend([fish, fish1])
messagen = input("Delete: ")
if messagen == 'yes':
    fish_list.pop()
    print(fish_list)

