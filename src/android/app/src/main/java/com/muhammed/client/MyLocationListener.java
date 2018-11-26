package com.muhammed.client;

import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;

public class MyLocationListener implements LocationListener {
    private String _host;
    private int _port;
    private String _username;
    private String _password;

    private boolean _error = false;
    private String _errorMessage = "";

    public MyLocationListener(String host, int port, String username, String password) {
        _host = host;
        _port = port;
        _username = username;
        _password = password;
    }

    @Override
    public void onLocationChanged(Location location) {
        double latitude = location.getLatitude();
        double longitude = location.getLongitude();

        SocketService ss = new SocketService();
        ss.send(_host, _port, _username, _password, latitude, longitude);
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
}
