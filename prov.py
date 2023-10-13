# Author: Ayad Mohiseny 
# Date:   2023-10-13 

def main():
   # hälsningsfras
   print("Ei22 -praktiskt prov ht23 ")

   # här frågar vi efter resistansvärden
   resistans1 = float(input("Ange Resistor 1: "))
   resistans2 = float(input("Ange Resistor 2: "))

   # här så beräknas serieresistans och parallellresistans
   serieresistans = resistans1 + resistans2
   parallellresistans = (resistans1 * resistans2) / (resistans1 + resistans2)

   # här skriv det serieresistans och parallellresistans
   print("Serieresistans:", serieresistans)
   print("Parallellresistans:", parallellresistans)



if __name__ == "__main__":
   main()
