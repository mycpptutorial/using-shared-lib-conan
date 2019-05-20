#include <time.h>
#include <ctime>
#include <iostream>
#include "datetimeutil.h"

int main() {
  // current date/time based on current system
  time_t now = time(0);

  // convert now to string form
  char* dt = ctime(&now);

  std::cout << "The local date and time is: " << dt << std::endl;

  // convert now to tm struct for UTC
  tm* gmtm = gmtime(&now);
  char* dt1 = time_to_string(gmtm, "");
  std::cout << "The time is:" << dt1 << std::endl;
}
