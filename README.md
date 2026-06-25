# Customer Product Detection & Counting System

A computer vision based product tracking and counting system.

The system allows a customer to upload an image of a product, and the system learns that product using visual embeddings. During live camera monitoring, only the selected customer product is detected, tracked, counted, and stored.

---

# Features

## Product Management

- Upload customer product image
- Generate product visual embedding
- Store product information in SQLite
- Support multiple registered products


## Product Detection

Pipeline:

Camera Input

↓

YOLO Object Detection

↓

CLIP Feature Matching

↓

ByteTrack Tracking

↓

Product Counting

↓

SQLite Storage


## Tracking

- Unique object IDs
- Prevent duplicate counting
- Track object movement


## Counting

- Line crossing based counting
- Unique ID based counting
- Product-specific counting


## Storage

SQLite database stores:

- Products
- Product embeddings
- Detection events
- Count events


## Reports

Supported:

- CSV export
- Future support:
    - Excel
    - PDF
    - Analytics


---

# System Architecture


             Customer

                |
                |

      Upload Product Image

                |
                |

         CLIP Encoder

                |
                |

      Product Embedding DB

                |
                |

          Live Camera

                |
                |

          YOLO Detector

                |
                |

      Product Similarity Match

                |
                |

          ByteTrack

                |
                |

           Counter

                |
                |

          SQLite Database

                |
                |

          Dashboard/API


---

# Technology Stack


## Computer Vision

- YOLOv8
- CLIP
- ByteTrack
- OpenCV


## Backend

- FastAPI


## Dashboard

- Streamlit


## Database

- SQLite


## Programming Language

- Python 3.10+


---

# Project Structure



video-analytics-system/

│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
│ └── settings.yaml
│
├── data/
│ ├── database/
│ ├── products/
│ │ ├── images/
│ │ └── embeddings/
│ ├── reports/
│ └── snapshots/
│
├── api/
│ ├── main.py
│ └── routes/
│
├── workers/
│ └── camera_worker.py
│
├── services/
│ └── pipeline_service.py
│
├── src/
│
│ ├── camera/
│ │ └── camera_manager.py
│
│ ├── detection/
│ │ └── detector.py
│
│ ├── embedding/
│ │ └── clip_encoder.py
│
│ ├── matching/
│ │ └── matcher.py
│
│ ├── tracking/
│ │ └── tracker.py
│
│ ├── counting/
│ │ └── counter.py
│
│ ├── database/
│ │ └── sqlite_manager.py
│
│ ├── products/
│ │ └── product_service.py
│
│ └── pipeline/
│ └── product_pipeline.py


---

# Installation


## Clone Repository


git clone <repository-url>

cd video-analytics-system



---

# Create Virtual Environment


Linux / Mac:


python -m venv venv

source venv/bin/activate



Windows:


python -m venv venv

venv\Scripts\activate



---

# Install Dependencies



pip install -r requirements.txt



---

# Download YOLO Model


Create folder:


data/models/



Download:


yolov8n.pt



Place:


data/models/yolov8n.pt



---

# Database Initialization


Database will automatically create:


data/database/production.db



Tables:


products

detections

count_events

snapshots



---

# Running the System


## Start API Server



uvicorn api.main:app --reload



API:


http://127.0.0.1:8000



---

## Start Dashboard



streamlit run dashboard/streamlit_app.py



Dashboard:


http://localhost:8501



---

# Product Registration Workflow


1. Upload product image

Example:


CocaCola_Bottle.jpg



2. System generates:


product image

CLIP embedding



3. Product stored:


SQLite

products table



---

# Detection Workflow


Input:


Camera Frame



Processing:



Frame

↓

YOLO

↓

Candidate Objects

↓

CLIP Similarity

↓

Customer Product Only

↓

ByteTrack

↓

Track ID

↓

Counter

↓

Database



---

# Database Schema


## Products



id

product_name

image_path

embedding_path

created_at



---

## Detections



id

product_id

track_id

confidence

bounding_box

timestamp



---

## Count Events



id

product_id

track_id

counted_at



---

# CPU Development Configuration


Recommended:


Model:

YOLOv8n

Image Size:

416

Device:

CPU

Confidence:

0.6



---

# Current Limitations


This is a development version.


Current limitations:

- Single camera
- CPU inference
- SQLite database
- Local deployment
- No authentication
- No cloud storage


---

# Future Improvements


## Performance

- GPU inference
- Frame batching
- Async workers


## Camera

- Multiple cameras
- RTSP support
- Camera management


## Database

- PostgreSQL
- Data analytics


## Platform

- User authentication
- Multi tenant support
- Cloud deployment


---

# Development Roadmap


Completed:

[x] Product upload

[x] CLIP embedding

[x] YOLO detection

[x] Product matching

[x] ByteTrack tracking

[x] Counting

[x] SQLite storage

[x] FastAPI foundation


Upcoming:

[ ] Multi camera

[ ] GPU optimization

[ ] Advanced reports

[ ] Cloud deployment


---

# License

For development and testing purposes.