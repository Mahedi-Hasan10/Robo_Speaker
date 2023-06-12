import os
if __name__ == '__main__':
    print("Welcome to robo speaker created by Mahedi")
    while True:
        x = input("Enter what you want to pronounce : ")
        if x == 'q':
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)
