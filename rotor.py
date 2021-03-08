from rotor_settings import rotor_settings
import helper


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
        self.__ring_setting = ring_setting - 1

        self.notch = rotor_settings[label]["notch"]
        self.position = ord(starting_position) - 65


    def encode_right_to_left(self, char):
        """pass signal from right to left through rotor
        """
        i = self.__offset(char)
        c = helper.convert_index_to_character(self.__contacts, i)
        i = helper.convert_character_to_index(self.__pins, c)

        return self.__reset(i)


    def encode_left_to_right(self, signal):
        """ pass signal from left to right through rotor
        """
        i = self.__offset(signal)
        c = helper.convert_index_to_character(self.__pins, i)
        i = helper.convert_character_to_index(self.__contacts, c)

        return self.__reset(i)

    
    def __offset(self, char):
        """ Offset incoming signal using pos & r. set, return index
        """
        incoming_index = helper.convert_character_to_index(self.__pins, char)
        offset_index = incoming_index + self.position - self.__ring_setting
        wrap_round_index = helper.wrap_round_index(self.__contacts, offset_index)
        return wrap_round_index


    def __reset(self, index):
        """ Reset outgoing signal using pos & r. set, return char
        """
        reset_index = index - self.position + self.__ring_setting
        wrap_round_index = helper.wrap_round_index(self.__contacts, reset_index)
        converted_char = helper.convert_index_to_character(self.__pins, wrap_round_index)
        return converted_char


    def advance(self):
        """moves rotor posistion along onw
        """
        new_position = self.position + 1
        wrap_round_index = new_position % len(self.__contacts)
        self.position = wrap_round_index


    def notched(self):
        """posistion is currently on notch
        """
        if self.notch != "":
            return chr(self.position + 65) in self.notch
        else:
            return False


    def status(self):
        """print rotor status
        """
        print(f"rotor: {self.__label}")
        print(f"pins: {self.__pins}")
        print(f"contacts: {self.__contacts}")
        print(f"notch: {self.notch}")
        print(f"position: {self.position}")
        print(f"ring_setting: {self.__ring_setting}")
        print("-----------------------")


if __name__ == "__main__":
    pass


    