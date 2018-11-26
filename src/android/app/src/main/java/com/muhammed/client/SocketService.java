package com.muhammed.client;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;

public class SocketService {
    public void send(final String host, final int port, final String username, final String password, final double latitude, final double longitude) {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Socket socket = new Socket();
                    socket.connect(new InetSocketAddress(host, port), 10000);

                    String data = "android," + username + "," + password + "," + latitude + "," + longitude;

                    OutputStream os = socket.getOutputStream();
                    os.write(data.getBytes(), 0, data.length());
                    os.flush();

                    InputStream is = socket.getInputStream();
                    InputStreamReader isr = new InputStreamReader(is);

                    char[] buffer = new char[1024];

                    StringBuilder sb = new StringBuilder();

                    int length = isr.read(buffer);
                    sb.append(buffer, 0, length);

                    String receivedData = sb.toString();

                    if (receivedData == "OK") {

                    } else if (receivedData == "ERR") {

                    }

                    socket.close();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        });

        thread.start();
    }
}
