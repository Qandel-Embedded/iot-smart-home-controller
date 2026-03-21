# IoT Smart Home Controller

A distributed IoT system for smart home automation featuring low-power sensor nodes, MQTT messaging, and a central hub with edge AI processing.

## Architecture
- **Edge Nodes:** ESP32-based sensor nodes (BLE + WiFi)
- **Protocol:** MQTT over TLS
- **Hub:** Raspberry Pi 4 with Node-RED dashboard
- **Cloud:** Optional AWS IoT Core integration

## Technologies
- ESP32, STM32, Raspberry Pi
- MQTT, BLE, WiFi, Zigbee
- TensorFlow Lite for occupancy prediction
- InfluxDB + Grafana monitoring

## Features
- 20+ sensor node support
- < 5ms command latency on local network
- OTA firmware updates
- Energy harvesting nodes (solar + battery)

---
**Portfolio:** https://ahmedqandel.com | **Hire me on Upwork**
