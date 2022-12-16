import requests


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    file = requests.get(path).json()
    return file

def get_candidate(data, candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in data:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(data, candidate_name):
    """возвращает кандидатов по имени"""
    for candidate in data:
        if candidate["name"] == candidate_name:
            return candidate


def get_candidates_by_skill(data, skill_name):
    """возвращает кандидатов по навыку"""
    result =[]
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result


def searching_name(data, name):
    result = []
    for candidate in data:
        if name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result
