import streamlit as st
import pandas as pd
from utils.google_sheets import write_to_google_sheet, connect_google_sheet
from utils.search import fetch_web_results, parse_results_with_llm

st.set_page_config(page_title="AI Agent Dashboard")

st.sidebar.title("Upload Data")
data_source = st.sidebar.selectbox("Select Data Source", ["CSV File", "Google Sheet"])

if data_source == "CSV File":
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
elif data_source == "Google Sheet":
    sheet_id = st.sidebar.text_input("Google Sheet ID")
    range_name = st.sidebar.text_input("Range Name", "Sheet1!A1:E10")
    if sheet_id and range_name:
        df = connect_google_sheet(sheet_id, range_name)

if 'df' in locals():
    st.write("Data Preview:", df)
    main_column = st.selectbox("Select Main Column", df.columns)

    custom_prompt = st.text_input("Enter Custom Prompt", "e.g., Retrieve the contact information of {entity} where entity represents the selected column")

    extracted_df = None

    if st.button("Start Extraction"):
        extracted_data = []
        for entity in df[main_column].unique():
            entity_str = str(entity) if entity is not None else ""
            prompt = custom_prompt.replace("{entity}", entity_str)
            
            results = fetch_web_results(entity_str, prompt)
            results_str = str(results) if results else "No results found."
            
            extracted_info = parse_results_with_llm(results_str, entity_str, custom_prompt)
            extracted_data.append({"Entity": entity_str, "Extracted Info": extracted_info})
        
        extracted_df = pd.DataFrame(extracted_data)
        st.write("Extracted Information", extracted_df)
        st.download_button("Download CSV", extracted_df.to_csv(index=False), "extracted_data.csv")

    # if st.button("Write to Google Sheet") and extracted_df is not None:
    #     if sheet_id and range_name:
    #         print("Button clicked and sheet ID and range name are set.")
    #         write_to_google_sheet(sheet_id, range_name, extracted_df)
    #         print("Data written to Google Sheet.")
    #         st.success("Data successfully written to Google Sheet!")

    #         updated_df = connect_google_sheet(sheet_id, range_name)
    #         st.write("Updated Google Sheet Data:")
    #         st.write(updated_df)  

    #         sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
    #         st.markdown(f"[Click here to view the updated sheet]({sheet_url})")
