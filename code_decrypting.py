import itertools as it
import string
from enigma import Enigma
from rotor_settings import rotor_settings

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

    count = 0
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
        
        count += 1
        if count % 1000 == 0:
            print(f"has done {count} attempts so far, please be patient....")


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
    return decrypted, ans[2], ans[4], ans[1]


def code_four():
    # Code 4

    # On my way home from working late as I walked past the computer science lab I saw one of the tutors 
    # playing with the Enigma machine. Mere tutors are not allowed to touch such important equipment! 
    # Suspicious, I open the door, but the tutor hears me, and jumps out of the nearest window. They left behind a coded message,
    # but some leads have been pulled out of the machine. It might contain a clue, but I'll have to find the missing 
    # lead positions (marked with question marks in the settings below).

    #     Code: SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW
    #     Crib: TUTOR

    #     Rotors: V III IV
    #     Reflector: A
    #     Ring settings: 24 1   2 10
    #     Starting positions: SWU
    #     Plugboard pairs: WP RJ A? VF I? HN CG BS


    code = "SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW"

    #NOTE had to update the crib as first only partially translated with orignal: Tutors
    cribs = ["NOTUTORSWEREHARMED"]

    remaining_letters = "D E K L M O Q T U X Y Z"

    possible_plug_boards = []
    orignal_string = "WP RJ A1 VF I2 HN CG BS"
    for a_letter in remaining_letters.split():
        string_a = orignal_string.replace("1", a_letter)
        
        i_remaining_letters = [x for x in remaining_letters.split() if x != a_letter]

        for i_letter in i_remaining_letters:
             string_i = string_a
             string_i = string_i.replace("2", i_letter)
             possible_plug_boards.append(string_i)

    possiblities = list(it.product(
        possible_plug_boards, # index 0
        ["A"], # index 1
        [("V", "III", "IV")], # index 2
        [("S", "W", "U")], # index 3
        [(24, 12, 10)], # index 4
    ))

    decrypted,ans = decrypter(msg=code, cribs=cribs, possiblities=possiblities)
    return decrypted, ans[0]


def create_rotor_variations(base_rotor_contacts, base_rotor_pins):
    caps_alpha = list(string.ascii_uppercase)

    variations = []
    four_char_comboz = list(it.combinations(caps_alpha,4))
    for combo in four_char_comboz:
        new_rotor = base_rotor_contacts.copy()

        i0 = new_rotor.index(combo[0])
        i1 = new_rotor.index(combo[1])

        c0 = caps_alpha[i0]
        c1 = caps_alpha[i1]

        c0 = new_rotor.index(c0)
        c1 = new_rotor.index(c1)

        new_rotor[i0], new_rotor[i1] = new_rotor[i1], new_rotor[i0]
        new_rotor[c0], new_rotor[c1] = new_rotor[c1], new_rotor[c0]

        i2 = new_rotor.index(combo[2])
        i3 = new_rotor.index(combo[3])

        c2 = caps_alpha[i2]
        c3 = caps_alpha[i3]

        c2 = new_rotor.index(c2)
        c3 = new_rotor.index(c3)

        new_rotor[i2], new_rotor[i3] = new_rotor[i3], new_rotor[i2]
        new_rotor[c2], new_rotor[c3] = new_rotor[c3], new_rotor[c2]
         
        s = "".join(new_rotor)

        variations.append(s)

    return variations


def decrypter_update_reflector(msg, cribs, possiblities):

    count = 0
    for p in possiblities:

        en = Enigma(
            plug_leads=p[0], 
            reflector="A",
            rotor_labels=p[2],
            starting_positions=p[3],
            ring_settings=p[4])

        en.rotor_board.reflector._Rotor__contacts = p[1]
        decrypted = en.encode_message(msg)

        ans = set()
        if __check_crib(cribs, decrypted):
            ans = (p[0], p[1], p[2], p[3], p[4])

        if ans != set():
            break
        
        count += 1
        if count % 1000 == 0:
            print(f"has done {count} attempts so far, please be patient....")


    return decrypted,ans



