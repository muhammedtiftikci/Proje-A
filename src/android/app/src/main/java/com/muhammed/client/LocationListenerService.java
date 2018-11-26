package com.muhammed.client;

import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;

public class LocationListenerService implements LocationListener {
    private Socket _socket;

    @Override
    public void onLocationChanged(Location location) {

    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {

    }

    @Override
    public void onProviderEnabled(String provider) {

    }

    @Override
    public void onProviderDisabled(String provider) {

    }

    public void start(String host, int port) {
        _socket = new Socket();

        try
        {
            _socket.connect(new InetSocketAddress(host, port));
        } catch (IOException ex) {

        }
    }

    public void stop() {

    }
}
