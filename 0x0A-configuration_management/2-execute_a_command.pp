# Kills a process named killmenow

exec { 'kill_proocess':
  command  => '/usr/bin/pkill killmenow',
  onlyif   => '/usr/bin/pgrep killmenow',
  provider => 'shell',
  returns  => [0, 1]
}
