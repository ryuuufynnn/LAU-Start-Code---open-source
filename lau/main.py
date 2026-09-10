import sys # for command line args
import subprocess # for vs code opening
import platform
import shutil
from pathlib import Path

penguin_name = "stcode lau"

LANGUAGES = {
    "1": ("Python", ".py"),
    "2": ("Java", ".java"),
    "3": ("C", ".c"),
    "4": ("C++", ".cpp"),
    "5": ("C#", ".cs"),
    "6": ("JavaScript", ".js"),
    "7": ("PHP", ".php"),
    "8": ("TypeScript", ".ts"),
    "9": ("Web Development", None),
}

SOURCE_TEMPLATES = {
    "Python": "# Python file and folder template.\nprint('Made by Laurence')\n",
    "Java": (
        "// Java file and folder template.\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        '        System.out.println("Made by Laurence");\n'
        "    }\n"
        "}\n"
    ),
    "C": (
        "// C file and folder template.\n"
        "#include <stdio.h>\n\n"
        "int main(void) {\n"
        '    printf("Made by Laurence\\n");\n'
        "    return 0;\n"
        "}\n"
    ),
    "C++": (
        "// C++ file and folder template.\n"
        "#include <iostream>\n\n"
        "int main() {\n"
        '    std::cout << "Made by Laurence\\n";\n'
        "    return 0;\n"
        "}\n"
    ),
    "C#": (
        "// C# file and folder template.\n"
        "using System;\n\n"
        "class Program\n"
        "{\n"
        "    static void Main()\n"
        "    {\n"
        '        Console.WriteLine("Made by Laurence");\n'
        "    }\n"
        "}\n"
    ),
    "JavaScript": "// JavaScript file and folder template.\nconsole.log('Made by Laurence');\n",
    "PHP": "<?php\n// PHP file and folder template.\necho 'Made by Laurence';\n",
    "TypeScript": "// TypeScript file and folder template.\nconsole.log('Made by Laurence');\n",
}

def choose_language():

    MAGENTA = colors()[4]
    RED = colors()[0]
    RESET = colors()[6]

    print(f"\n{MAGENTA}Choose a Programming Language: ")

    for key, (language, extension) in LANGUAGES.items():
        print(f" [{key}] {language}")
    print("")
    while True:
        choice = input(f"{MAGENTA}  > Choice > {RESET}").strip()

        if choice in LANGUAGES:
            return LANGUAGES[choice]
        print(f"{RED} Invalid choice. Please try again.{RESET}")

def get_available_project_path(projects_path, project_name):
    project_path = projects_path / project_name

    if not project_path.exists():
        return project_path
    counter = 2

    while True:
        new_name = project_name + str(counter)
        new_path = projects_path / new_name

        if not new_path.exists():
            return new_path
        counter = counter + 1

def create_project(project_name, language, extension):
    projects_path = Path.home() / "Projects"
    projects_path.mkdir(exist_ok=True)

    project_path = get_available_project_path(projects_path, project_name)
    project_path.mkdir()

    if language == "Web Development":
        (project_path / "index.html").write_text(
            """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <p>Made by Laurence</p>
</body>
<script src="script.js"></script>
</html>
"""
        )

        (project_path / "style.css").write_text("/* Web Development styles. */\n")
        (project_path / "script.js").write_text(
            "// Web Development script template.\nconsole.log('Made by Laurence');\n"
        )
    else:
        filename = "Main" if language == "Java" else "main"
        source_file = project_path / f"{filename}{extension}"
        source_file.write_text(SOURCE_TEMPLATES[language])

    return project_path

def colors():
    # ANSI escape codes for colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    return RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RESET

def main():
    args = sys.argv[1:]

    if args:
        if args[0] == "lau":
            start_code()
        else:
            print(f"Unknown command: {args[0]}")
    else:
        print("Usage: stcode lau")

def start_code():
    GREEN, YELLOW, MAGENTA, CYAN, RESET = colors()

    print(f"\n {CYAN}------------ LAU START CODE ------------{RESET}")
    print("|                 v2.1.0                 |")

    print(f"\n{CYAN}> Project Setup")
    print(f"{CYAN} ----------------------------------------{RESET}")
    project_name = input(f"\n{MAGENTA}  > Project Name >{RESET} ").strip()
    language, extension = choose_language()
    
    project_path = create_project(project_name, language, extension)
    
    print(F"\n{GREEN}Project created successfully!")
    print(f"Project Name          : {project_name}")
    print(f"Programming Language  : {language}")
    print(f"Location              : {project_path}{RESET}")

    open_editor = input(f"\n  > Do you want to open VS Code [Y/n]? > {RESET}").strip().lower()

    if open_editor == "y":
        open_code_editor(project_path)
    else:
        print(f"{YELLOW}Thank You for using LAU Start Code! Happy Coding!{RESET}\n")

def open_code_editor(project_path):
    RED =  colors()[0]
    RESET = colors()[6]
    system = platform.system()

    if shutil.which("code"):
        subprocess.run(["code", str(project_path)])
        return

    if system == "Linux" and shutil.which("flatpak"):
        result = subprocess.run(
            ["flatpak", "run", "com.visualstudio.code", str(project_path)]
        )

        if result.returncode == 0:
            return

    print(f"{RED}VS Code was not found on this system.{RESET}")

if __name__ == "__main__":
    main()

    # TO DO - v2 implementation idea.
    # if there's an existing folder name: "example" it should be "example2" - done
    # isama ang web-dev sa programing language choices - done
    # mag add ng print statement sa file na ginawa - done
