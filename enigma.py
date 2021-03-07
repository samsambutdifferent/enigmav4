from plug_board import Plugboard
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
        self.plug_board = Plugboard()
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
        for signal in msg:
            message += self.__encode(signal)
        return message
        

    def __encode(self, signal):
        """
        TODO update
        """
        # advance rotor postions
        self.__rotate_positions()

        # convert using plug board
        signal = self.plug_board.encode(signal)

        # encode
        signal = self.__signal_received(signal)

        # convert back using plug board
        signal = self.plug_board.encode(signal)
        
        return signal


    def __signal_received(self, signal):
        """ pass signal through rotors & reflectors in sequence
        TODO update
        """
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
        """rotate all rotatable rotors
        TODO Update
        """
        rotate_next = False
        first_static_rotor = 4

        for i, rotor in enumerate(reversed(self.rotors)):
            rotor_one = 0 == i
            rotor_final = (len(self.rotors) - 1) == i 

            if rotor_final and len(self.rotors) >= first_static_rotor:
                break

            if rotor_one or rotate_next or (not rotor_final and rotor.notched()):
                
                rotate_next = rotor.notched()
                rotor.rotate()

                if not rotate_next and rotor.notch == "":
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
    pass
