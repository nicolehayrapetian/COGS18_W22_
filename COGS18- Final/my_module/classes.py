import random 

class Player ():
    
    def __init__ (self, name):
        self.name = name 
        self.lives = 3
        self.rank = 0 
        self.dragonslayer = False
        
    def lose_life (self):
        """Player loses life. 
    
        Parameters
        ----------
        None. 

        Returns
        -------
        None. 
        """
        self.lives = self.lives - 1
    
    def upper_rank (self):
        """Increases a players rank. 
    
        Parameters
        ----------
        None. 

        Returns
        -------
        None. 
        """
        self.rank = (self.rank + 1)
    
    def rank_title (self):
        """Player will be given a title. 
    
        Parameters
        ----------
        None.
        
        Returns
        -------
        answer : string
            The rank title will be given to the player. 
        """
        if self.rank >= 0 and self.rank <= 3 and self.dragonslayer == False:
            return 'PEASANT'
        elif self.rank >= 4 and self.rank <= 6 and self.dragonslayer == False:
            return 'FARMER'
        elif self.rank >= 7 and self.rank <= 9 and self.dragonslayer == False:
            return 'KNIGHT'
        elif self.rank >= 10 and self.rank <= 13 and self.dragonslayer == False:
            return 'BLACK KNIGHT'
        elif self.rank == 14 or self.dragonslayer == True:
            return 'DRAGON SLAYER'
        
    def info (self):
        """Players information is documented. 
    
        Parameters
        ----------
        None.

        Returns
        -------
        answer : string
            This will result in the players information to be displayed. 
        """
        print ('Name: ' + self.name)
        print ('Questions Correct: ' + str(self.rank))
        print ('Ranking: ' + self.rank_title())
        print ('Lives Remaining: ' + str(self.lives))

class Question:

    def __init__ (self, question, choices, answers):
        """Creates an object of the question class. 
    
        Parameters
        ----------
        self : Question
            . 
        question : string
            It contains the question that will be asked in the trivia.
        choices : list 
            A list of strings containing mutiple choices to question.
        answers : list 
            A list of strings of the correct answer choice to the question provided.
            
        Returns
        -------
        None. 
        """
        self.question = question
        self.choices = choices
        self.answers = answers

    def print_choices(self):
        """Prints the choices. 
    
        Parameters
        ----------
        self : Question
            . 

        Returns
        -------
        None. 
        """
        for choices in self.choices:
            print(choices)

    def check_answer(self, userAnswer):
        """Allows to check if answer provided is correct. 
    
        Parameters
        ----------
        self : Question
            . 
        userAnswer : string
            A string that represents the players answer.

        Returns
        -------
        answer : boolean
            Results True if the players answer matches the correct answer choice, if not then it returns False. 
        """
        userAnswer = userAnswer.strip ()
        for answer in self.answers:
            if userAnswer.lower() == answer.lower():
                return True
        return False
    
    def validate (self, userAnswer):
        """Ensures that given answer is within the answer choices provided. 
    
        Parameters
        ----------
        self : Question
            . 
        userAnswer : string
            A string that stores the players answer. 

        Returns
        -------
        answer : boolean
            True if userAnswer is valid, false if it is not. 
        """
        userAnswer = userAnswer.strip ()
        a_list = ['a', 'b', 'c', 'd']
        if userAnswer.lower () not in a_list:
            return False 
        else:
            return True 

