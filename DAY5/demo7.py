'''
Write a python program:
   read a shell name from <STDIN>
   |
   test1 - test input shell name is bash  - initialize profile filename /etc/bashrc 
   test2 - test input shell name is ksh   - initialize profile filename /etc/kshrc 
   test3 - test input shell name is csh (or) tcsh  - initialize profile filename /etc/cshrc
				    ----     -----
   test4 - test input shell name is psh - initialize profile fileme is C:\\win32\\profile
   |
   default shell name /bin/nologin  
   default profile filename: /etc/profile

   ->display shell name and profile filename 
'''
shell_name = input('Enter a shell name:')
if(shell_name == "bash"):
    fname = "/etc/bashrc"
elif(shell_name == "ksh"):
    fname = "/etc/kshrc"
elif(shell_name == "csh" or shell_name == "tcsh"):
    fname = "/etc/cshrc"
elif(shell_name == "psh"):
    fname = "C:\\winx32\\profile"
else:
    shell_name = "/bin/nologin"
    fname = "/etc/profile"

print(f'Shell name is:{shell_name} profile filename:{fname}')
    