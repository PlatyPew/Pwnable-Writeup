#include <stdio.h>

int main(){
	unsigned int random;
	random = rand();	// random value!
	printf("Value: %d\n",random);

	unsigned int key=0;
	scanf("%d", &key);

	if( (key ^ random) == 0xdeadbeef ){
		printf("Good!\n");
		return 0;
	}

	printf("Wrong, maybe you should try 2^32 cases.\n");
	return 0;
}
