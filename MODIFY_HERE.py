

def hello():
    print("Hello World!")
    print("Nicole and Aliyah are teaching Git!")
    
    # TO DO: Add your name / a message here!
    print("An Undercover Unicorn was here")
    print("Said Unicorn apparently knows python.")
    print("ANd is powered by Magic Fairy Dust and Nix........ :/")

    print("I am a unicorn and I am powered by magic fairy dust")
    print("A dark unicorn has entered the chat. I am powered by dark magic and Nix.")
    for i in range(100):
        create_file("Nix_pkg" + str(i) + ".txt", i)

hello()
 


#THis creates the empty file, and saves it to the system
def create_file(filename,count):
    # THis is a function that will create a bunch of files on your system
    # This is a very dangerous function
    # It should be removed
    # It is a security risk
    with open(filename, 'w') as file:
        file.write("This file was created by a unicorn")
        print("A dark unicorn has struck with Nix")
