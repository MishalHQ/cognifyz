"""
Level 3 - Task 5: Enhanced CRUD with File I/O (Text File Storage)
This is an enhanced version of Task 3 with persistent storage using plain text files.
"""

from datetime import datetime

class Task:
    """Task class with necessary attributes"""
    def __init__(self, task_id, title, description, status="Pending", priority="Medium"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_text_line(self):
        """Convert task to text line for file storage"""
        # Format: ID|Title|Description|Status|Priority|CreatedAt
        return f"{self.task_id}|{self.title}|{self.description}|{self.status}|{self.priority}|{self.created_at}\n"
    
    @staticmethod
    def from_text_line(line):
        """Create task from text line"""
        try:
            parts = line.strip().split('|')
            if len(parts) == 6:
                task = Task(int(parts[0]), parts[1], parts[2], parts[3], parts[4])
                task.created_at = parts[5]
                return task
        except Exception as e:
            print(f"Error parsing line: {e}")
        return None

class TaskManagerWithFileIO:
    """Enhanced Task Manager with File I/O for persistent storage"""
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.next_id = 1
        self.filename = filename
    
    def create_task(self):
        """Create a new task"""
        print("\n--- Create New Task ---")
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        
        print("\nSelect priority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        priority_choice = input("Enter choice (1-3): ")
        
        priority_map = {'1': 'Low', '2': 'Medium', '3': 'High'}
        priority = priority_map.get(priority_choice, 'Medium')
        
        task = Task(self.next_id, title, description, priority=priority)
        self.tasks.append(task)
        self.next_id += 1
        
        print(f"\n✅ Task created successfully! (ID: {task.task_id})")
        
        # Auto-save after creating
        self.save_to_file()
    
    def read_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\n📭 No tasks available!")
            return
        
        print("\n" + "=" * 90)
        print(f"{'ID':<5} {'Title':<25} {'Status':<12} {'Priority':<10} {'Created':<20}")
        print("=" * 90)
        
        for task in self.tasks:
            print(f"{task.task_id:<5} {task.title[:25]:<25} {task.status:<12} "
                  f"{task.priority:<10} {task.created_at:<20}")
        print("=" * 90)
    
    def view_task_details(self):
        """View detailed information of a specific task"""
        self.read_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input("\nEnter task ID to view details: "))
            task = self.find_task(task_id)
            
            if task:
                print("\n" + "=" * 60)
                print(f"Task ID: {task.task_id}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Status: {task.status}")
                print(f"Priority: {task.priority}")
                print(f"Created At: {task.created_at}")
                print("=" * 60)
            else:
                print(f"\n❌ Task with ID {task_id} not found!")
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid task ID.")
    
    def update_task(self):
        """Update task details"""
        self.read_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input("\nEnter task ID to update: "))
            task = self.find_task(task_id)
            
            if not task:
                print(f"\n❌ Task with ID {task_id} not found!")
                return
            
            print("\nWhat would you like to update?")
            print("1. Title")
            print("2. Description")
            print("3. Status")
            print("4. Priority")
            print("5. All")
            
            choice = input("\nEnter choice (1-5): ")
            
            if choice in ['1', '5']:
                new_title = input(f"Enter new title (current: {task.title}): ")
                if new_title:
                    task.title = new_title
            
            if choice in ['2', '5']:
                new_desc = input(f"Enter new description (current: {task.description}): ")
                if new_desc:
                    task.description = new_desc
            
            if choice in ['3', '5']:
                print("\nSelect new status:")
                print("1. Pending")
                print("2. In Progress")
                print("3. Completed")
                status_choice = input("Enter choice (1-3): ")
                status_map = {'1': 'Pending', '2': 'In Progress', '3': 'Completed'}
                task.status = status_map.get(status_choice, task.status)
            
            if choice in ['4', '5']:
                print("\nSelect new priority:")
                print("1. Low")
                print("2. Medium")
                print("3. High")
                priority_choice = input("Enter choice (1-3): ")
                priority_map = {'1': 'Low', '2': 'Medium', '3': 'High'}
                task.priority = priority_map.get(priority_choice, task.priority)
            
            print(f"\n✅ Task {task_id} updated successfully!")
            
            # Auto-save after updating
            self.save_to_file()
            
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid task ID.")
    
    def delete_task(self):
        """Delete a task"""
        self.read_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            task = self.find_task(task_id)
            
            if task:
                confirm = input(f"Are you sure you want to delete '{task.title}'? (yes/no): ")
                if confirm.lower() in ['yes', 'y']:
                    self.tasks.remove(task)
                    print(f"\n✅ Task {task_id} deleted successfully!")
                    
                    # Auto-save after deleting
                    self.save_to_file()
                else:
                    print("\n❌ Deletion cancelled.")
            else:
                print(f"\n❌ Task with ID {task_id} not found!")
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid task ID.")
    
    def find_task(self, task_id):
        """Find task by ID"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def save_to_file(self):
        """Save tasks to text file with error handling"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                # Write header
                f.write("# Task Manager Data File\n")
                f.write("# Format: ID|Title|Description|Status|Priority|CreatedAt\n")
                f.write("# Do not edit this file manually\n")
                f.write("#" + "="*70 + "\n")
                
                # Write tasks
                for task in self.tasks:
                    f.write(task.to_text_line())
            
            print(f"💾 Tasks saved to {self.filename}")
            
        except PermissionError:
            print(f"❌ Error: Permission denied to write to {self.filename}")
        except IOError as e:
            print(f"❌ Error saving tasks: {e}")
        except Exception as e:
            print(f"❌ Unexpected error while saving: {e}")
    
    def load_from_file(self):
        """Load tasks from text file with error handling"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                # Skip header lines (lines starting with #)
                task_lines = [line for line in lines if not line.startswith('#') and line.strip()]
                
                # Parse tasks
                loaded_tasks = []
                for line in task_lines:
                    task = Task.from_text_line(line)
                    if task:
                        loaded_tasks.append(task)
                
                self.tasks = loaded_tasks
                
                # Update next_id
                if self.tasks:
                    self.next_id = max(task.task_id for task in self.tasks) + 1
                
                print(f"📂 Loaded {len(self.tasks)} task(s) from {self.filename}")
                
        except FileNotFoundError:
            print(f"⚠️ No saved tasks found in {self.filename}. Starting fresh!")
        except PermissionError:
            print(f"❌ Error: Permission denied to read {self.filename}")
        except IOError as e:
            print(f"❌ Error loading tasks: {e}")
        except Exception as e:
            print(f"❌ Unexpected error while loading: {e}")
    
    def test_persistence(self):
        """Test the persistence of task data"""
        print("\n" + "=" * 60)
        print("Testing Data Persistence")
        print("=" * 60)
        
        print("\n1. Current tasks in memory:")
        self.read_tasks()
        
        print("\n2. Saving to file...")
        self.save_to_file()
        
        print("\n3. Clearing memory...")
        original_tasks = len(self.tasks)
        self.tasks = []
        print(f"   Memory cleared. Tasks in memory: {len(self.tasks)}")
        
        print("\n4. Loading from file...")
        self.load_from_file()
        
        print("\n5. Tasks after loading:")
        self.read_tasks()
        
        if len(self.tasks) == original_tasks:
            print("\n✅ Persistence test PASSED! All tasks restored successfully.")
        else:
            print(f"\n⚠️ Persistence test WARNING: Expected {original_tasks} tasks, got {len(self.tasks)}")
        
        print("=" * 60)

def main():
    """Main function to run the enhanced task manager"""
    manager = TaskManagerWithFileIO()
    
    print("=" * 60)
    print("Enhanced Task Manager - With File I/O Persistence")
    print("=" * 60)
    
    # Load existing tasks
    manager.load_from_file()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. View Task Details")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Save Tasks (Manual)")
        print("7. Reload Tasks from File")
        print("8. Test Persistence")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == '1':
            manager.create_task()
        elif choice == '2':
            manager.read_tasks()
        elif choice == '3':
            manager.view_task_details()
        elif choice == '4':
            manager.update_task()
        elif choice == '5':
            manager.delete_task()
        elif choice == '6':
            manager.save_to_file()
        elif choice == '7':
            manager.load_from_file()
        elif choice == '8':
            manager.test_persistence()
        elif choice == '9':
            manager.save_to_file()
            print("\nThank you for using Enhanced Task Manager! Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
