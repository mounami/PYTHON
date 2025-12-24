import requests
print("Random quote generator\n")

def generate_quote():
    """Generate a random quote"""
    url = "https://api.quotable.io/random"

    try:
        response= requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"❌ Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    
def display_quote(data):
    if data is None:
        return
    
    content = data["content"]
    author = data["author"]
    print(f"\n{'='*40}")
    print(f'"{content}"')
    print(f" - {author}")
    print(f"{'='*40}\n")

while True:
    input("Press Enter to generate a random quote (or ctrl+c to exit): ")

    data = generate_quote()
    display_quote(data)