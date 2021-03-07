
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

        