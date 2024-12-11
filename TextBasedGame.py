def main():
    current_room = "Hopes End"
    inventory = []
    star_fragments_collected = 0
    game_over = False
    won = False

    # Color codes in lowercase
    green = "\033[92m"
    red = "\033[91m"
    yellow = "\033[93m"
    blue = "\033[94m"
    reset = "\033[0m"

    # Room connections according to the provided map
    rooms = {
        "Hopes End": {
            "east": "Chamber of Silent Lament"
        },
        "Chamber of Silent Lament": {
            "west": "Hopes End",
            "east": "Passage of Fading Warmth",
            "south": "Cavern of Lingering Doubt"
        },
        "Corridor of Whispers Past": {
            "east": "Cavern of Lingering Doubt"
        },
        "Cavern of Lingering Doubt": {
            "north": "Chamber of Silent Lament",
            "west": "Corridor of Whispers Past"
        },
        "The Withering Grove of Regret": {
            "north": "Halls of Sorrows Echo"
        },
        "Passage of Fading Warmth": {
            "west": "Chamber of Silent Lament",
            "north": "Gallery of Unending Yearn",
            "east": "Halls of Sorrows Echo"
        },
        "Halls of Sorrows Echo": {
            "west": "Passage of Fading Warmth",
            "north": "Vault of Dimming Faith",
            "south": "The Withering Grove of Regret"  # locked by Key of Frozen Tears
        },
        "Gallery of Unending Yearn": {
            "south": "Passage of Fading Warmth",
            "west": "Annex of Distant Cries"  # locked by Humble Key
        },
        "Annex of Distant Cries": {
            "east": "Gallery of Unending Yearn"
        },
        "Vault of Dimming Faith": {
            "north": "The Idle Pool of Reflection"
        },
        "The Idle Pool of Reflection": {
            "south": "Vault of Dimming Faith"
        }
    }

    # Room descriptions for immersion
    room_descriptions = {
        "Hopes End": "A bleak cave entrance. The still air hints that hope is scarce here.",
        "Chamber of Silent Lament": "A chamber where silent tears have etched sorrowful patterns into the walls.",
        "Corridor of Whispers Past": "A corridor where faint echoes of regrets drift like ghosts.",
        "Cavern of Lingering Doubt": "A cavern where every shadow questions your resolve, doubt clinging to the cold stone.",
        "The Withering Grove of Regret": "A secret grove, overgrown with spectral vines of remorse and regret.",
        "Passage of Fading Warmth": "A narrow passage where the memory of warmth slowly fades, leaving only chill.",
        "Halls of Sorrows Echo": "Long halls that carry the sobs of ancient sadness, repeated into eternity.",
        "Gallery of Unending Yearn": "A gallery of carved faces, each locked in eternal longing, forever reaching.",
        "Annex of Distant Cries": "A secluded annex where distant cries fade into uneasy silence.",
        "Vault of Dimming Faith": "A vault of broken idols and extinguished candles, where faith has withered to ash.",
        "The Idle Pool of Reflection": "A still, dark pool where the reflection of a lost presence hovers, timeless and foreboding."
    }

    # Items in rooms
    items_in_rooms = {
        "Chamber of Silent Lament": {
            "name": "Star Fragment",
            "desc": "A tiny shard of starlight that shimmers faintly, a memory of brighter times."
        },
        "Cavern of Lingering Doubt": {
            "name": "Star Fragment",
            "desc": "A fragile spark of hope, flickering within encroaching darkness."
        },
        "Halls of Sorrows Echo": {
            "name": "Star Fragment",
            "desc": "A glimmer of light, trembling as if uncertain in this chamber of endless weeping."
        },
        "Passage of Fading Warmth": {
            "name": "Humble Key",
            "desc": "A simple iron key, unadorned. Humility forged into metal."
        },
        "Gallery of Unending Yearn": {
            "name": "Star Fragment",
            "desc": "A gentle glow that tugs at your heart, reminding you of distant warmth."
        },
        "Vault of Dimming Faith": {
            "name": "Star Fragment",
            "desc": "A faint glow that seems to hum with lost hymns and quiet prayers."
        },
        "Corridor of Whispers Past": {
            "name": "Key of Frozen Tears",
            "desc": "A key shaped like a tear of ice, cold to the touch, forged from sorrow."
        },
        "The Withering Grove of Regret": {
            "name": "Crown of Despair",
            "desc": "A twisted circlet of black metal, offering resistance against the torment of stasis."
        },
        "Annex of Distant Cries": {
            "name": "Sigil of Hope",
            "desc": "A rune-carved talisman glowing faintly, holding a spark of lost integrity."
        }
    }

    # Locked rooms
    locked_rooms = {
        "The Withering Grove of Regret": "Key of Frozen Tears",
        "Annex of Distant Cries": "Humble Key"
    }

    def has_all_requirements():
        # Requirements: all 5 - star fragments, Crown of Despair, Sigil of Hope
        if star_fragments_collected < 5:
            return False
        if "Crown of Despair" not in inventory:
            return False
        if "Sigil of Hope" not in inventory:
            return False
        return True

    # Introduction
    print(green + "Long ago, before the world was cloaked in eternal twilight, Nicodemus was a revered master of stasis magic.")
    print("He preserved knowledge, relics, and souls, holding them in perfect moments of time.")
    print("But when the darkFrost fell upon the land, Nicodemus’s gift became a curse.")
    print("His magic, once gentle, turned cruel and twisted. Those caught in his spells now suffer endless torment.")
    print("With the land frozen in despair, the time has come to journey into his ancient domain,")
    print("to retrieve the pieces of Star (5 in total), two ancient relics and face Nicodemus himself.")
    print("Your quest begins now, guided by faint memories and fragile courage." + reset)
    print("Type 'go [direction]' to move, 'get [item]' to pick up an item, or 'q' to quit.\n")

    while not game_over:
        print(f"You are currently in: {current_room}")
        print(room_descriptions[current_room])

        # Show item if present (yellow for item lines)
        if current_room in items_in_rooms:
            item_name = items_in_rooms[current_room]["name"]
            print(yellow + f"There is an item here: {item_name}" + reset)

        # Show exits
        if current_room in rooms:
            exits = ", ".join(rooms[current_room].keys())
        else:
            exits = "None"
        print(f"Exits: {exits}")
        print(f"Inventory: {inventory} | Star Fragments: {star_fragments_collected}\n")

        # If villain room
        if current_room == "The Idle Pool of Reflection":
            if has_all_requirements():
                print("You have gathered all the fragments of hope, the Crown of Despair protects your mind from his pain,\n"
                      "and the Sigil of Hope rekindles lost integrity within Nicodemus, you see human awareness in his eyes.\n"
                      "Blinded by the fragments’ light, the time stasis storm he's created shatters....\n"
                      "You stand victorious over the curse that's infected Nicodemus’s sorrowful realm!")
                won = True
                game_over = True
            else:
                print("You stand before Nicodemus, unprepared. The stasis magic ensnares you,\n"
                      "and your resolve crumbles into eternal twilight.")
                game_over = True
            break

        command = input("What would you like to do? ").strip()
        if command.lower() == 'q':
            print("You turn back, abandoning the caves to their endless sorrow.")
            game_over = True
            continue

        parts = command.split()
        if len(parts) == 0:
            print(red + "Invalid command.\n" + reset)
            continue

        action = parts[0].lower()
        if action == "go":
            if len(parts) < 2:
                print(red + "Go where? You must specify a direction.\n" + reset)
                continue
            direction = parts[1].lower()

            if current_room in rooms and direction in rooms[current_room]:
                next_room = rooms[current_room][direction]
                if next_room in locked_rooms:
                    required_key = locked_rooms[next_room]
                    if required_key in inventory:
                        # Ask if they want to use the key
                        print(blue + f"You stand before a locked door leading to {next_room}. You hold the {required_key}." + reset)
                        use_key = input(blue + "Do you want to use the key to open the door? (yes/no): " + reset).strip().lower()
                        if use_key == 'yes':
                            print(green + f"You unlock the path to {next_room} using {required_key}." + reset)
                            current_room = next_room
                        else:
                            print(red + "You decide not to open the door." + reset)
                    else:
                        print(red + f"The way to {next_room} is locked. You need the {required_key}.\n" + reset)
                else:
                    current_room = next_room
                    print(green + f"You move {direction} and arrive at {current_room}.\n" + reset)
            else:
                print(red + "You cannot go that way.\n" + reset)

        elif action == "get":
            if len(parts) < 2:
                print(red + "Get what? Specify an item.\n" + reset)
                continue
            requested_item = " ".join(parts[1:])

            if current_room in items_in_rooms:
                room_item = items_in_rooms[current_room]["name"]
                room_item_desc = items_in_rooms[current_room]["desc"]
                if requested_item.lower() == room_item.lower():
                    if room_item == "Star Fragment":
                        star_fragments_collected += 1
                        print(yellow + f"You pick up the Star Fragment. {room_item_desc}\n"
                              f"You now have {star_fragments_collected} Star Fragments." + reset)
                    else:
                        print(yellow + f"You pick up the {room_item}. {room_item_desc}\n" + reset)
                        inventory.append(room_item)
                    del items_in_rooms[current_room]  # Remove item from room
                else:
                    print(red + "That item is not here.\n" + reset)
            else:
                print(red + "There are no items here to pick up.\n" + reset)

        else:
            print(red + "Invalid command. Try 'go [direction]' or 'get [item]'.\n" + reset)

    if won:
        print(green + "Your courage and perseverance have restored a faint hope to this sorrowful realm - but what's next?" + reset)
    else:
        if not won and game_over:
            print("Your journey ends in these silent halls. Your tears turn to ice, failure tolls the bells..")

if __name__ == "__main__":
    main()
