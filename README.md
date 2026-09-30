# AI-Powered Real-Time Video Surveillance and Threat Detection

An AI-powered real-time video surveillance system designed to automatically detect potential security threats from live camera feeds and recorded videos using Computer Vision and Deep Learning.

The system uses YOLO-based object detection and OpenCV to analyze video frames in real time and provide visual and audio alerts when suspicious objects or activities are detected.

---

## 🚀 Project Overview

Traditional CCTV systems mainly record video and require humans to continuously monitor the footage.

This project aims to make video surveillance more intelligent by automatically analyzing camera feeds and detecting potential threats such as:

- 🔫 Weapons
- 🔪 Knives
- 🔥 Fire
- 💨 Smoke
- 👤 Unauthorized or unknown persons
- ⚠️ Suspicious activities
- 👥 Physical fights or abnormal behavior

The system is designed with an **offline-first approach**, allowing AI-based detection without requiring continuous internet connectivity.

---

## 🎯 Objectives

- Detect security threats automatically from video streams.
- Perform real-time object detection using YOLO.
- Process webcam, CCTV, and recorded video.
- Reduce dependency on continuous human monitoring.
- Generate immediate alerts when threats are detected.
- Provide a simple monitoring dashboard.
- Improve detection performance through dataset expansion and model tuning.
- Support future integration of behavior and activity recognition.

---

## 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLO | Real-time object detection |
| OpenCV | Video processing and computer vision |
| Deep Learning | Threat/object recognition |
| Streamlit | Monitoring dashboard |
| NumPy | Numerical and image processing |
| ByteTrack / DeepSORT | Object tracking (planned/integrated) |

---

## 🏗️ System Architecture

```text
                ┌──────────────────────┐
                │   Video Input        │
                │ Webcam / CCTV / File │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     OpenCV            │
                │ Frame Acquisition     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   YOLO Detection      │
                │ Object Classification │
                └──────────┬───────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Weapon/Knife   Fire/Smoke   Person
              │            │            │
              └────────────┼────────────┘
                           ▼
                ┌──────────────────────┐
                │ Threat Analysis       │
                │ & Confidence Check    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Alert Generation      │
                │ Visual / Audio        │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Streamlit Dashboard   │
                │ Monitoring & Results  │
                └──────────────────────┘
