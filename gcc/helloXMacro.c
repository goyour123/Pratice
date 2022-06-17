#include <stdio.h>

#define LIST_OF_NAMES \
  X(Alice) \
  X(Bob) \
  X(Charlie) \
  X(Dan) \
  X(Emily)

int main() {
#define X(name) printf ("Hello %s\n", #name);
  LIST_OF_NAMES
#undef X
  return 0;
}