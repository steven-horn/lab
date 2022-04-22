class Television:
    """
    Class to represent the Television objects.
    """
    min_channel = 0     # Minimum TV channel
    max_channel = 3     # Maximum TV channel

    min_volume = 0      # Minimum TV volume
    max_volume = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default state.
        """
        self.__tv_power: bool = False
        self.__tv_channel: int = Television.min_channel
        self.__tv_volume: int = Television.min_volume

    def power(self) -> None:
        """
        Method to toggle power
        """
        if self.__tv_power == False:
            self.__tv_power = True
        else:
            self.__tv_power = False

    def channel_up(self) -> None:
        """
        Method to change channel counting up
        """
        if self.__tv_power == True:
            if self.__tv_channel == Television.max_channel:
                self.__tv_channel = Television.min_channel
            else:
                self.__tv_channel += 1

    def channel_down(self) -> None:
        """
        Method to change channel counting down
        """
        if self.__tv_power == True:
            if self.__tv_channel == Television.min_channel:
                self.__tv_channel = Television.max_channel
            else:
                self.__tv_channel -= 1

    def volume_up(self) -> None:
        """
        Method to turn volume up
        """
        if self.__tv_power == True:
            if self.__tv_volume != Television.max_volume:
                self.__tv_volume += 1

    def volume_down(self) -> None:
        """
        Method to turn volume down
        """
        if self.__tv_power == True:
            if self.__tv_volume != Television.min_volume:
                self.__tv_volume -= 1

    def __str__(self) -> str:
        """
        Method to portray the status
        :return: Status, channel, volume
        """
        return f'TV Status: Is on = {self.__tv_power}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}'
