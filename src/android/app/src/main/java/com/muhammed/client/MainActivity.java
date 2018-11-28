package com.muhammed.client;

import android.Manifest;
import android.content.ContentResolver;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.ConnectivityManager;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.provider.Settings;
import android.support.design.widget.TextInputLayout;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class MainActivity extends AppCompatActivity {
    private static final int PERMISSION_ACCESS_FINE_LOCATION = 1;

    private TextInputLayout _tilHost;
    private TextInputLayout _tilPort;
    private TextInputLayout _tilUsername;
    private TextInputLayout _tilPassword;
    private Button _btnConnect;
    private TextInputLayout _tilLatitude;
    private TextInputLayout _tilLongitude;

    LocationManager _locationManager;
    MyLocationListener _myLocationListener;

    @Override
    protected void onCreate(final Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        _tilHost = findViewById(R.id.tilHost);
        _tilPort = findViewById(R.id.tilPort);
        _tilUsername = findViewById(R.id.tilUsername);
        _tilPassword = findViewById(R.id.tilPassword);
        _btnConnect = findViewById(R.id.btnConnect);
        _tilLatitude = findViewById(R.id.tilLatitude);
        _tilLongitude = findViewById(R.id.tilLongitude);

        _locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
        _myLocationListener = new MyLocationListener(_locationManager, _tilLatitude, _tilLongitude);

        _btnConnect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (_myLocationListener.isStarted()) {
                    _myLocationListener.stop();

                    _btnConnect.setText("Start");
                } else {
                    if (!checkPermissions()) {
                        return;
                    }

                    Handler handler = new Handler();

                    Runnable runnable = new Runnable() {
                        @Override
                        public void run() {
                            String host = _tilHost.getEditText().getText().toString();
                            int port = Integer.parseInt(_tilPort.getEditText().getText().toString());
                            String username = _tilUsername.getEditText().getText().toString();
                            String password = _tilPassword.getEditText().getText().toString();

                            _myLocationListener.start(host, port, username, password);
                        }
                    };

                    handler.post(runnable);

                    _btnConnect.setText("Stop");
                }
            }
        });
    }

    private boolean checkPermissions() {
        if (!_locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)) {
            Toast.makeText(MainActivity.this, "Telefonun GPS özelliğini aktif etmelisiniz.", Toast.LENGTH_LONG).show();

            return false;
        }

        if (ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            if (ActivityCompat.shouldShowRequestPermissionRationale(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION)) {
                Toast.makeText(MainActivity.this, "GPS erişim izni gerekmektedir.", Toast.LENGTH_LONG).show();

                return false;
            }

            if (ActivityCompat.shouldShowRequestPermissionRationale(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION)) {
                ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, PERMISSION_ACCESS_FINE_LOCATION);

                return false;
            }
        }

        ConnectivityManager connectivityManager = (ConnectivityManager)getSystemService(Context.CONNECTIVITY_SERVICE);

        if (connectivityManager.getActiveNetworkInfo() == null) {
            Toast.makeText(MainActivity.this, "Telefonun internet özelliğini aktif etmelisiniz.", Toast.LENGTH_LONG).show();

            return false;
        }

        return true;
    }
}
