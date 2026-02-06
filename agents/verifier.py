def verify_and_format(results: list):
    final_output = {}
    errors = []

    for item in results:
        if "error" in item:
            errors.append(item)
            continue

        tool = item.get("tool")
        output = item.get("output")

        if tool == "github":
            final_output["github_repositories"] = output

        elif tool == "weather":
            final_output["weather"] = output

    if errors:
        final_output["errors"] = errors

    return final_output
