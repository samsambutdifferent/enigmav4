from enigma import Enigma
import itertools as it

all_rotors = ["Beta", "Gamma", "I", "II", "III", "IV", "V"]
even_rotors = ["Beta", "Gamma", "II", "IV"]
all_reflectors = ["A", "B", "C"]
all_ring_settings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
not_a_single_odd_ring_settings = [2, 4, 6, 8, 10, 20, 22, 24, 26]
all_starting_pos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def __check_crib(cribs, value):
    for crib in cribs:
        if crib in value:
            return True     
    return False

def decrypter(msg, cribs, possiblities):

    for p in possiblities:

        en = Enigma(
            plug_leads=p[0], 
            reflector=p[1],
            rotor_labels=p[2],
            starting_positions=p[3],
            ring_settings=p[4])

        decrypted = en.encode_message(msg)

        ans = set()
        if __check_crib(cribs, decrypted):
            ans = (p[0], p[1], p[2], p[3], p[4])

        if ans != set():
            break
     
    return decrypted,ans


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
        ["KI XN FL"], # index 0
        all_reflectors, # index 1
        [("Beta", "Gamma", "V")], # index 2
        [("M", "J", "M")], # index 3
        [(4, 2, 14)], # index 4
    ))

    decrypted,ans = decrypter(msg=code, cribs=cribs, possiblities=possiblities)
    return decrypted,ans[1]


def code_two():
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
        ["VH PT ZG BJ EY FS"], # index 0
        ["B"], # index 1
        [("Beta", "I", "III")], # index 2
        list(it.product(all_starting_pos, all_starting_pos, all_starting_pos)), # index 3
        [(23, 2, 10)], # index 4
    ))

    ans = set()
    decrypted,ans = decrypter(msg=code, cribs=cribs, possiblities=possiblities)
    return decrypted,ans[3]


def code_three():
    # Code 3¶

    # The department has intercepted a message from the admissions team. They know it contains the word "THOUSANDS"
    # and they are worried it might relate to how many students are arriving next semester. 
    # But the admissions team are a bit unusual: they love even numbers, and hate odd numbers. 
    # You happen to know they will never use an odd-numbered rotor, ruling out I, III, and V. 
    # They will also never use a ring setting that has even a single odd digit: 02 is allowed but 11 is certainly
    #  not, and even 12 is banned.

    # Code: ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY
    # Crib: THOUSANDS

    # Rotors: Unknown but restricted (see above)
    # Reflector: Unknown
    # Ring settings: Unknown but restricted (see above)
    # Starting positions: EMY
    # Plugboard pairs: FH TS BE UQ KD AL


    code = "ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY"
    cribs = ["THOUSANDS"]
    
    possiblities = list(it.product(
        ["FH TS BE UQ KD AL"], # index 0
        all_reflectors, # index 1
        list(it.product(even_rotors, even_rotors, even_rotors)), # index 2
        [("E", "M", "Y")], # index 3
        list(it.product(not_a_single_odd_ring_settings, not_a_single_odd_ring_settings, not_a_single_odd_ring_settings)) # index 4
    ))

    ans = set()
    decrypted,ans = decrypter(msg=code, cribs=cribs, possiblities=possiblities)
    return decrypted, ans[2], ans[4]


if __name__ == "__main__": 

    # # code 1
    decrypted_msg, code_one_ans = code_one()
    print(f"Code 1 decrypted message: {decrypted_msg}")
    print(f"Answer to question one, missing reflector: {code_one_ans}")

    # # code 2
    decrypted_msg, code_two_ans = code_two()
    print(f"Code 2 decrypted message: {decrypted_msg}")
    print(f"Answer to question two, missing starting positions: {code_two_ans}")

    # code 3
    decrypted_msg, code_three_ans_rotors, code_three_ans_ring_settings = code_three()
    print(f"Code 3 decrypted message: {decrypted_msg}")
    print(f"Answer to question three, missing rotors: {code_three_ans_rotors}, missing ring settings: {code_three_ans_ring_settings}")







    # possiblities list(it.product(
    #     list(it.product(all_rotors,all_rotors,all_rotors)), # index 0
    #     list(it.product(all_reflectors)), # index 1
    #     list(it.product(all_ring_settings,all_ring_settings,all_ring_settings)), # index 2
    #     list(it.product(all_ring_settings, all_ring_settings, all_ring_settings)), # index 3
    #     list(it.product(all_starting_pos, all_starting_pos, all_starting_pos)) # index 4
    # )


    pass