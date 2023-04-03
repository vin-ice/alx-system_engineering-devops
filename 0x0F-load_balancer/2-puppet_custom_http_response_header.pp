# creates a custom response
exec { 'response':
  command => 'apt-get -y update'
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
}