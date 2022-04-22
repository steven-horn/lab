from classes import *


class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        """
        Test init function.
        """
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        """
        Test power toggle
        """
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_up(self):
        """
        Test channel up // Channel doesn't exceed max channel
        """
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 1, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 2, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 3, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        """
        Test channel down // Ensure channel doesn't dip below min value
        """
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 3, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 2, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 1, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        """
        Test volume up function and ensure it doesn't exceed 2
        """
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 1'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 2'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        """
        Test volume down function and make sure it doesn't drop below 0
        """
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 2'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 1'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_volume(self):
        """
        Make sure channel and volume doesn't change when power is turned off
        """
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
