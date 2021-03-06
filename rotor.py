from rotor_settings import rotor_settings


class Rotor:
    def __init__(self, label, pins=rotor_settings["Base"]["settings"], starting_position="A", ring_setting=1):
        """initiate a rotor
            params:
                label: string
                pins: string
                starting_position: string
                ring_setting: int
        """
        self.__label = label
        self.__pins = pins
        self.__contacts = rotor_settings[label]["settings"]
        self.__notch = rotor_settings[label]["notch"]

        self.__position = ord(starting_position) - 65
        self.__ring_setting = ring_setting - 1


    def encode_right_to_left(self, char):
        """"""""
        pass

    def encode_left_to_right(self, char):
        """"""
        pass


    def status(self):
        """print rotor status
        """
        print(f"rotor: {self.__label}")
        print(f"pins: {self.__pins}")
        print(f"contacts: {self.__contacts}")
        print(f"notch: {self.__notch}")
        print(f"position: {self.__position}")
        print(f"ring_setting: {self.__ring_setting}")
        print("-----------------------")


if __name__ == "__main__":
    r = Rotor("I")
    r.status()
    assert(r.encode_right_to_left("A") == "E")

    r = Rotor("I", ring_setting=1, starting_position="M")
    assert r.encode_right_to_left("S") == "B"

    assert(r.encode_left_to_right("A") == "U")