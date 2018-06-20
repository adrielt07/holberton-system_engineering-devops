#!/usr/bin/env ruby
a = ARGV[0].scan(/from:.\w*/).join.slice(5..-1)
b = ARGV[0].scan(/to:.\d*/).join.slice(3..-1)
c = ARGV[0].scan(/flags:\W*\d\W*\d\W*\d\W*\d\W*\d/).join.slice(6..-1)
print "#{a},#{b},#{c}\n"