class Situations:
    def __init__ (self):
        """Description. 
    
        Parameters
        ----------
        num1 : int or float
            The first number, to be added. 

        Returns
        -------
        answer : int or float
            The result of the addition. 
        """
        self.nonfatal = {
            0: ['\nYou trip, answer the question.',
                '\nYou catch yourself and continue unscathed.',
                '\nYour sprain your ankle.'
                '\nIt\'s minor but slows your progress.'],
            
            1: ['\nYou come across a bloodied traveler at the beginning of a path.' \
                '\nHe warns you to go back and take a different path. Answer to find out if you heed his warning:',
                '\nYou decide to trust his word and find a new path to follow.',
                '\nYou ignore his warning and continue onto the path.'
                '\nThe terrain is treacherous and a falling rock crushes your arm.'
                '\nYou\'re badly injured but manage to make it through.'],
            
            2: ['\nYou were sleeping then wake up to the crunching of the leaves near by in a rapid pace.' \
                '\nAnswer the question to investigate:',
               '\nYou stop a robber who was about the rob you just in time!',
               '\nYou investigate to only find, nothing of value near you anymore.'
               '\nThe robber stole everything you had:'
               '\n-your torch'
               '\n-your map'
               '\nBut glad your still alive warrier.'],
            
            3: ['\nAs your traveling your skin brushes over a bush of leaves, answer the question to see what happened:',
               '\nYou are safe, it wasn\'t posion ivy, just a bush resembling it.',
               '\nJust your luck, it was poison ivy!'
               '\nYou have to deal with this immense sensation of wanting to scratch an itch that you can\'t.'],
            
            4: ['\nOh my goodness, it starts pouring raining on your jounrey, answer the question quickly to stay dry:',
               '\nYou found shelter! Hurray, now you won\'t get struck by lighting. Now you can stay dry and stay safe.',
               '\nOh No! You can\'t find shelter anywhere near you.'
               '\nYou hurry to the nearest biggest tree you could find to stay somewhat dry.'
               '\nHowever, there is only so much a tree can do to keep you dry and safe.'
               '\nBOOM!'
               '\nA big thurder strike hits you right as you were making due with your night.'
               '\nYou barely survive and now have built a fear of thunder and rain.'],
            
            5: ['\nThe sun starts the set, and you see your path getting less and less visable as time goes by.' \
                '\nNext thing you know its pitch black, answer the question to find out what you do:',
               '\nYou begin searching before the night settles in and you conveniently find a torch next to a corpse.',
               '\nYou begin your search for anything that can help you see in the dark abyss.'
               '\nBut there is nothing near of use.'
               '\nYou need to travel the night in the dark not knowing what you might stumble across.'
               '\nUnaware of any surroundings.'
               '\nThis may even lead you to take the wrong routes, hence prolonging your time spent here.'],
            
            6: ['\nSSSSSSSSSSSSSSSS, is that a snake? All you feel is immense pain on your ankle right now.' \
                '\nDid you actaully get bit by a snake? Could it be poisonous? Answer the question to figure it out:',
               '\nIt was not poisonous, and you have nothing to fear. The pain will subside shortly.',
               '\nYou feel the sharp pain in your ankle shooting through your veins.'
               '\nThe snake was in fact venomous and you need to act quickly.'
               '\nYou decide to suck out the venom from you ankle just in time to avoid death.'
               '\nWho would know how much longer you would\'ve survived with the venom in your system.'],
            
            7: ['\nStrolling along your adventure, you see in the distance a sparkle of the suns reflection.' 
                '\nAs you approach, you see a river in the middle of you and your remaining path.' \
                '\nAnswer the question correctly to across the river safey:',
               '\nYou found a boat a little ways down!'
               '\nPhew that was a close call.'
               '\nAlmost thought you would have to swim across.'
               '\nYikes. You really got lucky with that.',
               'After searching for any sign of hope to find a boat, there was not luck.'
               '\nYou come to the decision that nothing would get in the way of you slaying this dragon.'
               '\nYou decide to swim across!'
               '\nYou knew that your training would pay off and it is being tested right now.'],
            
            8: ['\nAs the day progresses, you begin to get tired after a days of long adventering to the dragon.' \
                '\nYou see a cave near by and appraoch it to settle their till the morning.'
               '\nAs you enter you were rudely greeted by a troll.' \
                '\nAnswer the question correctly to determine how your visit at the cave will go:',
               '\nYou threaten the troll by pulling out your sword.'
               '\nThe troll was too stunned and ran in the opposite direction allowing you to do as you please in \'his cave\'.',
               '\nYou pull out your sword ready to battle this troll for this cave, just for the night.'
               '\nThe troll, suprisingly, puts up a great fight.'
               '\nUnexpectingly, another troll appears behind you with a sword and severely injures your arm.'
               '\nYou manage to fled the scene with no other major injuries.'
               '\nThe trolls had cut into the back part of your forarm riasing to your shoulder.'
               '\nYou got out just in time, although choose your fights more carefully next time.'],
            
            9: ['\nIn plain sight, as clumsy as you are, you ..., answer the question correctly to determine what would happen to you on this path:',
               '\nCongrats!' \
               '\nYou managed to spot the trap that was in the forest before being severely wounded or even worse, killed.', \
               '\nYou failed to notice the trap!' \
               '\nOh no!' \
               '\nThe wire had triggered a spring to shoot out an arrow which pierced right through your arm.' \
               '\nYou are given no other option but to cut off your arm to stop you from bleeding out.' \
               '\nYou are lucky it didnt rupture any important bodily organs that would have been letal.' \
               '\nI hope your right arm is ready for all the hard work coming it\'s way.']
        }
   
        self.fatal = {
            0: ['\nYou get lost along your journey and find yourself sinking into the floor and it hits you...'
                '\nQUICKSAND!!!'
                '\nThink fast and answer the question!',
                '\nYou manage to grab a branch and pull yourself out.',
                '\nYou didn\'t think fast enough and sunk into the quicksand.'
                '\nYou find it harder and harder to breathe.'
                '\nThe world around you begins to go black.'
                '\nThe light at the end of the tunnel calls to you.'
                '\nYou know you will never wake again...It was all meaningless.'],
            
            1: ['\nLooking too closely at your map, you take a wrong step and begin to fall off of a cliff.' \
                ' You manage to grab the ledge.'
                '\nTo survive answer the following question correctly:',
                '\nAlthough your hand was sweaty you manage to pull yourself to safety.',
                '\nThe sweat on your hand causes you to slip.'
                '\nYou begin to plunge to your doom,'
                '\nFor a brief moment you feel weightless...free...'
                '\nonly ever seeing darkness again...'],
            
            2: ['\nParched, you make your way over to a river. As you reach the banks, a monster leaps out and charges at you.'
                '\nYou reach for your sword. Answer correctly to escape its clutches:',
                '\nYou grab your sword and slay the beast.',
                '\nYour sword slips out of your hand and the monster grabs you and drags you into the river...'
                '\nIt feasts on your body turning the river a dark red with your blood...'],
            
            3: ['\nYou trip, answer the question:',
                '\nYou catch yourself before your sword plunges through your eyes.',
                '\nAs you fall, your sword impales your skull leaving you motionless on the floor.'
                '\nThe monsters and scavengers in the forest come to pick your carcas clean.'
                '\nThe only memory of you are your bones...'],
            
            4: ['\nYou\'re hungry and see some berries nearby. Answer the question to find out if you eat them:',
                '\nYou decide to wait until the next town to buy food.',
                '\nYou decide to try the berries, not knowing that they\'re poisonous.'
                '\nYou feel your throat begin to swell, leaving you gasping for air...'
                '\nThe world goes black...'],
            
            5: ['\nAfter spending many nights without sleep, you begin to hallucinate.' \
                '\nVoices begin to scream in your head telling you to end it all. Answer the question to find out if you listen:',
                '\nYou find the will to resist the voices and hobble into the nearest inn for some rest.',
                '\nThe voices break you down.'
                '\nYou begin to question everything.'
                '\nWhy are you here?'
                '\nWhy should you have to do this?'
                '\nYou just want to rest...'
                '\nYou place the cold steel of your sword to your neck...'
                '\nResolved to get the rest you desire...'],
            
            6: ['\nYou encounter another brave soul seeking to slay the dragon.' \
                '\nHe challenges you to a fight to the death.' \
                '\nThere can only be on dragon slayer here. Answer the question to see if you can defeat him:',
                '\nYou emerge from the battle, bloodied and bruised, but ultimately victorious.',
                '\nThe fight is long and difficult, your many days on the road begin to weigh on you and your sword feels' \
                ' heavier and heavier.'
                '\nThe other traveler lunges at you.'
                '\nThere is no strength left in your arms.'
                '\nAs you lay on the floor and the world begins to fade you realize...'
                '\nthis is not your story...but his.'],
            
            7: ['\nYou get caught in the middle of a heat wave. Answer the question to try and survive:',
                '\nYou wander into a small town where you find shelter and water. That was close.',
                '\nYou can\'t find shelter and you run out of your water.'
                '\nYou begin to hallucinate and feel dizzy.'
                '\nThe world spins around you...'
                '\nWhere are you?'
                '\nWhat\'s your name?'
                '\nYou shut your eyes to rest for the last time...'],
            
            8: ['\nYou spend a night on the side of the road between towns.' \
                '\nIn the night, a hooded figure comes to rob you.' \
                '\nYou try to fight them off. Answer the question to see if you survive:',
                '\nYou manage to draw your sword and scare the robber away.',
                '\nYou can\'t find your sword in the darkness and the robber pulls a knife on you.'
                '\nTrying to stop them, you fight but get stabbed in the chest. They get away with all your belongings.'
                '\nYour chest burns with pain, you collapse as you watch the robber leave with everything.'
                '\nYou lay on the ground feeling defeated.'
                '\nThe world fades away...'
                '\nThere\'s no glory in this death...'],
            
            9: ['\nYou cross a bridge on a snowy morning, the planks give way and you fall into the river.'
                '\nAnswer correctly to live:',
                '\nYou make your way to the river bank and manage to get a fire going. That could have been much worse.',
                '\nYou crawl your way out of the river. You lost your hatchet in the river and can\'t collect firewood.'
                '\nYou sit alone on the riverbank feeling chilled to your bones.'
                '\nYou feel your skin tighten like never before.'
                '\nIt begins to crack and break...'
                '\nThe fire in your heart still burns...'
                '\nBut at last that won\'t even save you...']
        }
    
        self.dragon = {
            1: ['\nYou did it! You slayed the dragon! You have earned the title of \'DRAGON SLAYER\'. You saved the town!' \
               '\nThe king, nobels, and churches commend you on your successful quest!' \
               '\nYou have done well!' \
               '\nThe town is forever in your debt for your bravey!' \
               '\nTill next time \'DRAGON SLAYER\'!'],
        
            2: ['\nYou grabbed your sword charging at the dragons neck.' \
                '\nAs you approach your heart is racing.' \
                '\nYour palms are sweating.' \
                '\nEverything is in slow-motion.' \
                '\nThen BOOOMMM!' \
                '\nYour sword sliced in half upon impact.' \
                '\nThe impossible happened. Your greatest fear:' \
                '\nFAILING' \
                '\nThe dragon spots you on his neck, after doing so, he turns his head snatching your body as if you were dinner' \
                '\n*snap, snap, snap* as the dragon feasts on your body.']
        }
        
