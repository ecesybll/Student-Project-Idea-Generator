"""
Application Constants - Clean Code Practice

This file contains all magic strings and numbers used throughout the application.
Following clean code principles, all literal values should be defined here as constants
to improve maintainability, readability, and reduce errors.

Author: AI Project Generator Team
Date: 2025
"""

# =============================================================================
# UI CONSTANTS
# =============================================================================

# Page Configuration
PAGE_TITLE = "Student Project Idea Generator"
PAGE_ICON = "🎓"
LAYOUT_WIDE = "wide"
SIDEBAR_EXPANDED = "expanded"

# Headers and Titles
MAIN_HEADER = "🚀 Your Project Suggestion"
CHAT_HEADER = "💬 Project Chat"
MODEL_SETTINGS_TITLE = "⚙️ Model Settings"
SECURITY_SETTINGS_TITLE = "🛡️ Security Settings"

# Form Labels
FORM_KEY = "project_generator_form"
SUBMIT_BUTTON_TEXT = "Generate Project Ideas"
BACK_BUTTON_TEXT = "← Back to Project Generator"

# Input Form Labels
DETAILED_INFO_LABEL = "Detailed Project Information"
DETAILED_INFO_PLACEHOLDER = "Enter details about your project..."
DETAILED_INFO_HELP = "The more details you provide about your project, the more customized suggestions you'll receive."

CATEGORIES_LABEL = "Project Categories"
CATEGORIES_HELP = "Select the project categories you are interested in."

DIFFICULTY_LABEL = "Difficulty Level"
DIFFICULTY_HELP = "Select the difficulty level of the project."

PROJECT_TYPE_LABEL = "Project Type"
PROJECT_TYPE_HELP = "Select the type of the project."

INTERESTS_LABEL = "Areas of Interest"
INTERESTS_HELP = "Select the areas you are interested in."

KEYWORDS_LABEL = "Keywords"
KEYWORDS_PLACEHOLDER = "E.g.: e-commerce, data analysis, game..."
KEYWORDS_HELP = "Enter keywords related to your project."

TIMELINE_LABEL = "Project Timeline (Weeks)"
TIMELINE_HELP = "Select the duration you plan to complete the project."

COMPLEXITY_LABEL = "Project Complexity"
COMPLEXITY_HELP = "Select the complexity level of the project (1: Simple, 10: Very complex)."

FILE_UPLOAD_LABEL = "Upload a File for Inspiration (Optional)"

# Model Configuration Labels
TEMPERATURE_LABEL = "Creativity (Temperature)"
TEMPERATURE_HELP = "Higher values produce more creative results."

MAX_TOKENS_LABEL = "Maximum Output Length"
MAX_TOKENS_HELP = "Higher values produce longer and more detailed responses."

SAFETY_LEVEL_LABEL = "Safety Level"
SAFETY_LEVEL_HELP = "Sensitivity of safety filters. Minimum level blocks less."

# Button Labels
SAVE_PROJECT_BUTTON = "💾 Save Project"
DOWNLOAD_MARKDOWN_BUTTON = "📥 Download as Markdown"
START_CHAT_BUTTON = "💬 Start Chat"

# Chat Interface Labels
CHAT_INPUT_PLACEHOLDER = "Type your question..."

# =============================================================================
# STATUS MESSAGES
# =============================================================================

# Project Generation Status Messages
STATUS_GENERATING = "🚀 Generating project ideas..."
STATUS_PROCESSING_INPUTS = "⚙️ Processing inputs..."
STATUS_PROCESSING_IMAGE = "🖼️ Processing uploaded file..."
STATUS_CREATING_PROMPT = "📝 Creating customized prompt..."
STATUS_CONNECTING_API = "🤖 Connecting to Gemini API..."
STATUS_GENERATING_IDEAS = "🧠 Generating project ideas... (This may take a while)"
STATUS_PREPARING_RESULTS = "✅ Preparing results..."
STATUS_PROJECT_COMPLETE = "🎉 Project guide successfully created!"
STATUS_PROJECT_READY = "✅ Project guide is ready!"

# Chat Status Messages
STATUS_CHAT_PREPARING = "🤖 Preparing response..."
STATUS_CHAT_ANALYZING = "📝 Analyzing your question..."
STATUS_CHAT_GENERATING = "🧠 Generating detailed response..."
STATUS_CHAT_READY = "✅ Response is ready!"
STATUS_CHAT_COMPLETE = "✅ Response completed!"
STATUS_CHAT_ERROR = "❌ An error occurred"

# Success Messages
SUCCESS_PROJECT_SAVED = "Project saved successfully!"

# Warning Messages
WARNING_FILL_REQUIRED_FIELDS = "Please fill in at least one field related to your project idea (Project Details, Keywords, Categories, or Areas of Interest)."

# Info Messages
INFO_CHAT_WELCOME = ("You can ask questions to get more information about the project. "
                    "For example: 'How can I start this project?' or 'Which libraries are required?'")

