#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 256

typedef struct{
   char** strings;
   size_t size;
}ArrayString;

ArrayString newArrayString();
void append(ArrayString *arrayString, char *string);
void printArrayString(ArrayString *arrayString);
void freeArrayString(ArrayString *arrayString);

int main(int argc, char* argv[]){
  ArrayString arrayString = newArrayString();

  append(&arrayString, "dinausore");
  append(&arrayString, "cactus");
  append(&arrayString, "bulbizarre");

  printArrayString(&arrayString);
  freeArrayString(&arrayString);
}

ArrayString newArrayString(){
  return (ArrayString){ .strings = (char**)calloc(0, sizeof(char*)), .size = 0 };
}

void append(ArrayString *arrayString, char *string){
  (*arrayString).size++;
  (*arrayString).strings = realloc((*arrayString).strings, (*arrayString).size * MAX_SIZE);
  (*arrayString).strings[(*arrayString).size - 1] = (char*)malloc(sizeof(string) / sizeof(char));
  (*arrayString).strings[(*arrayString).size - 1] = string;
}

void printArrayString(ArrayString *arrayString){
  size_t i;
  printf("[");
  for(i = 0; i < (*arrayString).size; i++){
    printf("'%s'", (*arrayString).strings[i]);
    if(i < (*arrayString).size - 1){
      printf(", ");
    }
  }
  printf("]\n");
}

void freeArrayString(ArrayString *arrayString){
  free((*arrayString).strings);
}
