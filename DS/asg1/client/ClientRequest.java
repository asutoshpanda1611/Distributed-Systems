package asg1.client;

import java.rmi.Naming;
import java.util.Scanner;
import asg1.remotes.Search;

public class ClientRequest {

    public static void main(String[] args) {

        try {

            Scanner sc = new Scanner(System.in);

            System.out.print("Enter Username: ");
            String username = sc.nextLine();

            System.out.print("Enter Password: ");
            String password = sc.nextLine();

            Search access = (Search)
                    Naming.lookup(
                            "rmi://localhost:1099/REMOTE_SEARCH");

            String result =
                    access.query(username, password);

            System.out.println(result);

            sc.close();
        }

        catch (Exception e) {

            System.out.println(e);
        }
    }
}