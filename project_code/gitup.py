import subprocess

def push_to_github(repo_path, filename, commit_message, branch_name="main"):
    """
    Pushes a file to GitHub using Git commands and sets the upstream branch.

    Args:
        repo_path (str): Path to the Git repository.
        filename (str): The name of the file to be added and committed.
        commit_message (str): The commit message for the changes.
        branch_name (str, optional): The name of the branch (default is "main").

    Returns:
        str: A message indicating the success or failure of the operation.
    """
    try:
        # Change the working directory to the Git repository path
        subprocess.run(["git", "-C", repo_path, "add", filename])

        # Commit the changes with the provided message
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message])
        
        # Pull request to seek approval
        subprocess.run(["git", "-C", repo_path, "pull", "origin", branch_name])

        # Push the changes to the remote repository and set the upstream branch
        subprocess.run(["git", "-C", repo_path, "push", "--set-upstream", "origin",>
        return "File successfully pushed to GitHub with upstream set!"
    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    repo_path = input("Enter the path to your Git repository: ")
    filename = input("Enter filename: ")
    commit_message = input("Enter commit message: ")
    result = push_to_github(repo_path, filename, commit_message)
    print(result)
