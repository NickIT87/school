import requests

# Base URL for JSONPlaceholder
base_url = "https://jsonplaceholder.typicode.com"

def get_posts():
    """
    Function to fetch posts from JSONPlaceholder.
    """
    # Endpoint for fetching posts
    endpoint = "/posts"
    
    # URL for getting posts
    url = base_url + endpoint
    
    # Sending GET request
    response = requests.get(url)
    
    # Checking if request was successful (status code 200)
    if response.status_code == 200:
        # Parsing response JSON
        posts = response.json()
        print(posts)
        # Printing fetched posts
        for post in posts:
            print(f"Post {post['id']}: {post['title']}")
    else:
        print("Failed to fetch posts.")
    
    

if __name__ == "__main__":
    # Call the function to get posts
    get_posts()
