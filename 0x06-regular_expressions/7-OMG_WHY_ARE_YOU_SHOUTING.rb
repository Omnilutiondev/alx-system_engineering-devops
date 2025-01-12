#!/usr/bin/env ruby
# This script checks for capital letters only

puts ARGV[0].scan(/[A-Z]*/).join
