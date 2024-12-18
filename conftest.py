from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from support.common_actions import CommonActions
from support.config import BASE_URL 

@pytest.fixture(scope="session")
def browser():
    """Set up the Playwright browser."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, 
            args=["--window-size=1920,1080"]
        )
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def browser_context(browser):
    """Set up the browser context with a custom viewport size."""
    video_output_dir = Path("videos")
    video_output_dir.mkdir(exist_ok=True)

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},  
        record_video_dir=str(video_output_dir),
    )
    yield context
    context.close()

@pytest.fixture
def page(browser_context):
    """Provide a new page for each test."""
    page = browser_context.new_page()
    yield page

    
    try:
        video_path = page.video.path()
        print(f"Video saved at: {video_path}")
    except Exception as e:
        print(f"Video path retrieval failed: {e}")
    page.close()

@pytest.fixture
def common_actions(page):
    """Initialize and provide the CommonActions class."""
    return CommonActions(page)

@pytest.fixture
def home_page(page, browser_context):
    """Initialize and provide the HomePage class."""
    return HomePage(page, browser_context, BASE_URL)
