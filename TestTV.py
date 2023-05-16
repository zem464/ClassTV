# import the functions of tv class
from ClassTV import TV

# Create a program for testing
def TestTV():
    tv1 = TV("", "")
    tv2 = TV("", "")    

    # Assign the values for TV1
    tv1.channel_setting(30)
    tv1.volume_setting(3)
    tv1.TV_on()

    # Assign the values for TV2
    tv2.channel_setting(3)
    tv2.volume_setting(2)
    tv2.TV_on()

    # Print the values

# End the program
