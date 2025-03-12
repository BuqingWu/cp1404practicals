from prac_06.programming_language import ProgrammingLanguage

def main():
    """Test programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    # Create a list of programming languages
    languages = [python, ruby, visual_basic]

    # Print all languages
    print("All programming languages:")
    for language in languages:
        print(language)

    # Loop through and print the names of all the languages with dynamic typing
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()