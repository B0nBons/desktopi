### An intended flowchat of how the code will look (wip)

ROOT
.__________________
│   file_layout.md
│   LICENSE
│   README.md
│   requirements.txt
│   
├───.vscode
│       launch.json
│       settings.json
│       
└───focus_buddy
    │   main.py
    │   
    └───src
        │   app.py
        │   
        ├───core
        │   │   blocker.py
        │   │   timer.py
        │   │   weather.py
        │           
        ├───ui
        │   │   main_window.py
        │   │   system_tray.py
        │   │   __init__.py
        │   │   
        │   ├───widgets
        │   │   timer_widget.py
        │   │   weather_widget.py
        │   │   __init__.py
        │
        │
        │           
        ├───utils
        │       config.py
        │       __init__.py
