from rotor import Rotor

class RotorBoard:
    def __init__(self, rotor_labels, starting_positions, ring_settings, reflector):
        """initiate the rotor board
                params: rotor_labels
                        starting_positions
                        ring_settings
                        reflector
        """

        self.rotors = []
        for i,label in enumerate(rotor_labels):
            self.rotors.append(Rotor(
                label=label,
                starting_position=starting_positions[i],
                ring_setting=ring_settings[i]
            ))
        
        self.reflector = Rotor(reflector)

        self.__number_of_rotors = len(self.rotors)
        self.__max_rotor_index = len(self.rotors) - 1
        self.__first_static_rotor = 4


    def rotate_positions(self):
        """rotate all rotatable rotors
        TODO Update
        """
        rotate_next = False
        for i, rotor in enumerate(reversed(self.rotors)):
            rotor_one = 0 == i
            rotor_final = self.__max_rotor_index == i 

            if rotor_final and self.__number_of_rotors >= self.__first_static_rotor:
                break

            if rotor_one or rotate_next or (not rotor_final and rotor.notched()):
                
                rotate_next = rotor.notched()
                rotor.rotate()

                if not rotate_next and rotor.notch == "":
                    break
            else:
                break
    

    def signal_received(self, signal):
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


    def status(self):
            """print status
            """
            for r in self.rotors:
                r.status()


if __name__=="__main__":
    pass