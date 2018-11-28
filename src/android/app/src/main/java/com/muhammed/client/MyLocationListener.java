package com.muhammed.client;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.ConnectivityManager;
import android.os.Bundle;
import android.support.design.widget.TextInputLayout;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.widget.Toast;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;

public class MyLocationListener implements LocationListener {
    private LocationManager _locationManager;

    private TextInputLayout _tilLatitude;
    private TextInputLayout _tilLongitude;

    private String _host;
    private int _port;
    private String _username;
    private String _password;

    private boolean _error = false;
    private String _errorMessage = "";

    private boolean _started;

    public MyLocationListener(LocationManager locationManager, TextInputLayout tilLatitude, TextInputLayout tilLongitude) {
        _locationManager = locationManager;

        _tilLatitude = tilLatitude;
        _tilLongitude = tilLongitude;

        _started = false;
    }

    public void start(String host, int port, String username, String password) {
        _host = host;
        _port = port;
        _username = username;
        _password = password;

        _started = true;

        try {
            _locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 5000, 10, this);
        } catch (SecurityException ex) {
            _error = true;
            _errorMessage = ex.getMessage();
        }
    }

    public void stop() {
        _started = false;
    }

    @Override
    public void onLocationChanged(Location location) {
        double latitude = location.getLatitude();
        double longitude = location.getLongitude();

        _tilLatitude.getEditText().setText(String.valueOf(latitude));
        _tilLongitude.getEditText().setText(String.valueOf(longitude));

        SocketService ss = new SocketService();
        ss.send(_host, _port, _username, _password, latitude, longitude);

        if (_started) {
            try {
                _locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 5000, 10, this);
            } catch (SecurityException ex) {
                _error = true;
                _errorMessage = ex.getMessage();
            }
        }
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

    public boolean isStarted() {
        return _started;
    }
}
