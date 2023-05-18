# Increases open file limit for user: holberton
exec { 'Increase hard limit for user':
  command => 'sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'Increates soft limit for user':
  command => 'sed -i "/holberton soft/s/4/1024/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
