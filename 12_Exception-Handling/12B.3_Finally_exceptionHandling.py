def process_file():
    try:
        f = open("C://Course Work//Projects & Self Study//Code-Basics_Python//pythonProject//12_Exception-Handling//data.txt")
        x = 1/10
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("Cleaning up file")
        f.close()


process_file()