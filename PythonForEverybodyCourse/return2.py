def greet(lang):
    if lang == 'es':
        return 'Hola'
    if lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('es') , 'Glenn')
print(greet('fr') , 'Sally')
print(greet('en') , 'John')
