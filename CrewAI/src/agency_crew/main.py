"""
Agency Supervisor - Main Entry Point
Chat with 150+ specialized agents via supervisor
"""

import os
from dotenv import load_dotenv
from crew import AgencySupervisorCrew

load_dotenv()


def main():
    print("=" * 60)
    print("  Agency Supervisor - 150+ Agents at Your Service")
    print("=" * 60)
    print()
    print("Available Specialists:")
    print("  - Engineering: Frontend, Backend, AI, Data, DevOps, Security")
    print("  - Design: UI/UX, Visual Design")
    print("  - Marketing: Content, SEO, Growth")
    print("  - Testing: QA, Performance, Accessibility")
    print("  - And 140+ more from agency-agents repo!")
    print()
    print("Type 'exit' to quit")
    print("=" * 60)
    print()

    crew = AgencySupervisorCrew()

    while True:
        task = input("\nWhat would you like help with?\n> ").strip()

        if task.lower() in ["exit", "quit", "q"]:
            print("\nGoodbye!")
            break

        if not task:
            continue

        print("\n[Supervisor is delegating to specialists...]\n")

        try:
            result = crew.kickoff(task)
            print("\n" + "=" * 60)
            print("  RESULT")
            print("=" * 60)
            print(result)
        except Exception as e:
            print(f"\nError: {e}")
            print("Trying again...")


if __name__ == "__main__":
    main()
