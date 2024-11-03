import streamlit as st
import requests
import json

# Class for fetching industry data
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


# Class for generating a variety of use cases dynamically
class UseCaseAgent:
    def generate_use_cases(self, company_info, company_name, focus_areas=None):
        use_cases = []

        if company_info and 'organic' in company_info and len(company_info['organic']) > 0:
            industry_info = company_info['organic'][0]['snippet']
        else:
            industry_info = f"{company_name}'s industry"

        if not focus_areas:
            focus_areas = ["customer experience", "supply chain", "predictive maintenance", "cybersecurity", 
                           "HR management", "financial forecasting", "product development", "marketing optimization", 
                           "environmental impact", "quality control"]

        # Use cases based on different functional areas
        for focus in focus_areas:
            if "customer experience" in focus:
                use_cases.append({
                    "title": "Personalized Customer Experience",
                    "objective": f"Enhance customer satisfaction for {company_name}.",
                    "application": f"Use AI to analyze customer preferences and deliver personalized interactions in {industry_info}.",
                    "benefits": ["Improved customer satisfaction", "Higher retention rates", "Increased revenue"]
                })

            if "supply chain" in focus:
                use_cases.append({
                    "title": "AI-Driven Supply Chain Optimization",
                    "objective": "Optimize supply chain and logistics.",
                    "application": f"Using AI to forecast demand, manage inventory, and optimize routes in {industry_info}.",
                    "benefits": ["Cost savings", "Improved efficiency", "Reduced waste"]
                })

            if "predictive maintenance" in focus:
                use_cases.append({
                    "title": "Predictive Maintenance",
                    "objective": "Reduce equipment downtime through AI-driven maintenance predictions.",
                    "application": f"Analyze sensor data to predict and schedule maintenance in {industry_info}.",
                    "benefits": ["Reduced downtime", "Lower maintenance costs", "Extended asset lifespan"]
                })

            if "cybersecurity" in focus:
                use_cases.append({
                    "title": "Enhanced Cybersecurity Measures",
                    "objective": "Strengthen data security and prevent cyber attacks.",
                    "application": f"Using AI to detect anomalies and potential threats in {industry_info}.",
                    "benefits": ["Improved security", "Reduced risk of data breaches", "Enhanced trust"]
                })

            if "HR management" in focus:
                use_cases.append({
                    "title": "AI-Driven HR Management",
                    "objective": "Optimize talent acquisition and employee engagement.",
                    "application": f"Using AI to screen resumes, predict employee turnover, and personalize engagement strategies in {industry_info}.",
                    "benefits": ["Better talent acquisition", "Increased employee satisfaction", "Lower turnover"]
                })

            if "financial forecasting" in focus:
                use_cases.append({
                    "title": "Financial Forecasting and Risk Analysis",
                    "objective": "Enhance financial forecasting accuracy and risk management.",
                    "application": f"Using AI for predictive financial modeling, risk assessments, and fraud detection in {industry_info}.",
                    "benefits": ["Improved financial planning", "Reduced risk", "Enhanced decision-making"]
                })

            if "product development" in focus:
                use_cases.append({
                    "title": "Product Development and Innovation",
                    "objective": "Accelerate product development with AI insights.",
                    "application": f"Using AI to identify market trends, optimize product features, and streamline R&D in {industry_info}.",
                    "benefits": ["Faster time-to-market", "Improved product-market fit", "Competitive advantage"]
                })

            if "marketing optimization" in focus:
                use_cases.append({
                    "title": "Targeted Marketing and Customer Insights",
                    "objective": "Refine marketing strategies for higher conversion rates.",
                    "application": f"Using AI for customer segmentation, personalized campaigns, and sentiment analysis in {industry_info}.",
                    "benefits": ["Improved targeting", "Higher ROI on marketing spend", "Enhanced customer loyalty"]
                })

            if "environmental impact" in focus:
                use_cases.append({
                    "title": "Environmental Impact Reduction",
                    "objective": "Leverage AI to reduce environmental footprint.",
                    "application": f"Using AI to monitor emissions, optimize resource use, and manage waste in {industry_info}.",
                    "benefits": ["Lower carbon footprint", "Cost savings from efficiency", "Enhanced corporate social responsibility"]
                })

            if "quality control" in focus:
                use_cases.append({
                    "title": "Automated Quality Control",
                    "objective": "Improve quality control in production processes.",
                    "application": f"Using AI for defect detection, quality assurance, and process optimization in {industry_info}.",
                    "benefits": ["Consistent product quality", "Reduced waste", "Increased customer satisfaction"]
                })

        return use_cases


# Streamlit interface
def main():
    st.title("AI and ML Use Cases Generator")

    api_key = st.text_input("Enter API Key:")
    company_name = st.text_input("Enter Company Name:")
    industry = st.text_input("Enter Industry Name:")
    focus_areas = st.multiselect("Select Focus Areas", 
                                 ["customer experience", "supply chain", "predictive maintenance", "cybersecurity", 
                                  "HR management", "financial forecasting", "product development", "marketing optimization", 
                                  "environmental impact", "quality control"])

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
