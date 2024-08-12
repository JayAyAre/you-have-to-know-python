using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MoneyMaker
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // En este programa el usuario introduce la cantidad de dinero que quiere convertir 
            // a modenas de oro y plata

            Console.WriteLine("Bienvenido al juego de money maker");
            Console.WriteLine("Introduce la cantidad de dinero que quieres convertir");

            // La siguiente linea de entrada es la cantidad de dinero que el usuario introduce
            // permite escribir decimales con punto correctamente
            double amountToConvert = double.Parse(Console.ReadLine(), NumberStyles.Any, CultureInfo.InvariantCulture);

            // Coins

            double goldCoinValue = 10.0;
            double silverCoinValue = 5.0;

            double goldCoins = Math.Floor(amountToConvert / goldCoinValue);
            // Calcular el resto después de usar las monedas de oro
            double remainderAfterGold = amountToConvert - (goldCoins * goldCoinValue);

            // Calcular la cantidad de monedas de plata
            double silverCoins = Math.Floor(remainderAfterGold / silverCoinValue);
            // Calcular el resto después de usar las monedas de plata
            double remainderAfterSilver = remainderAfterGold - (silverCoins * silverCoinValue);

            double copperCoins = remainderAfterSilver;

            Console.WriteLine("Gold coins: " + goldCoins);
            Console.WriteLine("Silver coins: " + silverCoins);
            Console.WriteLine("Copper coins: " + copperCoins);
            Console.ReadLine();
        }
    }
}
