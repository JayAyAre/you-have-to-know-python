using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TrabajandoConTexto
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Working with text

            Console.WriteLine("\n Contruyendo Strings:");

            /*
             * Para construir un texto tiene que estar entre comillas
             * dobles o simples y para ello lo hjacemos de la siguiente manera
             */

            string nombreDeLaVariable = "puppy";

            // Escape cahracter sequences

            /*
             * Cuando necesitamos incluir comillas en el string, podemos usar el caracter \
             */

            string withSlash = "Ifemelu said, \"Hello!\"";

            // Ademas, si queremos incluir un salto de texto, usamos \n

            string withNewLine = "Ifemelu said, \"Hello!\nHow are you?\"";

            // Lesson 2/8
                // First string variable
                string firstSentence = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.";
                // Second string variable
                string firstSpeech = "\"My dear Mr. Bennet,\" said his lady to him one day, \"have you heard that Netherfield Park is let at last?\"";
                // Print variable and newline
                Console.WriteLine(firstSentence);
                Console.WriteLine("\n");
                Console.WriteLine(firstSpeech);
            // End Lesson 2/8








            // String concatenation
            Console.WriteLine("\n Concatenando Strings:");

            string yourFaveMusician = "David Bowie";
            string myFaveMusician = "Solange";

            Console.WriteLine("Your favorite musician is " + yourFaveMusician + " and mine is " + myFaveMusician + ".");

            // Importante!! si queremos unir otro tipo de dato, c# convierte en string dicha variable

            // Lesson 3/8
                // Declare the variables
                string beginning = "Hola";
                string middle = "buenos dias";
                string end = "Fin.";
                // Concatenate the string and the variables
                string story = beginning + "\n" + middle + "\n" + end;
                // Print the story to the console 
                Console.WriteLine(story);
            // End Lesson 3/8








            // String Interpolation
            Console.WriteLine("\n Interpolando Strings:");
            yourFaveMusician = "David Bowie";
            myFaveMusician = "Solange";

            Console.WriteLine($"Your favorite musician is {yourFaveMusician} and mine is {myFaveMusician}.");
            // Lesson 4/8
                // Declare the variables
                beginning = "Once upon a time,";
                middle = "The kid climbed a tree";
                end = "Everyone lived happily ever after.";

                // Interpolate the string and the variables

                story = $"{beginning}\n{middle}\n{end}\n";

                // Print the story to the console 
                Console.WriteLine(story);
            // End Lesson 4/8









            // Get Info About Strings
            Console.WriteLine("\n Get Info About Strings:");

            // Los string ademas del contenido textual, contienen informacion propia de ellos, con metodos.

            // Length nos permite saber la longitud del texto.
            string userTweet = "En una tierra muy muy lejana";
            Console.WriteLine(userTweet.Length);

            // IndexOf nos permite saber la posicion de una letra o palabra en el texto.
            string word = "radio";

            word.IndexOf("a"); // returns 1

            Console.WriteLine(userTweet.IndexOf("a")); // returns 5
            Console.WriteLine(userTweet.IndexOf("En")); // returns 0
            Console.WriteLine(userTweet.IndexOf("Hola")); // returns -1

            // Lesson 5/8
                // Create password
                string password = "a92301j2add";

                // Get password length

                int passwordLength = password.Length;

                // Check if password uses symbol

                int passwordCheck = password.IndexOf("!");

                // Print results
                Console.WriteLine($"The user password is {password}. " +
                    $"Its length is {passwordLength} and it receives a {passwordCheck} check.");
            // End Lesson 5/8









            // Get parts of string
            Console.WriteLine("\nConseguir partes de string:");

            // Substring nos permite obtener una parte de un string
            string plantName = "Cactaceae, Cactus";
            int charPosition = plantName.IndexOf("Cactus"); // returns 11
            string commonName = plantName.Substring(charPosition); // returns Cactus
            Console.WriteLine(commonName); // Cactus

            string name = "Codecademy";
            int start = 2;
            int length = 6;
            string substringName = name.Substring(start, length); // returns 'decade'

            // Bracket notation es una notacion para obtener valores de una coleccion

            plantName = "Cactaceae, Cactus";
            charPosition = plantName.IndexOf("u"); // returns 15
            char u = plantName[charPosition]; // returns u

            // Lesson 6/8
                // dna strand
                string startStrand = "ATGCGATGAGCTTAC";

                // find location of "tga"
                int tga = startStrand.IndexOf("TGA");

                // start point and stop point variables

                int startPoint = 0;
                length += 3;

                // define final strand

                string dna = startStrand.Substring(startPoint, length);
                Console.WriteLine(dna);
                // DNA mutation search

                Console.WriteLine(dna[3]);
            // End Lesson 6/8









            // Manipulating Strings
            Console.WriteLine("\nManipulando Strings:");

            // Tambien hay metodos propios en .NET para manipular strings.
            // No cambia el original ya que crea un nuevo string.

            string shouting = "Hola mundo".ToUpper();
            Console.WriteLine(shouting); // HOLA MUNDO

            shouting = "Hola mundo".ToLower();
            Console.WriteLine(shouting); // hola mundo

            // Lesson 7/8
                // Script line
                string script = "Close on a portrait of the HANDSOME PRINCE -- as the " +
                "BEAST'S giant paw slashes it.";

                // Get camera directions
                charPosition = script.IndexOf("Close on");
                length = "Close on".Length;
                string cameraDirections = script.Substring(charPosition, length);

                // Get scene description
                charPosition = script.IndexOf("a portrait");
                string sceneDescription = script.Substring(charPosition);

                // Make camera directions uppercase

                cameraDirections = cameraDirections.ToUpper();

                // Make scene description lowercase

                sceneDescription = sceneDescription.ToLower();


                // Print results
                Console.WriteLine(cameraDirections);
                Console.WriteLine(sceneDescription + "\n");
            // End Lesson 7/8









            // REVIEW
            /* use this space to write your own short program! 
                Here's what you learned:

                DATA TYPES: char, string
                STRING INTERPOLATION: $"blah blah"
                STRING INFO: .Length, .IndexOf()
                PARTS OF STRINGS: bracketNotation[], .Substring() 
                STRING MANIPULATION: .ToUpper(), .ToLower()

                Good luck! 

            Great job! You just learned about how to work with textual data in a few different ways:

                How to save char and string values to a variable.
                Use the addition symbol (+) to concatenate strings.
                Interpolate strings for easier string construction.
                Find information about a string using .Length and .IndexOf().
                Grab characters and parts of strings using bracket notation and .Substring().
                Use built-in methods such as .ToUpper() and .ToLower() to manipulate strings.
            */

            // Randomly convert part of a text to uppercase and lowercase

                string inputText = Console.ReadLine();
                Random random = new Random();
                string outputText = "";

                for (int i = 0; i < inputText.Length; i++)
                {
                    if (random.Next(0, 2) == 0)
                    {
                        outputText += inputText.Substring(i, 1).ToUpper();
                    }
                    else
                    {
                        outputText += inputText.Substring(i, 1).ToLower();
                    }
                }
                Console.WriteLine(outputText);
                Console.ReadLine();

            // A program that takes in a series of random words to construct and automated poem in the style of e.e. cummings.

                string[] words1 = { "moon", "sun", "star", "cloud", "dream" };
                string[] words2 = { "whisper", "shadow", "glimmer", "echo", "breath" };
                string[] words3 = { "silence", "night", "light", "sky", "sea" };
                string[] words4 = { "eternity", "infinity", "moment", "glance", "kiss" };
                string[] words5 = { "falls", "rises", "flows", "drifts", "whirls" };
                string[] words6 = { "between", "above", "under", "through", "within" };
                string[] words7 = { "the trees", "the stars", "the waves", "the hills", "the clouds" };

                Random rnd = new Random();

                string word1 = words1[rnd.Next(words1.Length)];
                string word2 = words2[rnd.Next(words2.Length)];
                string word3 = words3[rnd.Next(words3.Length)];
                string word4 = words4[rnd.Next(words4.Length)];
                string word5 = words5[rnd.Next(words5.Length)];
                string word6 = words6[rnd.Next(words6.Length)];
                string word7 = words7[rnd.Next(words7.Length)];

                string poem = $"{word1}light " +
                          $"and the\n" +
                          $"      {word2} of {word3}\n" +
                          $"           {word5} {word6} {word7}\n\n" +
                          $"{word3} {word5} like a\n" +
                          $"    {word4} of breath";

                Console.WriteLine(poem);
        }
    }
}
