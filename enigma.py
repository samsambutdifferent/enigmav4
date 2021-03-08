from plug_board import Plugboard
from plug_lead import PlugLead
from rotor import Rotor
from rotor_board import RotorBoard
import helper


class Enigma:
    def __init__(self, reflector, rotor_labels, starting_positions, ring_settings, plug_leads=""):
        """initiate a version of the enigma machine
            params:
                reflector: string
                rotor_labels: tuple
                starting_positions: tuple
                ring_setting: tuple
                plug_leads: string
        """

        if helper.lengths_out_of_range(keys=[rotor_labels, ring_settings, starting_positions] ,max=4,min=3):
            raise ValueError("Rotor labels, starting positions and ring settings must be of even lengths, and within max minimum range")

        self.plug_board = Plugboard()
        for connection in plug_leads.split(" "):
            if connection != "":
                self.plug_board.add(PlugLead(connection))

        self.rotor_board = RotorBoard(
            reflector=reflector,
            rotor_labels=rotor_labels,
            starting_positions=starting_positions,
            ring_settings=ring_settings
        )


    def encode_message(self, msg):
        message = ""
        for signal in msg:
            message += self.__encode(signal)
        return message
    

    def __encode(self, signal):
        """pass signal through plugboard to rotorboard then back through plugboard
        """
        # convert using plug board
        signal = self.plug_board.encode(signal)

        # transform
        signal = self.rotor_board.transform_signal(signal)

        # convert back using plug board
        signal = self.plug_board.encode(signal)
        
        return signal


    def status(self):
        """print status
        """
        print("Plugboard:")
        self.plug_board.status()
        print("Rotors:")
        self.rotor_board.status()


if __name__ == "__main__":
    pass
