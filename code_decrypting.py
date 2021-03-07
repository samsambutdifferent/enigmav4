from enigma import Enigma
import itertools as it

all_rotors = ["Beta", "Gamma", "I", "II", "III", "IV", "V"]
all_reflectors = ["A", "B", "C"]
all_ring_settings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
all_starting_pos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def __check_crib(cribs, value):
    for crib in cribs:
        if crib in value:
            return True     
    return False

def decrypter(msg, cribs,
                plug_leads, 
                reflector, 
                rotor_labels, 
                starting_positions, 
                ring_settings):


    en = Enigma(
        plug_leads=plug_leads, 
        reflector=reflector,
        rotor_labels=rotor_labels,
        starting_positions=starting_positions,
        ring_settings=ring_settings,
    )

    decrypted = en.encode_message(msg)

    ans = set()

    if __check_crib(cribs, decrypted):
        # print(f"found")
        # print(f"decrypted message: {decrypted}")
        # print(f"orignal message: {msg}")
        # print("Enigma Status:")
        # en.status()
        ans = (plug_leads, reflector, rotor_labels, starting_positions, ring_settings)

    return ans


def code_one():
    # CODE 1
    # You recovered an Enigma machine! Amazingly, it is set up in that day's position, ready for you to replicate in your software.
    # But unfortunately the label has worn off the reflector. All the other settings are still in place, however. 
    # You also found a book with the title "SECRETS" which contained the following code, 
    # could it be so simple that the code contains that text?

    #     Code: DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ
    #     Crib: SECRETS

    #     Rotors: Beta Gamma V
    #     Reflector: Unknown
    #     Ring settings: 04 02 14
    #     Starting positions: MJM
    #     Plugboard pairs: KI XN FL

    code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
    cribs = ["SECRETS"]

    possiblities = list(it.product(
        [("Beta", "Gamma", "V")], # index 0
        all_reflectors, # index 1
        [(4, 2, 14)], # index 2
        [("M", "J", "M")], # index 3
        ["KI XN FL"] # index 4
    ))

    ans = set()
    for p in possiblities:
        ans = decrypter(msg=code, cribs=cribs,
                plug_leads=p[4], 
                reflector=p[1], 
                rotor_labels=p[0], 
                starting_positions=p[3],
                ring_settings=p[2])
        

    print(f"Answer to question one, missing reflector: {ans[1]}")

    return ans[1]



 
    
# Driver Function  
if __name__ == "__main__": 

    # Code 2¶

    # You leave the machine in the hands of the university. The team have cracked the day's settings thanks to some earlier
    # codebreaking, but unfortunately, the initial rotor positions are changed for each message. For the message below, 
    # the team has no idea what the initial settings should be, but know the message was addressed to them. 
    # Help them out.

    #     Code: CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH
    #     Crib: UNIVERSITY

    #     Rotors: Beta I III
    #     Reflector: B
    #     Ring settings: 23 02 10
    #     Starting positions: Unknown
    #     Plugboard pairs: VH PT ZG BJ EY FS


    code = "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
    cribs = ["UNIVERSITY"]

    possiblities = list(it.product(
        [("Beta", "I", "III")], # index 0
        ["B"], # index 1
        [(23, 2, 10)], # index 2
        list(it.product(all_starting_pos, all_starting_pos, all_starting_pos)), # index 3
        ["VH PT ZG BJ EY FS"] # index 4
    ))

    ans = set()
    for p in possiblities:
        ans = decrypter(msg=code, cribs=cribs,
                plug_leads=p[4], 
                reflector=p[1], 
                rotor_labels=p[0], 
                starting_positions=p[3],
                ring_settings=p[2])

        if ans != set():
            break
    
    print(f"Answer to question two, missing starting positions: {ans[3]}")




    # possiblities list(it.product(
    #     list(it.product(all_rotors,all_rotors,all_rotors)), # index 0
    #     list(it.product(all_reflectors)), # index 1
    #     list(it.product(all_ring_settings,all_ring_settings,all_ring_settings)), # index 2
    #     list(it.product(all_ring_settings, all_ring_settings, all_ring_settings)), # index 3
    #     list(it.product(all_starting_pos, all_starting_pos, all_starting_pos)) # index 4
    # )


    pass