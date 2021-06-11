
#include <AFMotor.h>
#include <ros.h>

// comando para correr el nodo de arduino en la terminal
// rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600
// comando para dar permisos a arduino
// sudo chmod 777 /dev/ttyACM0

AF_DCMotor motorA(1); //SE ESTABLECEN NOMBRAN LOS MOTORES DEL SHIELD
AF_DCMotor motorB(2);
AF_DCMotor motorC(3);
AF_DCMotor motorD(4);

String nom = "Arduino";
String msg;
int error = 0;
byte type = 0;

void setup(){
  Serial.begin(9600);
  motorA.setSpeed(250); //SE ESTABLECE LA VELOCIDAD MAX DE LOS MOTORES
  motorB.setSpeed(250);
  motorC.setSpeed(250);
  motorD.setSpeed(250);
}

void setup() {
  readSerialPort();

  if (msg != "") {
    sendData();
  }
  delay(500);
  int temp;
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  arduinoNode.initNode(); // initialize the node on arduino board
  arduinoNode.advertise(arduControl);
  arduinoNode.subscribe(sub);
  randomSeed(analogRead(0));
}

void loop() {
  int temp
  readSerialPort();

  if (msg != "") {
    sendData();
  }
  delay(500);

//ADELANTE
  if msg == "front"{
    motorA.run(FORWARD);
    motorB.run(FORWARD);
    motorC.run(FORWARD);
    motorD.run(FORWARD);
    motorA.setSpeed(temp);
    motorB.setSpeed(temp);
    motorC.setSpeed(temp);
    motorD.setSpeed(temp);
  }
//ATRAS
  else if msg == "back"{
    motorA.run(BACKWARD);
    motorB.run(BACKWARD);
    motorC.run(BACKWARD);
    motorD.run(BACKWARD);
    motorA.setSpeed(temp)
    motorB.setSpeed(temp)
    motorC.setSpeed(temp)
    motorD.setSpeed(temp) 
  }
//LATERAL IZQUIERDO
  else if msg == "li"{
    motorA.run(BACKWARD);
    motorB.run(FORWARD);
    motorC.run(BACKWARD);
    motorD.run(FORWARD);
    motorA.setSpeed(temp)
    motorB.setSpeed(temp)
    motorC.setSpeed(temp)
    motorD.setSpeed(temp) 
  }
//LATERAL DERECHO
  else if msg == "li"{
    motorA.run(FORWARD);
    motorB.run(BACKWARD);
    motorC.run(FORWARD);
    motorD.run(FORWARD);
    motorA.setSpeed(temp)
    motorB.setSpeed(temp)
    motorC.setSpeed(temp)
    motorD.setSpeed(temp) 
  }
//DIAGONAL IZQUIERDO +
  else if msg == "dip"{
    motorB.run(BACKWARD);
    motorD.run(FORWARD);
    motorB.setSpeed(temp)
    motorD.setSpeed(temp) 
  }
//DIAGONAL DERECHO +  
  else if msg == "li"{
    motorA.run(FORWARD);
    motorC.run(FORWARD);
    motorA.setSpeed(temp)
    motorC.setSpeed(temp)
  }
//NINGUN MOVIMIENTO
  else {
    motorA.run(RELEASE);
    motorB.run(RELEASE);
    motorC.run(RELEASE);
    motorD.run(RELEASE);    
  }
}

void readSerialPort() {
  msg = "";
  if (Serial.available()) {
    delay(10);
    while (Serial.available() > 0) {
      msg += (char)Serial.read();
    }
    Serial.flush();
  }
}

void sendData() {
  //write data
  Serial.print(nom);
  Serial.print(" received : ");
  Serial.print(msg);
}
