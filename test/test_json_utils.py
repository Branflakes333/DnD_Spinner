import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from json_utils import *

# These test depend 100% on dnd_outcomes.json, if that changes, these have to change
# Since it should be changed Ever, this is fine (Until it isn't).
# These tests are more so here for completion rather than code correction. JSON is easy to work with.

def test_retrieve_base_keys():
    assert retrieve_base_keys() == ['Lineages','Backgrounds','Classes','Feats']

def test_retrieve_lineage_outcomes():
    assert retrieve_outcomes('Lineages') == ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling', 'Aarakocra', 'Aasimar', 'Changeling', 'Eladrin', 'Fairy', 'Firbolg', 'Genasi', 'Githyanki', 'Githzerai', 'Goliath', 'Harengon', 'Kenku', 'Locathah', 'Owlin', 'Satyr', 'Shadar-Kai', 'Tabaxi', 'Tortle', 'Triton', 'Verdan', 'Bugbear', 'Centaur', 'Goblin', 'Grung', 'Hobgoblin', 'Kobold', 'Lizardfolk', 'Minotaur', 'Orc', 'Shifter', 'Yuan-Ti']

def test_retrieve_background_outcomes():
    assert retrieve_outcomes('Backgrounds') == ['Acolyte', 'Anthropologist', 'Archaeologist', 'Athlete', 'Charlatan', 'City Watch', 'Clan Crafter', 'Cloistered Scholar', 'Courtier', 'Criminal', 'Entertainer', 'Faceless', 'Faction Agent', 'Far Traveler', 'Feylost', 'Fisher', 'Folk Hero', 'Giant Foundling', 'Gladiator', 'Guild Artisan', 'Guild Merchant', 'Haunted One', 'Hermit', 'House Agent', 'Inheritor', 'Investigator', 'Knight', 'Knight of the Order', 'Marine', 'Mercenary Veteran', 'Noble', 'Outlander', 'Pirate', 'Rewarded', 'Ruined', 'Rune Carver', 'Sage', 'Sailor', 'Shipwright', 'Smuggler', 'Soldier', 'Spy', 'Urban Bounty Hunter', 'Urchin', 'Uthgardt Tribe Member', 'Waterdhavian Noble', 'Witchlight Hand']

def test_retrieve_class_outcomes():
    assert retrieve_outcomes('Classes') == ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

def test_retrieve_feats_outcomes():
    assert retrieve_outcomes('Feats') == ['No Feat', 'Aberrant Dragonmark', 'Actor', 'Alert', 'Artificer Initiate', 'Athlete', 'Cartomancer', 'Charger', 'Chef', 'Crossbow Expert', 'Crusher', 'Defensive Duelist', 'Dual Wielder', 'Dungeon Delver', 'Durable', 'Eldritch Adept', 'Elemental Adept', 'Ember of the Fire Giant', 'Fey Touched', 'Fighting Initiate', 'Fury of the Frost Giant', 'Gift of the Chromatic Dragon', 'Gift of the Gem Dragon', 'Gift of the Metallic Dragon', 'Grappler', 'Great Weapon Master', 'Guile of the Cloud Giant', 'Gunner', 'Healer', 'Heavily Armored', 'Heavy Armor Master', 'Inspiring Leader', 'Keen Mind', 'Keenness of the Stone Giant', 'Lightly Armored', 'Linguist', 'Lucky', 'Mage Slayer', 'Magic Initiate', 'Martial Adept', 'Medium Armor Master', 'Metamagic Adept', 'Mobile', 'Moderately Armored', 'Mounted Combatant', 'Observant', 'Piercer', 'Poisoner', 'Polearm Master', 'Resilient', 'Ritual Caster', 'Rune Shaper', 'Savage Attacker', 'Sentinel', 'Shadow Touched', 'Sharpshooter', 'Shield Master', 'Skill Expert', 'Skilled', 'Skulker', 'Slasher', 'Soul of the Storm Giant', 'Spell Sniper', 'Strike of the Giants', 'Tavern Brawler', 'Telekinetic', 'Telepathic', 'Tough', 'Vigor of the Hill Giant', 'War Caster', 'Weapon Master', 'Bountiful Luck', 'Dragon Fear', 'Dragon Hide', 'Dwarven Fortitude', 'Drow High Magic', 'Elven Accuracy', 'Fade Away', 'Fey Teleportation', 'Flames of Phlegethos', 'Infernal Constitution', 'Orcish Fury', 'Prodigy', 'Revenant Blade', 'Second Chance', 'Squat Nimbleness', 'Svirfneblin Magic', 'Wood Elf Magic']

def test_retrieve_base_keys():
    assert retrieve_base_keys() == ['Lineages','Backgrounds','Classes','Feats']

def test_retrieve_sublineage_outcomes():
    assert retrieve_outcomes('Lineages','Dwarf') == ['Hill', 'Mountain', 'Duergar']

def test_retrieve_subclass_outcomes():
    assert retrieve_outcomes('Classes','Druid') == ['Circle of Dreams', 'Circle of the Land', 'Circle of the Moon', 'Circle of the Shepherd', 'Circle of Spores', 'Circle of Stars', 'Circle of Wildfire']

def test_retrieve_prereq_outcomes():
    assert retrieve_outcomes('Feats','Bountiful Luck') == ['Halfling']
