import random

class Element:
    """Klass för grundämnenas 'egenskaper'.
    Klassens uppgift är att skapa attribut för grundämnenas egenskaper
    som sedan lagras som 'Element' object!"""
    def __init__(self, symbol, atomic_number,atomic_weight):
        self.symbol = symbol
        self.atomic_number = int(atomic_number)
        self.atomic_weight = float(atomic_weight)

def read_elements_from_file(file_name):
    """Läser in alla grundämmen från filen och gör som till 'Element' object
    lögger till i en listan av listor
    Returnerar sedan denna värdig listan
    :param file_name: filen som ska läsas in av programmet
    :return all_elements_list: returnerar den färdia listan som ska sorteras"""
    all_elements_list = [] # Tom lista som ska fyllas med alla element
    atomic_number=1 # Sätter att atomnumren ska börja från 1
    with open(file_name, "r") as file:
        all_elements = file.read().strip() # Läser in hela filens innehåll och tar bort eventuella extra blankrader
        inside_lists = all_elements.split("\n") # Lista av listor, varje grundämne en egen lista
        for each_element in inside_lists: # Itererar över listorna för varje grundämne
            attributes = each_element.split()
            symbol = attributes[0]
            atomic_weight = float(attributes[1])
            all_elements_list.append(Element(symbol, atomic_number,atomic_weight)) # Skapar objekt av 'Element'-class
            atomic_number += 1 # Ökar atomnumret med 1 för varje nytt element som itereras över
    return all_elements_list # Returnar den färdiga listan

def periodic_table():
    """Ska hantera bytet av specifika grundämmen.
    Eftersom programmet sorterar efter atomvikt
    men periodiska sytemets atomvikter är inte exakt i ordning,
    programmet måste då manuellt byta plats på 4 grundämnen.
    Returnera listan med periodiska systemet,
    som sedan ska användas för alla quizzar i programmet
    :return: sorted_periodic_table: returnerar sorteade listan med grundäme, används i quizzarna"""
    sorted_periodic_table = read_elements_from_file("avikt.txt")
    sorted_periodic_table.sort(key=lambda atom: atom.atomic_weight) # Sorterar först efter atomvikt
    for i, element in enumerate(sorted_periodic_table, 1): # Tilldelar temporära atomnummer
        element.atomic_number = i
    swaps = [17,26,51,89,91]  # Bytena som ska göras utefter index dvs Ar(18),Co(27),Te(52),Th (90),U(92)
    for atomic_number in swaps:
        sorted_periodic_table[atomic_number],sorted_periodic_table[atomic_number+1] = (
        sorted_periodic_table[atomic_number+1], sorted_periodic_table[atomic_number])

    for i, element in enumerate(sorted_periodic_table,1):
        element.atomic_number = i # Uppdaterar atomnumren efter alla byten har skett
    return sorted_periodic_table # Returnerar den nu sorterade periodiska systemet!

def get_random_atom_weight():
    """Ska ta ett random grundämne från den nya sorterade listan och returnera atomvikten för den.
        Används för quizzen om atomvikter
        :return random_element.atomic_weight: returnerar en slumpmässigt aomtvikt
         som används i atomvikt quizzen."""
    list_of_elements = periodic_table()
    random_element = random.choice(list_of_elements)
    return random_element.atomic_weight

