# Creates file /tmp/school and changes ownership'
file { '/tmp/school':
  ensure  =>  'present',
  owner   =>  'www-data',
  group   =>  'www-data',
  mode    =>  '0744',
  content =>  'I love Puppet',
  path    =>  '/tmp/school'
}
