import requests
import json
from fpdf2 import FPDF
import os


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
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve industry information. Response: {response.text}")
            return None


class UseCaseAgent:
    def generate_use_cases(self, industry_info):
        use_cases = []
        industry = industry_info['organic'][0]['snippet'] if industry_info else 'the industry'
        
        # A comprehensive set of use cases tailored for Apple Inc.
        use_cases_data = [
            {
                "title": "Personalized Customer Experience",
                "objective": "Develop personalized recommendation systems that analyze user behavior.",
                "application": f"Use AI to suggest products and services based on user preferences in {industry}.",
                "cross_functional_benefits": [
                    "Sales: Increased sales through personalized offerings.",
                    "Marketing: Improved targeting and campaign effectiveness.",
                    "Customer Support: Enhanced user satisfaction."
                ]
            },
            {
                "title": "AI-Powered Supply Chain Optimization",
                "objective": "Optimize supply chain operations to reduce costs and improve efficiency.",
                "application": f"Utilize AI algorithms to forecast demand and manage inventory levels for {industry}.",
                "cross_functional_benefits": [
                    "Operations: Better inventory management.",
                    "Finance: Reduced costs and improved cash flow.",
                    "Logistics: Enhanced delivery performance."
                ]
            },
            {
                "title": "Dynamic Pricing Strategies",
                "objective": "Implement dynamic pricing models based on market trends and demand.",
                "application": f"Use AI to adjust prices in real-time, maximizing revenue in {industry}.",
                "cross_functional_benefits": [
                    "Finance: Improved revenue management.",
                    "Marketing: Better alignment with market conditions.",
                    "Sales: Increased competitiveness."
                ]
            },
            {
                "title": "Enhanced Product Development",
                "objective": "Accelerate innovation in product design using AI.",
                "application": f"Leverage generative design algorithms to create new product concepts in {industry}.",
                "cross_functional_benefits": [
                    "R&D: Faster time-to-market.",
                    "Engineering: Improved design efficiency.",
                    "Marketing: Unique product offerings."
                ]
            },
            {
                "title": "AI-Driven Customer Support",
                "objective": "Provide instant customer support using AI chatbots.",
                "application": f"Implement AI-driven chatbots for handling customer inquiries and troubleshooting in {industry}.",
                "cross_functional_benefits": [
                    "Customer Service: 24/7 support availability.",
                    "Sales: Increased lead generation through automated interactions.",
                    "IT: Reduced workload on human agents."
                ]
            },
            {
                "title": "Predictive Maintenance for Equipment",
                "objective": "Reduce equipment downtime through predictive maintenance.",
                "application": f"Use machine learning to analyze equipment data and predict failures in manufacturing facilities.",
                "cross_functional_benefits": [
                    "Operations: Minimizes unplanned downtime.",
                    "Finance: Reduces maintenance costs.",
                    "Supply Chain: Ensures timely production schedules."
                ]
            },
            {
                "title": "AI-Enhanced Market Trend Analysis",
                "objective": "Analyze market data to identify emerging trends.",
                "application": f"Deploy AI models to interpret consumer behavior and market dynamics in {industry}.",
                "cross_functional_benefits": [
                    "Strategic Planning: Informs long-term business strategies.",
                    "R&D: Guides innovation efforts.",
                    "Sales: Identifies new opportunities."
                ]
            },
            {
                "title": "Augmented Reality (AR) Experiences",
                "objective": "Create immersive customer experiences through AR.",
                "application": f"Use AI to enhance AR applications for product visualization and user engagement in {industry}.",
                "cross_functional_benefits": [
                    "Marketing: Increased engagement and brand loyalty.",
                    "Sales: Enhanced customer interaction.",
                    "Product Development: Insights into user preferences."
                ]
            },
            {
                "title": "Automated Document Processing",
                "objective": "Streamline processing of contracts and legal documents.",
                "application": f"Implement AI systems to extract and analyze key information from documents in {industry}.",
                "cross_functional_benefits": [
                    "Legal: Improved compliance and risk management.",
                    "Procurement: Faster supplier onboarding.",
                    "Finance: Enhanced accuracy in financial reporting."
                ]
            },
            {
                "title": "AI-Based Fraud Detection",
                "objective": "Identify and prevent fraudulent activities in transactions.",
                "application": f"Use AI to analyze transaction patterns and detect anomalies in {industry}.",
                "cross_functional_benefits": [
                    "Finance: Reduces financial losses due to fraud.",
                    "Risk Management: Enhances security measures.",
                    "Customer Trust: Builds confidence in services."
                ]
            },
            {
                "title": "Smart Inventory Management",
                "objective": "Optimize inventory levels with AI-driven insights.",
                "application": f"Utilize AI to forecast inventory needs based on sales data in {industry}.",
                "cross_functional_benefits": [
                    "Operations: Reduces holding costs.",
                    "Sales: Avoids stockouts and backorders.",
                    "Finance: Improves cash flow management."
                ]
            },
            {
                "title": "Employee Productivity Analytics",
                "objective": "Enhance workforce productivity using AI analytics.",
                "application": f"Analyze employee performance data to identify areas for improvement in {industry}.",
                "cross_functional_benefits": [
                    "HR: Improves training and development programs.",
                    "Management: Informs leadership decisions.",
                    "Finance: Reduces costs associated with inefficiencies."
                ]
            },
            {
                "title": "AI-Driven Environmental Impact Monitoring",
                "objective": "Monitor and reduce environmental impact through AI analytics.",
                "application": f"Use AI to track emissions and waste in manufacturing processes in {industry}.",
                "cross_functional_benefits": [
                    "Compliance: Meets regulatory requirements.",
                    "Sustainability: Enhances corporate responsibility initiatives.",
                    "Public Relations: Improves brand image."
                ]
            },
            {
                "title": "Virtual Reality (VR) Training Programs",
                "objective": "Improve employee training using VR and AI.",
                "application": f"Develop VR training modules for skills development in {industry}.",
                "cross_functional_benefits": [
                    "HR: Reduces training time and costs.",
                    "Operations: Ensures safety and efficiency.",
                    "Employee Engagement: Increases retention through innovative training."
                ]
            },
            {
                "title": "Intelligent Risk Management Systems",
                "objective": "Proactively manage risks with AI analytics.",
                "application": f"Implement AI systems to analyze risk factors and provide mitigation strategies in {industry}.",
                "cross_functional_benefits": [
                    "Risk Management: Enhances decision-making.",
                    "Finance: Minimizes potential financial impacts.",
                    "Operations: Improves overall resilience."
                ]
            },
            {
                "title": "Customer Sentiment Analysis",
                "objective": "Gauge customer sentiment through AI analytics.",
                "application": f"Use natural language processing to analyze customer feedback and reviews in {industry}.",
                "cross_functional_benefits": [
                    "Marketing: Informs product development.",
                    "Customer Service: Enhances support strategies.",
                    "Sales: Improves customer relationships."
                ]
            }
        ]

        # Add the use cases to the list
        for case_data in use_cases_data:
            use_cases.append(case_data)

        return use_cases


