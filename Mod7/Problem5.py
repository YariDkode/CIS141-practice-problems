'''
#5. Write a function called level_up(experience) that takes a player's experience
points and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''

# Write the function, player level based on experience points, return, and check
def level_up(experience):
    if experience < 100:
        return 1
    elif experience < 200:
        return 2
    else:
        return 3


print("Base on your experience points, you are in level:", level_up(52))   # Level 1
print("Base on your experience points, you are in level:", level_up(163))  # Level 2
print("Base on your experience points, you are in level:", level_up(400))  # Level 3

