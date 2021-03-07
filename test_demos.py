
"""a series of demonstrations from the .ipynb workbook
"""

from enigma import Enigma
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
    
        en.status()
        ans = en.encode_message("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI")
        assert ans == "CONGRATULATIONSONPRODUCINGYOURWORKINGENIGMAMACHINESIMULATOR"

        