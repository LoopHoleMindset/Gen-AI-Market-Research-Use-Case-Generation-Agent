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


# Flexible UseCaseAgent for dynamic generation
class UseCaseAgent:
    def generate_use_cases(self, company_info, company_name, focus_areas=None):
        use_cases = []

        # Determine industry context from API response if available
        if company_info and 'organic' in company_info and len(company_info['organic']) > 0:
            industry_info = company_info['organic'][0]['snippet']
        else:
            industry_info = f"{company_name}'s industry"

        # Default focus areas if none provided by user
        if not focus_areas:
            focus_areas = ["customer experience", "supply chain", "predictive maintenance", "cybersecurity"]

        # Generate use cases based on focus areas
        for focus in focus_areas:
            if "customer experience" in focus:
                use_cases.append({
                    "title": "Personalized Customer Experience",
                    "objective": f"Create a personalized recommendation system tailored for {company_name}'s customer base.",
                    "application": f"Using AI to analyze customer preferences in {industry_info} and deliver targeted suggestions.",
                    "benefits": ["Increased customer satisfaction", "Higher sales conversions"]
                })

            if "supply chain" in focus:
                use_cases.append({
                    "title": "Supply Chain Optimization",
                    "objective": f"Improve supply chain operations for {company_name}.",
                    "application": f"Leverage AI for inventory management, demand forecasting, and logistics optimization in {industry_info}.",
                    "benefits": ["Reduced operational costs", "Enhanced inventory management"]
                })

            if "predictive maintenance" in focus:
                use_cases.append({
                    "title": "Predictive Maintenance",
                    "objective": f"Implement predictive maintenance for {company_name}'s critical equipment.",
                    "application": f"AI algorithms analyze equipment data to predict maintenance needs before failures occur in {industry_info}.",
                    "benefits": ["Reduced downtime", "Extended equipment lifespan"]
                })

            if "cybersecurity" in focus:
                use_cases.append({
                    "title": "Enhanced Cybersecurity",
                    "objective": f"Strengthen cybersecurity for {company_name}'s data and infrastructure.",
                    "application": f"Using AI to monitor network activity, detect anomalies, and prevent security breaches in {industry_info}.",
                    "benefits": ["Improved data protection", "Reduced risk of cyber attacks"]
                })

            # Add more customizable areas based on API response insights
            if company_info and "innovation" in focus:
                use_cases.append({
                    "title": "Product Innovation with AI",
                    "objective": f"Develop innovative AI-driven products tailored to {company_name}'s target market.",
                    "application": f"AI can help identify new product trends and enhance product features within {industry_info}.",
                    "benefits": ["Competitive edge", "Higher customer engagement"]
                })

        return use_cases


# Streamlit interface
def main():
    st.title("AI and ML Use Cases Generator")

    api_key = st.text_input("Enter API Key:")
    company_name = st.text_input("Enter Company Name:")
    industry = st.text_input("Enter Industry Name:")
    focus_areas = st.multiselect("Select Focus Areas", 
                                 ["customer experience", "supply chain", "predictive maintenance", "cybersecurity", "innovation"])

    if st.button("Generate Report"):
        if api_key and company_name and industry:
            research_agent = ResearchAgent(api_key)
            company_info = research_agent.search_company_info(company_name, industry)

            if company_info:
                use_case_agent = UseCaseAgent()
                use_cases = use_case_agent.generate_use_cases(company_info, company_name, focus_areas)

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