# Error Messages
ERROR_PROJECT_SAVE = "An error occurred while saving the project."

# =============================================================================
# NUMERIC CONSTANTS
# =============================================================================

# Timing Constants (in seconds)
DELAY_SHORT = 0.3
DELAY_MEDIUM = 0.5
DELAY_LONG = 1.0

# Slider Ranges
TEMPERATURE_MIN = 0.0
TEMPERATURE_MAX = 1.0
TEMPERATURE_DEFAULT = 0.7
TEMPERATURE_STEP = 0.05

MAX_TOKENS_MIN = 1024
MAX_TOKENS_MAX = 8192
MAX_TOKENS_STEP = 256

TIMELINE_MIN = 1
TIMELINE_MAX = 16
TIMELINE_DEFAULT = 8
TIMELINE_STEP = 1

COMPLEXITY_MIN = 1
COMPLEXITY_MAX = 10
COMPLEXITY_DEFAULT = 5
COMPLEXITY_STEP = 1

# Text Lengths
MIN_RESPONSE_LENGTH_CHAT = 200
MIN_RESPONSE_LENGTH_GENERAL = 250

# =============================================================================
# SAFETY LEVELS
# =============================================================================

SAFETY_MINIMUM = "Minimum (BLOCK_NONE)"
SAFETY_LOW = "Low (BLOCK_ONLY_HIGH)"
SAFETY_MEDIUM = "Medium (BLOCK_MEDIUM_AND_ABOVE)"
SAFETY_HIGH = "High (BLOCK_LOW_AND_ABOVE)"

SAFETY_LEVELS = [SAFETY_MINIMUM, SAFETY_LOW, SAFETY_MEDIUM, SAFETY_HIGH]

# =============================================================================
# HTML/CSS CLASSES
# =============================================================================

CSS_SUB_HEADER = "sub-header"
CSS_SECTION_TITLE = "##### **{title}**"

# Section Titles
SECTION_CATEGORY = "Field and Category"
SECTION_SCOPE = "Scope and Level"

# =============================================================================
# FILE EXTENSIONS
# =============================================================================

MARKDOWN_EXTENSION = ".md"
JSON_EXTENSION = ".json"

# File Upload Help Text
FILE_UPLOAD_HELP = "Allowed file types: {allowed_types}"

# =============================================================================
# COMPLEXITY DESCRIPTIONS
# =============================================================================

COMPLEXITY_DESCRIPTIONS = {
    1: "Very simple - Basic concepts and simple structures",
    2: "Simple - Requires basic programming skills",
    3: "Easy - Uses several technologies together",
    4: "Medium-Easy - Integration of multiple components",
    5: "Medium - Data management and API usage",
    6: "Medium-Hard - Complex data structures and algorithms",
    7: "Hard - Advanced architecture and design patterns",
    8: "Very Hard - Performance optimization and scalability",
    9: "Expert - Distributed systems and microservices",
    10: "Professional - Industry-level solutions"
}

# =============================================================================
# SESSION STATE KEYS
# =============================================================================

SESSION_SHOW_CHAT = "show_chat"
SESSION_PROJECT_DATA = "project_data"
SESSION_PROJECT_CONTEXT = "project_context"
SESSION_MODEL_CONFIG = "model_config"
SESSION_MESSAGES = "messages"
SESSION_GEMINI_CLIENT = "gemini_client"

# =============================================================================
# CHAT HELP CONTENT
# =============================================================================

CHAT_HELP_TITLE = "### Chat Help"
CHAT_HELP_CONTENT = """
You can use this chat interface to get more information about your project. Here are some example questions:

- How can I start this project?
- Which programming languages and libraries are required?
- Can you explain the difficulty level of the project in more detail?
- How can I turn this project into a portfolio project?
- What can I do to make the project simpler/more complex?
- What resources do you recommend for developing this project?
- Can you suggest a timeline to complete the project?

The assistant AI will do its best to answer your questions about your project.
"""

# =============================================================================
# TAB NAMES
# =============================================================================

TAB_CHAT = "💬 Chat"
TAB_HELP = "ℹ️ Help"

# =============================================================================
# MARKDOWN FORMATTING
# =============================================================================

MARKDOWN_DIVIDER = "---"
MARKDOWN_BOLD_FORMAT = "**{text}**"

# =============================================================================
# DEFAULT VALUES
# =============================================================================

DEFAULT_EMPTY_STRING = ""
DEFAULT_EMPTY_LIST = []
DEFAULT_ZERO = 0
DEFAULT_NONE = None

# =============================================================================
# USER ROLES
# =============================================================================

USER_ROLE = "user"
ASSISTANT_ROLE = "assistant"

# =============================================================================
# VALIDATION MESSAGES
# =============================================================================

VALIDATION_REQUIRED_FIELD = "This field is required"
VALIDATION_MIN_LENGTH = "Minimum {min_length} characters required"
VALIDATION_MAX_LENGTH = "Maximum {max_length} characters allowed" 