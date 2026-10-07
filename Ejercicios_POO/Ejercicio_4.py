class Head:
    def __init__(self, eyes, nose, mouth, hair, ears):
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth
        self.hair = hair
        self.ears = ears


class Torso:
    def __init__(self, chest, abdomen, back):
        self.chest = chest
        self.abdomen = abdomen
        self.back = back


class Hand:
    def __init__(self, fingers, palm, nails):
        self.fingers = fingers
        self.palm = palm
        self.nails = nails


class Arm:
    def __init__(self, upper_arm, lower_arm, hand):
        self.upper_arm = upper_arm
        self.lower_arm = lower_arm
        self.hand = hand


class Foot:
    def __init__(self, toes, sole, nails):
        self.toes = toes
        self.sole = sole
        self.nails = nails


class Leg:
    def __init__(self, upper_leg, lower_leg, foot):
        self.upper_leg = upper_leg
        self.lower_leg = lower_leg
        self.foot = foot


class Human:
    def __init__(self, head, torso, arms, legs):
        self.head = head
        self.torso = torso
        self.arms = arms
        self.legs = legs

    def show_info(self):
        print("===== HUMAN BODY =====")

        print("\nHEAD")
        print(f"Eyes: {self.head.eyes}")
        print(f"Nose: {self.head.nose}")
        print(f"Mouth: {self.head.mouth}")
        print(f"Hair: {self.head.hair}")
        print(f"Ears: {self.head.ears}")

        print("\nTORSO")
        print(f"Chest: {self.torso.chest}")
        print(f"Abdomen: {self.torso.abdomen}")
        print(f"Back: {self.torso.back}")

        print("\nARMS")

        for arm in self.arms:
            print(f"Upper arm: {arm.upper_arm}")
            print(f"Lower arm: {arm.lower_arm}")
            print(f"Fingers: {arm.hand.fingers}")
            print(f"Palm: {arm.hand.palm}")
            print(f"Nails: {arm.hand.nails}")

        print("\nLEGS")

        for leg in self.legs:
            print(f"Upper leg: {leg.upper_leg}")
            print(f"Lower leg: {leg.lower_leg}")
            print(f"Toes: {leg.foot.toes}")
            print(f"Sole: {leg.foot.sole}")
            print(f"Nails: {leg.foot.nails}")

left_hand = Hand(fingers=5, palm="smooth", nails="short")
right_hand = Hand(fingers=5, palm="smooth", nails="short") 
left_arm = Arm(upper_arm="muscular", lower_arm="strong", hand=left_hand)
right_arm = Arm(upper_arm="muscular", lower_arm="strong", hand=right_hand)
left_foot = Foot(toes=5, sole="soft", nails="short")
right_foot = Foot(toes=5, sole="soft", nails="short")
left_leg = Leg(upper_leg="muscular", lower_leg="strong", foot=left_foot)
right_leg = Leg(upper_leg="muscular", lower_leg="strong", foot=right_foot)
head = Head(eyes="blue", nose="small", mouth="smiling", hair="blonde", ears="normal")
torso = Torso(chest="broad", abdomen="flat", back="strong")
human = Human(head=head, torso=torso, arms=[left_arm, right_arm], legs=[left_leg, right_leg])


human.show_info()