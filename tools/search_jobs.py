import sys
import random
import time

def search_jobs(query):
    print(f"Searching for '{query}' jobs...")
    time.sleep(1.5) # Simulate network delay

    # Mock Data Generation based on query
    titles = [f"Junior {query} Developer", f"Senior {query} Engineer", f"{query} Specialist", f"Lead {query} Architect", f"{query} Intern"]
    companies = ["TechCorp", "InnovateX", "GlobalSystems", "StartUpOne", "FutureNet"]
    
    results = []
    for _ in range(random.randint(3, 6)):
        title = random.choice(titles)
        company = random.choice(companies)
        gpa = round(random.uniform(2.5, 3.8), 2)
        results.append(f"{title}|{company}|{gpa}")

    # Save to file
    with open("search_results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")
    
    print(f"Found {len(results)} jobs. Saved to search_results.txt.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_jobs.py <query>")
    else:
        search_jobs(sys.argv[1])
