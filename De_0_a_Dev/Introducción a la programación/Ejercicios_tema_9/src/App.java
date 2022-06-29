public class App {
    public static void main(String[] args) throws Exception {

        System.out.println("-------------Clase Cliente-------------");
        Cliente cliente = new Cliente();
        cliente.edad = 30;
        cliente.telefono = 951753147;
        cliente.nombre = "Juan";
        cliente.credito = 9.99f;
        

        System.out.println(cliente.edad);
        System.out.println(cliente.telefono);
        System.out.println(cliente.nombre);
        System.out.println(cliente.credito);

        System.out.println("-------------Clase Trabajador-------------");
        Trabajador trabajador = new Trabajador();
        trabajador.edad = 27;
        trabajador.telefono = 999966658;
        trabajador.nombre = "Pepito";
        trabajador.salario = 800;

        System.out.println(trabajador.edad);
        System.out.println(trabajador.telefono);
        System.out.println(trabajador.nombre);
        System.out.println(trabajador.salario);

    }
}


class Persona {
    int edad;
    String nombre;
    int telefono;    
}

//Clase Cliente que hereda de persona
class Cliente extends Persona {
    float credito;
}

//Clase Trabajador que hereda de persona
class Trabajador extends Persona {
    double salario;
}

/**
* Crea una clase Persona con las siguientes variables:

* La edad

* El nombre

* El teléfono

Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.

Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.

Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.
 */