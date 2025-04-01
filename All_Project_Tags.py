import requests
import json

def extract_all_project_tags(org_id, api_token):
    """
    Retrieves and extracts tags for all projects within a specified Snyk organization.

    This function interacts with the Snyk REST API to fetch project details,
    including associated tags. It handles API pagination to ensure all projects
    are processed, regardless of the number of projects in the organization.

    Args:
        org_id (str): The unique identifier of the Snyk organization.
        api_token (str): The Snyk API token used for authentication.

    Returns:
        dict: A dictionary where keys are project names and values are lists of tags.
              Returns None if an error occurs during API interaction or data processing.
    """

    # Construct the base URL for the Snyk API projects endpoint.
    base_url = f"https://api.snyk.io/rest/orgs/{org_id}/projects?version=2024-10-15"

    # Define the headers required for API authentication and content type.
    headers = {
        "Authorization": f"token {api_token}",
        "Content-Type": "application/json",
    }

    # Initialize an empty dictionary to store project names and their associated tags.
    all_project_tags = {}

    # Initialize the URL for the first API request.
    next_url = base_url

    try:
        # Loop through API pages until all projects are retrieved.
        while next_url:
            # Make an API request to the current URL.
            response = requests.get(next_url, headers=headers)

            # Raise an HTTPError for bad responses (4xx or 5xx status codes).
            response.raise_for_status()

            # Parse the JSON response from the API.
            data = response.json()

            # Check if the response contains project data.
            if "data" in data:
                # Iterate through each project in the data array.
                for project in data["data"]:
                    # Extract the project name from the attributes.
                    project_name = project["attributes"]["name"]

                    # Extract the tags associated with the project, defaulting to an empty list if no tags are present.
                    tags = project["attributes"].get("tags", [])

                    # Store the project name and tags in the dictionary.
                    all_project_tags[project_name] = tags

                # Check if there are more pages of results.
                if "links" in data and "next" in data["links"]:
                    # Construct the full URL for the next page.
                    relative_next_url = data["links"]["next"]
                    next_url = f"https://api.snyk.io{relative_next_url}"
                else:
                    # No more pages, set next_url to None to exit the loop.
                    next_url = None

            else:
                # If the 'data' key is not found, print an error message and return None.
                print("Error: No project data found in API response.")
                return None

    # Handle potential exceptions during the API request or JSON parsing.
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to make API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON response: {e}")
        return None
    except KeyError as e:
        print(f"Error: Missing key in API response: {e}")
        return None

    # Return the dictionary of project names and tags.
    return all_project_tags

# Example usage (replace with your actual org_id and API token):
org_id = "YOUR_ORG_ID" #Very important to replace this string.
api_token = "YOUR_API_TOKEN" #Very important to replace this string.

project_tags = extract_all_project_tags(org_id, api_token)

if project_tags:
    for project_name, tags in project_tags.items():
        print(f"Project: {project_name}")
        if tags:
          print(f"  Tags: {tags}")
        else:
          print("  Tags: []")