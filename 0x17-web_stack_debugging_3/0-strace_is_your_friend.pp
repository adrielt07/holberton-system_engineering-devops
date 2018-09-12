# Looks for string 'phpp' and change it to 'php'
exec { 'Fix extension':
  command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
