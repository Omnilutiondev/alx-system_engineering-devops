#!/usr/bin/env ruby
# This script checks for 10 digit phone numbers

puts ARGV[0].scan(/^[0-9]{10}$/).join
