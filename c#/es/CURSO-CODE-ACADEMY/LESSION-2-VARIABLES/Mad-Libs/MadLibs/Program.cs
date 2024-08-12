using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MadLibs
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Crearemos un programa que cree un juego de palabras Mad libs, que consiste en
            // Historias cortas con huecos en blanco para rellenar por los jugadores

            Console.WriteLine("Mad Libs Game!!");

            Console.WriteLine("Escribe el titulo de la historia");

            string title = Console.ReadLine();

            Console.WriteLine("Escribe el nombre del personaje");
            string name = Console.ReadLine();
            Console.WriteLine("Escribe el primer adjectivo");
            string firstAdjective = Console.ReadLine();
            Console.WriteLine("Escribe el segundo adjectivo");
            string secondAdjective = Console.ReadLine();
            Console.WriteLine("Escribe el tercer adjectivo");
            string thirdAdjective = Console.ReadLine();

            string storyTemplate = $"Esta mañana {name} se despertó sintiéndose {firstAdjective}." +
                $" '¡Va a ser un día {secondAdjective}!' Afuera, " +
                $"un grupo de {firstAdjective}s estaban protestando para " +
                $"mantener {secondAdjective} en las tiendas. Empezaron a {thirdAdjective} al ritmo " +
                $"del {name}, lo que hizo que todos los {secondAdjective}s se sintieran muy {firstAdjective}. " +
                $"Preocupado, {name} le envió un mensaje a {name}, quien voló {secondAdjective} " +
                $"a {firstAdjective} y dejó caer {thirdAdjective} en un charco de {secondAdjective}." +
                $" {name} despertó en el año {firstAdjective}, en un mundo donde los {secondAdjective}s" +
                $" gobernaban el mundo.";

            Console.WriteLine("\n¡Aquí está tu historia Mad Libs!");
            Console.WriteLine(storyTemplate);

            Console.ReadLine();
        }
    }
}
