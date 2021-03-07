from plug_board import PlugBoard
from plug_lead import PlugLead
from rotor import Rotor


class Enigma:
    def __init__(self, reflector, rotor_labels, starting_positions, ring_settings, plug_leads=""):
        """initiate a version of the enigma machine
            params:
                plug_leads
                reflector
                rotors
                starting_positions:
                ring_setting
        """
        self.plug_board = PlugBoard()
        for connection in plug_leads.split(" "):
            if connection != "":
                self.plug_board.add(PlugLead(connection))

        self.rotors = []
        for i,label in enumerate(rotor_labels):
            self.rotors.append(Rotor(
                label=label,
                starting_position=starting_positions[i],
                ring_setting=ring_settings[i]
            ))

        self.reflector = Rotor(
            label=reflector
        )


    def encode_message(self, msg):
        message = ""
        for char in msg:
            message += self.__encode(char)

        return message
        

    def __encode(self, char):
        """
        TODO update
        """
        # convert using plug board
        char = self.plug_board.encode(char)

        # encode
        char = self.__signal_received(char)

        # convert back using plug board
        char = self.plug_board.encode(char)
        
        return char


    def __signal_received(self, signal):
        """
        TODO update
        """
        # advance rotor postions
        self.__rotate_positions()

        # pass signal from from right to left
        for r in self.rotors[::-1]:
            signal = r.encode_right_to_left(signal)

        # reflect
        signal = self.reflector.encode_right_to_left(signal)
        
        # pass signal from from left to right
        for r in self.rotors:
            signal = r.encode_left_to_right(signal)

        return signal


    def __rotate_positions(self):
        """
        TODO update
        Trigger a rotation of the rotors, starting by turning the right-most
        rotor. This should be called once for every keypress, before encoding.
        """
        should_next_rotor_rotate = False
        for index, rotor in enumerate(reversed(self.rotors)):
            is_first_rotor = (index == 0)
            is_last_rotor = (index == len(self.rotors) - 1)

            is_on_notch = rotor.is_on_notch()
            has_notch = rotor.has_notch()


            # 3 is the last rotor able to turn ??
            if is_last_rotor and len(self.rotors) > 3:
                break

            if is_first_rotor or should_next_rotor_rotate or (
                not is_last_rotor and is_on_notch
            ):
                should_next_rotor_rotate = is_on_notch
                rotor.rotate()

                if not should_next_rotor_rotate and has_notch:
                    break
            else:
                break


    def status(self):
        """print status
        """
        print("Plugboard:")
        self.plug_board.status()
        print("Rotors:")
        for r in self.rotors:
            r.status()


if __name__ == "__main__":

# * With rotors `I II III IV`, reflector `C`, ring settings `07 11 15 19`, and initial positions `Q E V Z`, encoding a `Z` produces a `V`.

    en = Enigma(
        plug_leads="", 
        reflector="C",
        rotor_labels=("I", "II", "III", "IV"),
        starting_positions=("Q", "E", "V", "Z"),
        ring_settings=(7,11,15,19),
    )

    en.status()
    ans = en.encode_message("Z")
    assert ans == "V"


# Set up your enigma machine with rotors IV V Beta I, reflector A, ring settings 18 24 03 05, and initial positions E Z G P.
# The plugboard should map the following pairs: PC XZ FM QA ST NB HY OR EV IU.
# Find the result of decoding the following string: BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI.


    en = Enigma(
        plug_leads="PC XZ FM QA ST NB HY OR EV IU", 
        reflector="A",
        rotor_labels=("IV", "V", "Beta", "I"),
        starting_positions=("E", "Z", "G", "P"),
        ring_settings=(1,1,1,1),
    )

    en.status()
    ans = en.encode_message("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI")

    assert ans == "RFKTMBXVVW"

