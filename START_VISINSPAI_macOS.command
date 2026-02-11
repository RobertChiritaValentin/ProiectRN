#!/bin/bash
# ne mutam in folder
cd "$(dirname "$0")"

echo "========================================"
echo "   PORNIRE APLICATIE VISINSPAI         "
echo "========================================"

# rulam streamlit
python3 -m streamlit run src/app/app.py