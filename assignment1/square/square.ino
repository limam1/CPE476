// This Assignment will move the Romi board in a square

#include <Romi32U4.h>

Romi32U4Motors motors;
Romi32U4ButtonA buttonA;
int straight = 200;
int right_turn = 172;
void setup()
{
  // Wait for the user to press button A.
  buttonA.waitForButton();

  // Delay so that the robot does not move away while the user is
  // still touching it.
  delay(1000);
}

void loop()
{
  // Run left and right motor forward.
  ledYellow(1);
  for (int speed = 0; speed <= straight; speed++)
  {
    motors.setLeftSpeed(speed);
    motors.setRightSpeed(speed);
    delay(2);
  }
  for (int speed = straight; speed >= 0; speed--)
  {
    motors.setLeftSpeed(speed);
    motors.setRightSpeed(speed);
    delay(2);
  }

  // turn right
  ledYellow(0);
  for(int speed = 0; speed <= right_turn; speed++)
  {
    motors.setLeftSpeed(speed);
    motors.setRightSpeed(0);
    delay(3);
  }
  for(int speed = right_turn; speed >= 0; speed--)
  {
    motors.setLeftSpeed(speed);
    motors.setRightSpeed(0);
    delay(3);
  }
 
  delay(500);
}
