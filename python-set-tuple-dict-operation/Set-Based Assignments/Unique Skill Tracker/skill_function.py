def get_unique_skills(skill_list: list):
    return set(skill_list)

def add_skill(skill_set: set, skill: str):
    a = list(skill_set)
    a.append(skill)
    b = set(a)

def remove_skill(skill_set: list, skill: str):
    a = set(skill_set)
    a.discard(skill)