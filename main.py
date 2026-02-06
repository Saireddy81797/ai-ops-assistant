from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_and_format
import json


def main():
    print("=== AI Operations Assistant ===")
    user_input = input("Enter your task: ")

    print("\n[1] Planning...")
    plan = create_plan(user_input)
    print(json.dumps(plan, indent=2))

    print("\n[2] Executing...")
    execution_results = execute_plan(plan)

    print("\n[3] Verifying...")
    final_output = verify_and_format(execution_results)

    print("\n=== FINAL OUTPUT ===")
    print(json.dumps(final_output, indent=2))


if __name__ == "__main__":
    main()

