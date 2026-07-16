# Slow play notes for The Bat

## Goals

Recognize the tension, freedom and expressiveness of limited verb sets.

## Tasks

1. Note where a traditional parser puzzle might have required multiple specific verbs, but The Bat just uses one.
2. Note puzzles where the solution is about timing.
3. Explore THINK and constraints.
4. Note The Bat's subversion at the very end.


## Notes

These are my notes during play of Release 2 found on the IFDB. I've already played and reviewed The Bat, so this will be brisker than a new playthrough.

- The game starts with a question about whether you have played IF before.
 - For giggles, I said "no" and it gives a very brief tutorial.
 - To be fair, there are a lot of verbs in this game: examine, attend to, each cardinal direction, up and down, inventory, look, again, and the meta commands of save, restore, load and help.
 - It also states its Zarfian cruelty rating (without using the term)
- The introduction is standard Inform style: title, subtitle, author. But there's also a preview of the sections, framing it theatrically.
- The newspaper clipping more-or-less spells out your requirements as a job. It's so focussed it doesn't really begin or finish the sentence, it just provides the key context.
- In the first two very brief bits of text we are introduced to your character (as a mere role, not really as a person) and Master Bryce, and his manifestation of a man acting like a bat.
- HELP lays out pretty clearly the ATTEND TO mechanic:
 - Attending to items picks them up
 - Attend to items you're carrying drops them
 - Attending to something else whilst holding an item may do USE X ON Y.
- Some of the verbs that this compresses into one:
 - GET, DROP, GIVE, SHOW, PUT IN/ON/UNDER/BEHIND, TALK TO, ASK, THROW, and all sorts of specific verbs like UNLOCK, TURN, CLEAN, FIX, INSERT...
- EXAMINE BED: "A king-sized bed, of course. With his revolving door of paramours, Master Bryce puts every inch of this mattress to use." There's something very deliciously "cellar door"-y about a "revolving door of paramours".
- A nice introduction to the layout of the manor by asking you to light all the candles.
- I'm reminded of the THINK command in the mosaic hall. It gives a clear list of things to do, and compresses some down into a single task (like lighting the candles).
- Wandering the manor highlights all the elements we'll use in the farce later. Loading all our Chekhov's guns.
- Despite Master Bryce losing his mind upstairs, there's no time pressure here in exploring the manor and lighting all the candles.
- The ballroom has a twist on the "ATTEND TO CANDLES" rhythm. You're explicitly told to use a crank from the downstairs utility closet. I think this is a subtle foreshadowing of the limited inventory issues as you'll naturally want to pack-rat items, but you can't in this game.
 - Yep I can hold the harness but not open the closet.
 - In true IF fashion, the crank completely disintegrates after it's not needed any more.
- I like how the more you explore, the more that Master Bryce is mad as a cut snake - bashing into closed windows, hiding under the bed from a light... Then you find sticky remnants of his digestive system (it's politely not mentioned whether they came up or down) and it's clear he's insane.
- I love the snippets of heavily implied chaos, from the harness, to the wine, to the mentions of other assistants, to the car embedded in the dining room wall. Master Bryce is both an animal and a toddler. Are those too different?
- The dread of the Chef saying "Now you are on your own" at the moment that the map is now as open as possible for you. Let the chaos continue.
- In this intro there's no time pressure, but there's other pressures like Bryce's tantrum about the light and the chef holding back a key from you whilst badgering you about his check. The guests will be here "any moment".
- Once you have the master dressed, the game deposits you by the door with a suggestion to answer it, rather than finding your way down the stairs and maybe getting lost or distracted with the rest of the manor, which is all set up for the chaos to ensue.
- The first few doorbells happen after you solve a small puzzle. The pace picks up.
- All the shattered glass points you to the kitchen... where the cat is stealing the chicken, right on cue.
- Ooh, my first bug: I swept up the broken bottles in the drawing room and dumped them in the dining room. I did the same for the broken glass in the mosaic room, but then it suggested ATTEND TO GLASS was attempting to shatter the windscreen with my broom.
- The chaos is a bunch of little latches: dump enough in the dining room and a curling iron appears. Get Bryce into shape and the Bishop arrives.
- The flaming curtains disrupts your flow or attempt to ignore the situation by serving drinks while everything is on fire. The guests start moving around and complexity just ticks up.
- I like that the guests all enter differently, and the last guest (Celina) brings herself in as you're dealing with chaos. I also enjoy how this transfers us to the past for a quick breather, then resets the stage for the finale.
- It's a repeated joke, but I love it: "You'd never read it yourself, so you have no idea that (explicit details)." Same with the vault. And later upstairs. It's a joke that keeps on winning.
- I also like the reveal of Master Bryce's attunement to the compass and how he bashes his way around the manor.
- Little touches like Bryce bashing into walls knocks over a candelabra, which you have to attend to. It makes the world feel more alive.
- Malatesta's obvious signalling to the player how the compass works on Bryce is just fine in a game like this. It's a little obscure so explicitness helps.
- Examining Celina... Groover's writing is just superb. Well researched!
- The detective's reveal is so absurd it's delightful. The Countess was a well-drawn character and then the switch... So good.
- There's a mechanism behind everything going on. Attending to Dina drops the glass, which prompts you to both deal with the broken glass and the puddle, which sets up both the Detective's appearance and the collar.
- The compass design is an interesting fly in the ointment for the simplified verb mechanic. In a normal parser game you'd TURN COMPASS SOUTH or somesuch, but here you have to attend to it, drop into a special mode, "move", and drop out. It's a good solution, but I feel like there's a tension between the puzzle and the aesthetics. It pays off later, but I wonder if it was always on the chopping block.
- I can't tell if the randomness of the scissors and curling iron in the dining room is a cheap hack or brilliant. The oddness helps clue in the odd solution to Baron Twombly.
- "Miss Constance, if you aren't mistaken, is already attending to Emilia Ives." Glorious.
- The ping-pong between the moose head and the detective and the fun upstairs is a nice interplay and way to clue the next bit of the puzzle.
- I also like the moving piece of Celina slowly stealing bits and pieces from the guests. And dropping obvious hints.
- The repetition of the newspaper as gross mitten is great.
- I love the joke of the reveal of Malatesta's teeth going missing. I wonder if you can discover that early.
- Retrieving the mattress is the only rough edge for me. In a way it's clued by the Ives/Constance/Constance dalliance and the introduction, but it's not obvious in the room description. I wandered from room to room trying to find a solution. The fainting couch isn't permitted, but it feels like a clean solution.
- Actually, the lock-in of the compass nudges us towards the nonobvious but fantastic ending of "I QUIT". I also like that Malatesta's other role in all of this is to explicitly tell you what to do in slightly tricky situations.
- One thing I hadn't noticed before was the crashed car might have been because of the magneto-plutonium.
- I also appreciated how all the elements dovetail. There's very little fat, and excellent use of an early problem to set your expectations for a later one.

