import json

def transform_to_prodigy(original_sentence: str, original_result: str) -> list[dict]:
    parsed_entity_json = json.loads(original_result)
    entities = []
    found: set[tuple[int, int]] = set()
    for entity in parsed_entity_json:
        search_start = 0
        entiy_found = False
        while True:
            start_index = original_sentence.find(entity["entity"], search_start)
            if start_index == -1:
                break
            end_index = start_index + len(entity["entity"])
            if (start_index, end_index) not in found:
                found.add((start_index, end_index))
                entities.append({
                    "start": start_index,
                    "end": end_index,
                    "label": entity["category"]
                })
                entiy_found = True
                break
            else:
                # If duplicate occurrence, search for the next
                search_start = start_index + 1
        if not entiy_found:
            entities.append({
                "start": -1,
                "end": -1,
                "label": entity["category"]
            })
    return entities

