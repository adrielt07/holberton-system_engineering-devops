# Increase max limit
exec { 'change limit':
  command => '/bin/sed -i "s/15/2000/g" /etc/default/nginx'
}
