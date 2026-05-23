class Idea:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.tags = [] # This will be populated by the 'AI' part

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nTags: {', '.join(self.tags) if self.tags else 'None'}\n"

ideas = []

# This dictionary simulates a knowledge base for categorization.
# In a real AI system, this would be learned from large datasets.
CATEGORY_KEYWORDS = {
    "AI/ML": ["yapay zeka", "makine öğrenimi", "derin öğrenme", "nlp", "model", "algoritma", "veri bilimi", "tahmin", "öğrenme"],
    "Web Development": ["web", "frontend", "backend", "api", "javascript", "python", "django", "flask", "react", "angular", "vue", "html", "css"],
    "Mobile Development": ["mobil", "android", "ios", "swift", "kotlin", "react native", "flutter"],
    "Data Science": ["veri", "analiz", "istatistik", "görselleştirme", "büyük veri", "sql", "nosql", "pandalar"],
    "IoT": ["nesnelerin interneti", "sensör", "cihaz", "bağlantı", "akıllı ev"],
    "Blockchain": ["blokzincir", "kripto", "ethereum", "bitcoin", "akıllı sözleşme"]
}

def analyze_idea_and_suggest_tags(idea_description):
    """
    Simulates an AI feature that analyzes an idea description
    and suggests relevant tags/categories based on keywords.
    This is a simple rule-based system, mimicking the concept of
    adding 'smart' features to an existing application.
    """
    suggested_tags = set()
    description_lower = idea_description.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in description_lower:
                suggested_tags.add(category)
                break # Move to the next category once a match is found

    # Add a generic "Hackathon" tag if no specific categories are found.
    if not suggested_tags:
        suggested_tags.add("General Project")
    
    # Add a "Productivity" tag if keywords related to efficiency or workspace are present.
    if any(k in description_lower for k in ["verimlilik", "otomasyon", "çalışma alanı", "asistan", "yardımcı"]):
        suggested_tags.add("Productivity")

    return list(suggested_tags)

def add_new_idea():
    title = input("Enter idea title: ")
    description = input("Enter idea description: ")
    
    new_idea = Idea(title, description)
    
    # --- This is where the AI transformation happens ---
    # The 'AI-like' function analyzes the new idea and automatically assigns tags.
    print("\nAnalyzing idea with AI-like features...")
    suggested_tags = analyze_idea_and_suggest_tags(new_idea.description)
    new_idea.tags = suggested_tags
    print(f"AI suggested tags: {', '.join(suggested_tags)}")
    
    ideas.append(new_idea)
    print("Idea added successfully!")

def list_ideas():
    if not ideas:
        print("No ideas yet. Add some!")
        return
    print("\n--- All Ideas ---")
    for i, idea in enumerate(ideas):
        print(f"Idea {i+1}:")
        print(idea)
        print("-" * 20)

def main_menu():
    while True:
        print("\n--- AI-Powered Idea Workspace ---")
        print("1. Add New Idea")
        print("2. List All Ideas")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_idea()
        elif choice == '2':
            list_ideas()
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
