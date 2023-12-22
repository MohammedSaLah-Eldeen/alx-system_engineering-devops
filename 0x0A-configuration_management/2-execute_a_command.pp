# Task 2
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
