# Customer Product Detection & Counting System

A computer vision based customer-specific product detection, tracking, and counting system.

The system allows a customer to upload an image of a product. The system learns the product appearance and then detects, tracks, and counts only that selected product from video streams.

The system supports:

- Video files
- Live camera input
- Product-specific counting
- Real-time tracking
- Analytics and reports


---

# Features


## Product Management


Customer can:

- Upload product image
- Register multiple products
- Store product information
- Generate product reference data
- Select product for counting

# Product Detection Pipeline


Complete pipeline:



Customer Product Image

    |
    |

Product Registration

    |
    |

YOLO11n Detection Model

    |
    |

Object Detection

    |
    |

Product Matching

    |
    |

ByteTrack Tracking

    |
    |

Unique Object ID

    |
    |

Counting Engine

    |
    |

SQLite Database

    |
    |

Dashboard/API

# Tracking


The system provides:


- Real-time object tracking
- Unique tracking IDs
- Duplicate counting prevention
- Object movement analysis
- Multi-direction movement support


# System Architecture

            Customer

               |

               |

      Upload Product Image

               |

               |

      Product Registration

               |

               |

          YOLO11n Model

               |

               |

      Object Detection

               |

               |

         ByteTrack

               |

               |

        Tracking IDs

               |

               |

         Counter Engine

               |

               |

          SQLite DB

               |

               |

          FastAPI

               |

               |

         Dashboard


# Project Structure


product-counting-system/

backend/
│
├── run.py
├── requirements.txt
├── README.md
│
│
├── config/
│ ├── settings.py
│ └── config.yaml
│
│
├── data/
│
│ ├── models/
│ │ └── yolo11n.pt
│ │
│ ├── videos/
│ │
│ ├── products/
│ │ ├── images/
│ │
│ ├── reports/
│ │
│ └── database/
│
│
├── api/
│
│ ├── main.py
│ │
│ └── routes/
│ ├── products.py
│ ├── camera.py
│ ├── stream.py
│ ├── snapshot.py
│ ├── reports.py
│ ├── statistics.py
│ ├── dashboard.py
│ ├── events.py
│ └── health.py
│
│
├── workers/
│
│ └── camera_worker.py
│
│
├── services/
│
│ ├── pipeline_service.py
│ ├── pipeline_state.py
│ ├── product_service.py
│ ├── statistics_service.py
│ └── dashboard_service.py
│
│
└── src/

├── camera/
│   └── camera.py
│
├── detection/
│   └── detector.py
│
├── tracking/
│   └── tracker.py
│
├── counting/
│   └── counter.py
│
├── pipeline/
│   └── pipeline.py
│
├── visualization/
│   └── draw.py
│
└── database/
    └── database.py