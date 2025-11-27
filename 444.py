import time
from local_llm import get_local_llm

class MiniJarvis:
    def __init__(self):
        self.llm = get_local_llm()
        self.agents = {
            'architect': 'Software Architect - designs system architecture',
            'engineer': 'Software Engineer - writes clean code', 
            'tester': 'QA Engineer - tests and verifies code'
        }
    
    def architect_design(self, task):
        """Architect agent designs the solution"""
        prompt = f"Design architecture for: {task}. Be concise and practical."
        return self.llm.invoke(prompt)
    
    def engineer_code(self, design):
        """Engineer agent implements the code"""
        prompt = f"Write Python code based on this design: {design}. Provide only code with comments."
        return self.llm.invoke(prompt)
    
    def tester_verify(self, code):
        """Tester agent verifies the code"""
        prompt = f"Test this Python code and report any issues: {code}. Be brief."
        return self.llm.invoke(prompt)
    
    def run_project(self, task_description):
        """Run complete project workflow"""
        print(f"🚀 Mini-Jarvis starting project: {task_description}")
        print("-" * 50)
        
        # Architect phase
        print("👨‍💼 Architect designing...")
        design = self.architect_design(task_description)
        print(f"📐 Design: {design}")
        
        # Engineer phase  
        print("\n👩‍💻 Engineer coding...")
        code = self.engineer_code(design)
        print(f"💻 Code: {code}")
        
        # Tester phase
        print("\n🧪 Tester verifying...")
        test_result = self.tester_verify(code)
        print(f"✅ Test Result: {test_result}")
        
        print("\n" + "=" * 50)
        print("🎉 Project completed!")

def main():
    jarvis = MiniJarvis()
    
    # Test with a simple project
    project = "Create a Python function to calculate the area of a circle"
    jarvis.run_project(project)

if __name__ == "__main__":
    main()