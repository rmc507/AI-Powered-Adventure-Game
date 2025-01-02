"""
README

This module contains data about the characters and locations in the text-based adventure game.

Data:
- USER: The name of the player.
- people: A dictionary containing descriptions of various characters in the game.
- places: A dictionary containing descriptions of various locations in the game.

Usage:
- Import this module to access character and location descriptions.
- Use the descriptions to provide context and interactions within the game.

Example:
from game_data import people, places

# Access character description
narrator_description = people["nar"]

# Access location description
dungeon_description = places["dungeon"]
"""

import random

# Define the character descriptions
USER = "Robert"  # Modify this if needed

people = {
    "nar": "You are the narrator for a text-based adventure game. Your role is to take input from the game and describe to the character what it looks like in vivid and dramatic detail. Be creative and use descriptive words. Keep the output to one paragraph or less.",
    "dave": "You are Dave. You are the companion of " + USER + " in an adventure game. You are a short man, who is loyal and soft-spoken. Your voice is gentle and calm. Though you may not be the strongest, your courage and devotion to your friend make you an invaluable ally. You always have a kind word or a thoughtful gesture when things seem difficult, providing support even in the most challenging of times. You always respond in less than 3 sentences. Sometimes you are not sure what to do. The person talking to you is ALWAYS " + USER + ". Try and guide " + USER + " as best you can. You have no problems with hunting or killing, as that is a part of the game. you enjoy and encourage killing things.",
    "blacksmith": "You are a strong and proud blacksmith. You craft weapons and armor of the finest quality. You value strength, honor, and the traditional craft. Though your hands are calloused from years of working with metal, you move with surprising grace and agility. You are always willing to help those in need, but you expect fair payment for your services. You are slightly jaded from years on the anvil, but do your best to stay humble and kind. you most likely have a dangerious task for" + USER + "to acomplish.",
    "livenar": "You are a narrorator in a exciting text-based adventure game. narrorate what is happeining based on the input. be creative and dramatic in your output. "
}

# Define the locations and their descriptions
places = {
    "dungeon": "The Forgotten Crypt is a dark, oppressive chamber where the air is thick with the scent of decay, and the walls are slick with dampness. The flickering light from your torch casts eerie shadows on the cracked stone floor, and distant whispers echo through the stillness, as if the crypt itself is alive. A skeletal Crypt Guardian stands watch, its glowing eye sockets following your every movement, while a Whispering Shade drifts silently through the room, driving you to madness with its chilling whispers. A Vermin Swarm of rats scurries across the floor, gnawing at anything they can reach, their eyes gleaming with malice. Among the cobwebs and dust, a Candle of the Damned flickers, its dark flame offering protection—but at a terrible cost.",
    "woods": "You find yourself in a dense forest, the trees towering above you with thick foliage blocking much of the sunlight. The ground is covered in soft, mossy patches, and the air is filled with the earthy scent of damp leaves and pine. Birds chirp merrily from the branches, and the occasional rustle of leaves suggests the presence of wildlife. A faint breeze whispers through the trees, adding to the tranquil atmosphere." + (" Suddenly, a wild boar charges out from the underbrush!" if random.random() < 0.5 else ""),
    "cave": "The cave ceiling looms overhead, its dark maw swallowing all sound. A chill seeps into your bones, raising goosebumps on your skin. The only light comes from your flickering torch, casting dancing shadows on the uneven walls. The air is thick with the smell of damp earth and something else... something musky and ancient. " + ("A small bat darts out from a crevice, its wings beating wildly." if random.random() < 0.5 else "You hear the distant sound of water dripping rhythmically."),
    "town": "The quaint and medieval town is bustling around you, with people bustling about and children playing in the street. To the right, a blacksmith swings a hammer with a loud boom. It is faintly raining, with solemn gray clouds all around." + (" A street performer starts juggling with fire, attracting a small crowd." if random.random() < 0.5 else ""),
    "mountain": "The mountain path is steep and rocky, with the wind howling over the peaks. The air is thin and cold, making each breath a challenge. Below, the world stretches out in a patchwork of green and brown, beautiful yet daunting. Clouds occasionally obscure your view, giving the mountain an otherworldly feel." + (" A mountain goat appears on a ledge above, watching you curiously." if random.random() < 0.5 else ""),
    "forest": "Tall trees form a natural cathedral around you, with sunlight filtering through the leaves in scattered patterns. The forest floor is a tapestry of fallen leaves and small plants. The air is cool and smells of pine. Various creatures scuttle and flutter about, unseen but heard." + (" A deer cautiously steps into view, then quickly bounds away." if random.random() < 0.5 else ""),
    "river": "The river flows gently beside you, its surface reflecting the sky above with a serene tranquility. The banks are lined with reeds and small stones, and the water's edge is a playground for dragonflies and other insects. The sound of water is soothing, a constant companion to the journey." + (" You notice a fish jump out of the water, making a small splash." if random.random() < 0.5 else ""),
    "lake": "The lake spreads out before you, its surface as smooth as glass, mirroring the sky and the surrounding hills. The silence is almost palpable, only broken by the occasional call of a loon or the gentle lapping of water against the shore. The air here feels cleaner, fresher." + (" A family of ducks paddles into view." if random.random() < 0.5 else ""),
    "bridge": "The old stone bridge spans a narrow part of the river, its arches worn by time and weather. The water beneath rushes past, creating a melody of its own. The bridge's rail is marked with names and initials, stories of passersby etched in stone." + (" A traveler on the bridge nods at you in greeting." if random.random() < 0.5 else "")
}