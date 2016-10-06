# Lecture 9 : October 6, 2016

## Recap: Multiprocessing
* Want to do system calls.
* Difficult because kernel and application memory separate. (safety)
* Exceptions: switch from unprivileged to privileged
* app calls syscall library
* kernel catches, saves registers carefully (only k0, k1, no stack)
* Switches to kernels stack frame
* saves, calls MIPS_TRAP
* saves the system call code in v0
* place results back into the trap frame
* when we restore, in the state after the system call.
* In each layer, none of the others knew what was happening.

Processes own threads and have virtual memory:
* In order to Switch process, need to:
  * Switch thread
  * virtual Memory space

### Interrupt
While handling an interrupt, interrupts are turned off.


## System Calls for Process Management
In UNIX, create a process and load an application into a process.

### fork syscall
Simply creates a new process that is a clone (the child) of the original (the parent).
  * Virtual Memory is a copy (but identical). Could diverge after this point.
  * fork is called in the parent process, but returns in both the parent and child processes.

``` C
#include <uistd.h>
#include <stdio.h>

// This prints six times
int main(){
  pid_t ret = fork(); // parent and child return from here
  fprintf(stderr, "%d\n", ret);
  ret = fork(); // two children for parent and two for child
  fprintf(stderr, "%d\n", ret);
  return 0;
}
```

### Example with sharing memory
* The parent changed the variable, but the child didn't see it (because of separate memory)
* The moment the parent quit, the shell thought the program was over and returned. Then the child returns.
``` C
#include <stdio.h>
#include <uistd.h>

int shared;
int main(){
  pid_t ret;
  shared = 42;

  ret = fork();
  fprintf(stderr, "%d %d\n", ret, shared);

  if(ret == 0){
    sleep(2);
    fprintf(stderr, "C: %d\n", shared);
  }else{
    sleep(1);
    shared = 84;
    fprintf(stderr, "P: %d\n", shared);
  }
  return 0;
}
```

## The execv syscall
* Used **fork** to make a new process, use **execv** to switch the process to a different application.
* Changes the program that a process is running.
* The calling processes current virtual memory is destroyed.
* The process gets a new virtual memory, initialized with the code and data of the new program to run.
* After execv, the new program starts executing.


``` C
#include <stdio.h>
#include <unistd.h>

int main(){
  pid_t ret;
  shared = 42;

  ret = fork();
  fprintf(stderr, "%d\n", ret);

  if(ret == 0){
    sleep(2);
    execl("/bin/ls", "/bin/ls", NULL);
    // execl("/bin/echo", "/bin/echo", "Hello", NULL);
  }else{
    sleep(1);
  }

  return 0;
}
```

### \_exit and waitpid
* \_exit terminates the process that called it
* waitpid: wait for process to terminate and get it's return code.

``` C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){
  pid_t ret;
  shared = 42;

  ret = fork();
  fprintf(stderr, "%d\n", ret);

  if(ret == 0){
    sleep(2);
    exit(42); // communicate 42 from child
  }else{
    int status;
    waitpid(ret, &status, 0);
    printf(stderr, "Status: %d\n", WEXITSTATUS(status));
  }

  return 0;
}
```

``` C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){
  pid_t ret;
  shared = 42;

  ret = fork();
  fprintf(stderr, "%d\n", ret);

  if(ret == 0){
    sleep(2);
    execl("/bin/echo", "/bin/echo", "Hello", NULL); // echo's exit code is returned
  }else{
    int status;
    waitpid(ret, &status, 0);
    printf(stderr, "Status: %d\n", WEXITSTATUS(status));
  }

  return 0;
}
```

If a child process is done and needs to return a status code, it will wait until the the code is retrieved before quitting.

## Virtual Memory
From each processes perspective, it owns all memory. The kernel will allocate virtual memory for each process.
