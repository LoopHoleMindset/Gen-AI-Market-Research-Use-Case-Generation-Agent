import streamlit as st
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
        
        # Extended list of use cases
        use_cases_data = [
            {"title": "Personalized Customer Experience", "objective": "Develop personalized recommendation systems", "application": f"Use AI in {industry}", "benefits": ["Sales: Increased sales", "Marketing: Improved targeting"]},
            {"title": "AI-Powered Supply Chain Optimization", "objective": "Optimize supply chain operations", "application": f"Use AI for inventory management in {industry}", "benefits": ["Operations: Better inventory management", "Finance: Cost reduction"]},
            {"title": "Predictive Maintenance", "objective": "Anticipate equipment failures", "application": f"Use AI to predict maintenance needs in {industry}", "benefits": ["Reduced downtime", "Lower maintenance costs"]},
            {"title": "Chatbot Customer Support", "objective": "Provide instant customer service", "application": f"Use AI chatbots to handle inquiries in {industry}", "benefits": ["Improved customer satisfaction", "Cost-effective support"]},
            {"title": "Fraud Detection", "objective": "Identify and prevent fraudulent activities", "application": f"Use AI to detect anomalies in transactions within {industry}", "benefits": ["Reduced fraud incidents", "Enhanced security"]},
            {"title": "Real-Time Analytics for Decision Making", "objective": "Deliver real-time insights", "application": f"Use AI analytics for faster decisions in {industry}", "benefits": ["Better operational decisions", "Increased agility"]},
            {"title": "Healthcare Diagnosis Support", "objective": "Assist doctors with diagnosis", "application": f"Use AI to analyze patient data in {industry}", "benefits": ["Improved diagnosis accuracy", "Enhanced patient outcomes"]},
            {"title": "Natural Language Processing (NLP) for Text Analysis", "objective": "Analyze and extract insights from text", "application": f"Use AI for processing customer feedback in {industry}", "benefits": ["Customer insights", "Better service offerings"]},
            {"title": "Image Recognition in Retail", "objective": "Identify products or customer preferences", "application": f"Use AI in retail to recognize items", "benefits": ["Improved inventory management", "Enhanced customer experience"]},
            {"title": "Credit Scoring", "objective": "Assess loan risk", "application": f"Use AI to evaluate creditworthiness in {industry}", "benefits": ["Lower default rates", "Better risk management"]},
            {"title": "Personalized Advertising", "objective": "Tailor ads to individual preferences", "application": f"Use AI to target ads based on behavior in {industry}", "benefits": ["Increased ad effectiveness", "Better customer engagement"]},
            {"title": "Smart Inventory Forecasting", "objective": "Predict inventory needs", "application": f"Use AI to forecast stock demand in {industry}", "benefits": ["Reduced overstock", "Minimized stockouts"]},
            {"title": "Employee Training and Skill Assessment", "objective": "Deliver personalized training", "application": f"Use AI to provide learning modules in {industry}", "benefits": ["Better skill development", "Reduced training costs"]},
            {"title": "Autonomous Vehicles for Logistics", "objective": "Automate transportation", "application": f"Use AI to operate delivery drones or vehicles in {industry}", "benefits": ["Lower labor costs", "Faster delivery times"]},
            {"title": "Energy Consumption Optimization", "objective": "Optimize energy use", "application": f"Use AI to manage energy demand in {industry}", "benefits": ["Reduced energy costs", "Sustainable operations"]},
            {"title": "Sentiment Analysis for Social Media", "objective": "Gauge public opinion", "application": f"Use AI to analyze social media mentions in {industry}", "benefits": ["Improved brand reputation", "Better customer relations"]},
            {"title": "Quality Control in Manufacturing", "objective": "Ensure high-quality production", "application": f"Use AI to detect defects in production in {industry}", "benefits": ["Reduced waste", "Consistent product quality"]},
            {"title": "Sales Forecasting", "objective": "Predict future sales trends", "application": f"Use AI for accurate sales forecasting in {industry}", "benefits": ["Optimized inventory", "Enhanced budgeting"]},
            {"title": "Cybersecurity Threat Detection", "objective": "Identify potential threats", "application": f"Use AI to protect data in {industry}", "benefits": ["Improved data security", "Faster threat response"]},
            {"title": "Virtual Shopping Assistants", "objective": "Enhance customer shopping experience", "application": f"Use AI to assist online shoppers in {industry}", "benefits": ["Better customer engagement", "Increased conversions"]}
        ]
        
        # Append each use case to the use_cases list
        for case in use_cases_data:
            use_cases.append(case)
        return use_cases


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

                # Display use cases
                st.subheader("Generated Use Cases")
                for i, case in enumerate(use_cases, start=1):
                    st.write(f"### Use Case {i}: {case['title']}")
                    st.write(f"**Objective:** {case['objective']}")
                    st.write(f"**Application:** {case['application']}")
                    st.write("**Benefits:**")
                    for benefit in case['benefits']:
                        st.write(f"- {benefit}")

        else:
            st.error("Please enter both API Key and Industry Name")

if __name__ == "__main__":
    main()
