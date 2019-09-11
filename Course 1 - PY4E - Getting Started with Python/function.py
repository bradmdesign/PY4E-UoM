
lang =input("Hello, what language do you speak? ")
name =input("And what is your name? ")
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    elif lang == 'en':
        return 'Hello'
    else:
        print("test")
        return
        print("test2")

print(greet(lang), name)
