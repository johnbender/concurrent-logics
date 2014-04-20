#include <stdio.h>

//    x1          x2         x3
// l1 -- l2    l3 -- l4
// l1 -- l2               l5 -- l6
// ( x1 v x3 ) & ( x1 v x4 )
int main(){
  int order;

  order = 1;
  goto l1;
 order1_return:
  order = 2;
  goto l1;
 order2_return:

  return 0;

 l1:
  printf( "x1\n" );
  if( order == 1 ) {
    // extra unique edge
    goto l3;
  } else if( order == 2 ) {
    goto l5;
  }
 l3:
  printf( "x2\n" );
  if( order == 1 ) {
    goto order1_return;
  }
 l5:
  printf( "x3\n" );
  if( order == 2 ) {
    goto order2_return;
  }
}
