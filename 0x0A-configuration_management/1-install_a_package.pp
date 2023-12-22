#!/usr/bin/pup
# Task 1
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
