def compile(bFile : list):
    memory : list = [0] * 2000
    pointer : int = 0
    i : int = 0
    while i < len(bFile):
        if bFile[i] == ">":
            pointer += 1
        elif bFile[i] == "<":
            pointer -= 1
        elif bFile[i] == "+":
            if memory[pointer] < 255:
                memory[pointer] += 1
            else:
                memory[pointer] = 0
        elif bFile[i] == "-":
            if memory[pointer] > 0:
                memory[pointer] -= 1
            else:
                memory[pointer] = 255
        elif bFile[i] == ".":
            print(chr(memory[pointer]), end="")
        elif bFile[i] == ",":
            memory[pointer] = ord(input())
        elif bFile[i] == "[":
            if memory[pointer] == 0:
                count = 1
                while count > 0:
                    i += 1
                    if bFile[i] == "[":
                        count += 1
                    elif bFile[i] == "]":
                        count -= 1
        elif bFile[i] == "]":
            if memory[pointer] != 0:
                count = 1
                while count > 0:
                    i -= 1
                    if bFile[i] == "]":
                        count += 1
                    elif bFile[i] == "[":
                        count -= 1
        i += 1

if __name__ == "__main__":
    print("\033[91m" + " _           _     ___         _   \n| |_ ___ ___|_|___|  _|_ _ ___| |_ \n| . |  _| .'| |   |  _| | |  _| '_|\n|___|_| |__,|_|_|_|_| |___|___|_,_|" + "\033[0m")
    print("")
    while True:
        command = input("> ")
        commands = command.split(" ")
        if commands[0] == "quit":
            break
        elif commands[0] == "help" or commands[0] == "-h":
            print("file to compile")
            print("doc to see the doc")
            print("file -see to see the code")
            print("quit to quit")
        elif len(commands) == 2 and commands[1] == "-see":
            try:
                print(open(commands[0], 'r').read())
            except:
                print(commands[0] + " not a file")
        elif command[0:4] == "doc":
            print("language :")
            print("> = moves the pointer to the right 1 block")
            print("< = moves the pointer to the left 1 block")
            print("+ = increases value stored at the block pointed to by the memory pointer")
            print("- = decreases value stored at the block pointed to by the memory pointer")
            print("[ = enter a loop if value is not equal to 0")
            print("] = jump back to [ if value is not equal to 0")
            print(". = print the ascii character from the value")
            print(", = input the ascii value of the character in the value")
            print("")
        else:
            if len(commands) > 1:
                print("unexistant : " + commands[1])
            else:
                try:
                    file = open(commands[0], 'r').read()
                    try:
                        compile(file)
                        print("")
                    except KeyboardInterrupt:
                        print("Interrupt")
                except FileNotFoundError:
                    print(commands[0] + " not a file")
                except:
                    print("error")