from skill_function import get_unique_skills,add_skill,remove_skill

def main():
    skills = ["Python", "SQL", "Python", "Docker", "SQL", "AWS"]
    s = "Java"
    print(get_unique_skills(skills))
    add_skill(skills,s)
    remove_skill(skills,s)

if __name__ == "__main__":
    main()