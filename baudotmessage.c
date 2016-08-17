// Create FSK message and write it to file
#include <stdio.h>

int fs=0xFFFFFFFF;
int nulls=0x00000000;

//32 thousand samples per second
int guess=1024*32;
int bitwidth=728;

void writebit(FILE* file, char bit){
    if(bit){
	for(int i=0;i<bitwidth;i++)
	    fwrite(&fs,4,1,file);
    }else{
	for(int i=0;i<bitwidth;i++)
	    fwrite(&nulls,4,1,file);
    }
}

void fsksym(FILE* file, char symbol){
    //Start bit.
    writebit(file,0);

    for(int i=0;i<5;i++){
	writebit(file,((symbol)>>i)&1);
    }

    //Stop bits.
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
    writebit(file,1);
}

int main(){
    const char *filename = "baudotmessage.bin";

    const char message[]={
	0x1F,  //LTRS_SHIFT
	0x04,  //Space
	0x03,  //A
	0x0C,  //N
	0x15,  //Y
	0x04,  //Space
	0x0A,  //R
	0x10,  //T
	0x10,  //T
	0x15,  //Y
	0x04,  //Space
	0x18,  //O
	0x07,  //U
	0x10,  //T
	0x04,  //Space
	0x10,  //T
	0x14,  //H
	0x01,  //E
	0x0A,  //R
	0x01,  //E
	0x1B,  //FIG_SHIFT
	0x19,  //?
	0x02,  //LF('\n')
    };

    FILE *foo=fopen(filename,"wb");

    //Begin with a second of each frequency.
    for(int i=0;i<guess;i++)
	fwrite(&nulls,4,1,foo);
    for(int i=0;i<guess;i++)
	fwrite(&fs,4,1,foo);

    //Then print symbols.
    for(int i=0; i<32; i++){
	for(int j=0; j < sizeof(message); j++){
	    fsksym(foo,message[j]); //Q or 1
	}
    }

    fclose(foo);
}
