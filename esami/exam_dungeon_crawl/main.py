from dungeon_crawl.game_manager import DungeonCrawlGame, DungeonCrawlException


def main():
    print("----------------- R1 -----------------")
    game = DungeonCrawlGame()

    game.add_effect("Rigenerazione", "Aumento punti vita", "R")
    game.add_action("Pugno", "Danneggia avversario")

    print(game.get_action_or_effect("Rigenerazione"))   # R: Aumento punti vita
    print(game.get_action_or_effect("Pugno"))           # Pugno: Danneggia avversario

    try:
        game.get_action_or_effect("Potenziamento")
        print("[ERROR] Missing action or effect NOT detected")
    except DungeonCrawlException:
        print("Missing action or effect correctly detected")    # Missing action or effect correctly detected

    print("----------------- R2 -----------------")
    game.add_card("Carta 1", 1)
    game.add_card("Carta 2", 2)
    game.add_card("Carta 3", 3)
    game.add_card("Carta 4", 4)
    game.add_card("Carta 5", 5)

    game.add_effect("Invincibility", "Aumento punti difesa", "I")
    game.add_action("Fuga", "Scappa dal nemico")

    game.add_effect_to_card("Carta 1", "Rigenerazione")
    game.add_effect_to_card("Carta 1", "Invincibility")
    game.add_action_to_card("Carta 1", "Pugno", value=5, action_range=1)
    game.add_action_to_card("Carta 1", "Fuga", value=3, action_range=10)

    print(game.get_card_effects("Carta 1"))     # ['Invincibility', 'Rigenerazione']
    print(game.get_card_actions("Carta 1"))     # ['Pugno,5,1', 'Fuga,3,10']
    print(game.get_card_effects("Carta 2"))     # []
    print(game.get_card_actions("Carta 2"))     # []

    print("----------------- R3 -----------------")
    game.add_role("Curatore", 2)
    game.add_role("Ladro", 4)
    game.add_role("Giullare", 1)

    game.add_card_to_role("Curatore", "Carta 1")
    game.add_card_to_role("Curatore", "Carta 2")
    game.add_card_to_role("Curatore", "Carta 3")
    game.add_card_to_role("Curatore", "Carta 4")
    game.add_card_to_role("Curatore", "Carta 5")

    game.add_card_to_role("Ladro", "Carta 3")
    game.add_card_to_role("Ladro", "Carta 4")
    game.add_card_to_role("Ladro", "Carta 5")

    print(game.get_role_cards("Ladro"))         # ['Carta 3', 'Carta 4', 'Carta 5']
    print(game.get_role_cards("Curatore", 4))   # ['Carta 1', 'Carta 2', 'Carta 3', 'Carta 4']
    print(game.get_role_cards("Ladro", 2))      # []
    print(game.get_role_cards("Giullare"))      # []

    try:
        game.add_card_to_role("Curatore", "Carta 20")
        print("[ERROR] failed to detect missing card")
    except DungeonCrawlException:
        print("Missing card correctly detected")    # Missing card correctly detected

    try:
        game.add_card_to_role("Guerriero", "Carta 2")
        print("[ERROR] failed to detect missing role")
    except DungeonCrawlException:
        print("Missing role correctly detected")    # Missing role correctly detected

    print("----------------- R5 -----------------")
    game.add_character("Personaggio 1", "Ladro", level=5)
    game.add_character("Personaggio 2", "Curatore", level=4)

    try:
        game.play_cards("Personaggio 2", "Carta 1", "Carta 5")
        print("[ERROR]  Failed to detect card level higher than character")
    except DungeonCrawlException:
        print("Card level higher than character correctly detected")    # Card level higher than character correctly detected

    game.play_cards("Personaggio 1", "Carta 3", "Carta 4")
    game.play_cards("Personaggio 2", "Carta 3", "Carta 4")

    try:
        game.play_cards("Personaggio 2", "Carta 1", "Carta 2")
        print("[ERROR] Failed to detect playing of more cards than allowed by role")
    except DungeonCrawlException:
        print("Playing of more cards than allowed by role correctly detected")  # Playing of more cards than allowed by role correctly detected

    try:
        game.play_cards("Personaggio 1", "Carta 4", "Carta 5")
        print("[ERROR] Failed to detect card played twice")
    except DungeonCrawlException:
        print("Card played twice correctly detected")   # Card played twice correctly detected


if __name__ == "__main__":
    main()
