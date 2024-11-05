#!/usr/bin/env ruby
# This script accepts one argument and passes to a regex method 
puts ARGV[0].scan(/hb?tn/).join
