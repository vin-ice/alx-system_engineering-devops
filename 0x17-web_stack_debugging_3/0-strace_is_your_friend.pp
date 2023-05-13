# Correct a typo in the settings file
exec { '/var/html/www/wp-settings.php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
