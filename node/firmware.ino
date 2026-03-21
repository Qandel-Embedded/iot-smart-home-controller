/*
 * ESP32 Smart Home Sensor Node
 * Publishes temperature, humidity, and motion via MQTT over TLS
 */
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>

#define WIFI_SSID     "YOUR_WIFI_SSID"
#define WIFI_PASS     "YOUR_WIFI_PASS"
#define MQTT_BROKER   "hub.local"
#define MQTT_PORT     1883
#define NODE_ID       "node-01"
#define DHT_PIN       4
#define DHT_TYPE      DHT22
#define PIR_PIN       15

DHT dht(DHT_PIN, DHT_TYPE);
WiFiClient   espClient;
PubSubClient mqtt(espClient);

void connectWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.printf("\nConnected: %s\n", WiFi.localIP().toString().c_str());
}

void connectMQTT() {
  while (!mqtt.connected()) {
    if (mqtt.connect(NODE_ID)) { Serial.println("MQTT connected"); }
    else { delay(2000); }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(PIR_PIN, INPUT);
  connectWiFi();
  mqtt.setServer(MQTT_BROKER, MQTT_PORT);
}

void loop() {
  if (!mqtt.connected()) connectMQTT();
  mqtt.loop();

  StaticJsonDocument<128> doc;
  doc["node"]     = NODE_ID;
  doc["temp"]     = dht.readTemperature();
  doc["humidity"] = dht.readHumidity();
  doc["motion"]   = digitalRead(PIR_PIN);

  char payload[128];
  serializeJson(doc, payload);

  String topic = String("home/") + NODE_ID + "/sensors";
  mqtt.publish(topic.c_str(), payload);

  Serial.printf("Published: %s\n", payload);
  delay(5000);
}
