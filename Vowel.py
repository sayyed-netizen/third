def Vowel(word, vowels): 
    final = [each for each in word if each in vowels] 
    print(final) 
      

string = "Python Training"    
vowels = "aeiou"
Vowel(string, vowels)