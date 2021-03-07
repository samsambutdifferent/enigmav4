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
        self.__ring_setting = ring_setting - 1

        self.notch = rotor_settings[label]["notch"]
        self.position = ord(starting_position) - 65


    def encode_right_to_left(self, char):
        """
            TODO update
        """
        in_contact_index = self._get_contact_in(char)
        pin_index = self._char_to_index(self.__contacts[in_contact_index])
        return self._get_contact_out(pin_index)


    def encode_left_to_right(self, char):
        """ TODO Update
        """
        in_contact_index = self._get_contact_in(char)
        contact_char = self._index_to_char(in_contact_index)
        pin_index = self.__contacts.index(contact_char)
        return self._get_contact_out(pin_index)

    
    def _get_contact_in(self, char):
        """
        TODO UPDATE
        Adjust an input character based on the current position and rotor's
        setting
        """
        in_contact_index = self._char_to_index(char)
        return (
            in_contact_index + self.position - self.__ring_setting
        ) % len(self.__contacts)


    def _get_contact_out(self, index):
        """
        TODO UPDATE
        Get the exit character for a given contact adjusting based on current
        position and rotor's setting
        """
        contact_out_index = (index - self.position +
                            self.__ring_setting) % len(self.__contacts)
        return self._index_to_char(contact_out_index)


    def _char_to_index(self, char: str):
        """
        TODO UPDATE
        Convert an input character into an index in the rotor's alphabet
        """
        try:
            return self.__pins.index(char)
        except:
            raise ValueError("Notch not in rotor pattern! " + char)


    def _index_to_char(self, index: int):
        """
        TODO UPDATE
        Convert an index in the rotor's alphabet into a character
        """
        return self.__pins[index]


    def rotate(self):
        """
        TODO UPDATE
        Trigger a rotation of this rotor. It will wrap around if it reaches
        the last position available
        """
        self.position = (self.position + 1) % len(self.__contacts)

    def get_posistion(self):
        return chr(self.position + 65)

    def has_notch(self):
        """
        TODO Update
        Return True if this rotor has any notches
        """
        return self.notch is not None and len(self.notch) > 0

    def is_on_notch(self):
        """
        TODO Update
        Return True if the current position is on a notch
        """
        return self.has_notch() and self.get_posistion() in self.notch


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
    r = Rotor("I")
    r.status()
    assert(r.encode_right_to_left("A") == "E")
    assert(r.encode_left_to_right("A") == "U")

    # r = Rotor("I", ring_setting=1, starting_position="M")
    # assert r.encode_right_to_left("S") == "B"

    r = Rotor("III", starting_position="Z")
    assert r.encode_right_to_left("A") == "P"
    assert r.encode_left_to_right("A") == "N"


    r = Rotor("III", ring_setting=2)
    assert r.encode_right_to_left("A") == "P"


    r = Rotor("III", ring_setting=3)
    assert r.encode_right_to_left("A") == "S"
    assert r.encode_left_to_right("A") == "Q"


    r = Rotor(label="III", starting_position="B", ring_setting=26)
    assert r.encode_right_to_left("L") == "L"
    r = Rotor(label="III", starting_position="C", ring_setting=26)
    assert r.encode_right_to_left("O") == "T"
    r = Rotor(label="III", starting_position="D", ring_setting=26)
    assert r.encode_right_to_left("V") == "K"
    r = Rotor(label="III", starting_position="E", ring_setting=26)
    assert r.encode_right_to_left("E") == "O"
    assert r.encode_left_to_right("P") == "R"
    r = Rotor(label="III", starting_position="F", ring_setting=26)
    assert r.encode_right_to_left("I") == "S"
    assert r.encode_left_to_right("S") == "I"
    r = Rotor(label="III", starting_position="G", ring_setting=26)
    assert r.encode_right_to_left("S") == "H"
    assert r.encode_left_to_right("Y") == "V"
    r = Rotor(label="III", starting_position="H", ring_setting=26)
    assert r.encode_right_to_left("C") == "P"
    assert r.encode_left_to_right("O") == "J"
    r = Rotor(label="III", starting_position="I", ring_setting=26)
    assert r.encode_right_to_left("O") == "J"
    assert r.encode_left_to_right("D") == "M"
    r = Rotor(label="III", starting_position="I", ring_setting=26)
    assert r.encode_right_to_left("O") == "J"
    assert r.encode_left_to_right("D") == "M"
    r = Rotor(label="III", starting_position="J", ring_setting=26)
    assert r.encode_right_to_left("P") == "E"
    assert r.encode_left_to_right("C") == "L"
    r = Rotor(label="III", starting_position="K", ring_setting=26)
    assert r.encode_right_to_left("U") == "A"
    assert r.encode_left_to_right("L") == "G"
    r = Rotor(label="III", starting_position="L", ring_setting=26)
    assert r.encode_right_to_left("V") == "D"
    assert r.encode_left_to_right("J") == "Z"
    r = Rotor(label="III", starting_position="M", ring_setting=26)
    assert r.encode_right_to_left("Q") == "U"
    assert r.encode_left_to_right("R") == "C"
    r = Rotor(label="III", starting_position="N", ring_setting=26)
    assert r.encode_right_to_left("B") == "Q"
    assert r.encode_left_to_right("S") == "E"
    r = Rotor(label="III", starting_position="O", ring_setting=26)
    assert r.encode_right_to_left("X") == "K"
    assert r.encode_left_to_right("B") == "J"
    r = Rotor(label="III", starting_position="P", ring_setting=26)
    assert r.encode_right_to_left("A") == "S"
    assert r.encode_left_to_right("Q") == "C"
    r = Rotor(label="III", starting_position="Q", ring_setting=26)
    assert r.encode_right_to_left("Q") == "Y"
    assert r.encode_left_to_right("H") == "X"
    r = Rotor(label="III", starting_position="R", ring_setting=26)
    assert r.encode_right_to_left("U") == "H"
    assert r.encode_left_to_right("Y") == "G"
    r = Rotor(label="III", starting_position="S", ring_setting=26)
    assert r.encode_right_to_left("F") == "X"
    assert r.encode_left_to_right("N") == "Z"
    r = Rotor(label="III", starting_position="T", ring_setting=26)
    assert r.encode_right_to_left("J") == "N"
    assert r.encode_left_to_right("X") == "O"
    r = Rotor(label="III", starting_position="U", ring_setting=26)
    assert r.encode_right_to_left("Q") == "A"
    assert r.encode_left_to_right("L") == "X"
    r = Rotor(label="III", starting_position="V", ring_setting=26)
    assert r.encode_right_to_left("W") == "K"
    assert r.encode_left_to_right("B") == "O"
    r = Rotor(label="III", starting_position="W", ring_setting=26)
    assert r.encode_right_to_left("F") == "I"
    assert r.encode_left_to_right("E") == "D"
    r = Rotor(label="III", starting_position="X", ring_setting=26)
    assert r.encode_right_to_left("T") == "Y"
    assert r.encode_left_to_right("M") == "W"
    r = Rotor(label="III", starting_position="X", ring_setting=26)
    assert r.encode_right_to_left("T") == "Y"
    assert r.encode_left_to_right("M") == "W"
    r = Rotor(label="III", starting_position="Y", ring_setting=26)
    assert r.encode_right_to_left("V") == "L"
    assert r.encode_left_to_right("G") == "D"
    r = Rotor(label="III", starting_position="Z", ring_setting=26)
    assert r.encode_right_to_left("D") == "H"
    assert r.encode_left_to_right("U") == "W"
    r = Rotor(label="III", starting_position="A", ring_setting=26)
    assert r.encode_right_to_left("R") == "F"
    assert r.encode_left_to_right("Z") == "S"


    