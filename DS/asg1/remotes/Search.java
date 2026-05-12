package asg1.remotes;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Search extends Remote {

    public String query(String username, String password)
            throws RemoteException;
}