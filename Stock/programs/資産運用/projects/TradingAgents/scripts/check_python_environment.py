#!/usr/bin/env python3
"""
Python Environment Check Script
Phase 6: Final Validation & Production Readiness

Checks:
- Python version (3.10+ required for yfinance)
- yfinance installation and version
- Real data fetch from yfinance (日経225)
- Documentation of limitations if Python 3.9
"""

import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path


def check_python_version():
    """Check Python version and compatibility"""
    print("=" * 60)
    print("Python Environment Check")
    print("=" * 60)

    version = sys.version_info
    print(f"\n✓ Python Version: {version.major}.{version.minor}.{version.micro}")

    if version.major < 3:
        print("❌ ERROR: Python 3.x required")
        return False

    if version.minor < 9:
        print("❌ ERROR: Python 3.9+ required")
        return False

    if version.minor == 9:
        print("⚠️  WARNING: Python 3.9 detected")
        print("   yfinance may have limited functionality")
        print("   Recommend upgrading to Python 3.10+")
        return True

    print("✓ Python version compatible")
    return True


def check_yfinance():
    """Check yfinance installation and version"""
    print("\n" + "-" * 60)
    print("Checking yfinance installation...")
    print("-" * 60)

    try:
        import yfinance as yf
        print(f"✓ yfinance installed: version {yf.__version__}")
        return True
    except ImportError:
        print("❌ yfinance not installed")
        print("\nTo install:")
        print("  pip install yfinance")
        return False
    except TypeError as e:
        print("❌ yfinance installed but incompatible with Python 3.9")
        print(f"   Error: {e}")
        print("\nTo fix:")
        print("  Upgrade to Python 3.10+ or use sample data fallback")
        return False


def test_real_data_fetch():
    """Test real data fetch from yfinance (Nikkei 225)"""
    print("\n" + "-" * 60)
    print("Testing real data fetch (Nikkei 225)...")
    print("-" * 60)

    try:
        import yfinance as yf

        # Fetch Nikkei 225 data
        ticker = "^N225"
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)

        print(f"\nFetching {ticker} data...")
        print(f"Period: {start_date.date()} to {end_date.date()}")

        data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if data.empty:
            print("❌ No data received")
            return False

        print(f"\n✓ Data fetched successfully")
        print(f"  Rows: {len(data)}")
        print(f"  Columns: {list(data.columns)}")
        print(f"\nSample data (last 5 days):")
        print(data.tail())

        return True

    except Exception as e:
        print(f"❌ Data fetch failed: {e}")
        print("\nPossible reasons:")
        print("  - Internet connection issue")
        print("  - Yahoo Finance API rate limit")
        print("  - Python version compatibility (use 3.10+)")
        return False


def check_dependencies():
    """Check other required dependencies"""
    print("\n" + "-" * 60)
    print("Checking other dependencies...")
    print("-" * 60)

    required = ['pandas', 'numpy', 'matplotlib']
    all_installed = True

    for package in required:
        try:
            __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"❌ {package} not installed")
            all_installed = False

    return all_installed


def generate_report():
    """Generate environment check report"""
    print("\n" + "=" * 60)
    print("Environment Check Summary")
    print("=" * 60)

    python_ok = check_python_version()
    yfinance_ok = check_yfinance()
    deps_ok = check_dependencies()

    if yfinance_ok:
        data_ok = test_real_data_fetch()
    else:
        data_ok = False

    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    results = {
        "Python Version": python_ok,
        "yfinance": yfinance_ok,
        "Dependencies": deps_ok,
        "Data Fetch": data_ok
    }

    for check, status in results.items():
        symbol = "✓" if status else "❌"
        print(f"{symbol} {check}: {'PASS' if status else 'FAIL'}")

    all_ok = all(results.values())

    print("\n" + "-" * 60)
    if all_ok:
        print("✓ Environment ready for production")
        print("  Proceed with final validation")
    else:
        print("⚠️  Environment has issues")
        if not yfinance_ok or not data_ok:
            print("\nFallback option:")
            print("  Use sample/demo data from Phase 5")
            print("  Document limitation in final report")
    print("-" * 60)

    # Save report to file
    report_path = Path(__file__).parent.parent / "data" / "results" / "environment_check.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"Environment Check Report\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"\n{'='*60}\n")
        for check, status in results.items():
            f.write(f"{check}: {'PASS' if status else 'FAIL'}\n")
        f.write(f"{'='*60}\n")
        f.write(f"\nOverall: {'READY' if all_ok else 'HAS ISSUES'}\n")

    print(f"\nReport saved to: {report_path}")

    return all_ok


if __name__ == "__main__":
    result = generate_report()
    sys.exit(0 if result else 1)
