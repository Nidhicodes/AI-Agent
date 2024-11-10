from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import streamlit as st
import gspread
from google.auth.transport.requests import Request

def connect_google_sheet(sheet_id, range_name):
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )

    service = build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    values = result.get("values", [])
    
    return pd.DataFrame(values[1:], columns=values[0]) if values else pd.DataFrame()

def write_to_google_sheet(sheet_id, range_name, data_frame):
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    )

    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    client = gspread.authorize(credentials)
    sheet = client.open_by_key(sheet_id).sheet1

    data_list = data_frame.values.tolist()

    sheet.update(range_name, data_list)
