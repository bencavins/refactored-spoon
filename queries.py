select_all_characters = """
SELECT *
FROM charactercreator_character
"""


create_character_table = """
CREATE TABLE IF NOT EXISTS character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
)
"""


total_characters = """
SELECT COUNT(*)
FROM charactercreator_character
"""


total_non_weapons = """
SELECT COUNT(*)
FROM armory_item
LEFT JOIN armory_weapon 
	ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE item_ptr_id is NULL
"""


character_items = """
SELECT charactercreator_character.character_id, charactercreator_character.name, COUNT(*)
FROM charactercreator_character
JOIN charactercreator_character_inventory
	ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
JOIN armory_item
	ON armory_item.item_id = charactercreator_character_inventory.item_id
GROUP BY charactercreator_character.character_id
LIMIT 20
"""


avg_character_items = """
SELECT AVG(item_count)
FROM
(
SELECT charactercreator_character.character_id, charactercreator_character.name, COUNT(*) as item_count
FROM charactercreator_character
JOIN charactercreator_character_inventory
	ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
JOIN armory_item
	ON armory_item.item_id = charactercreator_character_inventory.item_id
GROUP BY charactercreator_character.character_id
)
"""