# Increases default open files for nginx
file { '/etc/default/nginx':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => 'ULIMIT="-n 30000"',
}

service { 'nginx':
  ensure    => 'running',
  subscribe => File['/etc/default/nginx'],
}
