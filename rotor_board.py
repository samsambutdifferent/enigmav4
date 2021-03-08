from rotor import Rotor
import helper

class RotorBoard:
    def __init__(self, rotor_labels, starting_positions, ring_settings, reflector):
        """initiate the rotor board
                params: rotor_labels: tuple
                        starting_positions: tuple
                        ring_settings: tuple
                        reflector: string
        """

        if helper.lengths_out_of_range(keys=[rotor_labels, ring_settings, starting_positions] ,max=4,min=3):
            raise ValueError("Rotor labels, starting positions and ring settings must be of even lengths, and within max minimum range")
        
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


    def __advance_position(self):
        """move required rotor positions forward
        """
        r_to_l_rotors = [rotor for rotor in self.rotors[::-1]]

        advance_nxt = False
        for i, rotor in enumerate(r_to_l_rotors):

            # final rotor and is beyond the range of rotors able to advance
            if (self.__max_rotor_index == i) and self.__number_of_rotors >= self.__static_rotor_index:
                break 
            
            # if is first rotor always advance
            if 0 == i:
                advance_nxt = rotor.notched()
                rotor.advance()
            
            # if turnedover
            elif advance_nxt:
                advance_nxt = rotor.notched()
                rotor.advance()

            # if it is not the last one and is notched
            elif  self.__max_rotor_index != i and rotor.notched():
                advance_nxt = rotor.notched()
                rotor.advance()
            
            else:
                break

            if not advance_nxt and rotor.notch == "":
                break
    

    def transform_signal(self, signal):
        """ pass signal through rotors r/l then reflector then rotors l/r
        """
        # advance rotor postions
        self.__advance_position()

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