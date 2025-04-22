What happens to the 0-th bit in a when we perform a = a^1 ?


It gets toggled

Below is how XOR operator works -

1^1 ==> 0

1^0 ==> 1

0^1 ==> 1

0^0 ==>0


When we perform a = a^1 the 0-th bit will always get toggled.
e.g. a=15 ==> 15^1 ==> 1111 ^ 0001 ==> 1110 ==> 0th bit get toggled
         a=4 ==> 4^1 ==> 100 ^ 001 ==> 101 ==> 0th bit get toggled