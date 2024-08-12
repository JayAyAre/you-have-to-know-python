using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TiposDeDatosYVariables
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             
            Cuando creamos variables, estamos indicandole al computador en como procesar los datos 
             
            Ademas, debemos tener en cuenta en como el computador diferencia entre un numero y un texto
            y para ello le indicamos el tipo de dato mediante los data types

            Los data types representan los tipos de datos que se pueden usar en C# y como deben ser tratados.

            y teniendo en cuenta esto, pueden aparecer bugs donde intentamos hacerle la potencia a un texto.

            por ello podemos decir que C# es un lenguaje de programacion de tipado fuerte, o tipado estatico.


            Los Data Types ademas nos indican varias propiedades como las siguientes:

                - Como se guardan los datos en funcion de su tipo
                - Que operaciones se pueden hacer con los datos
                - Diferentes metodos para ser usadas


            Los Data types mas comunes son:
                
                - Int - numeros enteros como: 0, 1, 234, -34
                - Double - numeros decimales como: 0.0, 1.0, 2.34, -3.4
                - String - Cadenas de texto como "Hello World"
                - Char - Caracteres indicados entre comillas, ejemplo: 'a', 'b', 'c'
                - Boolean - True o False
             
            Cuando guardamos datos en una variable, es como guardar informacion dentro de una caja, teniendo en cuenta
            que la caja es la memoria del computador, y en esta misma, guardamos la informacion usada en nuestro codigo.


             */

            // Para declarar una variable, debemos indicar el tipo de dato y el nombre de la variable y podemos hacerlo de dos modos

            int myAge;
            myAge = 30;

            // O podemos declararlo todo en una linea

            int myAge2 = 30;

            int evenNumber = 22;
            int oddNumber = 45;
            Console.WriteLine(evenNumber + oddNumber); // Prints 67
            Console.WriteLine(oddNumber - evenNumber); // Prints 23

            // Ademas, las variables no se tienen que declarar mas de una vez, unicamente solo una.
            // En caso de que queramos actualizar el valor de una variable, podemos hacerlo las veces que queramos

            // Create Variables

            string name = "Shadow";
            string breed = "Golden Retriever";
            int age = 5;
            double weight = 65.22;
            bool spayed = true;

            // Print variables to the console

            Console.WriteLine(name);
            Console.WriteLine(breed);
            Console.WriteLine(age);
            Console.WriteLine(weight);
            Console.WriteLine(spayed);

            Console.ReadLine();

            // Handling errors

            /*
             
            Programar por primera vez con un lenguaje de tipado estatico o tipado fuerte, es comun encontrar
            los errores relacionados al declarar una variable o reasignarla
           
                randomData = "asdf jskdf"; No especificar el tipo de dato dara un error
                
                Console.WriteLine(randomData);
                
                El error es: The name 'randomData' does not exist in the current context[CS0103:]
            
            Si asignamos un tipo de dato y le asignamos incorrectamente un dato, tendremos el siguiente
            error en el codigo:
             
                int score = 45.39;

                Tendremos este error:
                    Cannot implicitly convert type 'double' to 'int'. An explicit conversion exists (are you missing a cast?)
            
            RECORDAMOS QUE USAMOS CAMELCASE: ciudadNatal
             
            ademas, al igual que en otros lenguajes de programacion, existen palabras reservadas.
            No podremos hacer lo siguiente:

                string string = "hello world";

            Y por ultimo tendremos que recordar que siempre debemos el final de una instruccion con ;


            Ejemplos de errores:

                int number = 38498.3222;

                dinosaur = "Barney";

                double lock = 293.000;

                bool is.yes = true;

                string band = "The Low Anthem"

            Solucion:

                double number = 38498.3222;

                string dinosaur = "Barney";

                double locko = 293.000;

                bool yes = true;

                string band = "The Low Anthem";
                
            */

            /*
              
            Converting data types

            Cuando las variables son strictamente tipadas estaticamente, comunmente vamos a querer convertir el tipo de dato a otro
            y para ello existen dos tipos de conversion

            - Implicit conversion : sucede cuando no hay ninguna perdida de dato int => double
            - Explicit conversion : quiere una operacion de cast para convertir el tipo de dato
            

            */

            // Implicit conversion

            int myAge3 = 21;
            Console.WriteLine(myAge3);
            double myAgeDouble = myAge3;
            Console.WriteLine(myAgeDouble);

            // Explicit conversion

            double myAgeDouble2 = 21.654;
            Console.WriteLine(myAgeDouble2);
            int myAge4 = (int) myAgeDouble2;
            Console.WriteLine(myAge4);

            // Ademas, existe una clase que nos permite convertir el tipo de dato a otro
            Convert.ToBoolean(myAgeDouble2);


            Console.Write("Enter your favorite number!: ");

            int faveNumber = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Your favorite number is: " + faveNumber);

            Console.ReadLine();


            /*
              
            Here's what you learned:

            DATA TYPES: int, double, char, string, bool

            VARIABLES: datatype variableName = value;

            COMMON ERRORS: wrong type, wrong value, no semicolon

            DATA TYPE CONVERSION: implicit, explicit, methods

            Good luck! 
            
            */


            string name3 = "pepe";

            double balance = 123.23;

            bool isRaining = true;
            
            string boolName = Convert.ToString(isRaining);

            char[] listChar = name3.ToCharArray();

            int roundedBalance = Convert.ToInt32(balance);
        }
    }
}
