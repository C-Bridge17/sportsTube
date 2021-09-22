from app.models import db, Video
from faker import Faker

faker = Faker()


# id = db.Column(db.Integer, primary_key=True)
#     caption = db.Column(db.String)
#     videoUrl = db.Column(db.String, nullable=False)
#     userId = db.Column(db.Integer, db.ForeignKey("users.id"))
#     createdAt = db.Column(db.DateTime)


def seed_videos():
    v1 = Video(caption='Premier League Matchweek 5: N\'Golo Kante stars for Chelsea | The Breakdown | NBC Sports',
               videoUrl="https://www.youtube.com/embed/QfN4OpAE9OE", userId=2, createdAt=faker.date())
    v2 = Video(caption='Premier League Matchweek 6 preview: Chelsea vs. Manchester City | Pro Soccer Talk | NBC Sports', videoUrl="https://www.youtube.com/embed/FJ9ATU7YSFo",
               userId=2, createdAt=faker.date())
    v3 = Video(caption='Premier League Matchweek 6 preview | Pro Soccer Talk | NBC Sports',
               videoUrl="https://www.youtube.com/embed/giJNXWpsmrY", userId=2, createdAt=faker.date())
    v4 = Video(caption='Turn the Page Tuesday: How did Bill Belichick confuse Zach Wilson? | Safety Blitz | NBC Sports', videoUrl="https://www.youtube.com/embed/K8jr-e5vSkI",
               userId=2, createdAt=faker.date())
    v5 = Video(caption='Lionel Messi, Cristiano Ronaldo have opposite starts with new clubs | Pro Soccer Talk | NBC Sports', videoUrl="https://www.youtube.com/embed/4bubYNEYlBY",
               userId=2, createdAt=faker.date())
    v6 = Video(caption='Does Ben Roethlisberger have the arm to win the AFC North? | Safety Blitz | NBC Sports', videoUrl="https://www.youtube.com/embed/Lobt4RrW5dU",
               userId=2, createdAt=faker.date())
    v7 = Video(caption='After Andy Dalton injury, is Justin Fields ready to start? | Pro Football Talk | NBC Sports', videoUrl="https://www.youtube.com/embed/EDi54r2gWGo",
               userId=2, createdAt=faker.date())
    v8 = Video(caption='Reliving Tom Brady\'s first Pats season 20 years later | Pro Football Talk | NBC Sports',
               videoUrl="https://www.youtube.com/embed/xfnSEO89soU", userId=2, createdAt=faker.date())
    v9 = Video(caption='Could lack of ownership be holding Green Bay Packers back? | Pro Football Talk | NBC Sports', videoUrl="https://www.youtube.com/embed/2_mprlpziDA",
               userId=2, createdAt=faker.date())
    v10 = Video(caption='Calahan Young leads miraculous goalball comeback to put USA in semis | NBC Sports', videoUrl="https://www.youtube.com/embed/r78aujabsNs",
                userId=2, createdAt=faker.date())
    v11 = Video(caption='USA goalball makes incredible comeback, wins shootout to advance to gold medal game | NBC Sports',
                videoUrl="https://www.youtube.com/embed/6lfckl8LU_8", userId=2, createdAt=faker.date())
    v12 = Video(caption='Top 4 finishers separated by just .03 in T64 100m; historic tie for bronze | Tokyo 2020 Paralympics',
                videoUrl="https://www.youtube.com/embed/G_zirl7iUq4", userId=2, createdAt=faker.date())
    v13 = Video(caption="See-Ya, Sixers! Who’s to Blame for Ben Simmons’ Philly Falling Out? | The Rich Eisen Show",
                videoUrl="https://www.youtube.com/embed/TqeM4j9ljWg", userId=2, createdAt=faker.date())
    v14 = Video(caption='World Record holder Karsten Warholm crushes 400m hurdles for Diamond League title | NBC Sports', videoUrl="https://www.youtube.com/embed/2_RaqOEV2P8",
                userId=2, createdAt=faker.date())
    v15 = Video(caption='Comparing Chelsea\'s Romelu Lukaku vs. Tottenham\'s Harry Kane | Premier League | NBC Sports',
                videoUrl="https://www.youtube.com/embed/UEsMSd7bE_Q", userId=2, createdAt=faker.date())
    v16 = Video(caption='Lowe Down: Special Ryder Cup edition | Premier League | NBC Sports',
                videoUrl="https://www.youtube.com/embed/zoRiySkoXP0", userId=2, createdAt=faker.date())
    v17 = Video(caption='PFT’s Mike Florio on Possibility Injury-Depleted Texans Would Start Deshaun Watson | Rich Eisen Show',
                videoUrl="https://www.youtube.com/embed/Hg1rnmduCuA", userId=2, createdAt=faker.date())
    v18 = Video(caption='Nuno Espirito Santo: Spurs couldn\'t sustain momentum v. Chelsea | Premier League | NBC Sports',
                videoUrl="https://www.youtube.com/embed/C40ax3kC5KM", userId=2, createdAt=faker.date())
    v19 = Video(caption='Tottenham Hotspur v. Chelsea | PREMIER LEAGUE HIGHLIGHTS | 9/19/2021 | NBC Sports',
                videoUrl="https://www.youtube.com/embed/udyweeLwTtM", userId=2, createdAt=faker.date())
    v20 = Video(caption='NFL Week 2 takeaways: It\'s Lamar Jackson\'s world, early MVP candidates | Safety Blitz | NBC Sports',
                videoUrl="https://www.youtube.com/embed/KLuW8LANQ40", userId=2, createdAt=faker.date())

    a1 = Video(caption="Hidden Chats You Surely Missed! #2", videoUrl='https://www.youtube.com/embed/dN6TUvFzI2Y',
               userId=3, createdAt=faker.date())
    a2 = Video(caption="Legendary Reactions #2",
               videoUrl='https://www.youtube.com/embed/OSow5E1n4Zs', userId=3, createdAt=faker.date())
    a3 = Video(caption="Moments That No One Expected", videoUrl='https://www.youtube.com/embed/iKTks3w7auc',
               userId=3, createdAt=faker.date())
    a4 = Video(caption="High IQ Moments in Sports",
               videoUrl='https://www.youtube.com/embed/AbnjSelQYV8', userId=3, createdAt=faker.date())
    a5 = Video(caption="Goals If Weren't Filmed, Nobody Would Believe",
               videoUrl='https://www.youtube.com/embed/0Yscayo0If4', userId=3, createdAt=faker.date())
    a6 = Video(caption="WTF Moments", videoUrl='https://www.youtube.com/embed/xkBR2P2zdHQ',
               userId=3, createdAt=faker.date())
    a7 = Video(caption="Penalty Mind Games",
               videoUrl='https://www.youtube.com/embed/ow4OfLD1C5Y', userId=3, createdAt=faker.date())
    a8 = Video(caption="High IQ Moments", videoUrl='https://www.youtube.com/embed/kfYqraFOpxQ',
               userId=3, createdAt=faker.date())
    a9 = Video(caption="Comedy Moments", videoUrl='https://www.youtube.com/embed/pAtfjBgR4Kk',
               userId=3, createdAt=faker.date())
    a10 = Video(caption="Angry Moments", videoUrl='https://www.youtube.com/embed/li__A2JDaLQ',
                userId=3, createdAt=faker.date())
    a11 = Video(caption="Legendary Reactions",
                videoUrl='https://www.youtube.com/embed/uxdLO6UxlIk', userId=3, createdAt=faker.date())
    a12 = Video(caption="Funny Penalty Kicks",
                videoUrl='https://www.youtube.com/embed/_TFribViDSs', userId=3, createdAt=faker.date())
    a13 = Video(caption="10 Legendary Things Ronaldo Did in 2021",
                videoUrl='https://www.youtube.com/embed/EXiv-U9J9XI', userId=3, createdAt=faker.date())
    a14 = Video(caption="Beautiful Moments of Respect",
                videoUrl='https://www.youtube.com/embed/AWg8cF614XM', userId=3, createdAt=faker.date())
    a15 = Video(caption="Hidden Chats You Surely Missed!",
                videoUrl='https://www.youtube.com/embed/Fk_SyN2fbHs', userId=3, createdAt=faker.date())
    a16 = Video(caption="Unbelievable Ronaldo Goals at Portugal",
                videoUrl='https://www.youtube.com/embed/i1fCccPOihM', userId=3, createdAt=faker.date())
    a17 = Video(caption="9 Impressive Things Ronaldo did for Portugal",
                videoUrl='https://www.youtube.com/embed/RY43vyms1J8', userId=3, createdAt=faker.date())
    a18 = Video(caption="Ridiculous Penalty Moments",
                videoUrl='https://www.youtube.com/embed/Kjbq2x8wQ88', userId=3, createdAt=faker.date())
    a19 = Video(caption="EURO Goals Worth Watching Again",
                videoUrl='https://www.youtube.com/embed/tMuYkCM_rdc', userId=3, createdAt=faker.date())
    a20 = Video(caption="It’s Ronaldo’s fault Juve is Horrible?",
                videoUrl='https://www.youtube.com/embed/4RvGdVBHut0', userId=3, createdAt=faker.date())

    b1 = Video(caption="Bucket List: Walking on a Plane",
               videoUrl="https://www.youtube.com/embed/rzi_iXUTuXY", userId=4, createdAt=faker.date())
    b2 = Video(caption="Chainsaw Carving Competition | OT 29",
               videoUrl="https://www.youtube.com/embed/D7f04YOXQq8", userId=4, createdAt=faker.date())
    b3 = Video(caption="Submarine Minefield Battle", videoUrl="https://www.youtube.com/embed/BTVMLRSsb3o",
               userId=4, createdAt=faker.date())
    b4 = Video(caption="Games With Consequences | Flight Simulator",
               videoUrl="https://www.youtube.com/embed/lHticm97HAI", userId=4, createdAt=faker.date())
    b5 = Video(caption="Games With Consequences | Flight Simulator",
               videoUrl="https://www.youtube.com/embed/lHticm97HAI", userId=4, createdAt=faker.date())
    b6 = Video(caption="Trying to Bench 405 lbs Underwater | OT 28",
               videoUrl="https://www.youtube.com/embed/RL42Yl4LS6c", userId=4, createdAt=faker.date())
    b7 = Video(caption="Demolition Derby Battle",
               videoUrl="https://www.youtube.com/embed/y2TPOTlPU9M", userId=4, createdAt=faker.date())
    b8 = Video(caption="Cell Phone Stereotypes",
               videoUrl="https://www.youtube.com/embed/2EGuVKx_MXA", userId=4, createdAt=faker.date())
    b9 = Video(caption="World's Hottest Hot Sauce | OT 27",
               videoUrl="https://www.youtube.com/embed/Tl1ycnEFk3I", userId=4, createdAt=faker.date())
    b10 = Video(caption="Fastest Soapbox Car Wins",
                videoUrl="https://www.youtube.com/embed/Df_hrHHcQ_g", userId=4, createdAt=faker.date())
    b11 = Video(caption="Bucket List: South Africa",
                videoUrl="https://www.youtube.com/embed/I4AgeDIrHGY", userId=4, createdAt=faker.date())
    b12 = Video(caption="Pet Peeves (Official Music Video)",
                videoUrl="https://www.youtube.com/embed/_eIH4F-24M4", userId=4, createdAt=faker.date())
    b13 = Video(caption="World's Weirdest Item | OT 26",
                videoUrl="https://www.youtube.com/embed/PAgQHcKMOIk", userId=4, createdAt=faker.date())
    b14 = Video(caption="RC Helicopter Battle | Dude Perfect",
                videoUrl="https://www.youtube.com/embed/Z8y05MbYm1Q", userId=4, createdAt=faker.date())
    b15 = Video(caption="OUR WIVES JOIN THE SHOW | OT 25",
                videoUrl="https://www.youtube.com/embed/8Mc6zZxBTLA", userId=4, createdAt=faker.date())
    b16 = Video(caption="Longest Dunk Wins",
                videoUrl="https://www.youtube.com/embed/qUUloBe5vEo", userId=4, createdAt=faker.date())
    b17 = Video(caption="Dude Wars | OT 24", videoUrl="https://www.youtube.com/embed/n1dEqq2hepw",
                userId=4, createdAt=faker.date())
    b18 = Video(caption="Toy Trick Shots | Dude Perfect",
                videoUrl="https://www.youtube.com/embed/cfZA6udrVUc", userId=4, createdAt=faker.date())
    b19 = Video(caption="Game Night Stereotypes", videoUrl="https://www.youtube.com/embed/EsVPUpDyGec",
                userId=4, createdAt=faker.date())
    b20 = Video(caption="Flying RC Car",
                videoUrl="https://www.youtube.com/embed/74ZSIJk2pcg", userId=4, createdAt=faker.date())

    c1 = Video(caption="SOMEONE FIND AARON JONES' CHAIN", videoUrl="https://www.youtube.com/embed/QxpitsqxDg8",
               userId=5, createdAt=faker.date())
    c3 = Video(caption="Aaron Rodgers welcomes Jared Goff to the NFC North",
               videoUrl="https://www.youtube.com/embed/ZXROQ9qjcOo", userId=5, createdAt=faker.date())
    c4 = Video(caption="0 context moment",
               videoUrl="https://www.youtube.com/embed/8lGey0hIonY", userId=5, createdAt=faker.date())
    c5 = Video(caption="that hurts", videoUrl="https://www.youtube.com/embed/wRgFjXG4siY",
               userId=5, createdAt=faker.date())
    c6 = Video(caption="Aaron Rodgers is back 😈",
               videoUrl="https://www.youtube.com/embed/YBi0fC6CgH4", userId=5, createdAt=faker.date())
    c7 = Video(caption="Eli Manning tells bar story w/ Brett Favre",
               videoUrl="https://www.youtube.com/embed/SnUMhES3gUs", userId=5, createdAt=faker.date())
    c8 = Video(caption="almost the catch of the year",
               videoUrl="https://www.youtube.com/embed/F56FCa9GtvE", userId=5, createdAt=faker.date())
    c9 = Video(caption="poor kicker 😢",
               videoUrl="https://www.youtube.com/embed/f_xtuDzriBY", userId=5, createdAt=faker.date())
    c10 = Video(caption="Gronk's secret to success",
                videoUrl="https://www.youtube.com/embed/5kvGg-HwRnM", userId=5, createdAt=faker.date())
    c11 = Video(caption="intentional grounding?",
                videoUrl="https://www.youtube.com/embed/YHSdjsU41_c", userId=5, createdAt=faker.date())
    c12 = Video(caption="the first Packers TD in 8 months 🔥🔥",
                videoUrl="https://www.youtube.com/embed/yGfLiqESKmQ", userId=5, createdAt=faker.date())
    c13 = Video(caption="Chiefs vs. Ravens INSANE FINAL MINUTES | Game of the Year? | NFL Week 2",
                videoUrl="https://www.youtube.com/embed/O_rcE1qLRZo", userId=5, createdAt=faker.date())
    c14 = Video(caption="Ravens make GUTSIEST CALL OF THE YEAR & it PAYS OFF",
                videoUrl="https://www.youtube.com/embed/ZKXABv_svjA", userId=5, createdAt=faker.date())
    c15 = Video(caption="Clyde Edwards-Helaire FUMBLES in Field Goal Range",
                videoUrl="https://www.youtube.com/embed/6cjejkOoD10", userId=5, createdAt=faker.date())
    c16 = Video(caption="Lamar fooled the entire defense 😳",
                videoUrl="https://www.youtube.com/embed/rB9FyFkPxhg", userId=5, createdAt=faker.date())
    c17 = Video(caption="offense.exe has temporarily stopped working",
                videoUrl="https://www.youtube.com/embed/VhUpEX5QK-E", userId=5, createdAt=faker.date())
    c18 = Video(caption="Chiefs defense has left the chat",
                videoUrl="https://www.youtube.com/embed/veZMy3hFi-s", userId=5, createdAt=faker.date())
    c19 = Video(caption="Ravens defense has left the chat",
                videoUrl="https://www.youtube.com/embed/f4x-DatWdbw", userId=5, createdAt=faker.date())
    c20 = Video(caption="Al Michaels is a savage",
                videoUrl="https://www.youtube.com/embed/FSNlbTFcFYA", userId=5, createdAt=faker.date())

    d1 = Video(caption="No. 7 Texas A&M at No. 16 Arkansas Betting Preview (Best Bets, Pick to Win, & MORE) | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/oms-umRjmic", userId=6, createdAt=faker.date())
    d2 = Video(caption="Gary Danielson Preview No. 7 Texas A&M vs No. 16 Arkansas | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/Ha8NPz7sONA", userId=6, createdAt=faker.date())
    d3 = Video(caption="NFL Analyst on Dolphins vs Raiders (Tua OUT, Derek Carr, & MORE) | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/oXWgJCzOT1w", userId=6, createdAt=faker.date())
    d4 = Video(caption="BREAKING: Justin Fields to Start Sunday at Browns | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/6hsPg3Dk74w", userId=6, createdAt=faker.date())
    d5 = Video(caption="CeeDee Lamb on Fantasy Football, Cowboys vs Eagles, Dak Prescott, & MORE | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/J7ZgWOZAGH4", userId=6, createdAt=faker.date())
    d6 = Video(caption="BREAKING: Tua Tagovailoa Ruled OUT Sunday vs Raiders with Fractured Ribs | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/kUHkwjrWJbI", userId=6, createdAt=faker.date())
    d7 = Video(caption="Former Super Bowl Champ on Titans, Ravens, Cowboys & MORE | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/r4izAmjPfOM", userId=6, createdAt=faker.date())
    d8 = Video(caption="NFL Insider on Panthers 2-0 Start, Texans Surprising, & Steelers Offense | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/4Bc8VTQOgh0", userId=6, createdAt=faker.date())
    d9 = Video(caption="Punches fly at Canelo Alvarez-Caleb Plant press conference [Instant Reaction] | CBS Sports HQ",
               videoUrl="https://www.youtube.com/embed/8mhJQ-aZPmM", userId=6, createdAt=faker.date())
    d10 = Video(caption="Picks for EVERY Big Week 3 NFL Game | Picks to Win, Best Bets, & MORE | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/BmITJgFHpiw", userId=6, createdAt=faker.date())
    d11 = Video(caption="Michael Breed Previews 2021 Ryder Cup (Bryson-Brooks Beef, Course Breakdown, & MORE) | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/MGN-Ultgm48", userId=6, createdAt=faker.date())
    d12 = Video(caption="Odds to Win Heisman, Penn State, Clemson, & Pick to Win CFP | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/W8UT7GN4dro", userId=6, createdAt=faker.date())
    d13 = Video(caption="NFL Analyst on The Good, The Bad, & The Ugly Through NFL Week 2 | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/RjhI04cW0Oo", userId=6, createdAt=faker.date())
    d14 = Video(caption="BREAKING: Ben Simmons Will Not Report to Sixers Training Camp | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/94txawSXFuU", userId=6, createdAt=faker.date())
    d15 = Video(caption="Week 3 NFL Picks: Eagles at Cowboys, Bucs at Rams, & MORE | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/84Ai__u5WB4", userId=6, createdAt=faker.date())
    d16 = Video(caption="NFL Week 3 Power Rankings: Bucs at No. 1; 49ers, Rams, Cardinals, & Raiders All Move Up",
                videoUrl="https://www.youtube.com/embed/rIx3a01ooNY", userId=6, createdAt=faker.date())
    d17 = Video(caption="Lions vs Packers: Aaron Rodgers, Aaron Jones shine for Green Bay [FULL recap] | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/rbfUAb0qyrs", userId=6, createdAt=faker.date())
    d18 = Video(caption="Aaron Rodgers speaks after Packers blow out Lions on Monday Night Football | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/w0kYr0t4zmE", userId=6, createdAt=faker.date())
    d19 = Video(caption="Aaron Jones scores 4 TDs in first home game after father's death: 'I saluted him' | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/IVz76T6fLHQ", userId=6, createdAt=faker.date())
    d20 = Video(caption="Lions vs Packers Monday Night Football Picks and Best Bets | CBS Sports HQ",
                videoUrl="https://www.youtube.com/embed/6wzRrvoIk9M", userId=6, createdAt=faker.date())

    e1 = Video(caption="NFL C'MON MAN - Week 2, 2021",
               videoUrl="https://www.youtube.com/embed/wguEdwvxIFw", userId=7, createdAt=faker.date())
    e2 = Video(caption="NFL C'MON MAN! - Week 1, 2021",
               videoUrl="https://www.youtube.com/embed/RXw5iRdqgVQ", userId=7, createdAt=faker.date())
    e3 = Video(caption="Real Life Sports Miracles #3 || (American Football)",
               videoUrl="https://www.youtube.com/embed/ACeYI8B_Orc", userId=7, createdAt=faker.date())
    e4 = Video(caption="Real Life Sports Miracles #2 || (NBA/NCAA Basketball)",
               videoUrl="https://www.youtube.com/embed/bpEGQxnVWYM", userId=7, createdAt=faker.date())

    f1 = Video(caption="30 Weirdest Moments In Motorsport History !",
               videoUrl="https://www.youtube.com/embed/4ZJr46TwqMk", userId=8, createdAt=faker.date())
    f2 = Video(caption="Unbelievable Animal Moments Caught On Camera !", videoUrl="https://www.youtube.com/embed/DNTdhxKgkrg",
               userId=8, createdAt=faker.date())
    f3 = Video(caption="35 Mind Blowing Moments You Won't Believe If Not Caught On Camera !",
               videoUrl="https://www.youtube.com/embed/tRxzWLLfYVw", userId=8, createdAt=faker.date())
    f4 = Video(caption="1 In A Million Moments In Sports History !",
               videoUrl="https://www.youtube.com/embed/ET3KgRRS42E", userId=8, createdAt=faker.date())

    g1 = Video(caption="The Best Sports Sketches - Key & Peele",
               videoUrl="https://www.youtube.com/embed/NDXuPCmbPVY", userId=9, createdAt=faker.date())
    g2 = Video(caption="The Best Roasts from Athletes - Comedy Central Roast",
               videoUrl="https://www.youtube.com/embed/7PerCt0PwrM", userId=9, createdAt=faker.date())
    g3 = Video(caption="Key & Peele - East/West College Bowl",
               videoUrl="https://www.youtube.com/embed/gODZzSOelss", userId=9, createdAt=faker.date())
    g4 = Video(caption="If We Treated Teachers Like Pro Athletes - Key & Peele",
               videoUrl="https://www.youtube.com/embed/aYOg8EON29Y", userId=9, createdAt=faker.date())
    g5 = Video(caption="Is Tennis the Ultimate Sport?",
               videoUrl="https://www.youtube.com/embed/DiVxLUeQAzM", userId=9, createdAt=faker.date())
    g6 = Video(caption="Golf Is a Fake Sport - Joe DeRosa",
               videoUrl="https://www.youtube.com/embed/iQlzyx2k4dI", userId=9, createdAt=faker.date())

    h1 = Video(caption="The Jump reacts to Doc Rivers' comments about Ben Simmons",
               videoUrl="https://www.youtube.com/embed/BJhW_qenadE", userId=10, createdAt=faker.date())
    h2 = Video(caption="You gotta be kidding me! - Stephen A. reacts to Simmons’ refusal to attend the 76ers training camp",
               videoUrl="https://www.youtube.com/embed/457h2fNpycA", userId=10, createdAt=faker.date())
    h3 = Video(caption="Doc Rivers tells Stephen A.: 'We would love to have Ben Simmons back' | First Take", videoUrl="https://www.youtube.com/embed/hs2Bob0anq0",
               userId=10, createdAt=faker.date())
    h4 = Video(caption="Reacting to Warriors owner Joe Lacob’s comments on Ben Simmons’ fit with the team | The Jump",
               videoUrl="https://www.youtube.com/embed/0lVwnngb2BE", userId=10, createdAt=faker.date())
    h5 = Video(caption="'It looks personal!' - Max's take on the Ben Simmons news | Keyshawn, JWill & Max",
               videoUrl="https://www.youtube.com/embed/5qzOrznO8k8", userId=10, createdAt=faker.date())
    h6 = Video(caption="Perk calls Anthony Edwards a generational talent going into 2nd NBA season | The Jump",
               videoUrl="https://www.youtube.com/embed/PhdDg-UGFBU", userId=10, createdAt=faker.date())
    h7 = Video(caption="Justin Fields is QB1 👀 The rookie will start for the Bears in Week 3 with Andy Dalton out | SC",
               videoUrl="https://www.youtube.com/embed/vyridfQc2f4", userId=10, createdAt=faker.date())
    h8 = Video(caption="Caleb Plant responds to Canelo Alvarez calling him insecure | ESPN Ringside",
               videoUrl="https://www.youtube.com/embed/VZn8e0C9GQI", userId=10, createdAt=faker.date())
    h9 = Video(caption="Evaluating the Chiefs after losing to the Ravens in Week 2 | Get Up",
               videoUrl="https://www.youtube.com/embed/T-SjX-Y5AHU", userId=10, createdAt=faker.date())
    h10 = Video(caption="Will Ben Simmons or John Wall be traded first? | The Jump",
                videoUrl="https://www.youtube.com/embed/_Wq-EsT_2xs", userId=10, createdAt=faker.date())

    i1 = Video(caption="Pat Talks About How Troy Polamalu Ruined His Life",
               videoUrl="https://www.youtube.com/embed/f13ahvYl0PE", userId=11, createdAt=faker.date())
    i2 = Video(caption="Pat McAfee Reacts To Story About How Advanced Andrew Luck Was Coming Into The NFL",
               videoUrl="https://www.youtube.com/embed/074rdMFH13U", userId=11, createdAt=faker.date())
    i3 = Video(caption="Tua Out With Fractured Ribs, Reported 'Not A Serious Injury' | Pat McAfee Reacts",
               videoUrl="https://www.youtube.com/embed/BSTHCVjBqkE", userId=11, createdAt=faker.date())
    i4 = Video(caption="Justin Fields First NFL Start Will Come Against The Browns | Pat McAfee Reacts",
               videoUrl="https://www.youtube.com/embed/rEORnJab60s", userId=11, createdAt=faker.date())
    i5 = Video(caption="It's Only Week 2 And The NFL Refs May Be Worse Than Ever.. | Pat McAfee Reacts",
               videoUrl="https://www.youtube.com/embed/fmHDerlwPzs", userId=11, createdAt=faker.date())
    i6 = Video(caption="Gronk Says He Never Watches Film, Brady Tells Him Everything | Pat McAfee Reacts",
               videoUrl="https://www.youtube.com/embed/Yb_AgHvcM5A", userId=11, createdAt=faker.date())
    i7 = Video(caption="The Pat McAfee Show | Tuesday September 21st, 2021",
               videoUrl="https://www.youtube.com/embed/Ll1IxpBOYRs", userId=11, createdAt=faker.date())
    i8 = Video(caption="Aaron Rodgers Tells Pat McAfee The Importance Of Teams Liking Each Other",
               videoUrl="https://www.youtube.com/embed/jeHjc8kwt9s", userId=11, createdAt=faker.date())
    i9 = Video(caption="The Saints Superdome Caught Fire During Work On The Roof?! | Pat McAfee Reacts",
               videoUrl="https://www.youtube.com/embed/pprP6V1RnLc", userId=11, createdAt=faker.date())
    i10 = Video(caption="Pat McAfee Talks About His Experience On Monday Night Manning",
                videoUrl="https://www.youtube.com/embed/z80VFXqqRRg", userId=11, createdAt=faker.date())
    i11 = Video(caption="NFL Network Is Absolutely BULLYING One Of Their Anchors | Pat McAfee Reacts",
                videoUrl="https://www.youtube.com/embed/txq9WxfGo0g", userId=11, createdAt=faker.date())
    i12 = Video(caption="NFL Network Has Doubled Down On Bullying Their Employee...",
                videoUrl="https://www.youtube.com/embed/t53VYB1iZIw", userId=11, createdAt=faker.date())

    j1 = Video(caption="Jordan Spieth reflects on best shots from 2020-21 season",
               videoUrl="https://www.youtube.com/embed/k1qaFYgdPrM", userId=12, createdAt=faker.date())
    j2 = Video(caption="Best of | Phil Mickelson fan interactions",
               videoUrl="https://www.youtube.com/embed/4-BDE21cdKc", userId=12, createdAt=faker.date())
    j3 = Video(caption="The best aces of the year 🎯",
               videoUrl="https://www.youtube.com/embed/iLq7lod45bM", userId=12, createdAt=faker.date())
    j4 = Video(caption="Best of “Golf is hard” from the 2020-21 season",
               videoUrl="https://www.youtube.com/embed/qNsLBBW5cV4", userId=12, createdAt=faker.date())
    j5 = Video(caption="Fastest round in golf history! 🏃‍♂️",
               videoUrl="https://www.youtube.com/embed/NTkvwtMp_C4", userId=12, createdAt=faker.date())
    j6 = Video(caption="The best shots from the 2020-21 PGA TOUR season",
               videoUrl="https://www.youtube.com/embed/dpj-gKuV7Fc", userId=12, createdAt=faker.date())
    j7 = Video(caption="Cantlay vs DeChambeau | Epic 6-hole playoff at BMW Championship",
               videoUrl="https://www.youtube.com/embed/QibX7Uh39k8", userId=12, createdAt=faker.date())
    j8 = Video(caption="Phil Mickelson’s driver from the woods leads to improbable birdie at Fortinet | 2021",
               videoUrl="https://www.youtube.com/embed/OdY_aRyfcm8", userId=12, createdAt=faker.date())
    j9 = Video(caption="Bryson DeChambeau’s back-to-back eagles at BMW Championship",
               videoUrl="https://www.youtube.com/embed/4VTjGJCEcgU", userId=12, createdAt=faker.date())
    j10 = Video(caption="Wrestler Goldberg tosses fan into water, goofs off at The American Express",
                videoUrl="https://www.youtube.com/embed/0luZHrRWkdY", userId=12, createdAt=faker.date())

    k1 = Video(caption="How Cam Jordan Spent His First $1M in the NFL | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/hg2vEgJVamE", userId=13, createdAt=faker.date())
    k2 = Video(caption="How Marshon Lattimore Spent His First $1M in the NFL | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/dOyoBbHirXw", userId=13, createdAt=faker.date())
    k3 = Video(caption="How Fernando Tatís Jr. Spent His First $1M+ in MLB | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/BgQRXmDylBI", userId=13, createdAt=faker.date())
    k4 = Video(caption="How Darius Leonard Spent His First $1M in the NFL | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/06ka1U5iAtA", userId=13, createdAt=faker.date())
    k5 = Video(caption="How Justin Jefferson Spent His First $1M in the NFL | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/ug5GX-sqEms", userId=13, createdAt=faker.date())
    k6 = Video(caption="How Jalen Hurts Spent His First $1M in the NFL | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/pGB1FSkwhCI", userId=13, createdAt=faker.date())
    k7 = Video(caption="How Manny Machado Spent His First $1M in MLB | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/9-L8jyvtaJo", userId=13, createdAt=faker.date())
    k8 = Video(caption="How Will Hernandez Spent His First $1M in the NFL | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/P1-1AL21oBA", userId=13, createdAt=faker.date())
    k9 = Video(caption="How Laremy Tunsil Spent His First $1M in the NFL | My First Million | GQ Sports",
               videoUrl="https://www.youtube.com/embed/wkn4SbFBcls", userId=13, createdAt=faker.date())
    k10 = Video(caption="How Austin Ekeler Spent His First $1M in the NFL | My First Million | GQ Sports",
                videoUrl="https://www.youtube.com/embed/RYmq72UCr6U", userId=13, createdAt=faker.date())

    l1 = Video(caption="Google It | Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/Ngloek9kBF0", userId=14, createdAt=faker.date())
    l2 = Video(caption="Best of Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/3DfIiM02iNQ", userId=14, createdAt=faker.date())
    l3 = Video(caption="Game Face Challenge | Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/pXr0DMxEhx8", userId=14, createdAt=faker.date())
    l4 = Video(caption="Robbie G Rhymes | Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/6SIA0L0kw6s", userId=14, createdAt=faker.date())
    l5 = Video(caption="Overrated or Underrated? | Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/b5KCGRW2rp8", userId=14, createdAt=faker.date())
    l6 = Video(caption="Mean Tweets | Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/VOkSADFKSGk", userId=14, createdAt=faker.date())
    l7 = Video(caption="Dad Jokes | Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/deCxeko1guw", userId=14, createdAt=faker.date())
    l8 = Video(caption="The Friendship Test | Tommy & Gronky",
               videoUrl="https://www.youtube.com/embed/7tHFCjS6byM", userId=14, createdAt=faker.date())

    m1 = Video(caption="A Choice to be Made: The 2020 SI Sportpersons of the Year | Sports Illustrated",
               videoUrl="https://www.youtube.com/embed/QO_VrWDNl78", userId=15, createdAt=faker.date())
    m2 = Video(caption="Sportsperson of the Year: Patrick Mahomes | Sports Illustrated",
               videoUrl="https://www.youtube.com/embed/rQP-XXeBlxg", userId=15, createdAt=faker.date())
    m3 = Video(caption="Sportsperson of the Year: Naomi Osaka | Sports Illustrated",
               videoUrl="https://www.youtube.com/embed/Bg6FYOlYu9c", userId=15, createdAt=faker.date())
    m4 = Video(caption="Sports Illustrated Sportsperson of the Year: LeBron James",
               videoUrl="https://www.youtube.com/embed/JxvJzB4SPog", userId=15, createdAt=faker.date())
    m5 = Video(caption="Sportsperson of the Year: Breanna Stewart | Sports Illustrated",
               videoUrl="https://www.youtube.com/embed/3kK2d-8IZ5w", userId=15, createdAt=faker.date())
    m6 = Video(caption="Sportsperson of the Year: Laurent Duvernay-Tardif | Sports Illustrated",
               videoUrl="https://www.youtube.com/embed/Hfa0t7XQX1M", userId=15, createdAt=faker.date())
    m7 = Video(caption="Ali Legacy Award: LeBron James | Sports Illustrated",
               videoUrl="https://www.youtube.com/embed/E4QGNOYPV7M", userId=15, createdAt=faker.date())

    n1 = Video(caption="Can I actually break 75!? #Break75",
               videoUrl="https://www.youtube.com/embed/pXzowvIudWU", userId=16, createdAt=faker.date())
    n2 = Video(caption="First round of golf this year - I WAS BAD! #Break75 EP1",
               videoUrl="https://www.youtube.com/embed/7gSWx197lHk", userId=16, createdAt=faker.date())
    n3 = Video(caption="Links golf almost DESTROYED me! #Break75 EP2",
               videoUrl="https://www.youtube.com/embed/rgqwSjjkQBk", userId=16, createdAt=faker.date())
    n4 = Video(caption="My BEST ROUND OF GOLF....so far! #Break75 EP3",
               videoUrl="https://www.youtube.com/embed/taL2E2CkSBE", userId=16, createdAt=faker.date())
    n5 = Video(caption="My golf is IMPROVING! #Break75 EP4",
               videoUrl="https://www.youtube.com/embed/imW5c9iEh8Y", userId=16, createdAt=faker.date())
    n6 = Video(caption="255 yrds PAR 3 - HARDEST golf course I’ve played #Break75 EP5",
               videoUrl="https://www.youtube.com/embed/GE1me4ScYSQ", userId=16, createdAt=faker.date())
    n7 = Video(caption="I played a RYDER CUP course with a TOUR PRO! #Break75 EP6",
               videoUrl="https://www.youtube.com/embed/Q_lbt7qQmWA", userId=16, createdAt=faker.date())
    n8 = Video(caption="This part of my golf game is TERRIBLE #Break75 EP7",
               videoUrl="https://www.youtube.com/embed/-RCJjaGZA68", userId=16, createdAt=faker.date())
    n9 = Video(caption="GOLF PRO Vs SCRATCH JUNIOR! #Break75 EP8",
               videoUrl="https://www.youtube.com/embed/KWdOJd39pYQ", userId=16, createdAt=faker.date())
    n10 = Video(caption="I played PERFECT golf! #Break75 EP9",
                videoUrl="https://www.youtube.com/embed/clp6UnDXNr0", userId=16, createdAt=faker.date())

    list = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,    v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,
            a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, c1, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, d1, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, e1, e2, e3, e4, f1, f2, f3, f4, g1, g2, g3, g4, g5, g6, h1, h3, h4, h5, h6, h7, h8, h9, h10, j1, j3, j4, j5, j6, j7, j8, j9, j10, k1, k3, k4, k5, k6, k7, k8, k9, k10, i1, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, l1, l3, l4, l5, l6, l7, l8, m1, m3, m4, m5, m6, m7]

    for i in list:
        db.session.add(i)

    db.session.commit()


def undo_videos():
    db.session.execute('TRUNCATE videos RESTART IDENTITY CASCADE;')
    db.session.commit()
