# Disaster Response Logistics System

A simulation system built with custom primitive data structures for optimizing aid management and pathfinding during emergency disaster response.

## Modules Implemented
1. **Graph & BFS**: Disaster route mapping and isolating unreached villages.
2. **Priority Queue**: Managed via Sorted Linked List for processing Critical locations first.
3. **BST**: Fast binary searching and registry updates for location levels.
4. **Stack**: Transaction logging supporting complete rollback functionalities (LIFO).
5. **Dijkstra**: Finding the shortest paths from primary hubs.

## Installation
```bash
pip install -r requirements.txt
python main.py
