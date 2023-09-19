
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

sys.path.append(parent)


from unittest import main, TestCase
from PatchScraper import Patch


class TestPatch(TestCase):
    def setUp(self) -> None:
        print("Starting Test")
        return super().setUp()
    
    def test_patch_func(self) -> None:
        HEADERS: dict[str, str] = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
        LINK: str = "https://www.leagueoflegends.com/en-us/news/tags/patch-notes/"
        self.assertIn("Patch" , Patch(LINK, HEADERS).scrape_patch(), "Patch is not scraped")

if __name__ == "__main__":
    main()