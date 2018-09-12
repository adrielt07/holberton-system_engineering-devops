# Web stack debugging #3

### Overview
When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and is the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

- Server is running apache2
- Wordpress Installed
- Task: Troubleshoot why apache2 could not communicate to wordpress. curl -sI 127.0.0.1 returns a status code 500.

### Steps
Used strace to track apache2 services. Found out that it's trying to access a file that does not exist with extension 'phpp'.

Look for where the setting configuration file is and replace the extension to 'php'

- 0-strace_is_your_friend.pp - using Puppet correct extension using sed
