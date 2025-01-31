# Detailed Task Checklists for Each Role  
Below are clear, actionable checklists for each role, broken into weekly tasks to ensure we stay on track while following the tutorial.  

---

## 1. Lead Developer  
### **Role Focus:** Core game loop, scene management, integration.  

### **Week 1: Setup and Core Mechanics**  
#### **Set Up Project Environment:**  
• Initialize GitHub repository.  
• Make sure yall niggas understand GitHub.  
• Create initial folder structure.  
• Set up `main.py` with a basic Pygame game loop.  

#### **State Management:**  
• Implement scene/state management (Menu, Gameplay, Game Over).  
• Create placeholder transitions between states (think loading screens).  

#### **Player Movement System:**  
• Develop the **Player** class with movement logic.  
• Handle key inputs (up, down, left, right)-cory kenshin reference.  

#### **Scene Transitions:**  
• Enable smooth transitions between levels and menus.  
• Add basic logic for winning/losing conditions.  

### **Week 2: Polish and Integration**  
#### **Integrate Gameplay Systems:**  
• Merge AI dialogues with gameplay interactions.  
• Ensure NPC interaction triggers work as expected.  

#### **Optimize Code Structure:**  
• Refactor messy code.  
• Ensure reusable functions for transitions and UI updates.  

#### **Testing and Debugging:**  
• Test core mechanics for bugs.  
• Optimize frame rates and resource management.  

#### **Deliverables:**  
• `main.py`  
• Scene/state management logic  
• Optimized core gameplay loop  

---

## 2. AI Integration Specialist  
### **Role Focus:** AI dialogue backend, API/model integration.  

### **Week 1: AI Backend Setup**  
#### **Set Up OpenAI API or Offline Model:**  
• Install necessary libraries (`openai`, `transformers`).  
• Test basic AI API connection.  

#### **Build AI Dialogue Backend:**  
• Write a function to send player inputs to the AI and receive responses.  
• Create fallback dialogue responses for edge cases (NOT EDGING).  

#### **Integrate Dialogue System into Game:**  
• Ensure AI responses display properly in dialogue boxes.  
• Create triggers for AI dialogue events (e.g., approaching an NPC, etc to be decided idfk).  

### **Week 2: Polish and Test**  
#### **Refine Dialogue Prompts:**  
• Adjust prompts for consistent character personalities.  
• Test different player inputs for diverse AI responses.  

#### **Optimize API Calls:**  
• Minimize unnecessary API calls (need to reduce load for shitty pcs).  
• Implement caching if applicable (same reason).  

#### **Handle Edge Cases:**  
• Test AI with invalid inputs (weird shit from ICT grade 9).  
• Create error handling for API failures (try IOErrors lesgo).  

#### **Deliverables:**  
• `ai/ai_engine.py`  
• `ai_prompts.json`  
• Smooth AI dialogue integration  

---

## 3. Gameplay & Dialogue Designer  
### **Role Focus:** Level design, puzzles, scripted interactions.  

### **Week 1: Basic Level and Dialogue Design**  
#### **Level Design (Level 1):**  
• Create the first level (`scenes/level1.py`).  
• Design level layout (e.g., placement of NPCs, triggers, obstacles).  

#### **Script Dialogue JSON:**  
• Write dialogues for at least 2 NPCs in JSON format.  
• Include branching dialogue paths based on player choices.  

#### **Implement NPC Logic:**  
• Add interaction triggers for NPCs.  
• Display pre-written dialogues when interacting.  

### **Week 2: Advanced Level Design**  
#### **Add Gameplay Mechanics:**  
• Design turn-based combat logic (if applicable).  
• Add simple puzzles or quest objectives.  

#### **Expand Dialogue Interactions:**  
• Add more branching paths and outcomes (no nigga word allowed).  
• Ensure dialogue consistency with AI responses.  

#### **Create Additional Levels:**  
• Build `level2.py` and `level3.py`.  
• Ensure smooth transitions between levels.  

#### **Deliverables:**  
• `scenes/level1.py`, `level2.py`, `level3.py`  
• `dialogues/npc1.json`, `npc2.json`, `intro.json`  
• Functional NPC interactions and dialogue flows  

---

## 4. Asset & UI Designer  
### **Role Focus:** Visual design, UI elements, asset integration.  

### **Week 1: Asset Collection and UI Design**  
#### **Collect/Create Assets:**  
• Gather sprites for player, NPCs, and enemies (u can use AI here just make sure its consistent).  
• Find or create background images for levels.  

#### **Design Dialogue Boxes and Menus:**  
• Create a dialogue box design.  
• Design main menu and game over screens.  

#### **Load Assets into the Game:**  
• Ensure all assets are loaded properly in Pygame.  
• Test sprite animations and asset display.  

### **Week 2: Polish Visuals and Add Effects**  
#### **Refine UI Elements:**  
• Add animations for dialogue boxes opening/closing.  
• Adjust font styles and text alignment.  

#### **Visual Feedback:**  
• Add effects for player actions (e.g., flashing screen on damage).  
• Animate NPCs if time permits.  

#### **Final Asset Integration:**  
• Ensure every level has proper visuals.  
• Test visual consistency across scenes.  

#### **Deliverables:**  
• `assets/characters/`, `assets/backgrounds/`, `assets/music/`  
• Complete UI designs for menus and dialogue boxes  

---

## **Pls do dis for documentation:**  
Use the Projects tab in GitHub to track work.  
Use To-Do, In-Progress, and Done with the assignee option so everybody can see who is working on what.  
All team members need to add and update their own tasks.  
The format is: #fractured-heart (insert issue here or make new issue).
### **Team Communication & Tools**  
• **GitHub:** Version control, branch management, pull requests. +progress updates and task tracking above cuz ion like using Notion  
• **Whatsapp/Zoom:** Daily communication and quick problem-solving.  

---

## **Final Week Preparation (Days 13-14)**  
• **Polish All Levels:** Final bug fixes and optimizations.  
• **Test Gameplay Thoroughly:** Ensure smooth scene transitions, AI responses, and visual performance.  
• **Prepare README.md:**  
   • Installation instructions  
   • Game controls  
   • Team credits  
• **Create Demo Video:** Showcase core gameplay, dialogues, and AI integration.  
• **Prepare Presentation Materials:** Highlight key features and team contributions.  
• **Send someone to umrah to pray for us**  
