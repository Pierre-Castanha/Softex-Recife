// Código em Java para serialização e deserialização

import java.io.*;
  
class Exemplo implements java.io.Serializable
{
    public int a;
    public String b;
  
    // Default constructor
    public Exemplo(int a, String b)
    {
        this.a = a;
        this.b = b;
    }
  
}
  
class Teste
{
    public static void main(String[] args)
    {   
        Exemplo object = new Exemplo(1, "geeksforgeeks");
        String filename = "file.ser";
          
        // Serialization 
        try
        {   
            //Saving of object in a file
            FileOutputStream file = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(file);
              
            // Method for serialization of object
            out.writeObject(object);
              
            out.close();
            file.close();
              
            System.out.println("Objeto foi serializado!");
  
        }
          
        catch(IOException ex)
        {
            System.out.println("IOException é recebido!");
        }
  
  
        Exemplo object1 = null;
  
        // Deserialization
        try
        {   
            // Reading the object from a file
            FileInputStream file = new FileInputStream(filename);
            ObjectInputStream in = new ObjectInputStream(file);
              
            // Method for deserialization of object
            object1 = (Exemplo)in.readObject();
              
            in.close();
            file.close();
              
            System.out.println("Objeto foi deserializado!");
            System.out.println("a = " + object1.a);
            System.out.println("b = " + object1.b);
        }
          
        catch(IOException ex)
        {
            System.out.println("IOException foi recebido!");
        }
          
        catch(ClassNotFoundException ex)
        {
            System.out.println("ClassNotFoundException foi recebido!");
        }
  
    }
}