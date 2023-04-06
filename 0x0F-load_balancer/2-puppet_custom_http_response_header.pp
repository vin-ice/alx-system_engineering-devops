# creates a custom response header
file_line { 'nginx custom response header'
  ensure => 'present'
  path   => '/etc/nginx/nginx.conf'
  after  => 'http {'
  line   => 'add_header X-Served-By $hostname;'
}
