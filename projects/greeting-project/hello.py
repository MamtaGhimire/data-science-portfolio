# My first Python project in GitHub

def greet_user():
    name = input("Enter your name: ")
    favorite_subject = input("What is your favorite subject? ")
    career_goal = input("What career are you interested in? ")

    print(f"Hello, {name}! Welcome to Data Science.")
    print(f"It is awesome that you like {favorite_subject}.")
    print(f"Data Science can help you work toward becoming a {career_goal}.")

if __name__ == "__main__":
    greet_user()
