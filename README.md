# execute post request
uvicorn createItem:app --host 127.0.0.1 --port 8010
uvicorn main:app --host 127.0.0.1 --port 8010 --reload
# execute get request

# execute pytest command
python -m pytest test_main.py



