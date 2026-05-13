package asg2.client;

import org.omg.CORBA.ORB;
import org.omg.CORBA.ORBPackage.InvalidName;
import org.omg.CosNaming.*;

import calculator_module.Calculator;
import calculator_module.CalculatorHelper;

public class CalculatorClient {

   public static void main(String args[]) {
       try {
            ORB orb = ORB.init(args, null);

            NamingContextExt nc = NamingContextExtHelper.narrow(orb.resolve_initial_references("NameService"));
            Calculator obj = CalculatorHelper.narrow(nc.resolve_str("Calculator"));

            System.out.println(obj.add(10, 5));
            System.out.println(obj.subtract(10, 5));
            System.out.println(obj.multiply(10, 5));
            System.out.println(obj.divide(10, 5));


       } catch (Exception e) {
           System.out.println("ERROR : " + e);
           e.printStackTrace(System.out);
       }
   }
}
