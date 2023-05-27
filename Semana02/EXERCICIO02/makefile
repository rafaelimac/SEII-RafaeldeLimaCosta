text: printy
printy: main.o hello.o
   gcc -o printy main.o hello.o

main.o: main.c hello.h
   gcc -o main.c -c -W -Wall -ansi -pedantic

hello.o: hello.c hello.h
   gcc -o hello.o hello.c -c -W -Wall -pedantic

clean:
   rm -rf *.o *~printy
