"""a series of demonstrations from the .ipynb workbook and beyond
"""

from enigma import Enigma
from rotor import Rotor
import pytest

class TestDemos:

    def test_demos(self):

        en = Enigma(
            plug_leads="HL MO AJ CX BZ SR NI YW DG PK", 
            reflector="B",
            rotor_labels=("I", "II", "III"),
            starting_positions=("A", "A", "Z"),
            ring_settings=(1,1,1),
        )

        en.status()
        ans = en.encode_message("HELLOWORLD")

        assert ans == "RFKTMBXVVW"

    # * With rotors `I II III`, reflector `B`, ring settings `01 01 01`, and initial positions `A A Z`, encoding an `A` produces a `U`.

        en = Enigma(
            plug_leads="", 
            reflector="B",
            rotor_labels=("I", "II", "III"),
            starting_positions=("A", "A", "Z"),
            ring_settings=(1,1,1),
        )

        en.status()
        ans = en.encode_message("A")

        assert ans == "U"


    # * With rotors `I II III`, reflector `B`, ring settings `01 01 01`, and initial positions `A A A`, encoding an `A` produces a `B`.

        en = Enigma(
            plug_leads="", 
            reflector="B",
            rotor_labels=("I", "II", "III"),
            starting_positions=("A", "A", "A"),
            ring_settings=(1,1,1),
        )

        en.status()
        ans = en.encode_message("A")

        assert ans == "B"

    # * With rotors `I II III`, reflector `B`, ring settings `01 01 01`, and initial positions `Q E V`, encoding an `A` produces an `L`.

        en = Enigma(
            plug_leads="", 
            reflector="B",
            rotor_labels=("I", "II", "III"),
            starting_positions=("Q", "E", "V"),
            ring_settings=(1,1,1),
        )

        en.status()
        ans = en.encode_message("A")
        assert ans == "L"


    # * With rotors `IV V Beta`, reflector `B`, ring settings `14 09 24`, and initial positions `A A A`, encoding an `H` produces a `Y`.

        en = Enigma(
            plug_leads="", 
            reflector="B",
            rotor_labels=("IV", "V", "Beta"),
            starting_positions=("A", "A", "A"),
            ring_settings=(14,9,24),
        )

        en.status()
        ans = en.encode_message("H")
        assert ans == "Y"


    # * With rotors `I II III IV`, reflector `C`,
    #  ring settings `07 11 15 19`, 
    #  and initial positions `Q E V Z`, encoding a `Z` produces a `V`.

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

    
    # Set up your enigma machine with rotors IV V Beta I, reflector A, 
    # ring settings 18 24 03 05, and initial positions E Z G P.
    # The plugboard should map the following pairs: PC XZ FM QA ST NB HY OR EV IU.
    # Find the result of decoding the following string: BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI.

        en = Enigma(
            plug_leads="PC XZ FM QA ST NB HY OR EV IU", 
            reflector="A",
            rotor_labels=("IV", "V", "Beta", "I"),
            starting_positions=("E", "Z", "G", "P"),
            ring_settings=(18,24,3,5),
        )
    
        ans = en.encode_message("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI")
        assert ans == "CONGRATULATIONSONPRODUCINGYOURWORKINGENIGMAMACHINESIMULATOR"
    

    def test_rotor(self):
        r = Rotor("I")
        r.status()
        assert(r.encode_right_to_left("A") == "E")
        assert(r.encode_left_to_right("A") == "U")

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

        