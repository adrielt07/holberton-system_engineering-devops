# creating a holberton file in /tmp/ directory
file {'/tmp/holberton':
  path    => '/tmp/',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
