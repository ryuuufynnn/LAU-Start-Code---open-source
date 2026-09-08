from pathlib import Path

LANGUAGES = {
    "1": ("Python", ".py"),
    "2": ("Java", ".java"),
    "3": ("C", ".c"),
    "4": ("C++", ".cpp"),
    "5": ("C#", ".cs"),   
    "6": ("JavaScript", ".js"),
    "7": ("PHP", ".php"),
    "8": ("TypeScript", ".ts"),   
}

def choose_language():
    print("\n Chose a Programming Language: ")

    for number, (name, extension) in LANGUAGES.items():
        print(f"{number}, {name}")

    while True:
        choice = input("Enter choice: ")

        if choice in LANGUAGES:
            return LANGUAGES[choice]
        print("Invalid choice.Please try again.")

def choose_template():
    print("\nChoose a project template:")
    print("1. Basic")
    print("2. Web dev")

    while True:
        choice = input("\nEnter choice: ")

        if choice == "1":
            return "basic"
        if choice == "2":
            return "web"
        
        print("Invalid choice. Please try again.")

def create_project(project_name, language, extension, template):
    projects_path = Path.home() / "Projects"
    projects_path.mkdir(exist_ok = True)

    project_path = projects_path / project_name
    project_path.mkdir()

    if template == "basic":
        filename = "Main" if language == 'Java' else "main"
        source_file = project_path / f"{filename}{extension}"
        source_file.touch()
    elif template == "web":
        (project_path / "index.html").touch()
        (project_path / "style.css").touch()
        (project_path / "script.js").touch()

    return project_path\

def main():
    print("LAU Start Code")

    project_name = input("\nProject Name: ")

    language, extension = choose_language()

    project_path = create_project(
        project_name,
        language,
        extension,
        template
    )

    print("\nProject craeted successfully!")
    print(f"Location: {project_path}")

if __name__ == "__main__":
    main()