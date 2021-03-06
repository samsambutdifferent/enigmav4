#from rotor_board import RotorBoard
from plug_board import PlugBoard
from plug_lead import PlugLead
from rotor import Rotor



class Enigma:
    def __init__(self, plug_leads, reflector, rotor_labels, starting_positions, ring_settings):
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
            message += self.encode(char)

        return message
        

    def encode(self, char):
        pass


    def status(self):
        """print status
        """
        print("Plugboard:")
        self.plug_board.status()
        print("Rotors:")
        for r in self.rotors:
            r.status()


if __name__ == "__main__":
    en = Enigma(
        plug_leads="AB CX", 
        reflector="A",
        rotor_labels=("I", "II", "III"),
        starting_positions=("A", "B", "C"),
        ring_settings=(1,2,3)
    )

    en.status()