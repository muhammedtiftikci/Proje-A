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
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class MainActivity extends AppCompatActivity {
    private static final int PERMISSION_ACCESS_FINE_LOCATION = 1;

    private TextInputLayout _tilHost;
    private TextInputLayout _tilPort;
    private TextInputLayout _tilUsername;
    private Button _btnConnect;
    private TextInputLayout _tilLatitude;
    private TextInputLayout _tilLongitude;

    private Socket _socket;

    @Override
    protected void onCreate(final Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        _tilHost = findViewById(R.id.tilHost);
        _tilPort = findViewById(R.id.tilPort);
        _tilUsername = findViewById(R.id.tilUsername);
        _btnConnect = findViewById(R.id.btnConnect);
        _tilLatitude = findViewById(R.id.tilLatitude);
        _tilLongitude = findViewById(R.id.tilLongitude);

        _btnConnect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!checkPermissions()) {
                    return;
                }

                final LocationManager locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);

                try
                {
                    locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 5000, 10, new LocationListener() {
                        @Override
                        public void onLocationChanged(Location location) {
                            _tilLatitude.getEditText().setText(String.valueOf(location.getLatitude()));
                            _tilLongitude.getEditText().setText(String.valueOf(location.getLongitude()));

                            initSocket();
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
                    });
                } catch (SecurityException ex) {

                }
            }
        });
    }

    private boolean checkPermissions() {
        final LocationManager locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);

        if (!locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)) {
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

    private void initSocket() {
        final Handler handler = new Handler(Looper.getMainLooper());

        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try
                {
                    String host = _tilHost.getEditText().getText().toString();
                    int port = Integer.parseInt(_tilPort.getEditText().getText().toString());

                    _socket = new Socket();
                    _socket.connect(new InetSocketAddress(host, port), 10000);

                    //InputStream is = _socket.getInputStream();
                    //InputStreamReader isr = new InputStreamReader(is);

                    String latitude = _tilLatitude.getEditText().getText().toString();
                    String longitude = _tilLongitude.getEditText().getText().toString();

                    String message = "Enlem: " + latitude + ". Boylam: " + longitude + ".";

                    OutputStream os = _socket.getOutputStream();
                    os.write(message.getBytes(), 0, message.length());
                    os.flush();

                    closeSocket();
                } catch (UnknownHostException ex) {
                    final String message = ex.getMessage();

                    handler.post(new Runnable() {
                        @Override
                        public void run() {
                            Toast.makeText(MainActivity.this, "UnknownHostException: " + message, Toast.LENGTH_SHORT).show();
                        }
                    });
                } catch (IOException ex) {
                    final String message = ex.getMessage();

                    handler.post(new Runnable() {
                        @Override
                        public void run() {
                            Toast.makeText(MainActivity.this, "IOException: " + message, Toast.LENGTH_SHORT).show();
                        }
                    });
                }
            }
        });

        thread.start();
    }

    private void closeSocket() {
        if (_socket.isConnected()) {
            try
            {
                _socket.close();
            } catch (IOException ex) {

            }
        }
    }
}
