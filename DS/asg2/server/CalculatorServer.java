package asg2.server;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.*;
import org.omg.PortableServer.*;

import calculator_module.Calculator;
import calculator_module.CalculatorHelper;


public class CalculatorServer {
   public static void main(String args[]){
       try {
            ORB orb = ORB.init(args, null);
            POA root = (POA) orb.resolve_initial_references("RootPOA");
            root.the_POAManager().activate();

            CalculatorImpl obj = new CalculatorImpl();
            obj.setORB(orb);

            Calculator ref = CalculatorHelper.narrow(root.servant_to_reference(obj));
            NamingContextExt nc = NamingContextExtHelper.narrow(orb.resolve_initial_references("NameService"));

            nc.rebind(nc.to_name("Calculator"), ref);
            System.out.println("Server Ready...");
            orb.run();

       } catch (Exception e) {
           System.err.println("ERROR: " + e);

       } finally {
           System.out.println("CalculatorServer Exiting ...");

       }
   }
}

