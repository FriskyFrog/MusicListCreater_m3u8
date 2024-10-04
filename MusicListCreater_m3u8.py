import os

def getInput():
    #Show options.
    #[0]=>Quit without alarming.
    #[1]=>Generate files(processOption()).
    #[2]=>Print usage then quit.
    print("\
        [0]Quit.(default)\n\
        [1]Generate lists\n\
        [2]Print usage and quit.\n")
    #Get option.
    user_input = input("Choose a option:")
    return user_input

def processOption():
    #Target parent_dir.
    parent_dir = input('Enter the targeted parent_dir(default: ~/音乐, "." for current folder): ')
    #Change dir.
    if parent_dir == "":
        os.chdir("/home/%s/音乐"%(os.getlogin()))
    elif parent_dir != ".":
        os.chdir(parent_dir)
    #Get content of parent_dir.
    parent_list = os.listdir()
    #Quit if empty.
    if parent_list == []:
        exit(1)

    #Fetch names of sub_dir by iterating parent_dir.
    for sub_list_name in parent_list:
        #Neglect m3u8lists and scripts.
        if ("py" in sub_list_name) or ("m3u8" in sub_list_name):
            continue

        #Create list for specific sub_dir.
        #This must be done first, having the list file be created in parent_dir.
        m3u8list = open("./%s.m3u8"%(sub_list_name), mode = "w")

        #Change dir, ensuring that it is generating list for sub_dir.
        os.chdir(sub_list_name)
        #Fetch current dir.
        sub_list_dir = os.getcwd()

        #Get names of music then sort, forming a sequence of A~Z, making it neat.
        sub_list = os.listdir()
        sub_list.sort()

        #Iterate each name in sub_dir.
        for sub_list_file in sub_list:
            #Neglect the lyric files (*.lrc).
            if not ((".mp3" in sub_list_file) or (".flac" in sub_list_file)):
                continue
            #Add path to file.
            m3u8list.write(sub_list_dir+"/"+sub_list_file+"\n")
        #Save list.
        m3u8list.close()
        #Return to parent_dir, prepareing to make list for another sub_dir.
        os.chdir("..")
    print("Lists successfully generated.")

def chooseMethod(user_input):
    if user_input == "1":
        return lambda: processOption()
    if user_input == "2":
        #Usage attached here.
        return lambda: print("Usage:\n\
            ##Structure            ##Concept\n\
                                   \n\
            parent_dir             #parent_dir\n\
            |___sub_dir01          The folder contains all the files.\n\
                |___music01.mp3    Generated m3u8lists will be here,\n\
                |___music02.mp3    which are named after names of the sub_dir.\n\
                |___musicxx.mp3    #sub_dir\n\
                |___...            Adequate classified ones.\n\
            |___sub_dir02          \n\
                |___...            ##Notice\n\
            |___sub_dirxx...       \n\
                |___...            Files will be neglected, except *.mp3 and *.flac.\n\
            |___sub_dir01.m3u8     Do not put files in the parent_dir, except *.py and *.m3u8.\n\
            |___sub_dir02.m3u8     \n\
            |___sub_dirxx.m3u8     \n\
            |___...                \n\
            ")
    #Quit if anything except "1" or "2" is entered.
    else:
        return lambda: print("quit"); exit(0)

def main():
    #Get input from console.
    userInput = getInput()
    #Match function then execute.
    processingMethod = chooseMethod(userInput)
    processingMethod()
    exit(0)

main()
