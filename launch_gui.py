#!/usr/bin/env python3
"""
Quick launch script for the Student Management System GUI.
This script handles dependencies and provides helpful error messages.
"""

import sys
import os

def check_dependencies():
    """Check for required dependencies and provide installation hints."""
    missing_deps = []
    
    try:
        import tkinter
    except ImportError:
        missing_deps.append("tkinter (usually included with Python)")
    
    # Optional dependencies
    optional_missing = []
    try:
        import matplotlib
    except ImportError:
        optional_missing.append("matplotlib")
    
    try:
        import numpy
    except ImportError:
        optional_missing.append("numpy")
    
    if missing_deps:
        print("❌ Missing required dependencies:")
        for dep in missing_deps:
            print(f"   - {dep}")
        print("\n💡 Please install missing dependencies and try again.")
        return False
    
    if optional_missing:
        print("⚠️  Optional dependencies missing (charts won't work):")
        for dep in optional_missing:
            print(f"   - {dep}")
        print("\n💡 Install with: pip install matplotlib numpy")
        print("   (You can still use the app without charts)")
    
    return True

def main():
    """Main function to launch the GUI."""
    print("🎓 Starting Student Management System GUI...")
    print("=" * 50)
    
    if not check_dependencies():
        sys.exit(1)
    
    try:
        # Import and run the GUI
        from student_gui import StudentGUI
        print("✅ All dependencies satisfied!")
        print("🚀 Launching GUI application...")
        
        app = StudentGUI()
        app.run()
        
    except ImportError as e:
        print(f"❌ Error importing student_gui module: {e}")
        print("💡 Make sure student_gui.py is in the same directory.")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 Please check the error message above and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
