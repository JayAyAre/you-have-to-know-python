using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
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
        }
    }
}
