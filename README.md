# IoT Smart Home Controller

[![CI](https://github.com/Qandel-Embedded/iot-smart-home-controller/actions/workflows/ci.yml/badge.svg)](https://github.com/Qandel-Embedded/iot-smart-home-controller/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-compose-blue)](docker-compose.yml)

Distributed IoT smart home system: ESP32 sensor nodes + Python hub + MQTT + Grafana dashboard.

## Architecture
```
ESP32 Nodes ─MQTT─► Hub (Python) ─► SQLite ─► Grafana
```

## Quick Start (Docker)
```bash
git clone https://github.com/Qandel-Embedded/iot-smart-home-controller
cd iot-smart-home-controller
docker-compose up -d
# Hub at localhost:1883, Grafana at localhost:3000
```

## Flash ESP32 Node
Open `node/firmware.ino` in Arduino IDE, set WiFi/MQTT credentials, flash to ESP32.

## Stack
| Component | Technology |
|-----------|-----------|
| Sensor nodes | ESP32 + DHT22 + PIR |
| Protocol | MQTT over WiFi |
| Hub | Python + paho-mqtt + SQLite |
| Dashboard | Grafana |
| Container | Docker Compose |

---
**Portfolio:** https://ahmedqandel.com | Available for hire on Upwork
