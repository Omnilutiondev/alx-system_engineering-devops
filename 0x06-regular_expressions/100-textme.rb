#!/usr/bin/env ruby
# This script checks for 10 digit phone numbers

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\] \[FID:()\]/).join(",")
