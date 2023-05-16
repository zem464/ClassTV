# Create a class named tv
class TV:
    # Create a constructor
    def __init__(self, channel, volume):
        # Initialize instance variables
        self.channel = channel
        self.volume = volume

# Create an instance method for:
        
    # Turned ON TV
    def TV_on(self):
        self.TV_on = True
    
    # Turned OFF TV
    def TV_off(self):
        self.TV_on = False
        
    # Getting the channel
    def get_channel(self):
        return self.channel
        
    # Setting the channel
    def channel_setting(self, channel):
        if self.TV_on and 1 <= channel <= 120:
            self.channel = channel
        
    # Getting the volume
    def get_volume(self):
        return self.volume
        
    # Setting the volume
    def volume_setting(self, volume):
        if self.TV_on and 1 <= volume <= 7:
            self.volume = volume
        
    # Switching channels up
        
    # Switching channels down
        
    # Turning volume up
        
    # Turning volume down