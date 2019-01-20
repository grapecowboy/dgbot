import discord
import os
import random
import pprint
from functools import reduce
import argparse
import sys
import string
import math
from functools import reduce
from keep_alive import keep_alive
from discord.ext import commands
import music

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):

    if message.author != client.user:
        #await client.send_message(message.channel, message.content[::-1])

        if message.content=="!dg":
          temp = message.content
          message.content = "making delta green agent..."
          message.content += "\n\n"
          message.content += temp + "\n\n"
          music.main()
          message.content += "CHARACTER PROFESSION : " + music.characterProfession +"\n\n" + "CHARACTER PREVIOUS PROFESSION : " + music.characterBeforeProfession + "\n\n"
          message.content += "CHARACTER STATISTICS : " + "\n" + pprint.pformat(music.characterStatistics) + "\n\n" + "CHARACTER ATTRIBUTES : " + pprint.pformat( music.characterAttributes ) + "\n\n" + "CHARACTER BONDS : " + pprint.pformat( music.characterBonds ) + "\n\n" + "CHARACTER SKILLS : " + pprint.pformat( music.characterSkills ) + "\n\n" + "CHARACTER DELTA GREEN EXPERIENCE : " + pprint.pformat( music.characterDeltaGreenExperience )
          message.content += "\n\n"
          await client.send_message(message.channel, message.content )
        elif message.content=="!dg -h":
          #music.botarguments = ['-h']
          #try:
            #music.main()
          #except:
          #  print("Help done")
          
          message.content ="""
usage: music.py [-h]
                [--prof {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26}]
                [--b4 {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40}]

Delta Green Character Generator v1.0

1. anthropologist1
2. anthropologist2
3. historian1
4. historian2
5. computer scientist
6. engineer
7. federal agent
8. physician
9. scientist
10. special operator
11. criminal
12. firefighter
13. foreign service officer
14. intelligence analyst
15. intelligence case officer
16. lawyer
17. business executive
18. media specialist
19. nurse
20. paramedic
21. pilot
22. sailor
23. police officer
24. program manager
25. soldier
26. marine

Previous Professions

1. artist
2. actor
3. musician
4. athlete
5. author
6. editor
7. journalist
8. black bag training
9. blue collar worker
10. bureaucrat
11. clergy
12. combat veteran
13. computer enthusiast
14. hacker
15. counselor
16. crimnalist
17. firefighter
18. gangster
19. deep cover
20. interrogator
21. liberal arts degree
22. military officer
23. mba
24. nurse
25. paramedic
26. pre-med
27. occult investigator
28. consipracy theorist
29. outdoorsman
30. photographer
31. pilot
32. sailor
33. police officer
34. science grad student
35. social worker
36. criminal justice degree
37. soldier
38. marine
39. translator
40. urban explorer

optional arguments:
  -h, --help            show this help message and exit
  --prof {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26}
                        Specify profession for generation with an integer
  --b4 {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40}
                        Specify previous profession for generation with an integer          
          """
          await client.send_message(message.channel,message.content)
        
        elif message.content.startswith("!dg --prof"):
          music.botarguments = message.content.split()[1:]
          try:
            music.main()
          except:
            print("runtime error in non random mode")
          temp = message.content
          message.content = "making delta green agent..."
          message.content += "\n\n"
          message.content += temp + "\n\n"
          message.content += "CHARACTER PROFESSION : " + music.characterProfession +"\n\n"+ "CHARACTER PREVIOUS PROFESSION : " + music.characterBeforeProfession + "\n\n"
          message.content += "CHARACTER STATISTICS : " + pprint.pformat(music.characterStatistics) + "\n\n"
          message.content += "\n\n"+ "CHARACTER ATTRIBUTES : " + pprint.pformat( music.characterAttributes ) + "\n\n" + "CHARACTER BONDS : " + pprint.pformat( music.characterBonds ) + "\n\n" + "CHARACTER SKILLS : " + pprint.pformat( music.characterSkills ) + "\n\n" + "CHARACTER DELTA GREEN EXPERIENCE : " + pprint.pformat( music.characterDeltaGreenExperience )
          message.content += "\n\n"
          await client.send_message(message.channel, message.content )
          

          
          
        
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)