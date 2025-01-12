#!/usr/bin/env ruby
# This script checks for sender, reciever and country code

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
