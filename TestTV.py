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
    print("TV1's channel is", tv1.get_channel(), "and the volume level is", tv1.get_volume())
    print("TV2's channel is", tv2.get_channel(), "and the volume level is", tv2.get_volume())

# End the program
TestTV()