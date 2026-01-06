import json
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
    
    def to_dict(self):
        """Convert task to dictionary"""
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        """Create task from dictionary"""
        task = Task(data['task_id'], data['title'], data['description'], 
                   data['status'], data['priority'])
        task.created_at = data['created_at']
        return task

class TaskManager:
    """Task Manager for CRUD operations"""
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
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
    
    def read_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\n📭 No tasks available!")
            return
        
        print("\n" + "=" * 80)
        print(f"{'ID':<5} {'Title':<20} {'Status':<12} {'Priority':<10} {'Created':<20}")
        print("=" * 80)
        
        for task in self.tasks:
            print(f"{task.task_id:<5} {task.title[:20]:<20} {task.status:<12} "
                  f"{task.priority:<10} {task.created_at:<20}")
        print("=" * 80)
    
    def view_task_details(self):
        """View detailed information of a specific task"""
        self.read_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input("\nEnter task ID to view details: "))
            task = self.find_task(task_id)
            
            if task:
                print("\n" + "=" * 50)
                print(f"Task ID: {task.task_id}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Status: {task.status}")
                print(f"Priority: {task.priority}")
                print(f"Created At: {task.created_at}")
                print("=" * 50)
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
    
    def save_to_file(self, filename="tasks.json"):
        """Save tasks to file"""
        try:
            with open(filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=4)
            print(f"\n💾 Tasks saved to {filename}")
        except Exception as e:
            print(f"\n❌ Error saving tasks: {e}")
    
    def load_from_file(self, filename="tasks.json"):
        """Load tasks from file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
                if self.tasks:
                    self.next_id = max(task.task_id for task in self.tasks) + 1
            print(f"\n📂 Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"\n⚠️ No saved tasks found. Starting fresh!")
        except Exception as e:
            print(f"\n❌ Error loading tasks: {e}")

def main():
    """Main function to run the task manager"""
    manager = TaskManager()
    manager.load_from_file()
    
    print("=" * 50)
    print("Task Manager - CRUD Application")
    print("=" * 50)
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. View Task Details")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Save Tasks")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
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
            manager.save_to_file()
            print("\nThank you for using Task Manager! Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