class Quiz:
    """Klassen används för programmets alla quizzar samt valmöjligheten att visa det periodiska systemet"""
    def __init__(self, elements):
        """Sparar listan med 'Element'-objekt i instansen
        :param elements: innehåller 'Element'-objekten"""
        self.elements = elements #Blir listor med 'Element'-objekt

    @staticmethod
    def get_answer(prompt_string):
            """Hanterar alla inputs från anvädnaren, utför bara en operation.
            Pga all felhantering ska vara olika för varje 'Quiz'-metod och outputen
            som printas ut ska vara olika för varje felhantering gör det i metoden.
            :param prompt_string: Tar en input från användaren
            :return user_input: returernar inputen från användaren"""
            user_input = input(prompt_string)
            return user_input

    def get_random_element_max_attempts_and_set_attempt(self):
        """Väljer ett slumpmässigt grundämne från self.element i __init__ metoden
            Sätter även att max antal försök ska vara 3
            :return random_element: ska returnera ett slumpmässigt grundämnet (en lista)
            :return max_attempt: returnerar vad max taket för användarens försök ska vara
            :return attempt: returnerar att attempt alltid ska börja på 0"""
        random_element = random.choice(self.elements)
        max_attempt = 3
        attempt = 0
        return random_element, max_attempt,attempt

    def show_periodic_table(self):
        """Använder den redan sorterade listan från __init__ och printar ut den"""
        for each_element in self.elements:
            print(f"{each_element.symbol} ({each_element.atomic_number}): "
                  f"- Atomvikt: {each_element.atomic_weight}u")

    def quiz_atomnumber(self):
        """Vid menyn om användarens val är 2 ska användaren quizzas på periodiska systemts atomnummer"""
        while True:
            element,max_attempt,attempt = self.get_random_element_max_attempts_and_set_attempt()
            while attempt < max_attempt: # Ger användaren 3 försök på sig
                correct_answer = element.atomic_number
                answer_str = self.get_answer(f"Vilket atomnummer har {element.symbol}? Ange ett svar mellan 1-103!"
                f" (Ange '0' för att återgå till menyn)").strip()  # Tar emot ett svar på frågan från användaren
                try:
                    answer =int(answer_str)# Försöker göra om svaret till en integer
                    if answer == 0: # Om användarens svar är 0 ska man komma tillbaka till menyn
                        return
                    elif answer == correct_answer: # Om det är rätt ska det visas och en ny fråga ska ställas
                        print("Det är rätt!")
                        break
                    if answer >= 104 or answer < 0:
                        print(f"Ditt svar '{answer_str}' är inte mellan 1-103 eller 0. Testa igen!")
                    else:
                        attempt += 1
                        if attempt < 3:
                            print(f"Fel försök, testa igen. {3 - attempt} försök kvar!") # Räknar ner hur många försök kvar
                        else:
                            print(f"Fel, du har inga försök kvar! Rätt svar var {correct_answer}")
                except ValueError:
                    print(f"Ditt svar '{answer_str}' är inte en siffra mllean 1-103 eller 0. Testa igen!")

    def quiz_atomsymbol(self):
        """Vid menyn, om användarens val är '3' ska användaren quizzas
        på periodiska systemts atomsymboler"""
        while True:
            element, max_attempt,attempt = self.get_random_element_max_attempts_and_set_attempt()
            while attempt < max_attempt:
                correct_answer = element.symbol
                answer = self.get_answer(f"Vad för grundämne har atomnummret {element.atomic_number}? "
                f"(Ange '0' för att återgå till menyn) ").capitalize().strip()
                if len(answer) > 2 or any(letters in "123456789" for letters in answer): # Felhantering
                    print(f"Ditt svar '{answer}' är inte på giltigt format. Ange endast en eller två bokstäver. Testa igen!")
                    continue
                if answer == "0":
                    return
                if answer == correct_answer:
                    print("Det är rätt!")
                    break
                else:
                    attempt += 1
                    if attempt < 3:
                        print(f"Fel försök, testa igen. {3 - attempt} försök kvar!")
                    else:
                        print(f"Fel, du har inga försök kvar! Rätt svar var {correct_answer}")

    def quiz_atom_weight(self):
        """Vid menyn om användarens val är 4 ska användaren
        quizzas på periodiska systemts atomvikt, med alternativ!"""
        random.shuffle(self.elements)
        for element in self.elements:
            print(f"Vad för atomvikt har {element.symbol}?. "
                  f"Välj ett av alternativen! (Ange 0 för att återgå till menyn) ")
            correct_answer = element.atomic_weight
            while True: #Hanterar så att inga alternativ blir samma
                wrong_answer_1 = get_random_atom_weight()
                wrong_answer_2 = get_random_atom_weight()
                if (wrong_answer_1 != correct_answer and
                        wrong_answer_2 != correct_answer and
                        wrong_answer_1 != wrong_answer_2):
                    break
            alternatives = [correct_answer, wrong_answer_1, wrong_answer_2]
            random.shuffle(alternatives)  # Shufflas så att rättsvar inte är på samma plats för varje fråga
            right_choice = alternatives.index(correct_answer) # Hittar indexet för rätt svar
            for i, alternative in enumerate(alternatives):
                print(f"Alternativ {i + 1}:", alternative)
            while True:
                    answer = self.get_answer("Ange ditt svar (1, 2 eller 3): ").strip()
                    if answer == "0":
                        return   # Går tillbaka till menyn
                    if answer not in ["1", "2", "3"]:
                        print("Ogiltigt val! Ange 1, 2 eller 3.")
                        continue  # Be om input igen
                    answer_index = int(answer) - 1  # Konverterar input till rätt index
                    if answer_index == right_choice:
                        print("Det är rätt!")
                    else:
                        print(f"Det är fel, rätt svar var {correct_answer}")
                    break  # Avslutar loopen och gå vidare till nästa fråga

def menu():
    """Menyn fungerar som en hub för programmet. Här väljer användaren vad den vill göra
        samt vid valt quizz kan användaren alltid komma tillbaka till menyn genom att ange 0 inne i quizzen"""
    get_sorted_periodic_table = periodic_table()
    play_quiz = Quiz(get_sorted_periodic_table) # Skapar en instans av 'Quiz' klassen som använder sig av 'Element'-objekt
    while True:
        print(" " * 36, "*" * 4, "" * 20, "\n" + "-" * 36, "Meny", "-" * 36)
        print("1. Visa periodiska systemet", "2. Träna på atomnummer", "3. Träna på atombeteckningar",
              "4. Träna på atomvikt","5. Avsluta",
              "OBS! Skriv 0 som input för att komma tillbaka till menyn!", sep="\n")
        print("-" * 78)
        user_choice = input("Vad vill du göra? ") # Tar input från användaren
        if user_choice == "1":
            play_quiz.show_periodic_table() # Använder metod från 'Quiz' klassen
        elif user_choice == "2":
            play_quiz.quiz_atomnumber() # Använder metod från 'Quiz' klassen
        elif user_choice == "3":
            play_quiz.quiz_atomsymbol() # Använder metod från 'Quiz' klassen
        elif user_choice == "4":
            play_quiz.quiz_atom_weight() # Använder metod från 'Quiz' klassen
        elif user_choice == "5": # Avslutar programmet
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val, försök igen! Välj ett av alternativen: 1, 2, 3, 4 eller 5")
if __name__ == "__main__":
    menu() # Påbörjar programmet!