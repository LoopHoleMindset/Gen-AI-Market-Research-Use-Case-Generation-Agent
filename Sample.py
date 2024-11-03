import streamlit as st
import requests
import json
import os

# Class for fetching company-specific data
class ResearchAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_company_info(self, company_name, industry):
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": f"AI applications for {company_name} in {industry} industry"})
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


# Class for generating use cases with a focus on company-specific insights
class UseCaseAgent:
    def generate_use_cases(self, company_info, company_name):
        use_cases = []
        if company_info:
            industry = company_info['organic'][0]['snippet']
        else:
            industry = 'the industry'
        
        # Generate company-specific use cases
        use_cases_data = [
            {"title": "Personalized Customer Experience", 
             "objective": "Develop personalized recommendation systems for customers of " + company_name, 
             "application": f"Using AI to understand customer preferences in {industry}", 
             "benefits": ["Sales: Increased sales", "Marketing: Improved targeting"]},
             
            {"title": "AI-Powered Supply Chain Optimization", 
             "objective": "Optimize supply chain operations specific to " + company_name, 
             "application": f"AI for inventory and logistics management in {industry}", 
             "benefits": ["Operations: Better inventory management", "Finance: Cost reduction"]},
             
            {"title": "Predictive Maintenance for Key Equipment", 
             "objective": f"Ensure reliable operation of critical equipment used by {company_name}", 
             "application": f"AI to predict equipment maintenance needs in {industry}", 
             "benefits": ["Reduced downtime", "Lower maintenance costs"]},
             
            {"title": "Enhanced Cybersecurity Measures", 
             "objective": f"Strengthen cybersecurity protocols for {company_name}", 
             "application": f"Using AI to monitor and protect data systems in {industry}", 
             "benefits": ["Enhanced data security", "Prevention of data breaches"]},
             
            # Add more use cases based on company needs or known industry challenges
        ]
        
        for case in use_cases_data:
            use_cases.append(case)
        
        return use_cases


# Streamlit interface
def main():
    st.title("AI and ML Use Cases Generator")

    api_key = st.text_input("Enter API Key:")
    company_name = st.text_input("Enter Company Name:")
    industry = st.text_input("Enter Industry Name:")

    if st.button("Generate Report"):
        if api_key and company_name and industry:
            research_agent = ResearchAgent(api_key)
            company_info = research_agent.search_company_info(company_name, industry)

            if company_info:
                use_case_agent = UseCaseAgent()
                use_cases = use_case_agent.generate_use_cases(company_info, company_name)

                # Display use cases
                st.subheader(f"Generated Use Cases for {company_name}")
                for i, case in enumerate(use_cases, start=1):
                    st.write(f"### Use Case {i}: {case['title']}")
                    st.write(f"**Objective:** {case['objective']}")
                    st.write(f"**Application:** {case['application']}")
                    st.write("**Benefits:**")
                    for benefit in case['benefits']:
                        st.write(f"- {benefit}")

        else:
            st.error("Please enter API Key, Company Name, and Industry Name")

if __name__ == "__main__":
    main()
