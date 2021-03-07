import java.io.*;
import java.net.*;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;
 

class JavaServer {
    public static void main(String args[]) throws Exception {
        String fromClient;
        String toClient;
        String rooms[] = {"admin","temp"};
        String chats[][] = {{"Welcome to Admin Chat"},{"Welcome to TempChat"}};
        ServerSocket server = new ServerSocket(8080);
        System.out.println("wait for connection on port 8080");
 
        boolean run = true;
        while(run) {
            Socket client = server.accept();
            System.out.println("got connection on port 8080");
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            PrintWriter out = new PrintWriter(client.getOutputStream(),true);
 
            fromClient = in.readLine();
            System.out.println("received: " + fromClient);
 
            if(fromClient.equals(("ROOMS"))) {
            	
            	 for (int index=0; index < rooms.length; index++) {
                      toClient = (Arrays.toString(rooms));
                      out.println(toClient);
                      TimeUnit.SECONDS.sleep(1);
                      
            	 }
            	 
            }
            if(fromClient.equals(("GETROOM"))) {
            	
            	toClient = "Getting Rooms";
                System.out.println("send getting rooms");
                out.println(toClient);
                fromClient = in.readLine();
                System.out.println("received: " + fromClient);
                
               for(int index=0; index<rooms.length;index++) {
            	   if(rooms[index].equals(fromClient)) {
            		   
            		   toClient = Arrays.toString(chats[index]);
            		   System.out.println(toClient);
            		   out.println(toClient);
            	   }
            	   
               }
               client.close();
            	
            	
            	
            }
			if(fromClient.equals(("UPDATECHAT"))) {
			            	
			            	toClient = "updating chat";
			                System.out.println("send updating chat ");
			                out.println(toClient);
			                fromClient = in.readLine();
			                System.out.println("received: " + fromClient);
			                
			               for(int index=0; index<rooms.length;index++) {
			            	   if(rooms[index].equals(fromClient)) {
			            		   
			            		   toClient = "Updating chats";
			            		   System.out.println(toClient);
			            		   out.println(toClient);
			            		   
			            		   fromClient = in.readLine();
			            		   
			            		   chats[index] = Arrays.copyOf(chats[index], chats[index].length + 1);
			            		   chats[index][chats[index].length - 1] = fromClient;
			            		   toClient = "Chats updated";
			            		   out.println(toClient);
			            		   
			            	   }
			            	   
			               }
			               client.close();
			            	
			            	
			            	
			            }
			if(fromClient.equals(("CREATEROOM"))) {
            	
            	toClient = "creating room";
                System.out.println("send creating room");
                out.println(toClient);
                fromClient = in.readLine();
                System.out.println("received: " + fromClient);
                
                
                chats = Arrays.copyOf(chats, chats.length + 1);
                
                rooms = Arrays.copyOf(rooms, rooms.length + 1);
                rooms[rooms.length - 1] = fromClient;
                
                chats[chats.length-1] = new String[]{"Welcome to that chat room"};
                
                toClient = "Created Room";
                out.println(toClient);
                
                client.close();
            	
            	
            	
            }
        }
        System.exit(0);
    }
}