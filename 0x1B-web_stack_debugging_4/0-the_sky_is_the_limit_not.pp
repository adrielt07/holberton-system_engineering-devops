# Increase max limit
exec { 'limit increase':
  command  => 'sed -i "s/-n 15/-n 2000/g"\
  provider => 'shell'
}