class PDFReport(FPDF):
    def __init__(self):
        super().__init__()
        self.use_case_number = 1  # Initialize the use case number

    def header(self):
        if self.page_no() == 1:  # Show header only on the first page
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'AI and ML Use Cases for Apple Inc.', 0, 1, 'C')
            self.ln(10)

    def add_use_case(self, use_case):
        # Add the use case number
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, f"Use Case {self.use_case_number}: {use_case['title']}", 0, 1)
        self.use_case_number += 1  # Increment use case number for each new use case
        
        self.set_font('Arial', '', 10)
        self.cell(0, 10, "Objective/Use Case:", 0, 1)
        self.multi_cell(0, 10, use_case["objective"])
        
        self.cell(0, 10, "AI Application:", 0, 1)
        self.multi_cell(0, 10, use_case["application"])
        
        self.cell(0, 10, "Cross-Functional Benefits:", 0, 1)
        for benefit in use_case["cross_functional_benefits"]:
            self.multi_cell(0, 10, f"  - {benefit}")
        self.ln(10)


def main():
    api_key = 'd1964ac11e1a10b92815bbac45b44dc8d7af7024'  # Replace with your actual API key
    industry = "Apple Inc."  # Updated to focus on Apple Inc.

    research_agent = ResearchAgent(api_key)
    industry_info = research_agent.search_industry_info(industry)

    if industry_info:
        use_case_agent = UseCaseAgent()
        use_cases = use_case_agent.generate_use_cases(industry_info)
        
        print("Generated Use Cases:")
        for case in use_cases:
            print(f"- {case['title']}")
    
    # Define PDF path and ensure directory exists
    pdf_file_path = r'C:\Users\Home-PC\Downloads\AI_Planet_Assignment\Report.pdf'
    pdf_dir = os.path.dirname(pdf_file_path)
    os.makedirs(pdf_dir, exist_ok=True)  # Create directory if it does not exist
    
    # Create PDF
    pdf = PDFReport()
    pdf.add_page()
    
    # Adding use cases to PDF
    for case in use_cases:
        pdf.add_use_case(case)
    
    # Save PDF
    pdf.output(pdf_file_path)
    print(f"PDF saved as {pdf_file_path}")

if __name__ == "__main__":
    main()
