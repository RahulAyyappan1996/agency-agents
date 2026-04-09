"""
Agency Supervisor Crew
A hierarchical crew where supervisor delegates to specialists
"""

import os
from crewai import Crew, Agent, Task, Process
from crewai.project import CrewBase, agent, crew, task

# Import agent personas from markdown files
AGENT_PERSONAS = {
    "frontend_dev": """
You are Frontend Developer - an expert frontend developer specializing in modern web technologies.

Your specialty:
- React, Vue, Angular, Svelte
- Pixel-perfect UI implementation
- Core Web Vitals optimization
- Responsive, accessible web apps

When asked to build, you deliver production-ready code with tests.
""",
    "backend_dev": """
You are Backend Architect - an expert in server-side systems.

Your specialty:
- API design (REST, GraphQL)
- Database architecture (PostgreSQL, MongoDB)
- Microservices
- Cloud infrastructure

When asked to build, you deliver scalable, secure backend systems.
""",
    "ai_engineer": """
You are AI Engineer - an expert in machine learning and AI systems.

Your specialty:
- ML model development and training
- Model deployment (TensorFlow, PyTorch)
- AI integration pipelines
- Data preprocessing

When asked, you build production ML systems.
""",
    "data_engineer": """
You are Data Engineer - an expert in data infrastructure.

Your specialty:
- ETL/ELT pipelines
- Data lakes and warehouses
- Apache Spark, Airflow
- Real-time streaming (Kafka)

When asked, you build reliable data pipelines.
""",
    "security_engineer": """
You are Security Engineer - an expert in application security.

Your specialty:
- Threat modeling
- Secure code review
- Vulnerability assessment
- Security architecture

When asked, you find and fix security issues.
""",
    "devops": """
You are DevOps Automator - an expert in CI/CD and infrastructure.

Your specialty:
- Kubernetes, Docker
- Terraform, CloudFormation
- CI/CD pipelines (GitHub Actions, Jenkins)
- Monitoring (Prometheus, Grafana)

When asked, you automate infrastructure.
""",
    "qa_engineer": """
You are QA Engineer - an expert in quality assurance.

Your specialty:
- Test automation (Selenium, Playwright)
- Performance testing (k6, JMeter)
- API testing
- Accessibility (WCAG)

When asked, you ensure quality.
""",
    "ui_designer": """
You are UI Designer - an expert in visual design.

Your specialty:
- Design systems
- Component libraries
- Figma to code
- Brand consistency

When asked, you create beautiful designs.
""",
    "content_creator": """
You are Content Creator - an expert in content strategy.

Your specialty:
- Copywriting
- Multi-platform content
- SEO optimization
- Brand storytelling

When asked, you create engaging content.
""",
}


