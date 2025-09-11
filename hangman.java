import java.util.Scanner;

//Nathan Brimhall

public class hangman
{
    public static void main(String[] args)
    {
        String word;
        int selectWord; 
        Scanner input = new Scanner(System.in);
        int mistakes, guessedIndex;
        boolean completed, playAgain;
        String yesno;
        
        do
        {
            String[] words = {"calculus", "english", "java", "track", "databases"};
            char[] alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
            char[] guessed = new char[26];
            int[] result;
            
            selectWord = (int) Math.round(Math.random() * 500) /100; // This selects a random number 1 through 5 in order to select once of the possible words.
            word = words[selectWord];
            char[] lettersInWord;
            
            completed = false; playAgain = true;
            mistakes = 0; guessedIndex = 0;
            
            lettersInWord = explode(word); // Selects a word from the word bank and converts the string to a char array.
            do
            {
                result = checkGuess(guessedIndex, input, guessed, lettersInWord, alphabet, mistakes);
                mistakes = result[1];
                guessedIndex = result[0];
                printGallows(mistakes);
                if (mistakes >= 6)
                {
                    System.out.println("Oh no! Looks like you made too many mistakes.");
                    System.out.println("The word was '" + String.valueOf(lettersInWord) + "'.");
                    System.out.println("GAME OVER");
                    System.out.println("-----------------------------------------");
                    completed = true;
                }
                if (winCondition(lettersInWord, guessed, guessedIndex))
                {
                    System.out.println("Congratulations!!! You won!!!");
                    System.out.println("-----------------------------------------");
                    completed = true;
                }
            } while (completed == false);
            
            OUTER: //This labeled loopis a suggestion from NetBeans, not from an outside AI source.
            while (true)
            {
                System.out.println("Do you want to play again? Enter 'Y' or 'N'.");
                yesno = input.next();
                switch (yesno)
                {
                    case "N":
                        playAgain = false;
                        break OUTER;
                    case "Y":
                        break OUTER;
                    default:
                        System.out.println("I didn't get that. Please enter 'Y' or 'N'.");
                        break;
                }
            }
        }   while(playAgain == true);        
    }
    
    public static boolean winCondition(char[] lettersInWord, char guessed[], int guessedIndex)
    {
        for (int i = 0; i < lettersInWord.length; i++)
        {
            boolean letterGuessed = false;
            for (int j = 0; j < guessedIndex; j++)
            {
                if (lettersInWord[i] == guessed[j])
                {
                    letterGuessed = true;
                    break;
                }
            }
            if (!letterGuessed)
            {
                return false;
            }
        }
        return true;
    }
    
    public static int[] checkGuess(int guessedIndex, Scanner input, char[] guessed, char[] lettersInWord, char[]alphabet, int mistakes)
    {
        char guessChar;
        String guess;
        boolean correctGuess = false;
        System.out.println("-----------------------------------------");
        System.out.println("Please enter your next guess as a letter.");
        guess = input.next();
        guessChar = guess.charAt(0);
        guessed[guessedIndex] = guessChar; // Here I add each guessed letter to the array of guesses. 
        guessedIndex++;
        System.out.println("-----------------------------------------");
        System.out.print("ALPHABET: ");
        for (int i = 0; i < alphabet.length; i++) // This removes guessed letters from possible options in the future and prints.
        {
            if (alphabet[i] == guessChar)
            {
                alphabet[i] = '_';
            }
            System.out.print(alphabet[i] + " ");
        }
        System.out.println();
        System.out.println();
        
        System.out.print("WORD: ");
        for (int i = 0; i < lettersInWord.length; i++) // This for loop was created with the help of AI because I was really confused about how to go about it. I was sorting through the whole array of guessed letters rather than sorting through the word.
        {
            boolean letterGuessed = false;
            for (int j = 0; j < guessedIndex; j++) // Check if this letter has been guessed
            {
                if (guessed[j] == lettersInWord[i])
                {
                    letterGuessed = true;
                    break;
                }
            }
            if (letterGuessed)
            {
                System.out.print(lettersInWord[i] + " ");
                if (lettersInWord[i] == guessChar)
                {
                    correctGuess = true;
                }
            } else
            {
                System.out.print("_ ");
            }
        }
        System.out.println();

// If the guess was incorrect (not in the word at all), increment mistakes
        if (!correctGuess)
        {
            mistakes++;
            if (mistakes < 6)
            {
                System.out.println("Oops! Looks like you have made " + mistakes + " mistake(s) so far. Be careful!");
            }
        }
        
        System.out.println();
        
        return new int[]{guessedIndex, mistakes}; // Returning an array that has both values and then using the array to assign them to values in the main was an idea from AI, but I actually had no idea that you could return multiple values from a method this way.
    }
        
    public static char[] explode(String word)
    {
        char[] lettersInWord = word.toCharArray();
        System.out.print("WORD: ");
        for (int i = 0; i < lettersInWord.length; i++)
        {
            System.out.print("_ ");
        }
        System.out.println();
        System.out.println();
        return lettersInWord;
    }
    
    public static void printGallows(int mistakes)
    {
        System.out.println("-------");
        System.out.println("|     |");
                
        if (mistakes > 0) // If there is one mistake or more
        {
            System.out.println("|     0");
            if (mistakes > 1) // If there are two mistakes or more
            {
                if (mistakes == 2) // If there are two mistakes
                {
                    System.out.println("|     |");
                    System.out.println("|     |");
                    System.out.println("|");
                    System.out.println("|");
                }
                else if (mistakes == 3) // If there are three mistakes
                {
                    System.out.println("|    /|");
                    System.out.println("|     |");
                    System.out.println("|");
                    System.out.println("|");
                }
                else if (mistakes > 3) // If there are four or more mistakes
                {
                    System.out.println("|    /|\\");
                    System.out.println("|     |");
                    if (mistakes > 4)
                    {
                        if (mistakes == 5) // When there are 5 mistakes
                        {
                            System.out.println("|    /");
                        }
                        else if (mistakes == 6) // When there are 6 mistakes
                        {
                            System.out.println("|    / \\");
                        }
                        System.out.println("|");
                    }
                    else // prints remaining lines for when there are 4 mistakes
                    {
                        System.out.println("|");
                        System.out.println("|");
                    }
                }
            }
            else // Prints remaining lines for when there is 1 mistake
            {
                System.out.println("|");
                System.out.println("|");
                System.out.println("|");
                System.out.println("|");
            }
        }
        else // Prints the rest of the gallows when there are no mistakes
        {
            System.out.println("|");
            System.out.println("|");
            System.out.println("|");
            System.out.println("|");
            System.out.println("|");
        }
    }
}
