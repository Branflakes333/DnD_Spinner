import json


_dnd_json = None  # Private module-level variable

def _load_data():
    """
    Load data to global variable if not loaded and return data
    """
    global _dnd_json
    if _dnd_json is None:
        with open('data/dnd_outcomes.json', 'r') as f:
            _dnd_json = json.load(f)
    return _dnd_json

def retrieve_base_keys():
    """
    Return the base/root level keys as a list, barring "Mappings"
    """
    data = _load_data()
    out = list(data.keys())
    out.remove('Mappings')
    return out
    # ^--> Believe will be useful in data_parser

def retrieve_outcomes(base_key: str, sub_key: str = None) -> list:
    """
    Retrieve value(s) associated with , and optional sub_key

    Param:
    base_key (str) : Key for type of DnD Class Attribute
    sub_key (str) : Key for a value within the base key dict pairing

    return (list) : a list of keys/values associated with the key arguments
    """
    data = _load_data()
    if sub_key is not None:
        return _dict_or_list(data[base_key][sub_key][_sub_key_mapping(base_key)])
    return _dict_or_list(data[base_key])
    
def _sub_key_mapping(key):
    """
    Given a (base) key, returns the sub_key
    """
    data = _load_data()
    return data['Mappings'][key]

def _dict_or_list(iterable):
    if isinstance(iterable, dict):
        return list(iterable.keys())
    if isinstance(iterable, list):
        return iterable
    else:
        raise ValueError

