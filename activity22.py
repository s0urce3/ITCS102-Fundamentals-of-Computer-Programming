# Multiple Dimensional List/Dictionary

# Anime_Power_Ranking_System
naruto = {
    "Character Description": "The genius of Konoha",
    "Name:": "shikamaru",
    "skill_1": "Shadow Possession Jutsu",
    "skill_2": "Advanced Shadow Techniques",
    "skill_3": "Limitations"
}

flame_recca = {
    "Character Description": "The Blazing Fire of Occa",
    "Name:": "Recca",
    "skill_1": "Flame Dragon : Saiha",
    "skill_2": "Flame Dragon : Nadare",
    "skill_3": "Flame Dragon : Homura",
    "skill_4": "Flame Dragon : Madoka"
}

fairy_tail = {
    "Character Description": "DnD",
    "Name:": "Natsu",
    "skill_1": "Fire Dragon Slayer Magic",
    "skill_2": "enhanced senses",
    "skill_3": "physical strength",
    "skill_4": " Dragon Force"
}


black_clover = {
    "Character Description": "Noblewoman of House Vermillion",
    "Name: ": "Mimosa",
    "skill_1": "Plant Creation & Manipulation Magic",
    "skill_2": "Recovery / Healing Magic",
    "skill_3": "Offensive & Utility Spells",
    "skill_4": "Mana Sensory & Large Magic Power"
}

saitama1 = {
    "Character Description": "The Nobody",
    "Name: ": "Saitama",
    "skill_1": "Normal Punch",
    "skill_2": "Killer Move: Serious Series:",
    "skill_3": "Serious Side Hops:",
    "skill_4": "Improvised & Copied Feats:"
}

demon_slayer = {
    "Character Description": "Upper Rank One: Kizuki",
    "Name:": "Kokushibo",
    "skill_1": "Moon Breathing",
    "skill_2": "Selfless-State",
    "skill_3": "See-Through World",
    "skill_4": "Regeneration"
}

sung_power = {
    "Character Description": "The Shadow Monarch",
    "Name: ": "Sung Jin Woo",
    "skill_1": "System",
    "skill_2": "Arise",
    "skill_3": "Limitless Growth",
    "skill_4": "Speed Rapid"
}

That_time_i_got_reincarnated_as_a_slime = {
    "Character Description": "The slime",
    "Name: ": "Rimuru Tempest",
    "skill_1": "Abnormal Condition Nullification",
    "skill_2": "Holy-Demonic Attack Resistance",
    "skill_3": "Natural Effects Nullification ",
    "skill_4": "Pain Nullification"
}

jujutsu_kaisen = {
    "Character Description": "THE GOAT",
    "Name: ": "Saturo Gojo",
    "skill_1": "Six Eyes",
    "skill_2": "Limitless & Infinity",
    "skill_3": "Teleportation"
}

# RECALLING VARIABLE NAMES
shikamaru = naruto
recca = flame_recca
kokushibo= demon_slayer

Natsu = fairy_tail
Mimosa = black_clover
saitama = saitama1

Jinwoo = sung_power
Rimuru = That_time_i_got_reincarnated_as_a_slime
gojo_Saturo = jujutsu_kaisen

# PUTTING CHARACTERS IN A LIST
Rank_1 = [saitama, Natsu, gojo_Saturo]
Rank_2 = [recca, Mimosa, shikamaru]
Rank_3 = [Rimuru, demon_slayer, Jinwoo]

# ANIMES
Anime = {
    "rank_1": Rank_1,
    "Rank_2": Rank_2,
    "Rank_3": Rank_3,
}
# PRINT LIBRARY
print("________________________________________________________________________")
print("<---- List of Anime: ---->")
print("________________________________________________________________________")
for name, description in Anime.items():
    print(f"Anime Name: {name} | Description: {description} \n")

while True:
    ask = input("Which number do you specifically want to check? \n [1] rank_1 \n [2] rank_2 \n [3]rank_3 \n [4] Quit \n -------> ")

    if ask == "1":
        print("________________________________________________________________________")
        print("<---- List of rank_1 Characters: ---->")
        print("________________________________________________________________________")
        for hero in Rank_1:
            print(f"Character Name: {hero} \n\n")  

        question = input("Press [0] to go Back. \n -------> ")   
    elif ask == "2":
        print("________________________________________________________________________")
        print("<---- List of rank_2 Characters: ---->")
        print("________________________________________________________________________")
        for hero in Rank_2:
                    print(f"Character Name: {hero} \n\n")  

        question = input("Press [0] to go Back. \n -------> ")   

    elif ask == "3":
        print("________________________________________________________________________")
        print("<---- List of rank_3 Characters: ---->")
        print("________________________________________________________________________")
        for hero in Rank_3:
                    print(f"Character Name: {hero} \n\n")  

        question = input("Press [0] to go Back. \n -------> ")   

    elif ask == "4":
        break 

    else:
        print("Error: Your choice isn't on the option.")
