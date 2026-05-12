package asg1.remotes;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class SearchQuery extends UnicastRemoteObject
        implements Search {

    Map<String, String> users;

    public SearchQuery() throws RemoteException {

        super();

        users = new HashMap<>();

        users.put("user1", "pass1");
        users.put("user2", "pass2");
        users.put("admin", "admin123");
    }

    public String query(String username, String password)
            throws RemoteException {

        if (users.containsKey(username)) {

            if (users.get(username).equals(password)) {
                return "Welcome " + username;
            }
            else {
                return "Incorrect Password";
            }
        }

        return "User Not Found";
    }
}