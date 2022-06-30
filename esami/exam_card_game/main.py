from games.card_game import Card, Player, GameException, Tournament


def main():
    # R1
    print("----------- R1 ------------")
    card_1 = Card("VoidWalker", 1, 3, 1)
    print(card_1.name)          # VoidWalker
    print(card_1.attack)        # 1
    print(card_1.life_points)   # 3
    print(card_1.mana_cost)     # 1
    print(card_1.is_dead())     # False
    print(card_1)               # VoidWalker 1 3 1

    card_2 = Card("Dread Infernal", 6, 6, 6)
    Card.fight(card_1, card_2)

    print(card_1.life_points)   # -3
    print(card_2.life_points)   # 5
    print(card_1.is_dead())     # True

    # R2
    print("----------- R2 ------------")
    player = Player("Yugi Mutou")
    print(player.name)      # "Yugi Mutou"
    player.mana = 5
    print(player.mana)      # 5
    print(player.hand)      # []
    print(player.field)     # []

    card_1 = Card("VoidWalker", 1, 3, 1)
    card_2 = Card("Dread Infernal", 6, 6, 6)
    player.draw(card_1)
    player.draw(card_2)
    print(player.hand)      # [VoidWalker 1 3 1, Dread Infernal 6 6 6]

    player.play("VoidWalker")
    print(player.hand)      # [Dread Infernal 6 6 6]
    print(player.field)     # [VoidWalker 1 3 1]
    print(player.mana)      # 4

    try:
        player.play("Dread Infernal")
        print("[ERROR] failed to detect not enough mana")
    except GameException:
        print("Missing mana correctly detected")    # Missing mana correctly detected

    # R3
    print("----------- R3 ------------")
    torneo = Tournament()

    player1 = Player("Anzu Mazaki")
    player2 = Player("Hiroto Honda")
    torneo.add_player(player1)
    torneo.add_player(player2)

    card_3 = Card("Fire Elemental", 6, 5, 6)
    card_4 = Card("WindSpeaker", 3,3, 4)
    card_5 = Card("Huffer", 4, 2, 3)
    torneo.add_card(card_3)
    torneo.add_card(card_4)
    torneo.add_card(card_5)

    torneo.player_uses_card("Anzu Mazaki", "Fire Elemental")
    torneo.player_uses_card("Anzu Mazaki", "WindSpeaker")
    torneo.player_uses_card("Anzu Mazaki", "Huffer")
    torneo.player_uses_card("Hiroto Honda", "Fire Elemental")

    print(torneo.get_players_of_card("Fire Elemental"))  # ['Anzu Mazaki', 'Hiroto Honda']

    # [Fire Elemental 6 5 6, WindSpeaker 3 3 4, Huffer 4 2 3] (any order)
    print(torneo.get_cards_of_player("Anzu Mazaki"))

    # [Fire Elemental 6 5 6, Huffer 4 2 3, WindSpeaker 3 3 4]
    print(torneo.get_cards_of_player("Anzu Mazaki", sort_res=True))

    try:
        torneo.add_player(player1)
        print("[ERROR] failed to detect duplicated player")
    except GameException:
        print("Duplicated player correctly detected") # Duplicated player correctly detected

    # R5
    print("----------- R5 ------------")
    player1.mana = 5
    player1.draw(card_2)
    player1.draw(card_3)
    player1.draw(card_4)
    player1.draw(card_5)
    print(player1.find_best_two())  # []

    player1.draw(card_1)
    print(player1.find_best_two())  # ['Huffer', 'VoidWalker']


if __name__ == "__main__":
    main()
