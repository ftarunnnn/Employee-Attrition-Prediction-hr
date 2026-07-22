"""Verification script to test imports of all required libraries."""
import sys

def test_imports():
    packages = [
        ("fastapi", "FastAPI"),
        ("uvicorn", "Uvicorn"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
        ("sklearn", "Scikit-Learn"),
        ("xgboost", "XGBoost"),
        ("joblib", "Joblib"),
        ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"),
        ("pydantic", "Pydantic"),
    ]
    
    print("Testing package imports...")
    all_success = True
    for pkg_import, pkg_name in packages:
        try:
            mod = __import__(pkg_import)
            version = getattr(mod, "__version__", "installed")
            print(f"  [OK] {pkg_name} ({version})")
        except ImportError as e:
            print(f"  [FAIL] {pkg_name}: {e}")
            all_success = False
            
    if all_success:
        print("\nAll Phase 1 environment packages successfully verified!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    test_imports()
