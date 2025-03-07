import os
import pandas as pd
import chardet
from crewai import Crew, Task, Agent, LLM, Process
from crewai_tools import FileReadTool, CSVSearchTool
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_openai import ChatOpenAI
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
llm = ChatOpenAI(model="gpt-4o",temperature=0)

csv_tool = FileReadTool(file_path='Emp_data.csv')
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## Agents

dataset_inference_agent = Agent(
    role="Dataset Context Specialist",
    goal=(
        "Infer the context and purpose of the dataset by analyzing column names, data types, "
        "and a few sample rows. Extract insights about the domain and the type of data provided."
    ),
    backstory=(
        "An expert in understanding datasets and identifying their purpose. You have a deep understanding of data science, "
        "machine learning, and data analysis."
    ),
    tools=[csv_tool],
    llm=llm,
    verbose=True,
    
)

data_analysis_agent = Agent(
    role="Data Cleaning Specialist",
    goal=(
        "Analyze the dataset to identify missing values, incorrect data types, and potential outliers. "
        "Generate statistical summaries like mean, median, and correlations between variables."
    ),
    backstory=(
        "Specializes in cleaning and preparing data for analysis with expertise in data cleaning and preprocessing."
    ),
    tools=[csv_tool],
    llm=llm,
    verbose=True
)

visualization_agent = Agent(
    role="Visualization Expert",
    goal=(
        "Generate meaningful visualizations such as histograms, scatter plots, line plots, bar charts, "
        "and heatmaps to provide insights into the data. Save all visualizations to a 'graphs/' directory."
    ),
    backstory=(
        "Specializes in creating compelling and informative visualizations. You are an expert in Python, pandas, "
        "matplotlib, seaborn, and data visualization, capable of creating impactful data stories."
    ),
    tools=[csv_tool],
    llm=llm,
    verbose=True
    
)

markdown_report_agent = Agent(
    role="Report Specialist",
    goal=(
        "Compile all findings, analysis, and visualizations into a structured markdown report. "
        "Embed graphs and provide clear sections for analysis and summary."
    ),
    backstory="An expert in synthesizing data insights into polished reports.",
    tools=[csv_tool],
    llm=llm,
    verbose=True,
)

## Tasks
dataset_inference_task = Task(
    description="Analyze the dataset to determine its context, purpose, and structure.",
    expected_output="A descriptive overview of the dataset's structure and purpose.",
    agent=dataset_inference_agent
)

data_analysis_task = Task(
    description="Perform a comprehensive analysis of the dataset to identify missing values, incorrect data types, and potential outliers.",
    expected_output="A summary of missing values, standardized data types, and statistical metrics.",
    agent=data_analysis_agent
)

visualization_task = Task(
    description="Generate visualizations dynamically based on the dataset's content.",
    expected_output="A set of annotated graphs saved in the 'graphs/' directory.",
    agent=visualization_agent
)

markdown_report_task = Task(
    description="Create a detailed markdown report summarizing all analysis and visualizations.",
    expected_output="A polished markdown report with embedded graphs and actionable insights.",
    agent=markdown_report_agent,
    context=[dataset_inference_task, data_analysis_task, visualization_task],
    output_file='report.md'
)

csv_analysis_crew = Crew(
    agents=[
        dataset_inference_agent,
        data_analysis_agent,
        visualization_agent,
        markdown_report_agent
    ],
    tasks=[dataset_inference_task, data_analysis_task, visualization_task, markdown_report_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == '__main__':
    result = csv_analysis_crew.kickoff()
    print("Crew Execution Complete. Final report generated.")
    print(result)
