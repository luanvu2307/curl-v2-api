import os
timeout = 3600
bind = f":{os.environ.get('PORT', '2307')}"
worker_class = "uvicorn.workers.UvicornWorker"