using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Working_With_Numbers
{
    internal class Program
    {
        static void Main(string[] args)
        {

            /*
           
            Cada vez que trabajamos con datos, tenemos muchas formas de representarlos

            por ello, es importante pensar detalles como si necesito un numero entero o flotante

            */

            // INT

            Console.WriteLine("\n Tipos de datos: ");
            int numeroEntero = 21;
            
            /*
             
            Para representar numeros reales, podemos usar float, double o decimal

            normalmente el double es la mejor opcion ya que es mas preciso que float y mas rapido
            para procesar que un decimal, es mejor usar decimal para aplicaciones financiales.
             
            */

            // DOUBLE

            double numeroDouble = 21.53245;

            decimal numeroDecimal = 21.53245m; // indica que es un decimal y no un double


            // Lesson 2/8

                // Number of pizza shops

                int pizzaShops = 4332;

                // Number of employees

                int totalEmployees = 86928;

                // Revenue

                double revenue = 390819.28;

                // Log the values to the console:

                Console.WriteLine(pizzaShops);
                Console.WriteLine(totalEmployees);
                Console.WriteLine(revenue);

            // End lesson 2/8











            /*
             
            Las operaciones aritmeticas mas comunes que se pueden usar en c# son:
            
            + = Suma
            - = Resta
            * = Multiplicacion
            / = Division
            % = Modulo

            Tambien existe los incrementos y decrementos

            ++ = Incremento
            -- = Decremento

            x++ = x = x + 1
            x-- = x = x - 1
             
            */
            Console.WriteLine("\n Operadores aritmeticos: ");

            int answer = 4 + 19;
            Console.WriteLine(answer);

            // Si usamos dos enteros, el resultado es un entero
            // Si usamos dos flotantes, el resultado es un flotante
            // Si usamos un entero y un flotante, el resultado es un flotante
            // Ademas, tambien c# sigue el orden de operaciones

            Console.WriteLine(5 / 3);
            Console.WriteLine(5 / 3.0);

            answer = 8 + (9 * 3);
            Console.Write(answer);

            // Lesson 3/8

                // Your Age

                int userAge = 21;

                // Length of years on Jupiter (in Earth years)

                double jupiterYears = 11.86;

                // Age on Jupiter

                double jupiterAge = userAge / jupiterYears;

                // Time to Jupiter

                double journeyToJupiter = 6.142466;

                // New Age on Earth

                double newEarthAge = userAge + journeyToJupiter;

                // New Age on Jupiter

                double newJupiterAge = newEarthAge / jupiterYears;

                // Log calculations to console

                Console.WriteLine(userAge);
                Console.WriteLine(jupiterAge);
                Console.WriteLine(newEarthAge);
                Console.WriteLine(newJupiterAge);
                Console.WriteLine(journeyToJupiter);

            // End lesson 3/8











            // Atajos para operaciones aritmeticas

            //Uno de los primeros atajos seria el incremento en uno a una variable

            Console.WriteLine("\n Atajos: ");

            int apple = 0;
            apple = apple + 1;
            Console.WriteLine(apple); // apple = 1

            apple++;    // apple = apple + 1
            Console.WriteLine(apple); // apple = 2

            apple += 10;    // apple = apple + 10
            Console.WriteLine(apple);   // apple = 12

            apple -= 10;    // apple = apple - 10
            Console.WriteLine(apple);   // apple = 2

            // Lesson 4/8

                // declare steps variable
                int steps = 0;

                // Two steps forward 

                steps += 2;

                // One step back 

                steps--;

                // Print result to the console

                Console.WriteLine(steps);

            // End lesson 4/8










            // Modulo

            // Una operacion aritmetica que nos permite saber si un numero es par o impar
            // Pero principalmente saber el residuo de una division

            Console.WriteLine("\n Modulo: ");
            Console.WriteLine(5 % 3);
            Console.WriteLine(4 % 3);
            Console.WriteLine(4 % 2);

            int eggs = 56;
            int createAmount = 12;

            int eggsLeftOver = eggs % createAmount;
            
            Console.WriteLine(eggsLeftOver); // 12

            int myNum = 85939824;
            Console.Write(myNum % 2); // 0

            // 0 is even, 1 is odd

            // Lesson 5/8

                // Number of students

                int students = 18;

                // Number of students in a group

                int groupSize = 3;

                // Does groupSize go evenly into students?

                Console.WriteLine(students % groupSize);

            // End lesson 5/8










            // Built-In Methods

            // Como hariamos una raiz cuadrada en C#? sabiendo que no se reconoce dicho simbolo

            Console.WriteLine("\n Metodos de C#: ");

            // Math.abs - returns the absolute value of a number
            // Math.sqrt - returns the square root of a number
            // Math.floor - will round the given double or decimal down to the nearest whole number.
            // Math.min - will return the smallest of the two numbers


            // Lesson 6/8

                // Starting variables 
                int numberOne = 12932;
                int numberTwo = -2828472;

                // Use built-in methods and save to variable 

                double numberOneSqrt = Math.Floor(Math.Sqrt(numberOne));

                // Use built-in methods and save to variable 

                double numberTwoSqrt = Math.Floor(Math.Sqrt(Math.Abs(numberTwo)));

                // Print the lowest number

                Console.WriteLine(Math.Min(numberOneSqrt, numberTwoSqrt));

            // End lesson 6/8










            // Using Documentation

            // Un buen sitio para consultar la documentacion de C# es: https://docs.microsoft.com/en-us/dotnet/csharp/
            // o si no https://learn.microsoft.com/en-us/dotnet/api/

            // Lesson 7/8

                double number1 = 6.5;
                double number2 = 4;

                // Raise numberOne to the numberTwo power
                Console.WriteLine(Math.Pow(number1, number2));

                // Round numberOne up
                Console.WriteLine(Math.Ceiling(number1));

                // Find the larger number between numberOne and numberTwo
                Console.WriteLine(Math.Max(number1, number2));

            // End Lesson 7/8










            // Review

            /*
             
             Great job! You just learned about numerical data types 
            and how to work with numerical data in a few different ways:

                Use arithmetic operators to write expressions.
                Combine operators together to write more concise programs.
                Use the modulo operator (%) to find remainders.
                Use built-in methods to do more complex math.
                Use documentation to look new things up.

                DATA TYPES: int, double
                ARITHMETIC OPERATORS: +, -, *, /
                INCREMENT/DECREMENT: ++, --
                MODULO: % 
                BUILT-IN METHODS: Abs, Pow, Sqrt, Floor, Ceiling, Min, Max        

             */

            // Write a program that calculates compound interest on c#

            double principal, rate, time, CI, amount;

                Console.WriteLine("\n Ingresa el capital inicial: ");
                principal = Convert.ToDouble(Console.ReadLine());
            
                Console.WriteLine("\n Ingresa la tasa de interes en años: ");
                rate = Convert.ToDouble(Console.ReadLine());

                Console.WriteLine("\n Ingresa el tiempo en años: ");
                time = Convert.ToDouble(Console.ReadLine());

                CI = principal * Math.Pow(1 + rate/100, time);

                Console.WriteLine("\n El capital total es: " + CI);

            // Write a program that finds your age in dog years

                int age;
                
                Console.WriteLine("\n Ingresa tu edad: ");
                age = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("\n Tu edad en anios de perro es: " + (age * 7));


            Console.ReadLine();

        }
    }
}
