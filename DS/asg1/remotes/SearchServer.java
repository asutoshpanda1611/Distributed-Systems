package asg1.remotes;

import java.rmi.Naming;

public class SearchServer {

    public static void main(String[] args) {

        try {

            SearchQuery obj = new SearchQuery();

            Naming.rebind("rmi://localhost:1099/REMOTE_SEARCH", obj);

            System.out.println("Server Started...");
        }

        catch (Exception e) {

            System.out.println(e);
        }
    }
}