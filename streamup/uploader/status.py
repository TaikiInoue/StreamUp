import streamlit as st


class UploaderStatus:
    def error(self, fn_name: str):
        st.error(f"Error: {fn_name}")

    def success(self, fn_name: str):
        st.success(f"Success: {fn_name}")
