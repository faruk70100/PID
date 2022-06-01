#define EnaA 2
#define EnaB 3
#define MotPWM 9
#define MotIn1 11
#define MotIn2 10
int posit = 0;
float kp=0;
float ki=0;
float kd=0;
float epre=0;
float eint=0;
int ep=0;
int tar = 1000;
int val;
void setup() {
  Serial.begin(9600);
  pinMode(EnaA,INPUT);
  pinMode(EnaB,INPUT);
  pinMode(MotIn1, OUTPUT);
  pinMode(MotIn2, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(EnaA),EncoderRead,RISING);//EnaA pininden digital değerde yükselme algılandığında interrupt modu devreye girer ve EncoderRead fonk çalışır
}
void loop() {
  int temp;
  String val;
  String valu;
  String valType;
  if(Serial.available()>0){//COM1'den veri geliyor mu kontrolü
    valu = Serial.read(); //COM1 gelen değeri okur
    valu.trim();//gelen verilerdeki boşlukları siler
    valu.toLowerCase();// bütün büyük harfleri küçük harf yapar
    temp = valu.indexOf(':');//gelen veri için de : olan değerin konumu bulur
    valType = valu.substring(0,temp);// ilk değerden :'in olduğu konuma kadar string olarak böler
    val = valu.substring(temp+1); // : dan başlar ve sona kadar olan kısmı bir strin olarak böler
    if(valType.equals('kp')){ // ilk bölünen parça kp diye kontrol eder
      kp = val.toInt(); // ikinci kısmı kp integer değeri olarak atar
    }
    if(valType.equals("ki")){// ilk bölünen parça ki diye kontrol eder
      ki = val.toInt(); // ikinci kısmı ki integer değeri olarak atar
    }
    if(valType.equals("kd")){// ilk bölünen parça kd diye kontrol eder
      kd = val.toInt(); // ikinci kısmı kd integer değeri olarak atar
    }
  }
  long currT = micros();//döngünün micro saniyesin olara alıyor
  float deltaT=((float)(currT-ep))/1.0e6; //zaman farkını saniye ceviriyor
  ep = currT; //şu an ki zamanı önceki zamana eşitliyor
  int e = tar-posit; // istenilen konum ile şu an ki konum arasındaki hata bulunuyor
  
  float dert = (e-epre)/deltaT; //türev hesaplaması (e2-e1)/dt 
  float eint = eint + e*deltaT; //integral hesaplaması 
  float Ut= kp*e + ki*eint + kd*dert;//u(t) hesaplanması
  
  float pwr = fabs(Ut); //ondalık sayı mutlak değeri alan fonk.
  if(pwr>255){
    // Ut mutlak değer max değerinden büyük olamayacağı için max değer yaptık
    pwr = 255;
  }
  // yön ileri olarak ayarlandı Ut negatif ise değiştirdik
  int direc = 1;
  if(Ut<0){
    direc = -1;
  }
  Motor(direc,pwr,MotPWM,MotIn1,MotIn2);// motor çalışması için gerekli veriler ile gönderdik
  epre=e; // şu an ki hatayı eski hata değerine atadık
  Serial.print(tar);
  Serial.print("-->");
  Serial.println(posit);
  Serial.print("\n");
}
void Motor(int Mdir, int PWMVal, int pwm, int in1, int in2){
  analogWrite(pwm,PWMVal);// motorun dönüş hızı ayarlandı
  if(Mdir==1){//ileri yönde ise motorlar çalıştı
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  }
  else if(Mdir==-1){// geri yön için motorlar çalıştı
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  }
  else{// motorları durdurduk
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
  }
}
void EncoderRead(){
  int b = digitalRead(EnaB);//EnaA pin tetiklendiği an EnaB değeri okundu
  if(b>0){//eğer EnaB değeri 0 değil ise saat yönünde dönüş algılandı
    posit ++; //saat yönünde dönüş ileri yönde pozisyonu değeri artır
  }
  else{//eğer EnaB değeri 0  ise saat yönünün tersine dönüş algılandı
    posit --; //saat yönünde tersi dönüş geri yönde pozisyonu değeri azaltıldı
  }
  b=0;
}
