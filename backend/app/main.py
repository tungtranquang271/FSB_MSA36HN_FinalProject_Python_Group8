from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.student import router as student_router

app = FastAPI(
    title="Student Management API Version 1.0.0",
    description="API for managing and analyzing student data",
    version="1.0.0"
)

# Include routers
app.include_router(student_router, prefix="/students", tags=["Students"])


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Management API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f7fa;
                padding: 40px;
            }
            .container {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
            }
            p {
                color: #555;
                line-height: 1.6;
            }
            a {
                display: inline-block;
                margin-top: 15px;
                padding: 10px 18px;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #2980b9;
            }
            .links a {
                margin-right: 10px;
            }
            footer {
                margin-top: 30px;
                font-size: 13px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 Student Management API</h1>
            <p>
                This backend service provides APIs to manage student information
                and support data analysis for the Desktop Application (FE3).
            </p>

            <div class="links">
                <a href="/docs">📘 Swagger UI</a>
                <a href="/redoc">📕 ReDoc</a>
            </div>

            <footer>
                <p>FastAPI • MongoDB • Python</p>
            </footer>
        </div>
    </body>
    </html>
    """