@CrewBase
class AgencySupervisorCrew:
    """Supervisor crew that delegates to specialists"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def supervisor(self):
        return Agent(
            role="Agency Supervisor",
            goal="Coordinate and delegate tasks to the right specialist",
            backstory="""
                You are the Agency Supervisor - a highly intelligent coordinator managing a team of 
                specialized agents. You understand requests fully and delegate to the perfect specialist.
                You NEVER do the work yourself - you orchestrate the specialists.
                
                Your specialists include:
                - Frontend Developer, Backend Architect, AI Engineer
                - Data Engineer, Security Engineer, DevOps
                - QA Engineer, UI Designer, Content Creator
                
                Route tasks to the right specialist based on their expertise.
            """,
            verbose=True,
            allow_delegation=True,
            llm={
                "provider": "gemini",
                "model": "gemini-2.5-flash",
                "api_key": os.getenv("GEMINI_API_KEY"),
            },
        )

    @agent
    def frontend_dev(self):
        return Agent(
            role="Frontend Developer",
            goal="Build responsive, accessible web applications",
            backstory=AGENT_PERSONAS["frontend_dev"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "groq",
                "model": "llama-3.3-70b-versatile",
                "api_key": os.getenv("GROQ_API_KEY"),
            },
        )

    @agent
    def backend_dev(self):
        return Agent(
            role="Backend Architect",
            goal="Design scalable APIs and database systems",
            backstory=AGENT_PERSONAS["backend_dev"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "groq",
                "model": "llama-3.3-70b-versatile",
                "api_key": os.getenv("GROQ_API_KEY"),
            },
        )

    @agent
    def ai_engineer(self):
        return Agent(
            role="AI Engineer",
            goal="Build and deploy machine learning models",
            backstory=AGENT_PERSONAS["ai_engineer"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "gemini",
                "model": "gemini-2.5-flash",
                "api_key": os.getenv("GEMINI_API_KEY"),
            },
        )

    @agent
    def data_engineer(self):
        return Agent(
            role="Data Engineer",
            goal="Build reliable data pipelines and ETL systems",
            backstory=AGENT_PERSONAS["data_engineer"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "groq",
                "model": "llama-3.3-70b-versatile",
                "api_key": os.getenv("GROQ_API_KEY"),
            },
        )

    @agent
    def security_engineer(self):
        return Agent(
            role="Security Engineer",
            goal="Identify vulnerabilities and implement secure systems",
            backstory=AGENT_PERSONAS["security_engineer"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "gemini",
                "model": "gemini-2.5-flash",
                "api_key": os.getenv("GEMINI_API_KEY"),
            },
        )

    @agent
    def devops(self):
        return Agent(
            role="DevOps Automator",
            goal="Build CI/CD pipelines and infrastructure automation",
            backstory=AGENT_PERSONAS["devops"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "groq",
                "model": "llama-3.3-70b-versatile",
                "api_key": os.getenv("GROQ_API_KEY"),
            },
        )

    @agent
    def qa_engineer(self):
        return Agent(
            role="QA Engineer",
            goal="Ensure quality through comprehensive testing",
            backstory=AGENT_PERSONAS["qa_engineer"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "groq",
                "model": "llama-3.3-70b-versatile",
                "api_key": os.getenv("GROQ_API_KEY"),
            },
        )

    @agent
    def ui_designer(self):
        return Agent(
            role="UI Designer",
            goal="Create beautiful, user-centric interfaces",
            backstory=AGENT_PERSONAS["ui_designer"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "gemini",
                "model": "gemini-2.5-flash",
                "api_key": os.getenv("GEMINI_API_KEY"),
            },
        )

    @agent
    def content_creator(self):
        return Agent(
            role="Content Creator",
            goal="Produce engaging, multi-platform content",
            backstory=AGENT_PERSONAS["content_creator"],
            verbose=True,
            allow_delegation=False,
            llm={
                "provider": "groq",
                "model": "llama-3.3-70b-versatile",
                "api_key": os.getenv("GROQ_API_KEY"),
            },
        )

    @crew
    def crew(self):
        return Crew(
            agents=[
                self.supervisor(),
                self.frontend_dev(),
                self.backend_dev(),
                self.ai_engineer(),
                self.data_engineer(),
                self.security_engineer(),
                self.devops(),
                self.qa_engineer(),
                self.ui_designer(),
                self.content_creator(),
            ],
            tasks=[],
            process=Process.hierarchical,  # Supervisor delegates
            manager_agent=self.supervisor(),
            verbose=True,
        )

    def kickoff(self, task):
        """Execute with a task"""
        coordination_task = Task(
            description=f"""
                Coordinate the following request by delegating to the right specialist(s):
                
                {task}
                
                Steps:
                1. Understand the request fully
                2. Identify the best specialist(s)
                3. Delegate with clear instructions
                4. Collect and synthesize results
                5. Present final response
            """,
            agent=self.supervisor(),
            expected_output="Complete, coordinated response from specialists",
        )

        crew = self.crew()
        crew.tasks = [coordination_task]
        return crew.kickoff()
