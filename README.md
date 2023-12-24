# Python Ebook Generator with OpenAI API

## Introduction
This project is a Python script that generates Ebooks utilizing the OpenAI APIs.

## Prerequisites
- Python 3.10.4
- Installed packages: [openai, python-docx].

## Installation
To set up and run the project:

1. Download the project files and navigate to the project directory.
   ```
   cd create-my-own-e-book
   ```
2. Install the required packages:
   ```
   pip install openai
   pip install python-docx 
   ```

3. Run the main Python script.
   ```python
   python main.py
   ```

## Usage
Executing the Python script will prompt you to enter the book title and the word count for each content item. The script will interact with OpenAI's APIs to generate your book content.

You can start the script with the following command:
```bash
$ python main.py
Enter the book title: Kubernetes
Enter the word count for each content item: 400

Content List:

- Introduction to Kubernetes
- Overview of containerization and orchestration
- Installation and setup of Kubernetes
- Understanding Kubernetes architecture
- Working with Pods, Deployments, and Replication Controllers
- Managing and scaling applications with Kubernetes
- Service discovery and load balancing in Kubernetes
- Configuring networking and storage in Kubernetes
- Monitoring and logging in Kubernetes
- Securing applications and cluster in Kubernetes
- Integrating Kubernetes with CI/CD pipelines
- Advanced topics: Custom Resource Definitions, Operators, and Controllers
- Troubleshooting common issues in Kubernetes
- Best practices for deploying applications on Kubernetes
- Case studies and real-world examples of Kubernetes usage

Are you satisfied with the content list? (yes[Generate the book]/no[Regenerate the list]): yes
Book generated successfully in MS Word with the filename 'Kubernetes.docx'.
```

### Important Notes
- Don't forget to specify and export your `OPENAI_API_KEY` Environment variable.
- The script supports GPT-3.5/4 Turbo Models. Legacy davinci Models won't work.
- If you specify a word limit, it will increase the token count, which might add a few cents to the cost, but it's all in good fun! 😁
