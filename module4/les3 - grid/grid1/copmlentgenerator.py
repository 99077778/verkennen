
import random



def get_random_compliment(naam: str) -> str:
    MIJN_COMPLIMENTEN = ('Je bent geweldig', 'Je doet het super', 'Niemand is zoals jij')
    compliment = random.choice(MIJN_COMPLIMENTEN)
    return f'{compliment} {naam}'



print(get_random_compliment('Oskar'))