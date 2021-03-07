from plug_board import Plugboard
from plug_lead import PlugLead
from rotor import Rotor
from rotor_board import RotorBoard


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
        """
        TODO update
        """
        # advance rotor postions
        self.rotor_board.rotate_positions()

        # convert using plug board
        signal = self.plug_board.encode(signal)

        # encode
        signal = self.rotor_board.signal_received(signal)

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
