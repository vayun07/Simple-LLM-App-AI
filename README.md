# Simple-LLM-App-AI

<h2 tabindex="-1" class="heading-element" dir="auto">Introduction</h2>
In this ever evolving world of Machine Learning and AI technologies, this article provides as a guide for building a simple Large Language Model (LLM) with Python which revolves about a personal AI personal assistant.

The picture below shows the final output of the app which allows you to enter any text and the model will generate the best possible human language reply.

![image](https://github.com/user-attachments/assets/551dc599-88a5-4fbc-a892-28c25254ab3f)

<h2 tabindex="-1" class="heading-element" dir="auto">Prerequisites</h2>
This includes:

1. Python (3.5+), and background writing Python scripts.

  
2. OpenAI: OpenAI is a research organization and technology company that aims to ensure artificial general intelligence (AGI) benefits all of humanity. One of its key contributions is the development of advanced LLMs such as GPT-3 and GPT-4. These models can understand and generate human-like text, making them powerful tools for various applications like chatbots, content creation, and more.
Sign up for OpenAI and copy your API keys from the API section in your account so that you can access the models.  Install OpenAI on your computer using the command below:

![image](https://github.com/user-attachments/assets/f1c750e4-711d-4f18-8fe6-3c80c84a8863)


4. Streamlit: Streamlit is a powerful and easy-to-use Python library for creating web applications. Streamlit allows you to create interactive web applications using Python alone. You don't need expertise in web development (HTML, CSS, JavaScript) to build functional and visually appealing web apps.
It's beneficial for building machine learning and data science apps, including those that utilize LLMs. Install streamlit on your computer using the command below:

![image](https://github.com/user-attachments/assets/c16d73d9-e52d-4e12-a48a-e535ecd442d3)

Another workaround to install all the dependancies faster would be to create a "requirements.txt" in the same directory of the project and run "pip install -r requirements.txt" to install all the dependancies all at once.

![image](https://github.com/user-attachments/assets/7f847804-17f3-4251-9388-0c038955d675)

<h2 tabindex="-1" class="heading-element" dir="auto">Coding</h2>
Create a python file app.py to add the codes.

Please see below code with the comments for each function:

![image](https://github.com/user-attachments/assets/51c7d0cb-746b-4c73-b2ac-a49b65ed598d)


<h2 tabindex="-1" class="heading-element" dir="auto">Output</h2>
Run the application by running "streamlit run app.py" from the terminal 

AI response:
AI has the potential to revolutionize the world’s future in several profound ways across various domains. Here are some key areas where AI could bring about transformative changes:

Healthcare:

Personalized Medicine: AI can analyze genetic information, lifestyle data, and medical histories to tailor treatments for individuals, leading to more effective healthcare solutions.
Diagnostics: AI algorithms can assist in diagnosing diseases more accurately and quickly than traditional methods, including image recognition for radiology and pathology.
Drug Discovery: AI can significantly shorten the time required to discover new drugs and develop treatments by simulating interactions at a molecular level.
Education:

Personalized Learning: AI can create adaptive learning systems that cater to the individual needs and pace of students, making education more effective.
Automation of Administrative Tasks: Educators can use AI to automate grading and administrative duties, freeing up time for teaching and student interaction.
Transportation:

Autonomous Vehicles: AI will drive the development of self-driving cars, which could enhance road safety, reduce traffic congestion, and lower transportation costs.
Optimized Logistics: AI can optimize supply chains, improving efficiency in the transport of goods, which can lead to reduced environmental impact and cost savings.
Work and Productivity:

Automation of Routine Tasks: AI can take over repetitive tasks, allowing humans to focus on higher-level thinking and creative work. This can lead to increased productivity and innovation.
Enhanced Decision-Making: AI can process vast amounts of data to provide insights and predictions, supporting better decision-making in business and government.
Sustainability and Environment:

Resource Management: AI can improve the management of natural resources, optimize energy consumption, and help in monitoring and mitigating environmental impacts.
Climate Modeling: AI can enhance climate modeling and predictions, helping to combat climate change by informing policies and strategies.
Economic Transformation:

New Business Models: AI can enable innovative business models and services, creating new markets and opportunities.
Job Creation: While there will be job displacement in some sectors, AI is also expected to create new jobs, particularly in tech, maintenance, and sectors that involve human-AI collaboration.
Governance and Public Policy:

Data-Driven Policy Making: AI can analyze data to inform public policy decisions, improving governance and resource allocation.
Fraud Detection: AI can help identify fraudulent activities in finance, taxation, and even voting processes, enhancing integrity and trust in systems.
Social Dynamics:

Enhanced Connectivity: AI can power communication tools, making it easier for individuals to connect and collaborate across geographical divides.
Inclusion: AI can assist in breaking down barriers for people with disabilities, providing tools and technologies that enhance accessibility.
Scientific Research:

Accelerated Discovery: AI can analyze complex datasets, leading to faster advancements in science and technology by identifying patterns and making connections that would be difficult for humans to discern.
Ethics and Society:

Addressing Ethical Challenges: The evolution of AI will spark discussions about ethics in technology, necessitating frameworks to ensure responsible use of AI, addressing bias, privacy, and accountability.
While the potential of AI is vast, it also poses challenges and risks, including ethical concerns, issues of bias and fairness, job displacement, and the need for robust regulatory frameworks. The way society navigates these challenges will significantly influence how AI shapes our future. Proper governance, education, and collaboration will be essential in harnessing AI's benefits while mitigating its risks.

![image](https://github.com/user-attachments/assets/ddb1a65d-8b6b-4f83-8889-8564ca72b3a9)

![image](https://github.com/user-attachments/assets/adea5c27-698a-436d-8417-da5ff0c95a67)

![image](https://github.com/user-attachments/assets/3332eecd-eb1c-4161-ab3e-bfd3069f8607)

<h2 tabindex="-1" class="heading-element" dir="auto">Conclusion</h2>
This AI model generated a human like response with a high accuracy throught the gpt-4o-mini model. Further frameworks like Langchain or HuggingFace can be explored to assess the behaviour of the AI models and build more sophisticated apps.
