"""
Vehicle-CV-ADAS: Computer Vision and Advanced Driver Assistance Systems
Compatible with macOS, Linux, and Windows
"""

__version__ = "1.0.0"

# Main imports for easy access
from .object_detector import YoloDetector
from .traffic_lane_detector import UltrafastLaneDetectorV2
from .task_conditions import TaskConditions
from .object_detector.distance_measure import SingleCamDistanceMeasure

__all__ = [
    "YoloDetector", 
    "UltrafastLaneDetectorV2", 
    "TaskConditions",
    "SingleCamDistanceMeasure"
]