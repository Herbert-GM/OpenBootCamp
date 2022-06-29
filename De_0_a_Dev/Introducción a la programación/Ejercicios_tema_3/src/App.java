
public class App {
    public static void main(String[] args) throws Exception {

        System.out.println("Alumno: Herbert GM!");

        /**
         ** Primera parte:
         * Crear una función con tres parámetros que sean números que se suman entre sí.
         * Llamar a la función en el main y darle valores.
         */
        System.out.println(Sumar(10, 10, 10));

        /**
         * 
         * *Segunda parte:
         * Crear una clase coche.
         * Dentro de la clase coche, una variable numérica que almacene el número de
         * puertas que tiene.
         * Una función que incremente el número de puertas que tiene el coche.
         * Crear un objeto miCoche en el main y añadirle una puerta.
         * Mostrar el número de puertas que tiene el objeto.
         */

        Coche miCoche = new Coche();
        miCoche.AgregarPuertas();
        System.out.println(miCoche.puertas);

    }

    /**
     * esta función suma tres numeros
     * * Numeros enteros
     * 
     * @param x first number
     * @param y second number
     * @param c third number
     * @return the sum of x + y and c
     */
    static int Sumar(int x, int y, int c) {
        return x + y + c;
    }

}

/**
 * Representa un coche 
 */
class Coche {
    public int puertas = 4;

    /**
     * Función que agrega puertas al objeto coche
     * *Incrementa de a 1
     */
    public void AgregarPuertas() {
        this.puertas++;
    }
}
