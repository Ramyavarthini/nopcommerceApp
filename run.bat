rem chrome
pytest -s -v -m "sanity" --html=./Reports/reports_chrome.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/reports_chrome.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/reports_chrome.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/reports_chrome.html testCases/ --browser chrome

rem firefox
rem pytest -s -v -m "sanity" --html=./Reports/reports_firefox.html testCases/ --browser firefox
rem pytest -s -v -m "sanity or regression" --html=./Reports/reports_firefox.html testCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./Reports/reports_firefox.html testCases/ --browser firefox
rem pytest -s -v -m "regression" --html=./Reports/reports_firefox.html testCases/ --browser firefox