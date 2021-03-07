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
        self.__static_rotor_index = 4


    def rotate_positions(self):
        """rotate all rotatable rotors
         TODO Update
        """
        reverse_rotors = list(reversed(self.rotors))
        rotate_next = False

        for i, rotor in enumerate(reverse_rotors):
            rotor_one = 0 == i
            rotor_is_final = self.__max_rotor_index == i

            # if it is the final rotor and is static
            if rotor_is_final and self.__number_of_rotors >= self.__static_rotor_index:
                break

            # if is first rotor always rotate
            if rotor_one:
                rotate_next = rotor.notched()
                rotor.rotate()
            # if turnover
            elif rotate_next:
                rotate_next = rotor.notched()
                rotor.rotate()
            # if it is not the last one and is notched
            elif not rotor_is_final and rotor.notched():
                rotate_next = rotor.notched()
                rotor.rotate()
            else:
                break
            
            if not rotate_next and rotor.notch == "":
                    break
    

    def signal_received(self, signal):
        """ pass signal through rotors & reflectors in sequence
        TODO update
        """
        # advance rotor postions
        self.rotate_positions()

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