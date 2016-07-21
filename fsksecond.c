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
  FILE *foo=fopen("fsksecond.bin","wb");
  
  const char message[]={
    0x1f, //Letters
    0x0f, //K
    0x0f, //K
    0x1b, //Numbers
    0x0a, //4
    0x1f, //Letters
    0x1e, //V
    0x0e, //C
    0x11,  //Z
    
    0x08, //Space
    0x08, //Space
    0x08, //Space
    0x08, //Space
  };
  
  //Begin with a second of each frequency.
  for(int i=0;i<guess;i++)
    fwrite(&nulls,4,1,foo);
  for(int i=0;i<guess;i++)
    fwrite(&fs,4,1,foo);
  
  //Then print symbols.
  for(int i=0;i<32;i++){
    for(int j=0;j<sizeof(message);j++){
      fsksym(foo,message[j]); //Q or 1
    }
    

  }


  fclose(foo);
}
