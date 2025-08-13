try:
    with open("myfile.txt", "r") as file:
        for index,line in enumerate(file,start=100):
            print(index,line)
except FileNotFoundError:
    print("THE FILE IS NOT FOUND")