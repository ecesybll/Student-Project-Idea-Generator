"""
Configuration settings for the Student Project Generator application.
"""
import os
from typing import Dict, Any, List

# Constants
DEFAULT_MODEL_NAME = "gemini-2.5-flash"
FALLBACK_MODEL_NAME = "gemini-1.5-flash"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 8192
DEFAULT_TOP_P = 0.95
DEFAULT_TOP_K = 40

# File size limits (in bytes)
MAX_FILE_SIZE_MB = 10
MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024

# Text input limits
MIN_TEXT_LENGTH = 10
MAX_TEXT_LENGTH = 2000

# Rate limiting
MAX_REQUESTS_PER_MINUTE = 10

# UI Constants
THEME_COLOR = "#1E88E5"
SECONDARY_COLOR = "#0D47A1"
SUCCESS_COLOR = "#43A047"
WARNING_COLOR = "#FFA000"
ERROR_COLOR = "#E53935"

class AppConfig:
    """
    Application configuration settings.
    """
    # API Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # Model Configuration
    DEFAULT_MODEL = DEFAULT_MODEL_NAME
    FALLBACK_MODEL = FALLBACK_MODEL_NAME
    DEFAULT_TEMPERATURE = DEFAULT_TEMPERATURE
    DEFAULT_MAX_TOKENS = DEFAULT_MAX_TOKENS
    
    # File Upload Limits
    MAX_FILE_SIZE = MAX_FILE_SIZE
    ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'pdf', 'txt', 'docx']
    
    # Text Input Limits
    MAX_TEXT_LENGTH = MAX_TEXT_LENGTH
    MIN_TEXT_LENGTH = MIN_TEXT_LENGTH
    
    # Rate Limiting
    MAX_REQUESTS_PER_MINUTE = MAX_REQUESTS_PER_MINUTE
    
    # UI Configuration
    THEME_COLOR = THEME_COLOR
    
    # Project Categories
    PROJECT_CATEGORIES = [
        "Web Development", 
        "Mobile Application", 
        "Data Science", 
        "Artificial Intelligence/Machine Learning", 
        "Game Development", 
        "IoT (Internet of Things)", 
        "Cyber Security", 
        "Blockchain", 
        "Augmented/Virtual Reality", 
        "Other"
    ]
    
    # Difficulty Levels
    DIFFICULTY_LEVELS = ["Beginner", "Intermediate", "Advanced"]
    
    # Project Types
    PROJECT_TYPES = ["Personal", "Team", "Academic"]
    
    # Areas of Interest
    AREAS_OF_INTEREST = [
        "Web Development",
        "Mobile Application Development",
        "Data Science",
        "Artificial Intelligence/Machine Learning",
        "Game Development",
        "IoT (Internet of Things)",
        "Cyber Security",
        "Blockchain",
        "Augmented/Virtual Reality",
        "Robotics",
        "Cloud Computing",
        "DevOps",
        "Embedded Systems",
        "Network Technologies",
        "Database Management",
        "UI/UX Design"
    ]
    
    # Error Messages (in English)
    ERROR_MESSAGES = {
        "api_key_missing": "API key is missing. Please add GEMINI_API_KEY to your .env file.",
        "api_error": "API error occurred: {error}",
        "input_too_short": "Please enter more information (at least {min_length} characters).",
        "input_too_long": "Input is too long (maximum {max_length} characters).",
        "file_too_large": "File is too large (maximum {max_size}MB).",
        "invalid_file_type": "Invalid file type. Allowed types: {allowed_types}",
        "rate_limit": "Too many requests sent. Please try again after {retry_after} seconds.",
        "general_error": "An error occurred. Please try again later.",
        "quota_limit": "API quota limit reached. Using alternative model."
    }
    
    @classmethod
    def validate_config(cls) -> Dict[str, Any]:
        """
        Validate all configuration settings
        
        Returns:
            Dict[str, Any]: Status of configuration settings
        """
        config_status = {
            'api_key_present': bool(cls.GEMINI_API_KEY),
            'file_limits_set': bool(cls.MAX_FILE_SIZE),
            'valid_extensions': bool(cls.ALLOWED_EXTENSIONS)
        }
        return config_status 