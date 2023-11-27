#Author: Ayad Mohiseny
#Date:  2023-11-27

def main():
    try:
        # Läs in tal från användaren, separerade med mellanslag
        input_values = input("Vilka tal vill du beräkna? (separerat med mellanslag): ").split()

        # Loopa igenom varje inmatat tal
        for value in input_values:
            
            num = int(value)

            # Gångertabellen skrivs ut
            print(f"\nGångertabell för {num}:\n")
            for i in range(1, 11):
                product = num * i
                print(f"{num} * {i} = {product}")

    except ValueError:
        print("Felaktig inmatning. Ange endast heltal.")

    finally:
        print("Programmet avslutas.")

if __name__ == "__main__":
    main()