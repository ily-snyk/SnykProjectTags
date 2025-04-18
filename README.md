
# Extract Snyk Project Tags

This script retrieves all projects and their associated tags from a specified Snyk organization using the Snyk REST API.

## Features
- ✅ Fetches all projects within a given Snyk organization.
- ✅ Extracts and lists tags for each project.
- ✅ Handles API pagination to retrieve all projects.
- ✅ Uses environment variables for authentication (improves security).
- ✅ Outputs structured JSON for easy parsing.
- ✅ Includes error handling and logging.

## Prerequisites
- Python 3.x installed.
- A valid **Snyk API token**.
- Your **Snyk organization ID**.

## Installation
1. Clone this repository or download the script.
2. Install required dependencies (if needed):
   ```sh
   pip install requests
   ```

## Usage
1. Set environment variables for authentication:
   ```sh
   export SNYK_ORG_ID="your-organization-id"
   export SNYK_API_TOKEN="your-api-token"
   ```

2. Run the script:
   ```sh
   python extract_snyk_tags.py
   ```

## Output
The script prints all projects and their associated tags in JSON format:
```json
{
  "Project A": ["tag1", "tag2"],
  "Project B": [],
  "Project C": ["tag3"]
}
```

## Error Handling
- Logs errors instead of printing them.
- Handles API request failures and JSON decoding errors gracefully.

## Notes
- Ensure your **Snyk API token** has the necessary permissions to access project details.
- If you get an authentication error, verify your API token and organization ID.

## License
This script is provided under the MIT License.

