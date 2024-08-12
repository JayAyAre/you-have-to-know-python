using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Introduccion
{
    internal class Introduccion
    {
        static void Main(string[] args)
        {
            // Esta es la primera lession del curso de Code Academy

            // Este es un comentario de linea, unicamente ocupa una linea de instruccion

            /*

            Y este de aqui
            Es un comentario de bloque
            y se puede escribir en varias lineas

             */

            /*

            C# es un lenguaje de programacion de tipado seguro, es decir, se deben declarar las variables. 
            Es decir, el compilador debe saber que tipo de variable es para poder funcionar y leerlas.
            Asignar un tipo esencialmente le dice a una computadora qué operaciones se pueden y no se pueden realizar en un fragmento de datos.
            Es como en java:
                String
                Int
                Bool
                Float

            C# ademas, es un lenguaje en el que puedes crear multitud de cosas, entre ellas aplicaciones para
            Escritorio, apps para movil, videojuegos, apps web, realidad aumentada y realidad virtual, etc.

            Por ultimo C# se diferencia por su alta velocidad con respecto a otros lenguajes de programacion

            */

            // A continuacion, veremos como se escribe por consola

            Console.WriteLine("Hola mundillo loquillo");

            Console.WriteLine("What's your name?");
            string name = Console.ReadLine();
            Console.WriteLine("Hello " + name);
            Console.WriteLine($"How are you, {name}?");

            Console.ReadLine();
            // Ademas, los comentarios sirven para 3 cosas priuncipales

            // 1. Para proporcionar contexto sobre una variable o el porque una instruccion esta escrita asi
            // 2. Para que otra gente pueda leer tu código
            // 3. Para ignorar instrucciones y ver que sucede en el futuro.

            // C# se utiliza ademas por tambien 3 razones principales

            // 1. Por su velocidad
            // 2. Por su gran comunidad
            // 3. Por su empleabilidad

        }
    }
}
