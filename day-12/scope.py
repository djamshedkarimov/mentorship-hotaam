# enemies_amount = 1
#
# def increase_enemies():
#     enemies_amount = 2
#     print(f"enemies inside function: {enemies_amount}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies_amount}\n")
#
#
# #local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
#
# #global scope
# player_strength = 10
# def train():
#     print(player_strength + 2)
#
# train()
#
# # there is no block scope
# game_level = 3
# def create_enemy():
#     enemies = ["skeleton", "zombie", "alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)
#
#
# # modifying global scope

# enemies = "skeleton"
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# global constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_angela"

