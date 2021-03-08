from rotor_settings import rotor_settings
import helper


class Rotor:
    def __init__(self, label, pins=rotor_settings["Base"]["settings"], starting_position="A", ring_setting=1):
        """initiate a version of the rotor
            params:
                label: string
                pins: string
                starting_position: string
                ring_setting: int
        """
        if type(label) != str:
            raise ValueError('Rotor label should be of string')
        if rotor_settings.get(label,"") == "":
            raise ValueError('Rotor label not available in the rotor settings')

        if type(pins) != str:
            raise ValueError('Rotor pins should be of type string')

        if type(starting_position) != str or len(starting_position) > 1:
            raise ValueError('Rotor starting posistion should be a single character string')
        if ord(starting_position) - 65 < 0 or ord(starting_position) - 65 > 25 :
            raise ValueError('Rotor starting posistion should be within the range of A-Z')

        if type(ring_setting) != int:
            raise ValueError('Rotor ring setting should be an int')
        if ring_setting < 1 or ring_setting > 26:
            raise ValueError('Rotor ring setting should be within the range 1-26')

        self.__label = label
        self.__pins = pins
        self.__contacts = rotor_settings[label]["settings"]
        self.__ring_setting = ring_setting - 1

        self.notch = rotor_settings[label]["notch"]
        self.position = ord(starting_position) - 65


    def encode_right_to_left(self, signal):
        """signal from r/l through rotor
            params:
                signal: string
        """
        # get offset using pos & ring set
        i = self.__offset(signal)
        # convert to contacts char
        c = helper.convert_index_to_character(self.__contacts, i)
        # convert to pin index
        i = helper.convert_character_to_index(self.__pins, c)
        # reset to char using pos & ring set
        c = self.__reset(i)

        return c


    def encode_left_to_right(self, signal):
        """signal from l/r through rotor
            params:
                signal: string
        """
        # get offset using pos & ring set
        i = self.__offset(signal)
        # convert to pins char
        c = helper.convert_index_to_character(self.__pins, i)
        # convert to contacts index
        i = helper.convert_character_to_index(self.__contacts, c)
        # reset to char using pos & ring set
        c =  self.__reset(i)

        return c

    
    def __offset(self, signal):
        """ Offset incoming signal using pos & r. set
                params:
                    char: string
        """
        # convert signal to pins index
        incoming_index = helper.convert_character_to_index(self.__pins, signal)
        # offset with pos - ring setting
        offset_index = incoming_index + self.position - self.__ring_setting
        # wrap round to ensure over hang dealt with
        wrap_round_index = helper.wrap_round_index(self.__contacts, offset_index)

        return wrap_round_index


    def __reset(self, index):
        """ Reset outgoing signal using pos & r. set
                params:
                    index: int
        """
        # reset index with pos & ring set
        reset_index = index - self.position + self.__ring_setting
        # wrap round to ensure over hang dealt with
        wrap_round_index = helper.wrap_round_index(self.__contacts, reset_index)
        # convert signal back to character
        converted_signal = helper.convert_index_to_character(self.__pins, wrap_round_index)

        return converted_signal


    def advance(self):
        """advances rotor posistion by one
        """
        # move position forward once
        new_position = self.position + 1
        # deal with wrap round overhang
        wrap_round_index =  helper.wrap_round_index(self.__contacts,new_position)
        
        self.position = wrap_round_index


    def check_rotor_notched(self):
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


    