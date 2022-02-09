
level1 = input("You were walking in the forest, the sun set and it became dark. You find an abandoned campsite with some matches and a flashlight. Should you light the WOOD or use the FLASHLIGHT?")
if level1 == "WOOD":
    level2 = input("You light the wood! The fire brings warmth to your cold fingers. You hear the bushes rustle behind you. Do you LOOK closer, HIDE in the trees, or RUN away?")
    if level2 == "LOOK":
        level3 = input("You come closer to the bush and you see the dark eyes of a wolf. It growls at you and gets ready to attack! Should you ATTACK the wolf or RUN away?")
        if level3 == "ATTACK":
            print("You grab a burning branch from the fire and lunge at the wolf! Your leg was wounded but you are victorious! The wolf ran off with burned bits of fur, as you sit down you feel very exausted. Exhauted you think that maybe this is a good place to rest. As you lay your head down and drift off to sleep, you see the figures of more wolves in the trees... THE END")
        if level3 == "RUN":
                level4 = input("You run as fast as you can away from the wolf. The landscape becomes dark and the wolf howls in excitement after you. The brush becomes very thick do you continue to RUN through the brush or CLIMB a tree?")
                if level4 == "CLIMB":
                    print("You quickly climb up the tree. At the top you hear the sound of more wolves at the base of the tree. Just as you are about to give up hope a gunshot rings out and the wolves scatter. Its a Forest Ranger your're saved! THE END")
                if level4 == "RUN":
                    print("You continue to run! In the dark of night, you didn't notice the cliff ledge and fell off. You scream could be heard across the canyon. THE END")
    if level2 == "HIDE":
         print("You hide behind a nearby tree. In the silence of night you listen carefully. The silence is broken by the growl of wolves all around you, closing in on you. THE END")
    if level2 == "RUN":
        level3 = input("You decide you don't wait to find out what's in the bush and run! As you leave the safety of the fire it gets really dark. You hear more rustleing in the bushes, almost like you're being followed. Do you continue to RUN or use your PHONE to call for help?")
        if level3 == "RUN":
            print("You continue to run! In the dark of night, you didn't notice the cliff ledge and fell off. You scream could be heard across the canyon. THE END")
        if level3 == "PHONE":
            print("As you call for help you hear the growling of wolves! Thinking quickly you climb the nearest tree just in time but In your haste, you dropped you phone! You yell out to the phone you need help. You hope they reach you before you starve. THE END")
if level1 == "FLASHLIGHT":
    level2 = input("You turn on the flashlight. The beam iluminates the wilderness around you. You hear a rustling in a nearby bush you shine your light on the source. You see a wolf in the brush! Do you ATTACK the wolf or RUN away?")
    if level2 == "ATTACK":
        print("CHARGE!!! You attack the wolf with everything you have, but without a weapon you are overpowered. The last thing you see before you faint is the wolf tearing into your throat. THE END")
    if level2 == "RUN":
        level3 = input("You rush into the brush! Some parts are obscured by thick brush but you tear through it. As you run, your flashlight exposes the edge of a cliff that would've spelled your demise. Far away you see a cabin across a BRIDGE and a RIVER down below the cliff.")
        if level3 == "RIVER":
            print("As you scale down the cliff, you lose your grip and fall into the river below breaking both of you legs. You last moments are spent in the suffocating darkness. THE END")
        if level3 == "BRIDGE":
            level4 = input("Making a quick decision you sprint for the far off bridge! You hear wolves howling in excitement behind you as you reach the bridge. You are halfway across when the wolves arrive. Do you jump into the RIVER below or make a mad dash for the CABIN ahead?")
            if level4 == "RIVER":
                print("You leap into the river! The rush of wind in your ears is intense as you plunge into the river below. You're sucked down into its depths and almost drown. Coughing you manage to make your way out of the river and pass out. When you come to, you hear a rattling sound. There's a rattlesnake right in front of you. You stay still as your fate is determined by this serpent... THE END")
            if level4 == "CABIN":
                print("Using the last of your strength you run across the bridge towards the cabin. With the wolves behind you, you barely have enough time to open the door and manage to close it before the wolves slam into it. You lock the door quickly to find you aren't alone. 'You are tresspassing' says the forest ranger. You are arrested but alleived of charges when your tale is told. THE END")
