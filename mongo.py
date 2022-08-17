import pymongo
from sqlite_example import connect_to_sqlite, execute_query
import queries
from pprint import pprint


def connect_to_mongo(db_name):
    client = pymongo.MongoClient("mongodb+srv://bencavins:@cluster0.wnownih.mongodb.net/?retryWrites=true&w=majority")
    db = client[db_name]
    return db


def build_character_dicts(character_tuples):
    """Convert list of tuples to list of dicts"""
    result = []
    for tuple in character_tuples:
        result.append(build_character_dict(tuple))
    return result


def build_character_dict(character_tuple):
    """Convert a single character tuple to dict"""
    d = {
        'character_id': character_tuple[0],
        'name': character_tuple[1],
        'level': character_tuple[2],
        'exp': character_tuple[3],
        'hp': character_tuple[4],
        'strength': character_tuple[5],
        'intelligence': character_tuple[6],
        'dexterity': character_tuple[7],
        'wisdom': character_tuple[8],
        'items': get_items_dicts_by_character_id(character_tuple[0]),
    }
    return d


def get_items_dicts_by_character_id(character_id):
    conn = connect_to_sqlite()
    query = f"""
    SELECT ai.*
    FROM charactercreator_character_inventory as ci
    JOIN armory_item as ai
        ON ci.item_id = ai.item_id
    WHERE ci.character_id = {character_id}"""
    item_tuples = execute_query(conn, query)
    result = []
    for tuple in item_tuples:
        result.append(build_item_dict(tuple))
    return result


def build_item_dict(item_tuple):
    return {
        'item_id': item_tuple[0],
        'name': item_tuple[1],
        'value': item_tuple[2],
        'weight': item_tuple[3],
    }


if __name__ == '__main__':
    # create mongo connection
    db = connect_to_mongo('rpg')
    # create sqlite connection 
    sqlite_conn = connect_to_sqlite()
    # query for character data
    character_tuples = execute_query(sqlite_conn, queries.select_all_characters)
    # convert character data to dict
    character_dicts = build_character_dicts(character_tuples)
    # # insert into mongo
    db.characters.insert_many(character_dicts)
