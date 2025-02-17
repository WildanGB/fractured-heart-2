
dialog_tree_1 = {
    "start": {
        "text": "AHHHHHH! I HAVE NO MONEY PLEASE DONT HURT ME",
        "choices": {
            "Sir Calm down! I've been sent here to help you!": "help",
            "I will be leaving then": "final"
        }
    },
    "help": {
        "text": " AAAAA- oh [clears throat]  Pardon me for my theatrics right then, I was simply practicing for my audition as a damsel in distress #25. ",
        "choices": {
            "Right ! ": "next",
            "......": "next"
        }
    },
    "next": {
        "text": " Anyways, you must be the one who the guild to help retrieve the holy relic, right?",
        "choices": {
            "Yes, what exactly happened to the relic?": "relic",
            "No, I'm just a passing adventurer": "final"
        }
    },
    "relic": {
        "text": "We were just transporting the relic to a museum for a temporary exhibit but the wagon was ambushed by a bunch of plants!",
        "choices": {
            "I am so sorry to hear that": "sorry",
            " always knew that the vegetarians were onto something.": "sorry"
        }
    },
    "sorry": {
        "text": "Well yes. But there is good news however. During the ambush, the relic was dropped so we still have half the relic",
        "choices": {
            "Thats somewhat great.": "great",
            "What happened to the other half? ": "great"
        }
    },
    "great": {
        "text": "Those darn forest creatures made off with the other half though.",
        "choices": {
            "where can I find this relic?": "where",
            "Thank you very much ! I will find them !!": "final"
        }
    },
    "where": {
        "text": "If you leave this island and follow the pathway you will eventually run into one of our scouts who is also trying to retrieve the relic, he has more information about the whereabouts than me",
        "choices": {
            "I will get to that scout right away !": "final",
            "Oh...you dont even know where they are? Fine ig thanks.": "final"
        }
    },
    "final": {
        "text": "BEST OF LUCK ON YOUR JOURNEY !! Come to the show when you are around next time , I may be a damsel. ",
        "choices": {"Bye":"end"}
    },

    "end": {
        "text": "",
        "choices": {}
    }
}

dialog_tree_2 = {
    "start": {
        "text": "Identify yourself bandit!",
        "choices": {
            "Calm down soldier, I was sent by your friend to help find the relic": "help",
            "I won't . Bye": "final"
        }
    },
    "help": {
        "text": "Oh, I see, glad you decided to help because the monsters up ahead are too strong for me.",
        "choices": {
            "What am I looking for?": "relic_info",
            "Where is it?": "location_info"
        }
    },
    "relic_info": {
        "text": "It's a heart of a mythical hero which turned into a gemstone after he died. They said that he once drank 20 beers in 15 minutes! ",
        "choices": {
            "He is so rad!": "beer_story",
            "Did he ever do anything other than irresponsible drinking?": "beer_story"
        }
    },
    "beer_story": {
        "text": "Do you want to know the location ? ",
        "choices": {
            "Yes": "location_info",
            "No": "final"
        }
    },
    "location_info": {
        "text": "It's down south. Be careful of the monsters down there though, there are more of them than usual. They seem to be drawn towards something",
        "choices": {
            "Hmm...": "monsters_drawn"
        }
    },
    "monsters_drawn": {
        "text": "Do you want to know what it is that you should be looking out for? ",
        "choices": {
            "Yes": "relic_info",
            "No": "final"
        }
    },
    "final": {
        "text": "Anyways, I must report back to the captain regarding this situation so I must bid you adieu.",
        "choices": {
            "Goodbye": "end"
        }
    },
    "end": {
        "text": "",
        "choices": {}
    }
}

dialog_tree_3 = {
    "start": {
        "text": "You there! Bring me here?",
        "choices": {
            "<I was sent here to retrieve the Fractured heart": "wounded"
        }
    },
    "wounded": {
        "text": "*cough cough* As you can see, I am tired and wounded. O' brave one.",
        "choices": {
            "What happened?": "ambushed"
        }
    },
    "ambushed": {
        "text": "I was ambushed by the plants of this forest and the huge creatures.",
        "choices": {
            "were you able to fend them off? I don't see many enemy corpses here": "relic"
        }
    },
    "relic": {
        "text": "YYes but the big animal ran into this cave and the door locked behind it",
        "choices": {
            "where can I find the key? ": "where"
        }
    },
    "where": {
        "text": "I had it on me but I must have dropped it in the grass somewhere around here while I was fighting",
        "choices": {
            "Now we have to look for the key.": "help"
        }
    },
    "help": {
        "text": "I would help out with your quest, but I'm too tired and wounded.",
        "choices": {
            "Oh that's fine, I can easily heal you right up": "heal",
        }
    },
    "heal": {
        "text": "Oh, umm that won’t be necessary cause…",
        "choices": {
            "cause what? ": "cause"
        }
    },
    "cause": {
        "text": "Oh right cause I'm allergic to healing ",
        "choices": {
            "...": "awkward"
        }
    },
    "awkward": { 
        "text": ".......... .. ... ",
        "choices": {
            " I think I'll go find the key": "final"
        }
    },
    "final": {
        "text": "yeah that sounds like a good idea",
        "choices": {
            "Goodbye": "end"
        }
    },
    "end": {
        "text": "",
        "choices": {}
    }
}



class DialogManager:
    def __init__(self, tree):
        self.tree = tree
        self.current_node = "start"

    def get_current_dialog(self):
        return self.tree[self.current_node]["text"]

    def get_choices(self):
        return self.tree[self.current_node]["choices"]

    def choose(self, choice):
        if choice in self.get_choices():
            self.current_node = self.get_choices()[choice]

    def is_end(self):
        return self.current_node == "end"

