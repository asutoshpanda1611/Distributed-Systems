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
           POA rootpoa = (POA)orb.resolve_initial_references("RootPOA");
           rootpoa.the_POAManager().activate();

           CalculatorImpl calculatorImpl = new CalculatorImpl();
           calculatorImpl.setORB(orb);

           org.omg.CORBA.Object ref = rootpoa.servant_to_reference(calculatorImpl);
           Calculator href = CalculatorHelper.narrow(ref);

           org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");        
           NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

           String name = "Calculator";
           NameComponent path[] = ncRef.to_name( name );
           ncRef.rebind(path, href);

           System.out.println("CalculatorServer ready and waiting ...");
           orb.run();

       } catch (Exception e) {
           System.err.println("ERROR: " + e);

       } finally {
           System.out.println("CalculatorServer Exiting ...");

       }
   }
}