def code_five():
    # Code 5¶

    # I later remembered that I had given the tutor permission to use the Enigma machine to solve some codes I'd received via
    # email. As for the window, they are just a big fan of parkour, this is always how they leave the building. It seems they
    # are stuck on one last code. It came in via email so we suspect it's just spam, probably related to a social media website,
    # but you never know when you'll find a gem in that kind of stuff.
    # The tutor has narrowed the search and found most of the settings, but it seems this code was made with a non-standard
    # reflector. Indeed, there was a photo attached to the email along with the code. It appears that the sender has taken a
    # standard reflector, cracked it open, and swapped some of the wires – two pairs of wires have been modified, by the looks
    # of the dodgy soldering job.
    # To be clear, a single wire connects two letters, e.g. mapping A to Y and Y to A. The sender has taken two wires
    # (fours pairs of letters), e.g. A-Y and H-J, and swapped one of the ends, so one option would be H-Y and A-J. 
    # They did this twice, so they modified eight letters total (they did not swap the same wire more than once).
    # In your answer, include what the original reflector was and the modifications.

    #     Code: HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX
    #     Crib: the name of a social media website/platform

    #     Rotors: V II IV
    #     Reflector: Unknown and non-standard (see above)
    #     Ring settings: 06 18 07
    #     Starting positions: AJL
    #     Plugboard pairs: UG IE PO NX WT

    code = "HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX"
    cribs = ["FACEBOOK", "INSTAGRAM", "TWITTER", "WEIBO", "YOUTUBE"]

    caps_alpha = list(string.ascii_uppercase)
    for reflector_label in all_reflectors:
        reflector = rotor_settings[reflector_label]["settings"]
        variations = create_rotor_variations(list(reflector), caps_alpha)

        possiblities = list(it.product(
            ["UG IE PO NX WT"], # index 0
            variations, # index 1
            [("V", "II", "IV")], # index 2
            [("A", "J", "L")], # index 3
            [(6, 18, 7)], # index 4
        ))  

        print(f"trying variations of reflector: {reflector_label}")  
        decrypted,ans = decrypter_update_reflector(code, cribs, possiblities)

        if ans != set():
            return reflector_label,decrypted,ans[1] 

        print(f"unable to find for reflector {reflector_label} variations")
        print("-----------------------------") 


if __name__ == "__main__": 

    # # code 1
    decrypted_msg, code_one_ans = code_one()
    print(f"Code 1 decrypted message: {decrypted_msg}")
    print(f"Answer to question one, missing reflector: {code_one_ans}")
    # Code 1 decrypted message: NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING
    # Answer to question one, missing reflector: C

    # # code 2
    decrypted_msg, code_two_ans = code_two()
    print(f"Code 2 decrypted message: {decrypted_msg}")
    print(f"Answer to question two, missing starting positions: {code_two_ans}")
    # Code 2 decrypted message: IHOPEYOUAREENJOYINGTHEUNIVERSITYOFBATHEXPERIENCESOFAR
    # Answer to question two, missing starting positions: ('I', 'M', 'G')

    # # code 3
    decrypted_msg, code_three_ans_rotors, code_three_ans_ring_settings, code_three_ans_reflector = code_three()
    print(f"Code 3 decrypted message: {decrypted_msg}")
    print(f"Answer to question three, missing rotors: {code_three_ans_rotors}, missing ring settings: {code_three_ans_ring_settings}, missing reflector settings: {code_three_ans_reflector}")

    # # Code 3 decrypted message: SQUIRRELSPLANTTHOUSANDSOFNEWTREESEACHYEARBYMERELYFORGETTINGWHERETHEYPUTTHEIRACORNS
    # # Answer to question three, missing rotors: ('II', 'Gamma',  'IV'), missing ring settings: (24, 8, 20)

    # # code 4
    decrypted_msg, code_four_ans = code_four()
    print(f"Code 4 decrypted message: {decrypted_msg}")
    print(f"Answer to question four, plug leads: {code_four_ans}")
    # # Code 4 decrypted message: NOTUTORSWEREHARMEDNORIMPLICATEDOFCRIMESDURINGTHEMAKINGOFTHESEEXAMPLES
    # # Answer to question four, plug leads: WP RJ AT VF IK HN CG BS

    # # code 5
    reflector_label,decrypted_msg,code_five_ans = code_five()
    print(f"Code 5 decrypted message: {decrypted_msg}")
    print(f"Answer to question five, orignal reflector: {reflector_label}")
    # Code 5 decrypted message: YOUCANFOLLOWMYDOGONINSTAGRAMATTALESOFHOFFMANN
    # Answer to question five, orignal reflector: B
    # PQUHRSLDYXNGOKMABEFZCWVJIT  
    # swapped pairs:

    # Y P, Q R, A I, B E
