import json
import os
from frontier import URLFrontier

STATE_FILE = "datasets/crawl_state.json"


def save_state(
    visited,
    seen_hashes,
    frontier,
    page_counter,
):
    state = {
        "page_counter": page_counter,
        "visited": list(visited),
        "seen_hashes": list(seen_hashes),
        "frontier": list(frontier.queue),
    }
    
    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(
            state,
            file,
            indent=4,
            ensure_ascii=False,
        )

def load_state():
    if not os.path.exists(STATE_FILE):
        return  (set(),
                set(),
                URLFrontier(),
                1
                )

    with open(STATE_FILE, "r", encoding="utf-8") as file:
        state = json.load(file)

    visited = set(state["visited"])
    seen_hashes = set(state["seen_hashes"])
    frontier = URLFrontier()
    for url, depth in state["frontier"]:
        frontier.add(url, depth)
    page_counter = state["page_counter"]

    return visited, seen_hashes, frontier, page_counter