# AI Agent Dashboard

## Project Summary
This project allows users to upload CSV files or connect to Google Sheets, input a custom prompt, and retrieve extracted information using AI. The extracted results can be viewed and downloaded as a CSV.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/AI_Agent_Project.git
    cd AI_Agent_Project
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - `GROQ_API_KEY` (for Groq API)
    - Google Sheets API credentials (refer to the [Google Sheets API documentation](https://developers.google.com/sheets/api)).

4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage Guide
1. Upload a CSV file or connect to a Google Sheet.
2. Select the primary column containing entities (e.g., companies).
3. Input a custom prompt (e.g., "Retrieve contact info for {entity}").
4. View and download the extracted data.

## Third-Party APIs/Tools
- **Groq API**: Used for querying and extracting data from AI models.
- **Google Sheets API**: Used for integrating Google Sheets.
- **Requests**: For making API calls to fetch web results.

