#!/usr/bin/env ruby
#This ruby regex script accepts one argument and passes it to a regex matching method

puts ARGV[0].scan(/hbt(2,5)n/).join
