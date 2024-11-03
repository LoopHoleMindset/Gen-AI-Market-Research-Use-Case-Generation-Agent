import streamlit as st
# from fpdf2 import FPDF
import requests
import json
import os

# Class for fetching industry data
class ResearchAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_industry_info(self, industry):
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": f"AI applications in {industry} industry"})
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to retrieve information: {response.text}")
            return None


# Class for generating use cases
class UseCaseAgent:
    def generate_use_cases(self, industry_info):
        use_cases = []
        industry = industry_info['organic'][0]['snippet'] if industry_info else 'the industry'
        
        # Define use cases
        use_cases_data = [
            {"title": "Personalized Customer Experience", "objective": "Develop personalized recommendation systems", "application": f"Use AI in {industry}", "benefits": ["Sales: Increased sales", "Marketing: Improved targeting"]},
            {"title": "AI-Powered Supply Chain Optimization", "objective": "Optimize supply chain operations", "application": f"Use AI for inventory management in {industry}", "benefits": ["Operations: Better inventory management", "Finance: Cost reduction"]},
            # Add more use cases as needed
        ]
        for case in use_cases_data:
            use_cases.append(case)
        return use_cases


# PDF Report class
class PDFReport(FPDF):
    def __init__(self):
        super().__init__()

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'AI and ML Use Cases Report', 0, 1, 'C')
        self.ln(10)

    def add_use_case(self, use_case):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, f"Use Case: {use_case['title']}", 0, 1)
        self.set_font('Arial', '', 10)
        self.cell(0, 10, "Objective:", 0, 1)
        self.multi_cell(0, 10, use_case["objective"])
        self.cell(0, 10, "Application:", 0, 1)
        self.multi_cell(0, 10, use_case["application"])
        self.cell(0, 10, "Cross-Functional Benefits:", 0, 1)
        for benefit in use_case["benefits"]:
            self.multi_cell(0, 10, f"- {benefit}")
        self.ln(10)


# Streamlit interface
def main():
    st.title("AI and ML Use Cases Generator")

    api_key = st.text_input("Enter API Key:")
    industry = st.text_input("Enter Industry Name:")

    if st.button("Generate Report"):
        if api_key and industry:
            research_agent = ResearchAgent(api_key)
            industry_info = research_agent.search_industry_info(industry)

            if industry_info:
                use_case_agent = UseCaseAgent()
                use_cases = use_case_agent.generate_use_cases(industry_info)

                # # Create PDF
                # pdf = PDFReport()
                # pdf.add_page()
                # for case in use_cases:
                #     pdf.add_use_case(case)

                # # Save and display PDF
                # pdf_output_path = "/tmp/Report.pdf"
                # pdf.output(pdf_output_path)
                # with open(pdf_output_path, "rb") as pdf_file:
                #     st.download_button("Download Report", pdf_file, file_name="AI_Report.pdf")
        else:
            st.error("Please enter both API Key and Industry Name")

if __name__ == "__main__":
    main()
